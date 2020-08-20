#!/usr/bin/env python
""" The first positional argument supplied is
    interpreted as the filepath of the python script to execute."""
from __future__ import unicode_literals
from platform import python_version_tuple
import socket # to catch socket.error

if python_version_tuple()[0] == '3':
    from past.builtins import xrange

def main():
    import pride.components.interpreter
    running = True
    while running:
        assert "/Program" not in pride.objects
        python = pride.components.interpreter.Program(parse_args=True)

        try:
            python.start_machine()
        except BaseException as error:
            running = False
            pride.objects["/Finalizer"].run()
            if isinstance(error, SystemExit) or isinstance(error, KeyboardInterrupt):
                python.alert("Session shutdown intiated... ", level=python.verbosity["shutdown"])
                if getattr(error, "code", '') == "Restart":
                    try:
                        pride.objects["/User"].delete()
                    except KeyError:
                        if "/User" in pride.objects:
                            print("User not logged out; re-raising exception")
                            raise
                    python.alert("Initiating restart.. ", level=python.verbosity["restart"])
                    python.delete()
                    del python
                    running = True
                else:
                    raise SystemExit()
            else:
                python.alert("Unhandled exception caused a fatal error", level=0)
                raise

if __name__ == "__main__":
    main()
