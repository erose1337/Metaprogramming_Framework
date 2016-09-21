pride.gui.chess
==============



Bishop
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
	 'text': 'Bishop',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.chess.Bishop'>,
	 <class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **get_potential_moves**(self):

				No documentation available


Chess
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_scroll_bar_h': None,
	 '_scroll_bar_w': None,
	 'allow_text_edit': False,
	 'background_color': (0, 0, 0, 0),
	 'black_background_color': (25, 25, 25, 155),
	 'black_color': (75, 75, 125, 255),
	 'black_square_color': (55, 55, 55, 255),
	 'black_square_outline_color': (0, 0, 0, 255),
	 'black_text_color': (230, 230, 230, 255),
	 'capture_outline_color': (255, 75, 125, 255),
	 'color': (15, 165, 25, 255),
	 'column_count': 8,
	 'deleted': False,
	 'dont_save': False,
	 'held': False,
	 'hidden': False,
	 'movable': False,
	 'movable_square_outline_color': (155, 155, 255, 255),
	 'outline_width': 1,
	 'pack_mode': 'main',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'row_count': 8,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'selected_piece_outline_color': (255, 175, 125, 255),
	 'size': (800, 600),
	 'square_outline_color': (0, 0, 0, 255),
	 'startup_components': ('pride.gui.widgetlibrary.Task_Bar',
	                        'pride.gui.gui.Window'),
	 'text': '',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'white_background_color': (205, 205, 205, 155),
	 'white_color': (255, 255, 255, 255),
	 'white_square_color': (205, 205, 205, 255),
	 'white_square_outline_color': (0, 0, 0, 255),
	 'white_text_color': (55, 55, 85, 255),
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.chess.Chess'>,
	 <class 'pride.gui.boardgame.Board_Game'>,
	 <class 'pride.gui.gui.Application'>,
	 <class 'pride.gui.gui.Window'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **setup_game**(self):

				No documentation available


Game_Piece
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
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

	(<class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **left_click**(self, mouse):

				No documentation available


- **get_potential_moves**(self):

				No documentation available


- **toggle_outline_highlight**(self, color):

				No documentation available


- **toggle_highlight_available_moves**(self):

				No documentation available


King
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
	 'text': 'King',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.chess.King'>,
	 <class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **get_potential_moves**(self):

				No documentation available


Knight
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
	 'text': 'Knight',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.chess.Knight'>,
	 <class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **get_potential_moves**(self):

				No documentation available


Pawn
--------------

	No docstring found


Instance defaults: 

	{'_ignore_click': False,
	 '_move_direction': 1,
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
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

	(<class 'pride.gui.chess.Pawn'>,
	 <class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **get_potential_moves**(self):

				No documentation available


Queen
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
	 'text': 'Queen',
	 'text_color': (15, 165, 25, 255),
	 'texture': None,
	 'texture_size': (800, 600),
	 'theme_type': 'pride.gui.gui.Minimal_Theme',
	 'wrap_text': True,
	 'x': 0,
	 'y': 0,
	 'z': 0}

Method resolution order: 

	(<class 'pride.gui.chess.Queen'>,
	 <class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **get_potential_moves**(self):

				No documentation available


- **get_potential_moves**(self):

				No documentation available


- **get_potential_moves**(self):

				No documentation available


Rook
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
	 'outline_width': 2,
	 'pack_mode': 'top',
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'scroll_bars_enabled': False,
	 'sdl_window': '',
	 'shape': 'rect',
	 'size': (0, 0),
	 'startup_components': (),
	 'team': '',
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

	(<class 'pride.gui.chess.Rook'>,
	 <class 'pride.gui.boardgame.Game_Piece'>,
	 <class 'pride.gui.gui.Button'>,
	 <class 'pride.gui.gui.Window_Object'>,
	 <class 'pride.gui.shapes.Bounded_Shape'>,
	 <class 'pride.gui.shapes.Shape'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **get_potential_moves**(self):

				No documentation available


determine_move_information
--------------

**determine_move_information**(game_board, piece, next_row, column):

				No documentation available
