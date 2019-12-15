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
            self.sdl_window.enable_fullscreen()
        else:
            self.sdl_window.disable_fullscreen()


class Resolution_Selector(pride.gui.widgets.buttons.Selection_Bar):

    defaults = {"resolutions" : ((800, 600), (1024, 768), (1280, 1024),
                                 (1600, 900))}

    def _get_selection(self):
        for index, button in enumerate(self.buttons):
            if button.value:
                return self.resolutions[index]

    def initialize_buttons(self):
        self.buttons = [self.create(self.button_type, text=str(resolution)) for
                        resolution in self.resolutions]


class Window_Options(pride.gui.gui.Window):

    defaults = {"delete_callback" : None}
    autoreferences = ("fullscreen_toggle", "resolution_selector")

    def __init__(self, **kwargs):
        super(Window_Options, self).__init__(**kwargs)
        self.create("pride.gui.widgetlibrary.Task_Bar")
        self.fullscreen_toggle = self.create(Fullscreen_Toggle)
        self.resolution_selector = self.create(Resolution_Selector)

    def delete(self):
        if self.delete_callback is not None:
            self.delete_callback()
        super(Window_Options, self).delete()
