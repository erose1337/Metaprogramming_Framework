# fullscreen toggle     off   on
# resolution presets
#   800x600  1024x768  ...

# specify field type, name, states, default state,
# dictionary of field:value pairs
#

import pride.gui.gui
import pride.gui.widgets.buttons

class Fullscreen_Toggle(pride.gui.widgets.buttons.Toggle):

    defaults = {"label" : "Fullscreen"}

    def left_click(self, mouse):
        super(Fullscreen_Toggle, self).left_click(mouse)
        if self.state:
            self.sdl_window.



class Window_Options(pride.gui.gui.Window):

    autoreferences = ("fullscreen_toggle", )

    def __init__(self, **kwargs):
        super(Window_Options, self).__init__(**kwargs)
        self.fullscreen_toggle = self.create(Fullscreen_Toggle)
        self.resolution_selector = self.create(Resolution_Selector)
