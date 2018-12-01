pride.gui.text_editor
==============



Edit_Button
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
	 'pack_mode': 'left',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'text': 'Edit',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.text_editor.Edit_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

File_Button
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_popup': None,
	 '_popup_type': 'pride.gui.text_editor.File_Menu',
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
	 'pack_mode': 'left',
	 'parse_args': False,
	 'popup_type': '',
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'text': 'File',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.text_editor.File_Button'>,
	 <class 'pride.gui.widgetlibrary.Popup_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

File_Menu
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
	 'size': (0, 0),
	 'startup_components': ('pride.gui.text_editor.New_Button',
	                        'pride.gui.text_editor.Open_Button',
	                        'pride.gui.text_editor.Save_Button'),
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

	(<class 'pride.gui.text_editor.File_Menu'>,
	 <class 'pride.gui.gui.Container'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

New_Button
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
	 'text_file_type': 'pride.gui.text_editor.Text_File',
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.text_editor.New_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


Open_Button
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
	 'text_file_type': 'pride.gui.text_editor.Text_File',
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.text_editor.Open_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


Options_Button
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
	 'pack_mode': 'left',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'text': 'options',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.text_editor.Options_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

Save_Button
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

	(<class 'pride.gui.text_editor.Save_Button'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


Shortcut
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
	 'h_range': (0, 40),
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'grid',
	 'parse_args': False,
	 'popup_type': 'pride.gui.text_editor.Text_Editor',
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'text': 'Text Editor',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'w_range': (0, 40),
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.text_editor.Shortcut'>,
	 <class 'pride.gui.widgetlibrary.Icon'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

Text_Editor
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

	(<class 'pride.gui.text_editor.Text_Editor'>,
	 <class 'pride.gui.gui.Application'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

Text_File
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
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'outline_width': 1,
	 'pack_mode': 'top',
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

	(<class 'pride.gui.text_editor.Text_File'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **text_entry**(self, text):

				No documentation available
