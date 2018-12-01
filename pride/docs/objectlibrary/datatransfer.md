datatransfer
==============

 pride.objectlibrary.datatransfer - Authenticated services for transferring data on a network
    Constructs a service for the transfer of arbitrary data from one registered 
    party to another. 

Background_Refresh
--------------

	 Usage: pride.objects['/Python/Background_Refresh'].add(client_object)
    
        Calls client.refresh for all clients in Background_Refresh.children.
        
        Newly initialized Data_Transfer_Client objects will call this method
        automatically inside the __init__ method. 


Instance defaults: 

	{'_run_queued': False,
	 'context_managed': False,
	 'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'priority': 0.5,
	 'replace_reference_on_load': True,
	 'reschedule_run_after_exception': True,
	 'run_callback': None,
	 'run_condition': '',
	 'running': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'datatransfer.Background_Refresh'>,
	 <class 'pride.objectlibrary.vmlibrary.Process'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **run**(self):

				No documentation available


Data_Transfer_Client
--------------

	 Client program for sending data to a party registered with the target service. 
        
        Security is provided by TLS, which provides end to end security between
        machines. However, any Data Transfer Service that forwards the data towards
        its destination will be able to view and/or manipulate the data. 


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
	 'password': None,
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'password_prompt': '{}: Please provide the pass phrase or word for {}@{}: ',
	 'port': 40022,
	 'registration_failed_message': "Failed to register with {}@{} as '{}'",
	 'registration_success_message': "Registered with {}@{} as '{}'",
	 'replace_reference_on_load': True,
	 'salt': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
	 'salt_size': 16,
	 'startup_components': (),
	 'sub_algorithm': 'sha512',
	 'target_service': '/Python/Data_Transfer_Service',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'datatransfer.Data_Transfer_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **refresh**(self):

		 Checks for new data from the server 


- **receive**(self, messages):

		 Receives messages and supplies them to alert for user notification.
            self.verbosity may feature usernames of other clients; entries not
            found default to 0. 


- **_make_rpc**(self, *args, **kwargs):

				No documentation available


Data_Transfer_Service
--------------

	 Service for transferring arbitrary data from one registered client to another 


Instance defaults: 

	{'allow_login': True,
	 'allow_registration': True,
	 'constant_time_registration': True,
	 'database_name': '',
	 'database_type': 'pride.objectlibrary.database.Database',
	 'deleted': False,
	 'dont_save': False,
	 'iterations': 100000,
	 'login_failure_message': 'Failed to login to {} as {}@{}',
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

	(<class 'datatransfer.Data_Transfer_Service'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Service'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **send_to**(self, receiver, message):

				No documentation available


File_Storage_Daemon
--------------

	No docstring found


Instance defaults: 

	{'auto_login': True,
	 'auto_register': False,
	 'deleted': False,
	 'dont_save': False,
	 'file_type': '',
	 'hash_password_clientside': True,
	 'ip': 'localhost',
	 'iterations': 100000,
	 'output_size': 32,
	 'parse_args': False,
	 'password': None,
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'password_prompt': '{}: Please provide the pass phrase or word for {}@{}: ',
	 'port': 40022,
	 'registration_failed_message': "Failed to register with {}@{} as '{}'",
	 'registration_success_message': "Registered with {}@{} as '{}'",
	 'replace_reference_on_load': True,
	 'salt': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
	 'salt_size': 16,
	 'startup_components': (),
	 'sub_algorithm': 'sha512',
	 'target_service': '/Python/Data_Transfer_Service',
	 'username': 'File_Storage_Daemon',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'datatransfer.File_Storage_Daemon'>,
	 <class 'datatransfer.Data_Transfer_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **receive**(self, message):

				No documentation available


File_Transfer
--------------

	No docstring found


Instance defaults: 

	{'auto_login': True,
	 'auto_register': False,
	 'deleted': False,
	 'dont_save': False,
	 'file': None,
	 'file_type': 'open',
	 'filename': '',
	 'hash_password_clientside': True,
	 'ip': 'localhost',
	 'iterations': 100000,
	 'output_size': 32,
	 'parse_args': False,
	 'password': None,
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'password_prompt': '{}: Please provide the pass phrase or word for {}@{}: ',
	 'permission_string': "{}:{} Accept file transfer from '{}'?\n'{}' ({} bytes) ",
	 'port': 40022,
	 'receivers': (),
	 'registration_failed_message': "Failed to register with {}@{} as '{}'",
	 'registration_success_message': "Registered with {}@{} as '{}'",
	 'replace_reference_on_load': True,
	 'salt': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
	 'salt_size': 16,
	 'startup_components': (),
	 'sub_algorithm': 'sha512',
	 'target_service': '/Python/Data_Transfer_Service',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'datatransfer.File_Transfer'>,
	 <class 'datatransfer.Data_Transfer_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **receive**(self, messages):

				No documentation available


Proxy
--------------

	No docstring found


Instance defaults: 

	{'auto_login': True,
	 'auto_register': True,
	 'deleted': False,
	 'dont_save': False,
	 'hash_password_clientside': True,
	 'ip': 'localhost',
	 'iterations': 100000,
	 'output_size': 32,
	 'parse_args': False,
	 'password': None,
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'password_prompt': '{}: Please provide the pass phrase or word for {}@{}: ',
	 'port': 40022,
	 'registration_failed_message': "Failed to register with {}@{} as '{}'",
	 'registration_success_message': "Registered with {}@{} as '{}'",
	 'replace_reference_on_load': True,
	 'salt': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
	 'salt_size': 16,
	 'startup_components': (),
	 'sub_algorithm': 'sha512',
	 'target_service': '/Python/Data_Transfer_Service',
	 'username': 'Proxy',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'datatransfer.Proxy'>,
	 <class 'datatransfer.Data_Transfer_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **receive**(self, messages):

				No documentation available


file_operation
--------------

**file_operation**(filename, mode, method, file_type, offset, data):

				No documentation available


test_File_Transfer
--------------

**test_File_Transfer**():

				No documentation available


test_dts
--------------

**test_dts**():

				No documentation available
