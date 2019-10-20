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
    autoreferences = ("_file_selector", "bar")
    required_attributes = ("target_theme", )

    def initialize_tabs_and_windows(self):
        if self.bar is None:
            bar = self.create("pride.gui.gui.Container", h_range=(0, .05), pack_mode="top")
            bar.create("pride.gui.widgetlibrary.Method_Button", target=self.reference,
                    method="delete_color_options", text='x', pack_mode="right")
            bar.create("pride.gui.widgetlibrary.Method_Button", target=self.reference,
                    method="export_color_options", text="Export color options",
                    pack_mode="right")
            bar.create("pride.gui.widgetlibrary.Method_Button", target=self.reference,
                    method="import_color_options", text="Import color options",
                    pack_mode="right")
            self.bar = bar

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

    def export_color_options(self):
        self._file_selector = self.parent.create("game3.gui.window2.File_Selector",
                                                 write_field_method=self._write_color_filename_export,
                                                 file_category="color",
                                                 delete_callback=self.close_file_selector)
        self.hide()

    def close_file_selector(self):
        if self._file_selector is not None:
            assert not self._file_selector.deleted
            self._file_selector.delete()
            self._file_selector = None
        self.show()

    def _write_color_filename_export(self, field_name, value):
        self._file_selector.update_recent_files(value, "color")
        self.color_options_file = value
        self.close_file_selector()
        self._export_color_options()

    def _export_color_options(self):
        self.show_status("Exporting color options...")
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

        with open(self.color_options_file, 'w') as _file:
            _file.write('\n'.join(lines))

    def import_color_options(self):
        self._file_selector = self.parent.create("game3.gui.window2.File_Selector",
                                                 write_field_method=self._write_color_filename_import,
                                                 file_category="color",
                                                 delete_callback=self.close_file_selector)
        self.hide()

    def _write_color_filename_import(self, field_name, value):
        if not os.path.exists(value):
            self.show_status("File does not exist")
            return
        self._file_selector.update_recent_files(value, "color")
        self.color_options_file = value
        self._file_selector.delete()
        self.show()
        self._import_color_options()

    def _import_color_options(self):
        self.show_status("Importing color options...")
        theme = cefparser.parse_filename(self.color_options_file)
        theme_colors = self.theme.theme_colors
        for profile, values in theme["Theme Profiles"].iteritems():
            bad_keys = []
            for key, value in values.iteritems():
                values[key] = ast.literal_eval(value)
                try:
                    r, g, b, a = values[key]
                except (ValueError, TypeError):
                    bad_keys.append(key)
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
        self.hide_status()
        #self.readjust_sliders()

    def delete_color_options(self):
        self.delete()
        if self.delete_callback is not None:
            self.delete_callback()


if __name__ == "__main__":
    import pride.gui
    import pride.gui.themes
    window = pride.gui.enable()
    pride.objects[window].create(Theme_Customizer, target_theme=pride.gui.themes.Minimal_Theme)
