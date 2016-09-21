pride.gui.messenger
==============



Add_Contact_Button
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': False,
	 'background_color': (0, 0, 0, 0),
	 'color': (15, 165, 25, 255),
	 'deleted': False,
	 'dont_save': False,
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'text': 'add contact...',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.messenger.Add_Contact_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


Client
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
	 'target_service': '/Python/Data_Transfer_Service',
	 'username': '',
	 'username_prompt': '{}: Please provide the user name for {}@{}: '}

Method resolution order: 

	(<class 'pride.gui.messenger.Client'>,
	 <class 'pride.objectlibrary.datatransfer.Data_Transfer_Client'>,
	 <class 'pride.objectlibrary.authentication3.Authenticated_Client'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **receive**(self, messages):

				No documentation available


Contact_Button
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': False,
	 'background_color': (0, 0, 0, 0),
	 'color': (15, 165, 25, 255),
	 'deleted': False,
	 'dont_save': False,
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'text': '',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.messenger.Contact_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


Contacts
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': False,
	 'background_color': (0, 0, 0, 0),
	 'color': (15, 165, 25, 255),
	 'deleted': False,
	 'dont_save': False,
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'main',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'size': (800, 600),
	 'startup_components': (),
	 'text': '',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.messenger.Contacts'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

Message_Database
--------------

	No docstring found


Instance defaults: 

	{'auto_commit': True,
	 'connection': None,
	 'cursor': None,
	 'database_name': '',
	 'deleted': False,
	 'detect_types_flags': 1,
	 'dont_save': False,
	 'hash_function': 'SHA256',
	 'indexable': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'return_cursor': False,
	 'startup_components': (),
	 'text_factory': <type 'str'>,
	 'wrapped_object': None}

Method resolution order: 

	(<class 'pride.gui.messenger.Message_Database'>,
	 <class 'pride.objectlibrary.database.Database'>,
	 <class 'pride.objectlibrary.base.Wrapper'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **store_message**(self, sender, message, timestamp):

				No documentation available


- **retrieve_message**(self, sender, message_id):

				No documentation available


Messenger
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': False,
	 'background_color': (0, 0, 0, 0),
	 'color': (15, 165, 25, 255),
	 'current_contact': '',
	 'deleted': False,
	 'display_message_timestamps': True,
	 'dont_save': False,
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'main',
	 'parse_args': False,
	 'password': '',
	 'password_prompt': '{}: Please enter the password: ',
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'size': (800, 600),
	 'startup_components': ('pride.gui.widgetlibrary.Task_Bar',
	                        'pride.gui.gui.Window'),
	 'text': '',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.messenger.Messenger'>,
	 <class 'pride.gui.gui.Application'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **receive_message**(self, sender, message):

				No documentation available


- **send_message**(self, message):

				No documentation available


- **set_current_contact**(self, contact):

				No documentation available


Popup_Menu
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': False,
	 'background_color': (15, 65, 15, 225),
	 'color': (15, 165, 25, 255),
	 'deleted': False,
	 'dont_save': False,
	 'h_range': (0, 300),
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'popup_menu',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'size': (800, 600),
	 'startup_components': (),
	 'text': '',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'w_range': (0, 400),
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.messenger.Popup_Menu'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **handle_input**(self, text):

				No documentation available
