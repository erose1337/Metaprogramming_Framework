pride.gui.sdllibrary
==============



Font_Manager
--------------

	No docstring found


Instance defaults: 

	{'default_background': (0, 0, 0),
	 'default_color': (150, 150, 255),
	 'default_font_size': 14,
	 'deleted': False,
	 'dont_save': False,
	 'font_path': 'c:\\users\\_\\pythonbs\\pride\\gui\\resources\\fonts\\Aero.ttf',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.Font_Manager'>,
	 <class 'pride.gui.sdllibrary.SDL_Component'>,
	 <class 'pride.objectlibrary.base.Proxy'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **save**(self):

				No documentation available


- **on_load**(self, attributes):

				No documentation available


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


Renderer
--------------

	No docstring found


Instance defaults: 

	{'blendmode_flag': 1,
	 'deleted': False,
	 'dont_save': False,
	 'flags': 2,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.Renderer'>,
	 <class 'pride.gui.sdllibrary.SDL_Component'>,
	 <class 'pride.objectlibrary.base.Proxy'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **draw**(self, texture, draw_instructions, background, clear):

				No documentation available


- **merge_layers**(self, textures):

				No documentation available


- **get_text_size**(self, area, text, **kwargs):

				No documentation available


- **set_render_target**(self, texture):

				No documentation available


- **draw_rect_width**(self, area, **kwargs):

				No documentation available


- **draw_text**(self, area, text, **kwargs):

				No documentation available


SDL_Component
--------------

	No docstring found


Instance defaults: 

	{'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.SDL_Component'>,
	 <class 'pride.objectlibrary.base.Proxy'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

SDL_User_Input
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_run_queued': False,
	 'active_item': None,
	 'context_managed': False,
	 'deleted': False,
	 'dont_save': False,
	 'event_verbosity': 0,
	 'parse_args': False,
	 'priority': 0.04,
	 'replace_reference_on_load': True,
	 'reschedule_run_after_exception': True,
	 'run_callback': None,
	 'run_condition': '',
	 'running': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.SDL_User_Input'>,
	 <class 'pride.objectlibrary.vmlibrary.Process'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **handle_textinput**(self, event):

				No documentation available


- **handle_unhandled_event**(self, event):

				No documentation available


- **handle_mousemotion**(self, event):

				No documentation available


- **handle_quit**(self, event):

				No documentation available


- **run**(self):

				No documentation available


- **handle_mousewheel**(self, event):

				No documentation available


- **handle_keydown**(self, event):

				No documentation available


- **setup_event_handler**(self):

				No documentation available


- **save**(self):

				No documentation available


- **handle_mousebuttondown**(self, event):

				No documentation available


- **handle_mousebuttonup**(self, event):

				No documentation available


- **on_load**(self, attributes):

				No documentation available


- **handle_keyup**(self, event):

				No documentation available


- **get_hotkey**(self, instance, key_press):

				No documentation available


SDL_Window
--------------

	No docstring found


Instance defaults: 

	{'area': (0, 0, 800, 600),
	 'deleted': False,
	 'dont_save': False,
	 'h': 600,
	 'name': '/Python',
	 'parse_args': False,
	 'position': (0, 0),
	 'priority': 0.04,
	 'renderer_flags': 10,
	 'replace_reference_on_load': True,
	 'showing': True,
	 'size': (800, 600),
	 'startup_components': (),
	 'texture_access_flag': 2,
	 'w': 800,
	 'window_flags': None,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.SDL_Window'>,
	 <class 'pride.gui.sdllibrary.SDL_Component'>,
	 <class 'pride.objectlibrary.base.Proxy'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **run**(self):

				No documentation available


- **pack**(self, modifiers):

				No documentation available


- **draw**(self, instructions):

				No documentation available


- **remove**(self, instance):

				No documentation available


- **invalidate_object**(self, instance):

				No documentation available


- **delete**(self):

				No documentation available


- **get_mouse_position**(self):

				No documentation available


- **get_mouse_state**(self):

				No documentation available


- **create**(self, *args, **kwargs):

				No documentation available


Sprite_Factory
--------------

	No docstring found


Instance defaults: 

	{'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.Sprite_Factory'>,
	 <class 'pride.gui.sdllibrary.SDL_Component'>,
	 <class 'pride.objectlibrary.base.Proxy'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **save**(self):

				No documentation available


Window_Context
--------------

	No docstring found


Instance defaults: 

	{'area': (0, 0, 800, 600),
	 'deleted': False,
	 'dont_save': False,
	 'h': 600,
	 'name': '/Python',
	 'parse_args': False,
	 'position': (0, 0),
	 'priority': 0.04,
	 'renderer_flags': 10,
	 'replace_reference_on_load': True,
	 'showing': False,
	 'size': (800, 600),
	 'startup_components': (),
	 'texture_access_flag': 2,
	 'w': 800,
	 'window_flags': None,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.Window_Context'>,
	 <class 'pride.gui.sdllibrary.SDL_Window'>,
	 <class 'pride.gui.sdllibrary.SDL_Component'>,
	 <class 'pride.objectlibrary.base.Proxy'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **run**(self):

				No documentation available


- **invalidate_object**(self, item):

				No documentation available


Window_Handler
--------------

	No docstring found


Instance defaults: 

	{'deleted': False,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'startup_components': ()}

Method resolution order: 

	(<class 'pride.gui.sdllibrary.Window_Handler'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **handle_shown**(self, event):

				No documentation available


- **handle_restored**(self, event):

				No documentation available


- **handle_focus_gained**(self, event):

				No documentation available


- **handle_hidden**(self, event):

				No documentation available


- **handle_event**(self, event):

				No documentation available


- **handle_minimized**(self, event):

				No documentation available


- **handle_exposed**(self, event):

				No documentation available


- **handle_enter**(self, event):

				No documentation available


- **handle_moved**(self, event):

				No documentation available


- **handle_maximized**(self, event):

				No documentation available


- **handle_close**(self, event):

				No documentation available


- **handle_size_changed**(self, event):

				No documentation available


- **handle_focus_lost**(self, event):

				No documentation available


- **handle_leave**(self, event):

				No documentation available


- **handle_resized**(self, event):

				No documentation available
