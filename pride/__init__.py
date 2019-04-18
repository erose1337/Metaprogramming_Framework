""" Stores global objects including instructions, the alert handler, and the finalizer """
import sys
import traceback
import os
import heapq

_alert_handler_config = dict()

def parse_site_config(alert_handler_config=_alert_handler_config):
    if "--site_config" in sys.argv:
        import ast
        import site_config
        index = sys.argv.index("--site_config")
        sys.argv.pop(index)
        site_config_entries = sys.argv.pop(index)
        configuration = site_config.config
        for name_equals_value in site_config_entries.split(';'):
            name, value_code = name_equals_value.split('=', 1)
            while True:
                try:
                    value = ast.literal_eval(value_code)
                except SyntaxError:
                    value_code += sys.argv.pop(index)
                else:
                    break
            if name.split('.', 1)[0] == "Alert_Handler":
                attribute = name.split('.', 1)[1]
                try:
                    alert_handler_config[attribute].update(value)
                except KeyError:
                    alert_handler_config[attribute] = value
            for key, entry in value.items():
                configuration[(name, key)] = entry
    
parse_site_config()

import additional_builtins
try:
    import __builtin__
except ImportError:
    import builtins as __builtin__
for name in additional_builtins.__all__:
    setattr(__builtin__, name, getattr(additional_builtins, name))

import heapq
import timeit
import platform
import mmap
CURRENT_PLATFORM = platform.system()
timestamp = timeit.default_timer

class Instruction(object):
    """ usage: Instruction(component_name, method_name,
                           *args, **kwargs).execute(priority=priority,
                                                    callback=callback)

            - component_name is the string reference of the component
            - method_name is a string of the component method to be called
            - Positional and keyword arguments for the method may be
              supplied after the method_name.


        A priority attribute can be supplied when executing an instruction.
        It defaults to 0.0 and is the time in seconds until this instruction
        will be performed. Instructions are useful for explicitly
        timed/recurring tasks.

        Instructions may be reused. The same instruction object can be
        executed any number of times.

        Note that Instructions must be executed to have any effect, and
        that they do not happen inline even if the priority is 0.0. In
        order to access the result of the executed function, a callback
        function can be provided."""

    instructions = []

    def __init__(self, component_name, method, *args, **kwargs):
        super(Instruction, self).__init__()
        self.created_at = timestamp()
        self.component_name = component_name
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def execute(self, priority=0.0, callback=None):
        """ usage: instruction.execute(priority=0.0, callback=None)

            Submits an instruction to the processing queue.
            The instruction will be executed in priority seconds.
            An optional callback function can be provided if the return value
            of the instruction is needed. """
        heapq.heappush(self.instructions, [timestamp() + priority, self,
                                           callback, self.component_name,
                                           self.method, self.args, self.kwargs,
                                           True])

    @classmethod
    def purge(cls, reference):
        instructions = cls.instructions
        for entry in instructions:
            if entry[3] == reference:
                entry[-1] = False

    def unschedule(self):
        for entry in self.instructions:
            if entry[1] == self:
                entry[-1] = False

    def __str__(self):
        return "Instruction({}.{}, {}, {})".format(self.component_name, self.method,
                                                   self.args, self.kwargs)

_last_creator = ''
objects = objects # compatibility purposes

# Things must be done in this order for Alert_Handler to exist inside this file
# and reuse Base machinery, namely for argument parsing.
import pride.components.base as base
import pride.site_config as site_config

class Alert_Handler(base.Base):
    """ Provides the backend for the base.alert method. The print_level
        and log_level attributes act as global levels for alerts;
        print_level and log_level may be specified as command line arguments
        upon program startup to globally control verbosity/logging. """
    # the .updates are a hack that facilitates site_config support for the Alert_Handler

    level_map = {0 : 'alert ',
                '' : "stdout ",
                'v' : "notification ",
                'vv' : "verbose notification ",
                'vvv' : "very verbose notification ",
                'vvvv' : "extremely verbose notification "}
    level_map.update(_alert_handler_config.get("level_map", dict()))

    defaults = {"log_level" : '0+v', "print_level" : '0',
                "log_name" : os.path.join(site_config.LOG_DIRECTORY, "Alerts.log"),
                "log_is_persistent" : False, "parse_args" : True}
    defaults.update(_alert_handler_config.get("defaults", dict()))

    parser_ignore = ("parse_args", "log_is_persistent", "verbosity")
    parser_ignore += _alert_handler_config.get("parser_ignore", tuple())

    parser_modifiers = {"exit_on_help" : False}
    parser_modifiers.update(_alert_handler_config.get("parser_modifiers", dict()))

    auto_verbosity_ignore = ("append_to_log", )
    auto_verbosity_ignore += _alert_handler_config.get("auto_verbosity_ignore", tuple())

    def _get_print_level(self):
        return self._print_level
    def _set_print_level(self, value):
        value = value or '0'
        print_level = value.split('+')
        if '0' in print_level:
            print_level.remove('0')
            print_level.append(0)
        self._print_level = set(print_level)
    print_level = property(_get_print_level, _set_print_level)

    def _get_log_level(self):
        return self._log_level
    def _set_log_level(self, value):
        value = value or '0'
        log_level = value.split('+')
        if '0' in log_level:
            log_level.remove('0')
            log_level.append(0)
        self._log_level = set(log_level)
    log_level = property(_get_log_level, _set_log_level)

    def __init__(self, **kwargs):
        super(Alert_Handler, self).__init__(**kwargs)
        self.log = open(self.log_name, 'a+')

    def append_to_log(self, message, level):
        self.log.seek(0, 1) # windows might complain about files in + mode if this isn't done
        self.log.write(str(level) + message + "\n")

    def dump_log(self, byte_count=0, lines=0):
        log = self.log
        backup_position = log.tell()
        if byte_count:
            log.seek(backup_position - byte_count)
            output = log.read(byte_count)
        elif lines:
            mmap_log = self._open_mmap(log)
            output = self._tail_lines(mmap_log, lines)
            mmap_log.close()
        else:
            log.seek(0)
            output = log.read()
        log.seek(backup_position)
        return output

    @staticmethod
    def _open_mmap(_file):
        if CURRENT_PLATFORM == "Windows":
            mmap_file = mmap.mmap(_file.fileno(), 0, access=mmap.ACCESS_READ)
        else:
            # for Windows the mmap parameters are different
            mmap_file = mmap.mmap(_file.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
        return mmap_file

    @staticmethod
    def _tail_lines(string_like_object, line_count):
        index = string_like_object.rfind('\n')
        count = 1
        while count < line_count:
            index = string_like_object.rfind('\n', 0, index - 1)
            count += 1
        return string_like_object[index:]

del _alert_handler_config
alert_handler = Alert_Handler()

class Finalizer(base.Base):

    mutable_defaults = {"_callbacks" : list, "_function_callback" : list}
    verbosity = {"execute_callback" : 'v', "callback_success" : 'v',
                 "unable_to_load_object" : 0, "unable_to_get_method" : 0,
                 "callback_exception" : 0}

    def run(self):
        verbosity = self.verbosity

        _callbacks = self._callbacks
        while _callbacks:
            _, callback, args, kwargs = heapq.heappop(_callbacks)
            try:
                reference, method = callback
            except TypeError:
                reference = method = callback.__name__
            else:
                try:
                    callback = getattr(objects[reference], method)
                except KeyError:
                    if reference in objects:
                        raise
                    else:
                        self.alert("Unable to load object for callback: '{}'; Object does not exist".format(callback),
                                   level=verbosity["unable_to_load_object"])
                        continue
                except AttributeError:
                    self.alert("Unable to get method: '{}.{}'".format(reference, method),
                               level=verbosity["unable_to_get_method"])

            self.alert("Executing finalizer callback: {}({}, {})".format(callback, args, kwargs),
                       level=verbosity["execute_callback"])
            try:
                callback(*args, **kwargs)
            except Exception as error:
                message = "Unhandled exception running finalizer method '{}.{}'\n{}"
                self.alert(message.format(reference, method, traceback.format_exc()),
                           level=verbosity["callback_exception"])
            else:
                self.alert("Finalizer callback success", level=verbosity["callback_success"])
        self._callbacks = []

    def add_callback(self, callback, priority, *args, **kwargs):
        heapq.heappush(self._callbacks, (priority, callback, args, kwargs))

    def remove_callback(self, callback, priority, *args, **kwargs):
        try:
            self._callbacks.remove((priority, callback, args, kwargs))
        except ValueError:
            pass
        else:
            heapq.heapify(self._callbacks)

finalizer = Finalizer()

import pride.components.patch as patch
for name in patch.patches:
    getattr(patch, name)()
