pride.gui.shell
==============



Prompt
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': True,
	 'background_color': (0, 0, 0, 0),
	 'color': (15, 165, 25, 255),
	 'deleted': False,
	 'dont_save': False,
	 'editing': False,
	 'end_of_field': 5,
	 'h': 16,
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'main',
	 'parse_args': False,
	 'program': '',
	 'prompt': '\n>>> ',
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': True,
	 'sdl_window': '',
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

	(<class 'pride.gui.shell.Prompt'>,
	 <class 'pride.gui.widgetlibrary.Text_Box'>,
	 <class 'pride.gui.gui.Container'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **handle_return**(self):

				No documentation available


Python_Shell
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
	 'ip': 'localhost',
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'main',
	 'parse_args': False,
	 'port': 40022,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'size': (800, 600),
	 'startup_components': ('pride.gui.widgetlibrary.Task_Bar',
	                        'pride.gui.gui.Window'),
	 'startup_definitions': '',
	 'target_service': '/Python/Interpreter',
	 'text': '',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'username': '',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.shell.Python_Shell'>,
	 <class 'pride.gui.gui.Application'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **write**(self, data):

				No documentation available
