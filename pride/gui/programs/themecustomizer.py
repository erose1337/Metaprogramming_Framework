import ast
import os.path

import pride.gui.gui
import pride.gui.widgetlibrary
import pride.gui.widgets.tabs
import pride.gui.widgets.form

try:
    import cefparser
except ImportError:
    print("cefparser package not installed")
    print("Please download and install cefparser from https://github.com/erose1337/cef_parser")
    raise


class Color_Field(pride.gui.widgets.form.Form):

    def handle_value_changed(self, field, old_value, new_value):
        super(Color_Field, self).handle_value_changed(field, old_value, new_value)
        self.theme.update_theme_users()


class Profile_Customizer(pride.gui.widgets.tabs.Tab_Switching_Window):

    color_keys = ("background", "shadow", "text", "text_background")
    defaults = {"profile_info" : None}
    required_attributes = ("profile_info", )

    def initialize_tabs_and_windows(self):
        self.tab_types = tuple(pride.gui.widgets.tabs.Tab_Button.from_info(text=text, include_delete_button=False) for
                               text in sorted(self.profile_info.keys()))
        super(Profile_Customizer, self).initialize_tabs_and_windows()

    def create_windows(self):
        # create r/g/b/a/ sliders for each color key in profile_info
        info = self.profile_info
        target_theme = self.target_theme
        for index, tab in enumerate(self.tab_bar.tabs):
            key = tab.text
            tab.text = key.replace('_', ' ')
            _object = info[key]
            kwargs = dict()
            try:
                rmin, rmax = _object.r_range; gmin, gmax = _object.g_range
                bmin, bmax = _object.b_range; amin, amax = _object.a_range
                fields = [
                          [('a', {"minimum" : amin, "maximum" : amax})],
                          [('r', {"minimum" : rmin, "maximum" : rmax})],
                          [('g', {"minimum" : gmin, "maximum" : gmax})],
                          [('b', {"minimum" : bmin, "maximum" : bmax})]
                         ]
            except AttributeError:
                fields = [
                          [(key, {"minimum" : 0, "maximum" : 16})]
                         ]
                # make field here
                kwargs["target_object"] = info
                kwargs["h_range"] = (0, .25)
            else:
                kwargs["target_object"] = _object
            field = self.create(Color_Field, tab=tab, fields=fields, **kwargs)
            tab.window = field
            if index:
                field.hide()
            else:
                tab.indicator.enable_indicator()

    @classmethod
    def from_info(cls, **kwargs):
        def callable(**_kwargs):
            _kwargs.update(kwargs)
            return cls(**_kwargs)
        return callable


class Theme_Customizer(pride.gui.widgets.tabs.Tab_Switching_Window):

    defaults = {"target_theme" : None, "bar" : None, "delete_callback" : None}
    autoreferences = ("file_selector", "bar")
    required_attributes = ("target_theme", )

    def initialize_tabs_and_windows(self):
        if self.bar is None:
            self.bar = self.create("pride.gui.widgets.form.Form", target_object=self,
                                   pack_mode="top", h_range=(0, .05),
                                   fields=[[("delete_color_options", {"button_text" : 'x',
                                                                      "scale_to_text" : True,
                                                                      "pack_mode" : "right"}),
                                            ("save_color_options", {"button_text" : "Export color options",
                                                                    "pack_mode" : "right"}),
                                            ("load_color_options", {"button_text" : "Import color options",
                                                                    "pack_mode" : "right"})
                                          ]])
        profiles = self.target_theme.theme_colors
        self.tab_types = tuple(pride.gui.widgets.tabs.Tab_Button.from_info(text=text, include_delete_button=False) for
                               text in sorted(profiles.keys()))
        super(Theme_Customizer, self).initialize_tabs_and_windows()

    def create_windows(self):
        target_theme = self.target_theme
        profiles = target_theme.theme_colors
        for index, tab in enumerate(self.tab_bar.tabs):
            key = tab.text
            profile = profiles[key]
            tab.window_type = Profile_Customizer.from_info(target_theme=target_theme,
                                                           profile_info=profile)
            if not index:
                tab.left_click(None)

    def save_color_options(self):
        self.create("pride.gui.programs.fileexplorer2.File_Saver",
                    pack_mode="fill", data=self.serialize_color_options())

    def serialize_color_options(self):
        self.show_status("Serializing color options...")
        theme = self.theme.__class__.theme_colors
        lines = ["Theme Profiles",
                 '=' * len("Theme Profiles"),
                 '']

        for profile, profile_data in sorted(theme.items()):
            lines.append(profile)
            lines.append('-' * len(profile) + '\n')
            for parameter, value in sorted(profile_data.items()):
                try:
                    r, g, b, a = value # unpack Color objects into their constituent values
                except (ValueError, TypeError):
                    lines.append("      " + "- {}: {}".format(parameter, value))
                else:
                    lines.append("      " + "- {}: {}".format(parameter, (r, g, b, a)))
            lines.append('\n')
        return '\n'.join(lines)

    def load_color_options(self):
        self.file_selector = self.create("pride.gui.programs.fileexplorer2.File_Selector",
                                         pack_mode="top", callback=self._load_color_options)

    def _load_color_options(self, filename):
        self.show_status("Importing color options from {}...".format(filename))
        theme = cefparser.parse_filename(filename)
        theme_colors = self.theme.theme_colors
        for profile, values in theme["Theme Profiles"].iteritems():
            bad_keys = []
            for key, value in values.iteritems():
                values[key] = ast.literal_eval(value)
                try:
                    r, g, b, a = values[key]
                except (ValueError, TypeError):
                    theme_colors[profile][key] = values[key]
                else:
                    _color = theme_colors[profile][key]
                    _color.r = r
                    _color.g = g
                    _color.b = b
                    _color.a = a
                    values[key] = _color
            theme_colors[profile].update(values)
            for key in bad_keys:
                del theme_colors[profile][key]
        self.theme.update_theme_users()
        self.clear_status()
        self.file_selector.delete()


    def delete_color_options(self):
        self.delete()
        if self.delete_callback is not None:
            self.delete_callback()


if __name__ == "__main__":
    import pride.gui
    import pride.gui.themes
    window = pride.objects[pride.gui.enable()]
    window.create("pride.gui.main.Gui", user=pride.objects["/User"],
                  startup_programs=(lambda **kwargs: Theme_Customizer(target_theme=pride.gui.themes.Minimal_Theme, **kwargs), ))
