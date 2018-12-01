helloworldrpc
==============



Rpc_Hello_World_Client
--------------

	No docstring found


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
	 'target_service': '/Rpc_Hello_World_Service',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'helloworldrpc.Rpc_Hello_World_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **_make_rpc**(self, *args, **kwargs):

				No documentation available


Rpc_Hello_World_Service
--------------

	No docstring found


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

	(<class 'helloworldrpc.Rpc_Hello_World_Service'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Service'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **hello_world**(self, argument, *args, **kwargs):

				No documentation available


test_hello_world_rpc
--------------

**test_hello_world_rpc**():

				No documentation available
