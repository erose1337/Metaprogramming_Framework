import pride.gui.gui
import pride.gui.widgetlibrary

class Color_Field(pride.gui.gui.Container):

    defaults = {"field_info" : tuple(), "field_attributes" : dict(),
                "pack_mode" : "top"}

    def __init__(self, **kwargs):
        super(Color_Field, self).__init__(**kwargs)
        field_name, _object = self.field_info
        for key, bounds in self.field_attributes.items():
            self.create(pride.gui.widgetlibrary.Slider_Widget, label=key,
                        bounds=bounds, target=(_object, key), h_range=(0, .10),
                        on_adjustment=self._adjustment_callback)

    def _adjustment_callback(self):
        queue = pride.objects[self.sdl_window].predraw_queue
        method = self.target_theme.update_theme_users
        if method not in queue:
            queue.append(method)

    def readjust_sliders(self):
        for slider_widget in self.objects["Slider_Widget"]:
            slider_widget.readjust_sliders()


class Profile_Customizer(pride.gui.widgetlibrary.Tab_Switching_Window):

    color_keys = ("background", "shadow", "text", "text_background")
    defaults = {"profile_info" : None}
    required_attributes = ("profile_info", )

    def readjust_sliders(self):
        for tab_reference in pride.objects[self.tab_bar].tabs:
            pride.objects[pride.objects[tab_reference].window].readjust_sliders()

    def initialize_tabs_and_windows(self):
        self.tab_types = tuple(pride.gui.widgetlibrary.Tab_Button.from_info(text=text, include_delete_button=False) for
                               text in sorted(self.profile_info.keys()))
        super(Profile_Customizer, self).initialize_tabs_and_windows()

    def create_windows(self):
        # create r/g/b/a/ sliders for each color key in profile_info
        info = self.profile_info
        target_theme = self.target_theme
        for index, tab_reference in enumerate(pride.objects[self.tab_bar].tabs):
            tab = pride.objects[tab_reference]
            key = tab.text
            _object = info[key]
            try:
                kwargs = {"field_attributes" : {'r' : _object.r_range, 'g' : _object.g_range,
                                                'b' : _object.b_range, 'a' : _object.a_range},
                          "field_info" : (key, _object)}
            except AttributeError:
                kwargs = {"field_attributes" : {key : (0, 16)},
                          "field_info" : (key, info)}
            kwargs["target_theme"] = target_theme
            field = self.create(Color_Field, tab=tab_reference, **kwargs)
            tab.window = field.reference
            if index:
                field.hide()
            else:
                pride.objects[tab.indicator].enable_indicator()


class Theme_Customizer(pride.gui.widgetlibrary.Tab_Switching_Window):

    defaults = {"target_theme" : None}

    def readjust_sliders(self):
        for tab_reference in pride.objects[self.tab_bar].tabs:
            pride.objects[pride.objects[tab_reference].window].readjust_sliders()

    def initialize_tabs_and_windows(self):
        try:
            profiles = self.target_theme.colors
        except AttributeError:
            profiles = self.target_theme.theme_colors
        self.tab_types = tuple(pride.gui.widgetlibrary.Tab_Button.from_info(text=text, include_delete_button=False) for
                               text in sorted(profiles.keys()))
        super(Theme_Customizer, self).initialize_tabs_and_windows()

    def create_windows(self):
        target_theme = self.target_theme
        try:
            profiles = target_theme.colors
        except AttributeError:
            profiles = target_theme.theme_colors
        for index, tab_reference in enumerate(pride.objects[self.tab_bar].tabs):
            tab = pride.objects[tab_reference]
            key = tab.text
            profile = profiles[key]
            switcher = self.create(Profile_Customizer, target_theme=target_theme,
                                   profile_info=profile)

            tab.window = switcher.reference
            if index:
                switcher.hide()
            else:
                pride.objects[tab.indicator].enable_indicator()


if __name__ == "__main__":
    import pride.gui
    window = pride.gui.enable()
    pride.objects[window].create(Theme_Customizer, target_theme=pride.gui.gui.Minimal_Theme)
