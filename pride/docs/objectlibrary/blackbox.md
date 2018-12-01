blackbox
==============

 Provides network services that do not reveal information about how 
    application logic produces its result. Black_Box_Services receive input
    in the form of keystrokes, mouse clicks, and potentially audio,
    operate on the input in a manner opaque to the client, and return output
    to the client. 

Black_Box_Client
--------------

	No docstring found


Instance defaults: 

	{'audio_source': '/Python/Audio_Manager/Audio_Input',
	 'audio_support': False,
	 'auto_login': True,
	 'auto_register': False,
	 'deleted': False,
	 'dont_save': False,
	 'hash_password_clientside': True,
	 'ip': 'localhost',
	 'iterations': 100000,
	 'microphone_on': False,
	 'mouse_support': False,
	 'output_size': 32,
	 'parse_args': False,
	 'password': None,
	 'password_hashing_algorithm': 'pbkdf2hmac',
	 'password_prompt': '{}: Please provide the pass phrase or word for {}@{}: ',
	 'port': 40022,
	 'refresh_interval': 0.95,
	 'registration_failed_message': "Failed to register with {}@{} as '{}'",
	 'registration_success_message': "Registered with {}@{} as '{}'",
	 'replace_reference_on_load': True,
	 'response_methods': ('handle_response_draw',),
	 'salt': '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
	 'salt_size': 16,
	 'startup_components': (),
	 'sub_algorithm': 'sha512',
	 'target_service': '/Python/Black_Box_Service',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'blackbox.Black_Box_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **handle_response_draw**(self, draw_instructions):

				No documentation available


- **handle_audio_input**(self, audio_bytes):

				No documentation available


- **_make_rpc**(self, *args, **kwargs):

				No documentation available


- **handle_keyboard_input**(self, input_bytes):

				No documentation available


- **receive_response**(self, packet):

				No documentation available


- **handle_mouse_input**(self, mouse_info):

				No documentation available


Black_Box_Service
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
	 'input_types': ('keyboard', 'mouse', 'audio'),
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
	 'validation_failure_string': ".validate: Authorization Failure:\n    ip blacklisted: {}    ip whitelisted: {}\n    session_id logged in: {}\n    method_name: '{}'    method available remotely: {}\n    login allowed: {}    registration allowed: {}",
	 'window_type': 'pride.gui.sdllibrary.Window_Context'}

Method resolution order: 

	(<class 'blackbox.Black_Box_Service'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Service'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **handle_audio_input**(self, audio_bytes):

				No documentation available


- **login_success**(self, username):

				No documentation available


- **handle_input**(self, packed_user_input):

				No documentation available


- **handle_keyboard_input**(self, input_bytes):

				No documentation available


- **handle_mouse_input**(self, mouse_info):

				No documentation available


Event_Structure
--------------

	No documentation available


Method resolution order: 

	(<class 'blackbox.Event_Structure'>, <type 'object'>)

Mouse_Structure
--------------

	No documentation available


Method resolution order: 

	(<class 'blackbox.Mouse_Structure'>, <type 'object'>)

test_black_box_service
--------------

**test_black_box_service**():

				No documentation available
