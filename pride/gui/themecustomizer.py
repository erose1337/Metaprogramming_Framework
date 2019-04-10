import pride.gui.gui
import pride.gui.widgetlibrary

class Color_Field(pride.gui.gui.Container):

    defaults = {"field_info" : tuple(), "field_attributes" : dict(),
                "pack_mode" : "top"}

    def __init__(self, **kwargs):
        super(Color_Field, self).__init__(**kwargs)
        field_name, _object = self.field_info
    #    self.create("pride.gui.gui.Container", text=field_name, pack_mode="top")
        for key, bounds in self.field_attributes.items():
            self.create(pride.gui.widgetlibrary.Slider_Widget, label=key, bounds=bounds, target=(_object, key),
                        h_range=(0, .10))


class Theme_Customizer(pride.gui.widgetlibrary.Tab_Switching_Window):

    color_keys = ("background", "shadow", "text", "text_background")
    defaults = {"target_theme" : None,
                "tab_types" : tuple(pride.gui.widgetlibrary.Tab_Button.from_info(text=text, include_delete_button=False) for
                                    text in color_keys)}
    required_attributes = ("target_theme", )

    def create_windows(self):
        try:
            info = self.target_theme.colors # customize instance colors
        except AttributeError:
            info = self.target_theme.theme_colors # customize generic theme colors
        # create r/g/b/a/ sliders for each color key in theme_info
        for index, tab_reference in enumerate(self.tab_bar.tabs):
            tab = pride.objects[tab_reference]
            key = tab.text
            _object = info[key]
            field = self.create(Color_Field, field_info=(key, _object), tab=tab_reference,
                                field_attributes={'r' : _object.r_range, 'g' : _object.g_range,
                                                  'b' : _object.b_range, 'a' : _object.a_range})
            tab.window = field.reference
            if index:
                field.hide()
            else:
                pride.objects[tab.indicator].enable_indicator()

if __name__ == "__main__":
    import pride.gui
    window = pride.gui.enable()
    pride.objects[window].create(Theme_Customizer, target_theme=pride.gui.gui.Minimal_Theme)
