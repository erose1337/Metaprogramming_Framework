pride.gui.gui
==============



Application
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

	(<class 'pride.gui.gui.Application'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **draw_texture**(self):

				No documentation available


Button
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

	(<class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

Container
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

	(<class 'pride.gui.gui.Container'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

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


Minimal_Theme
--------------

	No docstring found


Instance defaults: 

	{'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': (),
	 'wrapped_object': None}

Method resolution order: 

	(<class 'pride.gui.gui.Minimal_Theme'>,
	 <class 'pride.gui.gui.Theme'>,
	 <class 'pride.objectlibrary.base.Wrapper'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **draw_texture**(self):

				No documentation available


Organizer
--------------

	No docstring found


Instance defaults: 

	{'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.gui.Organizer'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **set_pack_mode**(self, instance, value):

				No documentation available


- **pack_top**(self, parent, item, count, length):

				No documentation available


- **get_pack_mode**(self, instance):

				No documentation available


- **pack_left**(self, parent, item, count, length):

				No documentation available


- **pack_main**(self, parent, item, count, length):

				No documentation available


- **pack_grid**(self, parent, item, count, length):

				No documentation available


- **pack_popup_menu**(self, parent, item, count, length):

				No documentation available


- **pack_bottom**(self, parent, item, count, length):

				No documentation available


- **pack_drop_down_menu**(self, parent, item, count, length):

				No documentation available


- **pack_right**(self, parent, item, count, length):

				No documentation available


- **pack_z**(self, parent, item, count, length):

				No documentation available


- **add_pack_method**(self, name, callback):

				No documentation available


- **pack**(self, item):

				No documentation available


SDL_Rect
--------------

	No documentation available


Method resolution order: 

	(<class 'sdl2.rect.SDL_Rect'>,
	 <type '_ctypes.Structure'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

Theme
--------------

	No docstring found


Instance defaults: 

	{'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': (),
	 'wrapped_object': None}

Method resolution order: 

	(<class 'pride.gui.gui.Theme'>,
	 <class 'pride.objectlibrary.base.Wrapper'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **draw_texture**(self):

				No documentation available


Window
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

	(<class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

Window_Object
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
	 'pack_mode': '',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
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

	(<class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


- **select**(self, mouse):

				No documentation available


- **mousemotion**(self, x_change, y_change, top_level):

				No documentation available


- **create**(self, *args, **kwargs):

				No documentation available


- **add**(self, _object):

				No documentation available


- **release**(self, mouse):

				No documentation available


- **draw_texture**(self):

				No documentation available


- **right_click**(self, mouse):

				No documentation available


- **press**(self, mouse):

				No documentation available


- **handle_backspace**(self):

				No documentation available


- **pack**(self, modifiers):

				No documentation available


- **remove**(self, _object):

				No documentation available


- **deselect**(self, mouse, next_active_object):

				No documentation available


- **toggle_hidden**(self):

				No documentation available


- **handle_return**(self):

				No documentation available


- **draw**(self, figure, *args, **kwargs):

		 Draws the specified figure on self. figure can be any shape supported
            by the renderer, namely: "rect", "line", "point", "text", and "rect_width".
            The first argument(s) will include the destination of the shape in the
            form appropriate for the figure specified (i.e. an area for a rect, a
            pair of points for a point). For a full list of arguments for a 
            particular figure, see the appropriate draw method of the renderer. 


- **mousewheel**(self, x_amount, y_amount):

				No documentation available


- **text_entry**(self, text):

				No documentation available


- **delete**(self):

				No documentation available


create_texture
--------------

**create_texture**(size, access, factory, renderer):

				No documentation available
