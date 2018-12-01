authentication3
==============



Authenticated_Client
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
	 'target_service': '/Python/Authenticated_Service',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **register_failure**(self):

				No documentation available


- **new_call**(args, **kwargs):

				No documentation available


- **register_success**(self):

				No documentation available


- **new_call**(args, **kwargs):

				No documentation available


- **login_result**(self, server_response):

				No documentation available


- **new_call**(self, *args, **kwargs):

				No documentation available


- **login_success**(self, login_message):

				No documentation available


- **login_failure**(self, server_response):

				No documentation available


- **register_results**(self, server_response):

				No documentation available


- **on_load**(self, attributes):

				No documentation available


- **handle_not_logged_in**(self, instruction, callback):

				No documentation available


- **get_credentials**(self):

				No documentation available


- **change_credential_result**(self, server_response):

				No documentation available


- **new_call**(args, **kwargs):

				No documentation available


- **logout_success**(self, server_response):

				No documentation available


- **delete**(self):

				No documentation available


Authenticated_Service
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

	(<class 'authentication3.Authenticated_Service'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **register_failure**(self, username):

		 usage: called during register() when registration fails.
            returns: (success_flag, server_message, session_id)
                - success_flag is False when registration fails
                - server message is a string to be print or used by the client


- **register**(self, identifier, password_verifier):

		 usage: 
                
                ...
                def get_credentials(self):
                    return self.username, self.password_hash if self.hash_password_clientside else self.password
                            
                @pride.functions.decorators.with_arguments_from(lambda self: ((self, ) + self.get_credentials(), {}))        
                @remote_procedure_call(callback_name="register_results")
                def register(self, username, password_hash): 
                    pass      
                                
            On success, inserts (identifier, hashed_password_verifier, salt) into database and returns register_success()
            On failure, returns register_failure() 


- **register_success**(self, username):

		 usage: called during register() when registration succeeds.
            returns: (success_flag, server_message, session_id)            
                - success_flag is True when registration succeeds 
                - server message is a string to be printed or used by the client


- **change_credentials**(self, identifier, password_verifier, new_identifier, new_password_verifier):

				No documentation available


- **execute_remote_procedure_call**(self, session_id, peername, method_name, args, kwargs):

				No documentation available


- **logout**(self):

		 usage:
        
            @pride.functions.decorators.call_if(logged_in=True) # don't call if not logged in
            @pride.functions.decorators.exit(_reset_login_flags)
            @remote_procedure_call(callback_name="logout_success")
            def logout(self): 
                pass
        
            Returns None. Forgets the current session associated with the currently logged in user.


- **login_success**(self, username):

		 usage: called inside login() when an attempt succeeds
            returns: (success_flag, login_message, session_id)
                - success_flag is True when login succeeds
                - login_message is a string to be printed or used by the client                
                - session_id is a string of random bytes that identifies the client


- **validate**(self, session_id, peername, method_name):

		 Determines whether or not the peer with the supplied
            session id is allowed to call the requested method.

            Sets current_session attribute to (session_id, peername) if validation
            is successful. 


- **on_load**(self, attributes):

				No documentation available


- **login_failure**(self, username):

		 usage: called inside login() when an attempt fails
            returns: (success_flag, login_message, session_id)
                - success_flag is False when login fails
                - login_message is a string to be printed or used by the client                
                - session_id is reset to '0'


- **login**(self, username, password):

		 usage:
                
                ...
                def _login(self):                                
                    self._logging_in = True    
                    self.session.id = '0'
                    return (self, ) + self.get_credentials(), {}
                        
                @pride.functions.decorators.with_arguments_from(_login)
                @remote_procedure_call(callback_name="login_result")
                def login(self, username, password):
                    pass        
                
                ...
                
            Returns login_success() if username and password are verified
            Returns login_failure() otherwise


Instruction
--------------

	 usage: Instruction(component_name, method_name,
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
        function can be provided.


Method resolution order: 

	(<class 'pride.Instruction'>, <type 'object'>)

- **execute**(self, priority, callback):

		 usage: instruction.execute(priority=0.0, callback=None)

            Submits an instruction to the processing queue.
            The instruction will be executed in priority seconds.
            An optional callback function can be provided if the return value
            of the instruction is needed. 


- **purge**(cls, reference):

				No documentation available


- **unschedule**(self):

				No documentation available


SecurityError
--------------

	No documentation available


Method resolution order: 

	(<class 'pride.errors.SecurityError'>,
	 <type 'exceptions.Exception'>,
	 <type 'exceptions.BaseException'>,
	 <type 'object'>)

UnauthorizedError
--------------

	No documentation available


Method resolution order: 

	(<class 'pride.errors.UnauthorizedError'>,
	 <class 'pride.errors.SecurityError'>,
	 <type 'exceptions.Exception'>,
	 <type 'exceptions.BaseException'>,
	 <type 'object'>)

hash_function
--------------

**hash_function**(algorithm_name, backend):

		 Returns a Hash object of type algorithm_name from 
            cryptography.hazmat.primitives.hashes 


remote_procedure_call
--------------

**new_call**(args, **kwargs):

				No documentation available


test_Authenticated_Service3
--------------

**test_Authenticated_Service3**():

				No documentation available
