interpreter
==============

 Provides an entry point to the environment and a shell connection for interacting with it. 

Interpreter
--------------

	 Executes python source. Requires authentication from remote hosts. 
        The source code and return value of all requests are logged. 


Instance defaults: 

	{'_logger_type': 'StringIO.StringIO',
	 'allow_login': True,
	 'allow_registration': False,
	 'constant_time_registration': True,
	 'database_name': '',
	 'database_type': 'pride.objectlibrary.database.Database',
	 'deleted': False,
	 'dont_save': False,
	 'help_string': 'Type "help", "copyright", "credits" or "license" for more information.',
	 'iterations': 100000,
	 'login_failure_message': 'Failed to login to {} as {}@{}',
	 'login_message': 'Welcome {} from {}\nPython {} on {}\n{}\n',
	 'login_success_message': 'Welcome to the {}, {}@{}',
	 'output_size': 32,
	 'parse_args': False,
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'registration_failure_message': "Failed to register as '{}'@{}",
	 'registration_success_message': "Registered as '{}'@{}",
	 'replace_reference_on_load': True,
	 'salt_size': 16,
	 'session_id_size': 16,
	 'startup_components': (),
	 'sub_algorithm': 'sha512',
	 'validation_failure_string': ".validate: Authorization Failure:\n    ip blacklisted: {}    ip whitelisted: {}\n    session_id logged in: {}\n    method_name: '{}'    method available remotely: {}\n    login allowed: {}    registration allowed: {}"}

Method resolution order: 

	(<class 'interpreter.Interpreter'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Service'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **execute_instruction**(self, instruction, priority, callback):

		 Executes the supplied instruction with the specified priority and callback 


- **execute_source**(self, source):

				No documentation available


- **login_success**(self, username):

				No documentation available


Python
--------------

	 The "main" class. Provides an entry point to the environment. 
        Instantiating this component and calling the start_machine method 
        starts the execution of the Processor component.


Instance defaults: 

	{'command': '',
	 'deleted': False,
	 'dont_save': False,
	 'environment_setup': ('PYSDL2_DLL_PATH = c:\\users\\_\\pythonbs\\pride\\gui\\',),
	 'interpreter_type': 'pride.objectlibrary.interpreter.Interpreter',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ('pride.objectlibrary.storage.Persistent_Storage',
	                        'pride.objectlibrary.vcs.Version_Control',
	                        'pride.objectlibrary.vmlibrary.Processor',
	                        'pride.objectlibrary.fileio.File_System',
	                        'pride.objectlibrary.network.Network_Connection_Manager',
	                        'pride.objectlibrary.network.Network',
	                        'pride.objectlibrary.interpreter.Interpreter',
	                        'pride.objectlibrary.rpc.Rpc_Connection_Manager',
	                        'pride.objectlibrary.rpc.Rpc_Server',
	                        'pride.objectlibrary.rpc.Rpc_Worker',
	                        'pride.objectlibrary.datatransfer.Data_Transfer_Service',
	                        'pride.objectlibrary.datatransfer.Background_Refresh',
	                        'pride.objectlibrary.encryptedstorage.Encryption_Service'),
	 'startup_definitions': ''}

Method resolution order: 

	(<class 'interpreter.Python'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **start_machine**(self):

		 Begins the processing of Instruction objects.


- **exit**(self, exit_code):

				No documentation available


- **setup_os_environ**(self):

		 This method is called automatically in Python.__init__; os.environ can
            be customized on startup via modifying Python.defaults["environment_setup"].
            This can be useful for modifying system path only for the duration of the applications run time.
            Currently this is only used to point to this files directory for SDL2 dll files. 


Shell
--------------

	 Handles keystrokes and sends python source to the Interpreter to 
        be executed. This requires authentication via username/password.


Instance defaults: 

	{'auto_login': True,
	 'auto_register': False,
	 'deleted': False,
	 'dont_save': False,
	 'hash_password_clientside': True,
	 'ip': 'localhost',
	 'iterations': 100000,
	 'output_size': 32,
	 'parse_args': False,
	 'password': '',
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'password_prompt': '{}: Please provide the pass phrase or word for {}@{}: ',
	 'port': 40022,
	 'registration_failed_message': "Failed to register with {}@{} as '{}'",
	 'registration_success_message': "Registered with {}@{} as '{}'",
	 'replace_reference_on_load': True,
	 'salt': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
	 'salt_size': 16,
	 'startup_components': (),
	 'startup_definitions': '',
	 'stdout': None,
	 'sub_algorithm': 'sha512',
	 'target_service': '/Python/Interpreter',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'interpreter.Shell'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **_make_rpc**(self, *args, **kwargs):

				No documentation available


- **login_success**(self, message):

				No documentation available


- **handle_result**(self, packet):

				No documentation available


- **handle_startup_definitions**(self):

				No documentation available


main_as_name
--------------

**main_as_name**(args, **kwds):

				No documentation available
