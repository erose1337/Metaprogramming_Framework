""" Provides an entry point to the environment and a shell connection for interacting with it. """
import sys
import codeop
import os
import traceback
import time
import contextlib
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
import socket # for .error
import base64 # for standard_b64encode on machine username

import pride
import pride.components.base as base
import pride.components.authentication3
import pride.components.shell
import pride.components.user
import pride.functions.contextmanagers
import pride.site_config
import pride.functions.utilities

@contextlib.contextmanager
def main_as_name():
    backup = globals()["__name__"]
    globals()["__name__"] = "__main__"
    try:
        yield
    finally:
        globals()["__name__"] = backup

class Shell(pride.components.authentication3.Authenticated_Client):
    """ Handles keystrokes and sends python source to the Interpreter to
        be executed. This requires authentication via username/password."""
    defaults = {"username" : None, "password" : None, "startup_definitions" : '',
                "target_service" : "/Python/Interpreter", "stdout" : None}

    verbosity = {"login" : 0, "execute_source" : "vv"}

    def login_success(self, message):
        super(Shell, self).login_success(message)
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        if self.startup_definitions:
            self.handle_startup_definitions()

    def handle_startup_definitions(self):
        source = self.startup_definitions
        try:
            compile(source, "Shell", 'exec')
        except:
            self.alert("Startup defintions failed to compile:\n{}".format(traceback.format_exc()), level=0)
        else:
            self.startup_definitions = ''
            self.execute_source(source)

    @pride.components.authentication3.remote_procedure_call(callback_name="handle_result")
    def execute_source(self, source):
        """ Sends source to the interpreter specified in self.target_service for execution """

    def handle_result(self, packet):
        if packet:
            packet += ">>> "
            (self.stdout or sys.stdout).write('\r' + packet)


class Loud_Logger(object):
    """ Logger that prints written data to sys.__stdout__. Used by Interpreter to synchronize message output when in use by a local user. """

    def __init__(self):
        self._logger = StringIO.StringIO()

    def __getattr__(self, attribute):
        getter = super(Loud_Logger, self).__getattribute__
        if attribute in ("write", "_logger"):
            return getter(attribute)
        else:
            return getattr(getter("_logger"), attribute)

    def write(self, data):
        sys.__stdout__.write(data)
        _logger = self._logger
        _logger.write(data)
        _logger.flush()


class Interpreter(pride.components.authentication3.Authenticated_Service):
    """ Executes python source. Requires authentication from remote hosts.
        The source code and return value of all requests are logged. """

    defaults = {"help_string" : 'Type "help", "copyright", "credits" or "license" for more information.',
                "login_message" : "Welcome {} from {}\nPython {} on {}\n{}\n",
                "_logger_type" : "StringIO.StringIO", "allow_registration" : False}

    mutable_defaults = {"user_namespaces" : dict, "user_session" : dict}

    remotely_available_procedures = ("execute_source", "execute_instruction")

    def __init__(self, **kwargs):
        super(Interpreter, self).__init__(**kwargs)
        filename = os.path.join(pride.site_config.LOG_DIRECTORY,
                                '_'.join(word for word in self.reference.split("/") if word))
        self.log = self.create("pride.components.fileio.File",
                               "{}.log".format(filename), 'a+',
                               persistent=False).reference
        self._logger = pride.functions.utilities.invoke(self._logger_type)

    def login_success(self, username):
        flag, message, session_id = super(Interpreter, self).login_success(username)
        session_id, sender = self.current_session
        username = self.session_id[session_id]
        self.user_session[username] = ''
        string_info = (username, sender, sys.version, sys.platform, self.help_string)
        return (flag, self.login_message.format(*string_info), session_id)

    def execute_source(self, source):
        log = pride.objects[self.log]
        session_id, sender = self.current_session

        username = self.session_id[session_id]
        log.write("{}\n{} {} from {}:\n".format('-' * 80, time.asctime(), username,
                                                sender) + source)
        try:
            code = compile(source, "{}@{}_execute_source".format(username, sender), 'exec')
        except (SyntaxError, OverflowError, ValueError):
            result = traceback.format_exc()
        else:
            if sender == "localhost":
                _logger = Loud_Logger()
            else:
                _logger = self._logger
            backup = sys.stdout
            sys.stdout = _logger
            try:
                self.execute_code(code, globals())
            except SystemExit:
                sys.stdout = backup
                raise
            except: # we explicitly really do want to catch everything here
                _logger.seek(0)
                result = _logger.read() + '\n' + traceback.format_exc()
            else:
                self.user_session[username] += source
                _logger.seek(0)
                if sender != "localhost":
                    result = _logger.read()
                else:
                    result = '\b'
            log.write("{}\n".format(result))
            _logger.truncate(0)
            sys.stdout = backup
        log.flush()
        return result

    def execute_code(self, code, _locals):
        exec code in _locals

    def _exec_command(self, source):
        """ Executes the supplied source as the __main__ module"""
        try:
            code = compile(source, "__main__", "exec")
            with main_as_name():
                exec code in globals(), globals()
        except Exception as error:
            self.alert("{}".format(traceback.format_exc()), level=0)
            raise SystemExit()

    def execute_instruction(self, instruction, priority, callback):
        """ Executes the supplied instruction with the specified priority and callback """
        instruction.execute(priority=priority, callback=callback)

    def __getstate__(self):
        attributes = super(Interpreter, self).__getstate__()
        log = attributes["_logger"]
        log.seek(0)
        attributes["_logger"] = log.read()
        return attributes


class Python(base.Base):
    """ The "main" class. Provides an entry point to the environment.
        Instantiating this component and calling the start_machine method
        starts the execution of the Processor component.

        Warning: Using the following flag:

            --log_level debug

        will result in the cryptographic key for the session being logged."""
    defaults = {"command" : '',
                "environment_setup" : ("PYSDL2_DLL_PATH = " + pride.site_config.PYSDL2_PATH, ),
                "startup_components" : ("pride.components.storage.Persistent_Storage",
                                        "pride.components.vcs.Version_Control",
                                        "pride.components.scheduler.Processor",
                                        "pride.components.fileio.File_System",
                                        "pride.components.network.Network_Connection_Manager",
                                        "pride.components.network.Network",
                                        "pride.components.interpreter.Interpreter",
                                        "pride.components.rpc.Rpc_Connection_Manager",
                                        "pride.components.rpc.Rpc_Worker",
                                        "pride.components.datatransfer.Data_Transfer_Service",
                                        "pride.components.datatransfer.Background_Refresh",
                                        "pride.components.encryptedstorage.Encryption_Service"),
                "startup_definitions" : '', "use_existing_server" : True,
                "interpreter_type" : "pride.components.interpreter.Interpreter",
                "rpc_server_type" : "pride.components.rpc.Rpc_Server",
                }

    parser_args = ("command", )
    # make an optional "command" positional argument and allow
    # both -h and --help flags
    parser_modifiers = {"command" : {"types" : ("positional", ),
                                     "nargs" : '?'},
                        "help" : {"types" : ("short", "long"),
                                  "nargs" : '?'},
                        "exit_on_help" : False}

    verbosity = {"shutdown" : 0, "restart" : 0, "os_environ_set" : 'v'}

    def __init__(self, **kwargs):
        super(Python, self).__init__(**kwargs)
        try:
            self.rpc_server = self.create(self.rpc_server_type)
        except socket.error as exception:
            if exception.errno != 98 or not self.use_existing_server:
                raise
        self.setup_os_environ()

        # ephemeral keys for encrypted in memory only data storage
        self.session = self.create("pride.components.user.Session",
                                   username=os.urandom(16), auto_register=True,
                                   password=os.urandom(32), kdf_iterations=1)
        pride.objects["/Finalizer"].add_callback((self.session.reference, "delete"), -1)

        machine_id, machine_password = self.get_machine_credentials()
        User = pride.components.user.User
        with pride.functions.contextmanagers.backup(User, "verbosity"):
            User.verbosity["login_success"] = "vv"
            user = User(username=machine_id, password=machine_password,
                        auto_register=True, kdf_iterations=1)
        assert user.reference == "/User"
        if not self.command:
            command = os.path.join((os.getcwd() if "__file__"
                                    not in globals() else
                                    pride.site_config.PRIDE_DIRECTORY),
                                    os.path.join("programs", "shell_launcher.py"))
        else:
            command = self.command
        source = ''
        if self.startup_definitions:
            source += self.startup_definitions + "\n"
        try:
            with open(command, 'r') as module_file:
                source += module_file.read()
        except IOError:
            self.alert("Unable to locate '{}';\nCWD: {}".format(command, os.getcwd()))
            raise SystemExit()
        pride.Instruction(self.interpreter, "_exec_command", source).execute()

    def get_machine_credentials(self):
        try:
            machine_id, machine_password = pride.objects["/Python/Persistent_Storage"]["_MACHINE_CREDENTIALS"]
        except KeyError:
            machine_id, machine_password = os.urandom(32), os.urandom(32)
            pride.objects["/Python/Persistent_Storage"]["_MACHINE_CREDENTIALS"] = (machine_id, machine_password)
        return base64.standard_b64encode(machine_id), machine_password

    def setup_os_environ(self):
        """ This method is called automatically in Python.__init__; os.environ can
            be customized on startup via modifying Python.defaults["environment_setup"].
            This can be useful for modifying system path only for the duration of the applications run time.
            Currently this is only used to point to this files directory for SDL2 dll files. """
        modes = {"=" : "equals",
                 "+=" : "__add__", # append strings or add ints
                 "-=" : "__sub__", # integer values only
                 "*=" : "__mul__",
                 "/=" : "__div__"}

        for command in self.environment_setup:
            variable, mode, value = command.split()
            if modes[mode] == "equals":
                result = value
            else:
                environment_value = os.environ[variable]
                method = modes[mode]
                result = getattr(environment_value, method)(value)
            self.alert("Setting os.environ[{}] = {}".format(variable, result),
                       level=self.verbosity["os_environ_set"])
            os.environ[variable] = result
            assert os.getenv(variable) == result

    def start_machine(self):
        """ Begins the processing of Instruction objects."""
        processor = pride.objects[self.processor]
        processor.running = True
        processor.run()

    def exit(self, exit_code=0):
        raise SystemExit(exit_code)
