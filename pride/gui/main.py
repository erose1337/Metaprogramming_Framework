import ast
import argparse
import os.path

import pride.components.user
import pride.gui.gui


class User(pride.components.user.User):

    defaults = {"auto_login" : False, "auto_register" : False}

    def handle_not_registered(self, identifier):
        if self.auto_register:
            super(User, self).handle_not_registered(identifier)
        else:
            raise ValueError()


class Gui(pride.gui.gui.Application):

    defaults = {"lockscreen_type" : "pride.gui.programs.lockscreen.Login_Screen",
                "startup_components" : tuple(), "startup_programs" : tuple(),
                "theme_file" : os.path.join(pride.site_config.GUI_DIRECTORY,
                                            "resources", "themes",
                                            "default.theme")}
    mutable_defaults = {"user" : User}
    autoreferences = ("lockscreen", )

    def __init__(self, **kwargs):
        super(Gui, self).__init__(**kwargs)
        self.set_theme_colors(self.theme_file)
        if not self.user.logged_in:
            self.lockscreen = self.application_window.create(self.lockscreen_type, user=self.user,
                                                             service_name="User", host_info=("localhost", 40022))
        else:
            self.launch_programs()

    def set_theme_colors(self, filename):
        self.show_status("Importing color options...")
        with open(filename, 'r') as _file:
            data = _file.read()
        new_theme_colors = self.theme.deserialize(data)
        theme_colors = self.theme.theme_colors
        for profile, values in new_theme_colors.items():
            for key, value in values.iteritems():
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
        self.clear_status()

    def login_success(self, username):
        self.show_status("Logged in as {}".format(username))
        self.lockscreen.delete()
        self.launch_programs()

    def launch_programs(self):
        window = self.sdl_window
        for program_type in self.startup_programs:
            window.create(program_type)
        self.delete()

    def login_failed(self):
        self.alert("Login failed")

def run_programs(programs, user_ref="/User", **window_kwargs):
    import pride
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable(**window_kwargs)]
    window.create(pride.gui.main.Gui, startup_programs=programs,
                  user=pride.objects[user_ref])

def main(**kwargs):
    window = pride.objects[pride.gui.enable(position=(100, 100))]
    kwargs["startup_programs"] = kwargs.get("startup_programs", tuple()) + ("pride.gui.programs.fileexplorer.Directory_Viewer", )
    gui = window.create(Gui, **kwargs)

if __name__ == "__main__":
    main()
