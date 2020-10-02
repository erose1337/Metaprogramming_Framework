import pprint
import sys
import argparse
import types
import functools
import ast
from copy import copy, deepcopy

#import cython

import autodocumentation
import pride
import pride.components
import pride.site_config as site_config
from pride.functions.utilities import resolve_string

class Docstring(object):
    """ A descriptor object used by the Documented metaclass. Augments
        instance docstrings with introspected information"""
    def __init__(self):
        super(Docstring, self).__init__()

    def __get__(self, instance, _class):
        _object = instance if instance else _class
        return autodocumentation.documentation(_object)


class Documented(type):
    """ A metaclass that uses the Docstring object to supply
        abundant documentation for classes"""
    def __new__(cls, name, bases, attributes):
        cls.make_docstring(attributes)
        return super(Documented, cls).__new__(cls, name, bases, attributes)

    @staticmethod
    def make_docstring(attributes):
        attributes["__doc"] = attributes.get("__doc__", "No docstring found")
        attributes["__doc__"] = Docstring()


class alert_on_call(object):
    """ Decorator that automatically calls self.alert when the decorated method is called """
    def __init__(self, method):
        self.method = method
        self.method_name = self.get_method_name(method)

    @staticmethod
    def get_method_name(method):
        try:
            return method.im_func.func_name
        except AttributeError:
            return method.func_name

    def __call__(self, *args, **kwargs):
        method_name = self.method_name
        alert_handler = pride.objects["/Alert_Handler"]
        if (method_name != "on_load" and # can cause problems otherwise
            "debug" in alert_handler.print_level or
            "debug" in alert_handler.log_level):
            component = args[0]
            # if verbosity is something other than "debug" it is presumably already being used for some other alert
            if component.verbosity[method_name] == "debug":
                message = "{}{}{}".format(method_name,
                                        "({},".format(pprint.pformat(args[1:])) if args[1:] else '(',
                                        " {})".format(pprint.pformat(kwargs)) if kwargs else ')')
                component.alert(message, level=component.verbosity[method_name])
        return self.method(*args, **kwargs)



class Method_Hook(type):
    """ Provides a hook for decorating methods for the new class. """

    enabled = True
    decorator = alert_on_call#cython.ccall
    default_verbosity = "debug"

    def __new__(cls, name, bases, attributes):
        new_class = super(Method_Hook, cls).__new__(cls, name, bases, attributes)
        if cls.enabled:
            Method_Hook.decorate(new_class)
        return new_class

    @classmethod
    def decorate(cls, new_class):
        """ Wraps all non private/magic methods with Method_Hook.decorator, which is
            set to the alert_on_call decorator. Private methods have names that begin
            with '_'."""
        decorator = cls.decorator
        default_verbosity = cls.default_verbosity
        for key, value in new_class.__dict__.items():
            # filter out things that aren't functions/are private or magic methods
            if (key[0] != "_") and callable(value) and key not in new_class.auto_verbosity_ignore:
                try:
                    if isinstance(value, BaseException) or issubclass(value, BaseException):
                        continue
                except TypeError:
                    if issubclass(type(value), BaseException):
                        continue

                try:
                    decorated_function = decorator(value)
                except AttributeError: # value could be a nested class and not a function or method
                    assert not hasattr(value, "im_func") and not hasattr(value, "func_name")
                    continue

                functools.update_wrapper(decorated_function, value)
                bound_method = types.MethodType(decorated_function,
                                                None,
                                                new_class)
                setattr(new_class, key, bound_method)
                if key not in new_class.verbosity:
                    new_class.verbosity.setdefault(key, default_verbosity)
        return new_class


class Runtime_Decorator(object):
    """ Provides the ability to call a method with a decorator, decorators,
        or monkey patch specified via keyword argument. This decorator
        inherits from object and utilizes the Documented metaclass.

        usage: wrapped_method(my_argument, decorator="decorators.Tracer")"""
    __metaclass__ = Documented

    enabled = False

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)
        self.handler_map = {"monkey_patch" : self._handle_monkey_patch,
                            "decorator" : self._handle_decorator,
                            "decorators" : self._handle_decorators}

    def __call__(self, *args, **kwargs):
        check_for = kwargs.pop
        modifiers = ("monkey_patch", "decorator", "decorators")

        for modifier in modifiers:
            found = check_for(modifier, None)
            if found:
                call = self.handler_map[modifier](found)
                break
        else:
            call = self.function
        return call(*args, **kwargs)

    """def _handle_context_manager(self, context_manager):
        raise NotImplementedError
        if isinstance(context_manager, str):
            context_manager = resolve_string(context_manager)
        return context_manager

        with context_manager():
            result = self.function(*args, **kwargs)
        return result"""

    def _handle_monkey_patch(self, monkey_patch):
        if isinstance(monkey_patch, str):
            monkey_patch = resolve_string(monkey_patch)
        try:
            monkey_patch = functools.partial(monkey_patch, self.function.im_self)
        finally: # function has no attribute im_self (not a method)
            return monkey_patch

    def _handle_decorator(self, decorator_type):
        if isinstance(decorator_type, unicode) or isinstance(decorator_type, str):
            decorator_type = resolve_string(decorator_type)
        return decorator_type(self.function)

    def _handle_decorators(self, decorator_info):
        decorators = []
        for decorator in decorator_info:
            if isinstance(decorator, str):
                decorator = resolve_string(decorator)

            decorators.append(decorator)

        wrapped_function = self.function
        for item in reversed(decorators):
            wrapped_function = item(wrapped_function)
        return wrapped_function


class Parser_Metaclass(type):
    """ Provides a command line parser for a class based upon
        the class.defaults dictionary"""

    parser = argparse.ArgumentParser()
    command_parser = parser.add_subparsers(help="filename")
    #run_parser = command_parser.add_parser("run", help="execute the specified script")
    #profile_parser = command_parser.add_parser("profile", help="profile the specified script")

    def __new__(cls, name, bases, attributes):
        new_class = super(Parser_Metaclass, cls).__new__(cls, name, bases, attributes)

        base_class = bases[0]
        modifiers = getattr(base_class, "parser_modifiers", {}).copy()
        exit_on_help = attributes.get("parser_modifiers", {}).get("exit_on_help", True)

        new_modifiers = attributes.get("parser_modifiers", {})
        modifiers.update(new_modifiers)

        new_class = Parser_Metaclass.make_parser(new_class, name,
                                                 modifiers, exit_on_help)
        return new_class

    @staticmethod
    def make_parser(new_class, name, modifiers, exit_on_help):
        parser = Parser_Metaclass.command_parser.add_parser(name)
        new_class.parser = Parser(parser, modifiers, exit_on_help, name,
                                  dict((key, new_class.defaults[key]) for key in
                                        new_class.parser_args))
        return new_class


class Parser(object):
    """ Faciltates automatically generated command line parsers. Parser
        instances are class attributes assigned by the Parser_Metaclass"""
    sys_argv_backup = copy(sys.argv)
    sys_argv = sys.argv
    __metaclass__ = Documented

    def __init__(self, parser, modifiers, exit_on_help, name, argument_info):
        super(Parser, self).__init__()
        self.parser = parser
        self.modifiers = modifiers
        self.exit_on_help = exit_on_help
        self.name = name

        arguments = {}
        argument_names = argument_info.keys()
        switch = {"short" : "-",
                  "long" : "--",
                  "positional" : ""}

        default_modifiers = {"types" : ("long", )}
        self_modifiers = modifiers
        positionals = 0
        for name in argument_names:
            _modifiers = self_modifiers.get(name, default_modifiers)
            if _modifiers == "ignore":
                continue
            info = {}
            for keyword_argument, value in _modifiers.items():
                info[keyword_argument] = value

            temporary = {}
            for arg_type in info.pop("types"):
                if arg_type != "positional":
                    temporary["dest"] = name
                else:
                    positionals += 1

                default_value = argument_info[name]
                temporary["default"] = default_value
                value_type = type(default_value)
                if value_type == bool:
                    value_type = ast.literal_eval
                temporary["type"] = value_type

                for key, value in temporary.items():
                    info.setdefault(key, value)

                arg_name = switch[arg_type] + name
                arguments[arg_name] = info

        for argument_name, options in arguments.items():
            parser.add_argument(argument_name, **options)

        self.positionals_count = positionals

    def get_arguments(self):
        parser = self.parser
        new_argv = Parser.sys_argv
        sys.argv = new_argv
        help_index = None
        try:
            arguments, unused = parser.parse_known_args()
        except SystemExit as error:
            if self.exit_on_help:
                raise SystemExit()
            try:
                help_index = new_argv.index("-h")
            except ValueError:
                try:
                    help_index = new_argv.index("--help")
                except ValueError:
                    raise error
                else:
                    help_token = "--help"
            else:
                help_token = "-h"
            removed_help = new_argv.pop(help_index)
            arguments, unused = parser.parse_known_args()
            new_argv.insert(help_index, removed_help)
            print

        if unused:
            new_argv = sys.argv = copy(Parser.sys_argv)
            if help_index is not None:
                new_argv.remove(help_token)
            for unused_name in unused:
                index = new_argv.index(unused_name)
                new_argv.pop(index)

                if "-" in unused_name: # pop whatever the value for the positional arg was too
                    try:
                        word = new_argv.pop(index)
                    except IndexError: # no argument supplied to positional arg
                        pass
                    else:
                        try:
                            unused.remove(word)
                        except ValueError:
                            pass

            arguments, unused = parser.parse_known_args()
            sys.argv = Parser.sys_argv

        is_keyword_argument = False
        positionals = self.positionals_count
        while positionals and len(sys.argv) > 1:
            positionals -= 1
            for item in sys.argv[1:]:
                if "-" != item[0]:
                    if is_keyword_argument:
                        is_keyword_argument = False
                        continue
                    sys.argv.remove(item)
                    break
                else:
                    is_keyword_argument = True
        Parser.sys_argv = sys.argv
        sys.argv = Parser.sys_argv_backup#print sys.argv # this might cause a bug? it consumes sys.argv otherwise
        return arguments

    def get_options(self):
        namespace = self.get_arguments()
        options = dict((key, getattr(namespace, key)) for key in namespace.__dict__.keys())
        return options


class Inherited_Attributes(type):

    inherited_attributes = {}

    def __new__(cls, name, bases, attributes):
        inherited_attributes = cls.inherited_attributes
        if "inherited_attributes" in attributes:
            inherited_attributes.update(attributes["inherited_attributes"])
        attributes["inherited_attributes"] = inherited_attributes

        for attribute_name, attribute_type in inherited_attributes.items():
            if issubclass(attribute_type, dict):
                empty_dict = attribute_type()
                _attribute = attribute_type()
                for _class in bases:
                    _attribute.update(deepcopy(getattr(_class, attribute_name,
                                                       empty_dict)))
                _attribute.update(attributes.get(attribute_name, empty_dict))

            elif issubclass(attribute_type, tuple):
                empty_tuple = attribute_type()
                _attribute = attribute_type()
                for _class in bases:
                    _attribute += getattr(_class, attribute_name, empty_tuple)
                _attribute += attributes.get(attribute_name, empty_tuple)
                #assert len(_attribute) == len(set(_attribute)), (name, attribute_name,  _attribute, set(_attribute), _attribute == set(_attribute))
                _attribute = attribute_type(_attribute)

            elif issubclass(attribute_type, list):
                _attribute = attribute_type()
                for _class in bases:
                    _attribute += getattr(_class, attribute_name,
                                         attribute_type())
                _attribute += attributes.get(attribute_name, attribute_type)
                assert len(_attribute) == len(set(_attribute)), _attribute
                _attribute = attribute_type(_attribute)

            elif issubclass(attribute_type, str):
                _attribute = attributes.get(attribute_name, getattr(_class, attribute_name, ''))
            attributes[attribute_name] = _attribute

        return super(Inherited_Attributes, cls).__new__(cls, name, bases, attributes)


class Defaults(Inherited_Attributes):

    inherited_attributes = {"defaults" : dict, "verbosity" : dict,
                            "predefaults" : dict, "mutable_defaults" : dict,
                            "required_attributes" : tuple,
                            "site_config_support" : tuple,
                            "post_initializer" : str, "allowed_values" : dict,
                            "auto_verbosity_ignore" : tuple,
                            "autoreferences" : tuple, "parser_args" : tuple,
                            "subcomponents" : pride.components.Config,
                            "interface" : pride.components.Interface}


class Site_Configuration(type):

    def __new__(cls, name, bases, attributes):
        new_class = super(Site_Configuration, cls).__new__(cls, name, bases, attributes)
        new_class_name = new_class.__module__ + '.' + name
        config = site_config.config
        for attribute in new_class.site_config_support:
            attribute_name = '.'.join((new_class_name, attribute))
            if attribute_name in config:
                value = getattr(new_class, attribute)
                try:
                    value.update(config[attribute_name])
                except AttributeError:
                    setattr(new_class, config[attribute_name], value)
        return new_class


def _create_pointers_to_base_object(pointers):
    for pointer_id in pointers:
        pointer_name = "_pointer_{}".format(pointer_id)
        def _getter(self, _pointer_name=pointer_name):
            try:
                return pride.objects[getattr(self, _pointer_name)]
            except AttributeError:
                pass
            except KeyError:
                pass
                #raise Warning("Autodereferencer: '{}' value not set before descriptor was accessed".format(_pointer_name[9:]))
        def _setter(self, value, _pointer_name=pointer_name):
            if value:
                setattr(self, _pointer_name, value.reference)
            else:
                setattr(self, _pointer_name, value)
        def _deler(self, _pointer_name=pointer_name):
            delattr(self, _pointer_name)
        yield pointer_id, property(_getter, _setter, _deler)


class Autodereferencer(type):

    def __new__(cls, name, bases, attributes):
        try:
            for (pointer_name,
                 _property) in _create_pointers_to_base_object(attributes["autoreferences"]):
                attributes[pointer_name] = _property
        except KeyError:
            if "pointers" in attributes:
                raise
        return super(Autodereferencer, cls).__new__(cls, name, bases, attributes)


class Metaclass(Documented, Parser_Metaclass, Method_Hook, Defaults,
                Site_Configuration, Autodereferencer):
    """ A metaclass that applies other metaclasses. """

    @classmethod
    def __prepare__(metaclass, cls, bases):
        return dict()

    @classmethod
    def update_metaclass(cls):
        cls._metaclass = type(cls.__name__,
                              tuple(cls.metaclasses),
                              {})

    @classmethod
    def insert_metaclass(cls, metaclass, index=-1):
        cls.metaclasses.insert(index, metaclass)
        cls.update_metaclass()

    @classmethod
    def remove_metaclass(cls, metaclass):
        cls.metaclasses.remove(metaclass)
        cls.update_metaclass()


if __name__ == "__main__":
    import unittest
    import pride.components.base as base


    class Test_Metaclass(unittest.TestCase):

        def testdocumentation(self):
            print base.Base.__doc__[:256] + "..."
            print "End documentation test"

        def testdecoration(self):
            test_base = base.Base()

            def test_decorator1(function):
                def wrapped_function(*args, **kwargs):
                    print "inside local decorator1"
                    return function(*args, **kwargs)
                return wrapped_function

            def test_decorator2(function):
                def wrapped_function(*args, **kwargs):
                    print "inside local decorator2"
                    return function(*args, **kwargs)
                return wrapped_function

            sock = test_base.create("socket.socket", decorator=test_decorator1)

            other_base = test_base.create("pride.components.base.Base", decorators=(test_decorator1, test_decorator2))

            def monkey_patch(*args, **kwargs):
                print "inside monkey patch"

            another_sock = test_base.create("socket.socket",
                                            monkey_patch=monkey_patch)
            self.failIf(another_sock) # monkey_patch returns False

        def testparser(self):
            import sys


            backup = sys.argv
            arguments = ("--test_string", "test_value", "--test_int", '8',
                         "--test_bool", "False", "--test_float", 3.14)
            sys.argv = list(arguments)
            print len(sys.argv)

            class TestBase(base.Base):
                defaults = pride.defaults.Base.copy()

                arg_index = 1
                for item in arguments[::2]:
                    defaults[item] = arguments[arg_index]
                    arg_index += 2

            test_base = TestBase(parse_args=True, testattr=1,
                                 test_string="ishouldn'tbehere")

            print "Ensuring parser attribute assignment works"

            print "Testing keyword arg assignment..."
            self.failUnless(test_base.testattr == 1)


            # as above, iteratively for the pairs in sys.argv
            arg_index = 1
            for index, item in enumerate(arguments[::2]):
                value = arguments[arg_index]
                arg_index += 2
                print "Testing {}: {} == {}".format(item, getattr(test_base, item), value)
                self.failUnless(getattr(test_base, item) == value)

            sys.argv = backup
    unittest.main()
