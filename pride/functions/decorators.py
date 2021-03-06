# pride.functions.decorators
import sys
import trace
import time
import inspect
import StringIO
from functools import wraps

from pride import errors
if "win" in sys.platform:
    timer = time.clock
else:
    timer = time.time

def required_arguments(no_args=False, no_kwargs=False, requires_args=False, 
                       requires_kwargs=False, **_kwargs):
    def decorate(function):
        def new_call(*args, **kwargs):
            raise_error = False
            if ((no_args and args) or (requires_args and not args) or
                (no_kwargs and kwargs) or (requires_kwargs and kwargs)):                
                raise errors.ArgumentError("Unable to call {};\n".format(function) +
                                           "args supplied : {}    kwargs supplied : {}\n".format(bool(args), bool(kwargs)) +
                                           "args_prohibited : {}    kwargs prohibited : {}\n".format(no_args, no_kwargs) +
                                           "requires_args : {}    requires_kwargs : {}".format(requires_args, requires_kwargs))
            if _kwargs:
                for key, value in _kwargs.items():
                    if kwargs[key] != value:
                        raise pride.errors.ArgumentError("expected {} == {}; found {} == {}".format(key, value, key, kwargs[value]))
            return function(*args, **kwargs)
        return new_call
    return decorate
    
def with_arguments_from(entry_function):
    def decorate(function):
        @wraps(function)
        def new_call(*args, **kwargs):            
            args, kwargs = entry_function(*args, **kwargs)
            return function(*args, **kwargs)
        return new_call
    return decorate

def enter(enter_function):
    def decorate(function):
        @wraps(function)
        def new_call(*args, **kwargs):
            enter_function(*args, **kwargs)
            return function(*args, **kwargs)
        return new_call
    return decorate
    
def exit(exit_function):
    def decorate(function):
        @wraps(function)
        def new_call(*args, **kwargs):
            result = function(*args, **kwargs)
            exit_function(*args, **kwargs)
            return result
        return new_call
    return decorate
    
def call_if(**conditions):
    callback = conditions.pop("otherwise_callback", None)
    def decorate(function):
        @wraps(function)
        def new_call(self, *args, **kwargs):            
            for key, value in conditions.items():
                if not getattr(self, key) == value:
                    if callback:
                        return callback(self, *args, **kwargs)
                    else:
                        break
            else:                
                return function(self, *args, **kwargs)
        return new_call
    return decorate
    
def on_exception(exception, callback):
    @wraps(function)
    def decorate(function):
        def new_call(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except exception:
                callback(*args, **kwargs)
        return new_call
    return decorate
    
class Pystone_Test(object):

    def __init__(self, function):        
        from test import pystone
        self.function = function
        if not hasattr(Pystone_Test, "pystones_per_second"):
            Pystone_Test.pystones_per_second = pystone.pystones(pystone.LOOPS)

    def __call__(self, *args, **kwargs):
        pystones_per_second = Pystone_Test.pystones_per_second
        if sys.platform == "win32":
            timer = time.clock
        else:
            timer = time.time
        start_time = timer()
        try:
            result = self.function(*args, **kwargs)
        except:
            end_time = timer()
            time_taken = end_time-start_time
            pystones_result = time_taken/pystones_per_second
            print "%s crashed after %s pystones of work" % (self.function, pystones_result)
            print "local variables: ", locals(), "\n"
            raise
        else:
            end_time = timer()
            time_taken = end_time-start_time
            pystones_result = time_taken/pystones_per_second
            print "%s took %s pystones to perform" % (self.function, pystones_result)
            return result


class Timed(object):

    def __init__(self, function, iterations=1):
        self.function = function
        self.iterations = iterations
        
    def __call__(self, *args, **kwargs):
        function = self.function
        if self.iterations > 1:
            start = timer()
            for x in xrange(self.iterations):
                function(*args, **kwargs)
        else:
            start = timer()
            function(*args, **kwargs)
        return (timer() - start) / self.iterations

        
class Tracer(object):

    def __init__(self, function):
        self.function = function
        self.source = ''
        self.debug = ''
        self.print_mode = "source"
        self.function_source = ''

    def get_frame_info(self, frame):
        code = frame.f_code
        call_info = {"code" : code,
                     "function_name" : code.co_name,
                     "line_number" : frame.f_lineno,
                     "called_from" : code.co_filename}

                     
        module = code.co_filename.split("\\")[-1].replace(".py", "")
        source_info = {"function" : inspect.getsource(code),
                       "module" : inspect.getsource(__import__(module))}

        caller = frame.f_back
        if caller:
            caller_code = caller.f_code
            caller_info = {"caller" : caller,
                           "code" : caller_code,
                           "line_number" : caller.f_lineno,
                           "function_name" : caller_code.co_name}
            source_info["caller"] = inspect.getsource(caller_code)
        else:
            caller_info = {}

        return call_info, caller_info, source_info

    def trace(self, frame, instruction, arg):
        if instruction != "exception":
            call_info, caller_info, source_info = self.get_frame_info(frame)
            local_trace = None
            function_name = call_info["function_name"]
            frame_locals = frame.f_locals
            if call_info["function_name"] == "write":
                pass # ignore print calls
            elif instruction == "return":
                self.source += "returned %s\n" % type(arg)
                self.debug += "%s returned %s\n" % (function_name, arg)
            else:
                source = source_info["module"].split("\n")[call_info["line_number"]]

                #for attribute, value in frame_locals.items():
                #    source = source.replace(attribute, attribute + "::" + str(value))
                backup = sys.stdout
                sys.stdout = sys.__stdout__
                print source
                sys.stdout = backup
                #self.source += source
                #self.debug += "call to %s from %s line %s\n" % \
                #(function_name, call_info["called_from"], call_info["line_number"])
                local_trace = self.trace
            return local_trace

    def __call__(self, *args, **kwargs):
        old_trace = sys.gettrace()
        sys.settrace(self.trace)
        print "calling ", self.function
        results = self.function(*args, **kwargs)
        sys.settrace(old_trace)
        if "debug" in self.print_mode:
            print self.debug
        if "source" in self.print_mode:
            print self.source
        return results


class Dump_Source(Tracer):
    """Tracer decorator that dumps source code to disk instead of writing to sys.stdout."""

    def __init__(self, function):
        super(Dump_Source, self).__init__(function)

    def __call__(self, *args, **kwargs):
        old_stdout = sys.stdout
        with open("%s_source.txt" % self.function.func_name, "w") as file:
            sys.stdout = file
            super(Dump_Source, self).__call__(*args, **kwargs)
            sys.stdout = old_stdout
            file.close()
            