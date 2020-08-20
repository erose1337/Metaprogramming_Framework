""" Additional builtin functions that are generally, frequently, and obviously useful.
    Functions defined here become available as builtins when pride is imported.
    Default builtins can be replaced by defining them here

    This module should only receive additions when absolutely necessary. """
import sys
import importlib
import platform
import itertools
import pprint
import time
is_version_two = platform.python_version_tuple()[0] == '2'

__all__ = ("raw_input" if is_version_two else "input",
           "restart", "shutdown", "objects", "system_update")

_NUMBERS = ''.join(str(x) for x in xrange(10))

# used in way too many places. no need to bother importing utilities everywhere

if is_version_two:
    __raw_input = raw_input
    class RequestDenied(BaseException): pass


    _PERSISTENCE = [] # readline in one thread and raw_input in another doesn't play nicely
    def _store(text, _persistence=_PERSISTENCE):
        _persistence.append(text)

    def _get_input(_persistence=_PERSISTENCE):
        try:
            objects["/User/Command_Line"]._raw_input_callback = _store
        except KeyError:
            reply = __raw_input('')
        else:
            while not _persistence:
                time.sleep(.005)
            reply = _persistence.pop(0)
        return reply

    def raw_input(prompt='', must_reply=False, _persistence=_PERSISTENCE):
        """ raw_input function that plays nicely when sys.stdout is swapped.
            If must_reply equals True, then the prompt will be redisplayed
            until a non empty string is returned.

            For documentation of the standard CPython raw_input function, consult
            the python interpreter or the internet. """
        if getattr(objects.get("/Program/Interpreter", None), "_disable_raw_input", None):
            raise RequestDenied("raw_input does not function remotely")
        if must_reply:
            reply = ''
            while not reply:
                sys.__stdout__.write(prompt)
                sys.__stdout__.flush()
                reply = _get_input()
        else:
            sys.__stdout__.write(prompt)
            sys.__stdout__.flush()
            reply = _get_input()
        return reply
else:
    __input = input
    def input(prompt='', must_reply=False):
        """ input function that plays nicely when sys.stdout is swapped.
            If must_reply equals True, then the prompt will be redisplayed
            until a non empty string is returned.

            For documentation of the standard CPython input function, consult
            the python interpreter or the internet. """
        if must_reply:
            reply = ''
            while not reply:
                sys.__stdout__.write(prompt)
                sys.__stdout__.flush()
                reply = __input('')
        else:
            sys.__stdout__.write(prompt)
            sys.__stdout__.flush()
            reply = __input('')
        return reply

def restart():
    raise SystemExit("Restart")

def system_update():
    for reference, root_object in ((reference, _object) for reference, _object in
                                    objects.items() if reference.count("/") == 1):
        if reference not in ("/Finalizer", "/Alert_Handler"):
            root_object.update(True)

def shutdown():
    raise SystemExit(0)

objects = {}#Objects_Dictionary()
