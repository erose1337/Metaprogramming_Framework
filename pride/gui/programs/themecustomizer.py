import ast

import pride.gui.widgets.tabs
import pride.gui.widgets.form

try:
    import cefparser
except ImportError:
    print("cefparser package not installed")
    print("Please download and install cefparser from https://github.com/erose1337/cef_parser")
    raise

class Value_Editor(pride.gui.widgets.tabs.Tabbed_Window):

    defaults = {"include_new_tab_button" : False, "pack_mode" : "top",
                "include_delete_button" : False, "names" : tuple(),
                "new_window_type" : "pride.gui.widgets.form.Form"}
    mutable_defaults = {"target_object" : dict}
    required_attributes = ("target_object", )

    def create_subcomponents(self):
        create_window = self.create_window
        targets = self.tab_targets = []
        for name in self.names:
            def callable(name=name):
                return create_window(name)
            callable.tab_kwargs = {"button_text" : name}
            targets.append(callable)
        super(Value_Editor, self).create_subcomponents()

    def create_window(self, name):
        window = self.main_window.create(self.new_window_type, fields=[[name]],
                                         tab_kwargs={"button_text" : name.replace('_', ' ')},
                                         target_object=self.target_object)
        return window


class Color_Form(pride.gui.widgets.form.Form):

    def handle_value_changed(self, field, old_value, new_value):
        super(Color_Form, self).handle_value_changed(field, old_value,
                                                     new_value)
        self.theme.update_theme_users()


class Profile_Editor(Value_Editor):

    def create_window(self, name):
        try:
            _object = self.target_object[name]
        except KeyError as error:
            try:
                _object = self.target_object["{}_color".format(name)]
            except KeyError:
                raise error
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
            orientation = "side by side"
            field_info = pride.gui.widgets.form.field_info
            fields = [
                      [field_info(name,
                       entry_kwargs=dict(orientation=orientation),
                       minimum=0)]
                     ]
            target = self.target_object
            if orientation == "stacked":
                kwargs["w_range"] = (0, .25)
        else:
            target = _object

        window = self.main_window
        form = window.create(Color_Form, fields=fields, pack_mode="top",
                             target_object=target,
                             tab_kwargs={"button_text" : name}, **kwargs)
        return form


class Theme_Editor(Value_Editor):

    defaults = {"new_window_type" : Profile_Editor}
    autoreferences = ("file_saver", "file_selector")

    def create_subcomponents(self):
        self.show_status("Initializing theme editor...", immediately=True)
        theme = self.target_object
        self.names = sorted(theme.theme_colors.keys())
        self.create("pride.gui.widgets.form.Form", target_object=self,
                    pack_mode="top", h_range=(0, .05),
                    fields=[[("delete_color_options", {"button_text" : 'x',
                                                       "scale_to_text" : True,
                                                       "pack_mode" : "right"}),
                             ("save_color_options", {"button_text" : "Export color options",
                                                     "pack_mode" : "right"}),
                             ("load_color_options", {"button_text" : "Import color options",
                                                     "pack_mode" : "right"})
                           ]])

        targets = self.tab_targets = []
        for profile in self.target_object.theme_colors.keys():
            def callable(profile=profile):
                return self.create_window(profile)
            targets.append(callable)
        super(Theme_Editor, self).create_subcomponents()
        self.show_status("...Done")

    def create_window(self, profile):
        theme = self.target_object; theme_colors = theme.theme_colors
        names = sorted(theme_colors.values()[0].keys())
        window = self.main_window.create(self.new_window_type, names=names,
                                         target_object=theme_colors[profile],
                                         tab_bar_title_text="{} profile settings".format(profile),
                                         tab_kwargs={"button_text" : profile})
        return window

    def save_color_options(self):
        if self.file_saver is None:
            self.file_saver = self.create("pride.gui.programs.fileexplorer.File_Saver",
                                          pack_mode="top", data=self.serialize_color_options())

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
        if self.file_selector is None:
            self.file_selector = self.create("pride.gui.programs.fileexplorer.File_Selector",
                                            pack_mode="top", callback=self._load_color_options)

    def _load_color_options(self, filename):
        self.show_status("Importing color options from {}...".format(filename),
                         immediately=True)
        try:
            theme = cefparser.parse_filename(filename)
        except Exception: # cefparser needs to be improved to throw exceptions properly on malformed files
            assert hasattr(cefparser, "parse_filename")
            self.show_status("Invalid or corrupt theme file")
            return
        else:
            if "Theme Profiles" not in theme:
                self.show_status("Invalid or corrupt theme file")
                return
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

if __name__ == "__main__":
    import pride.gui
    import pride.gui.themes
    import pride.components.base
    window = pride.objects[pride.gui.enable(x=50, y=50)]
    _object = pride.components.base.Base(test_value=1)
    #callable = lambda **kwargs: Value_Editor(target_object=_object,
    #                                         names=("test_value", ),
    #                                         **kwargs)
    theme = pride.gui.themes.Minimal_Theme
    info = theme.theme_colors
    #callable = lambda **kwargs: Profile_Editor(target_object=info.values()[0],
    #                                           names=sorted(info.values()[0].keys()),
    #                                           **kwargs)
    callable = lambda **kwargs: Theme_Editor(target_object=theme,
                                             **kwargs)
    window.create("pride.gui.main.Gui", user=pride.objects["/User"],
                  startup_programs=(callable, ))
