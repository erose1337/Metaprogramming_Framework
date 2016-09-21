vcs
==============



Version_Control
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

	(<class 'vcs.Version_Control'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Service'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **load_module**(self, module_name, module_id, repo_id):

				No documentation available


- **save_module**(self, module_name, module_source, module_id, repo_id):

				No documentation available
