import ast
import argparse
import os.path

import pride.components.user
import pride.gui.gui

try:
    import cefparser
except ImportError:
    print("install cefparser package from https://github.com/erose1337/cef_parser")
    raise

class User(pride.components.user.User):

    def handle_not_registered(self, identifier):
        if self.auto_register:
            super(User, self).handle_not_registered(identifier)
        else:
            raise ValueError()


class Gui(pride.gui.gui.Application):

    defaults = {"lockscreen_type" : "pride.gui.widgets.lockscreen.Login_Screen",
                "startup_components" : tuple(), "startup_programs" : tuple(),
                "theme_file" : os.path.join(pride.site_config.GUI_DIRECTORY,
                                            "resources", "themes",
                                            "default.theme"),
                "user_type" : User}

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)
        self.set_theme_colors(self.theme_file)
        user = self.user = self.user_type(auto_login=False, auto_register=True)
        self.application_window.create(self.lockscreen_type, user=user,
                                       service_name="User", host_info=("localhost", 40022))

    def set_theme_colors(self, filename):
        self.show_status("Importing color options...")
        theme = cefparser.parse_filename(filename)
        theme_colors = self.theme.theme_colors
        for profile, values in theme["Theme Profiles"].iteritems():
            for key, value in values.iteritems():
                values[key] = ast.literal_eval(value)
                try:
                    r, g, b, a = values[key]
                except TypeError:
                    pass
                else:
                    _color = theme_colors[profile][key]
                    _color.r = r
                    _color.g = g
                    _color.b = b
                    _color.a = a
                    values[key] = _color
            theme_colors[profile].update(values)
        self.theme.update_theme_users()

    def login_success(self, username):
        self.show_status("Logged in as {}".format(username))
        window = self.application_window
        for program_type in self.startup_programs:
            self.create(program_type)

    def login_failed(self):
        self.alert("Login failed")




def main(**kwargs):
    window = pride.objects[pride.gui.enable()]
    gui = window.create(Gui, **kwargs)

if __name__ == "__main__":
    main()
