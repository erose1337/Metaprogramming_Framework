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

import pride
import pride.objectlibrary.base as base
import pride.objectlibrary.authentication3
import pride.objectlibrary.shell
import pride.objectlibrary.user
import pride.site_config

@contextlib.contextmanager
def main_as_name():
    backup = globals()["__name__"]        
    globals()["__name__"] = "__main__"    
    try:
        yield
    finally:
        globals()["__name__"] = backup        
    
class Shell(pride.objectlibrary.authentication3.Authenticated_Client):
    """ Handles keystrokes and sends python source to the Interpreter to 
        be executed. This requires authentication via username/password."""
    defaults = {"username" : "", "password" : "", "startup_definitions" : '', 
                "target_service" : "/Python/Interpreter", "stdout" : None}
    
    verbosity = {"login" : 0, "execute_source" : "vv"}
                
    def login_success(self, message):
        super(Shell, self).login_success(message)        
        sys.stdout.write(">>> ")     
        sys.stdout.flush()
        if self.startup_definitions:
            self.handle_startup_definitions()                
             
    def handle_startup_definitions(self):
        source = pride.compiler.preprocess(self.startup_definitions)
        try:
            compile(source, "Shell", 'exec')
        except:
            self.alert("Startup defintions failed to compile:\n{}",
                       [traceback.format_exc()],
                       level=0)
        else:
            self.startup_definitions = ''            
            self.execute_source(source)
                        
    @pride.objectlibrary.authentication3.remote_procedure_call(callback_name="handle_result")
    def execute_source(self, source): 
        """ Sends source to the interpreter specified in self.target_service for execution """
                                    
    def handle_result(self, packet):
        if packet:        
            (self.stdout or sys.stdout).write('\r' + packet)                            
            

class Interpreter(pride.objectlibrary.authentication3.Authenticated_Service):
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
        self.log = self.create("pride.objectlibrary.fileio.File", 
                               "{}.log".format(filename), 'a+',
                               persistent=False).reference
        self._logger = invoke(self._logger_type)
        
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
            code = pride.compiler.compile(source)
        except (SyntaxError, OverflowError, ValueError):
            result = traceback.format_exc()           
        else:          
            _logger = self._logger
            backup = sys.stdout                 
            sys.stdout = _logger                          
            try:
                exec code in globals()
            except SystemExit:  
                sys.stdout = backup
                raise
            except: # we explicitly really do want to catch everything here   
                _logger.seek(0)
                result = _logger.read() + '\n' + traceback.format_exc()                    
            else:
                self.user_session[username] += source                
                _logger.seek(0)
                result = _logger.read()                         
            log.write("{}\n".format(result))                    
            _logger.truncate(0)      
            sys.stdout = backup
        log.flush()                 
        return result
        
    def _exec_command(self, source):
        """ Executes the supplied source as the __main__ module"""
        code = pride.compiler.compile(source, "__main__")
        with main_as_name():
            exec code in globals(), globals()
            
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
        starts the execution of the Processor component."""
    defaults = {"command" : '',
                "environment_setup" : ("PYSDL2_DLL_PATH = " + 
                                       pride.site_config.GUI_DIRECTORY + os.path.sep, ),
                "startup_components" : ("pride.objectlibrary.storage.Persistent_Storage",
                                        "pride.objectlibrary.vcs.Version_Control",
                                        "pride.objectlibrary.vmlibrary.Processor",                                        
                                        "pride.objectlibrary.fileio.File_System",
                                        "pride.objectlibrary.network.Network_Connection_Manager",
                                        "pride.objectlibrary.network.Network", 
                                        "pride.objectlibrary.interpreter.Interpreter",
                                        "pride.objectlibrary.rpc.Rpc_Connection_Manager",
                                        "pride.objectlibrary.rpc.Rpc_Server",
                                        "pride.objectlibrary.rpc.Rpc_Worker",
                                        "pride.objectlibrary.datatransfer.Data_Transfer_Service",
                                        "pride.objectlibrary.datatransfer.Background_Refresh",
                                        "pride.objectlibrary.encryptedstorage.Encryption_Service"),
                "startup_definitions" : '',
                "interpreter_type" : "pride.objectlibrary.interpreter.Interpreter"}
                     
    parser_ignore = ("environment_setup", "startup_components", 
                     "startup_definitions", "interpreter_type")
                     
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
        self.setup_os_environ()

        session_id, key1, key2, key3, salt = [random_bytes for random_bytes in slide(os.urandom(80), 16)] # ephemeral keys for encrypted in memory only data storage
        self.session = self.create("pride.objectlibrary.user.Session", username=session_id, 
                                   encryption_key=key1,  mac_key=key2, file_system_key=key3, salt=salt)
                                   
        if not self.command:
            command = os.path.join((os.getcwd() if "__file__" 
                                    not in globals() else 
                                    pride.site_config.PRIDE_DIRECTORY), 
                                    os.path.join("programs", "shell_launcher.py"))
        else:
            try:
                machine_info_file = pride.objects["/Python/File_System"].open_file("machine_credentials.bin", 'r')
            except IOError:
                machine_info_file = pride.objects["/Python/File_System"].open_file("machine_credentials.bin", 'w')
                urandom = os.urandom
                machine_id, key1, key2, key3, salt = urandom(16), urandom(16), urandom(16), urandom(16), urandom(16)
                machine_info_file.write(machine_id + key1 + key2 + key3 + salt)
                machine_info_file.flush()
            else:
                machine_info = machine_info_file.read()                
                machine_id = machine_info[:16]
                key1, key2, key3, salt = machine_info[16:32], machine_info[32:48], machine_info[48:64], machine_info[64:80]
            user = pride.objectlibrary.user.User(username=machine_id, encryption_key=key1, mac_key=key2, 
                                   file_system_key=key3, salt=salt, open_command_line=False)                    
            command = self.command  
        source = ''    
        if self.startup_definitions:
            source += self.startup_definitions + "\n"        
        with open(command, 'r') as module_file:
            source += module_file.read()            
        pride.Instruction(self.interpreter, "_exec_command", source).execute()
             
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
            self.alert("Setting os.environ[{}] = {}", (variable, result),
                       level=self.verbosity["os_environ_set"])
            os.environ[variable] = result
            
    def start_machine(self):
        """ Begins the processing of Instruction objects."""
        processor = pride.objects[self.processor]
        processor.running = True
        processor.run()
                
    def exit(self, exit_code=0):
        raise SystemExit(exit_code)
        