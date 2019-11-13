import pride.gui.gui

class Status_Display(pride.gui.gui.Button):

    defaults = {"center_text" : False, "scale_to_text" : False,
                "pack_mode" : "left"}

    def write_to(self, text):
        self.text += text


class Login_Screen(pride.gui.gui.Window):

    defaults = {"service_name" : '', "host_info" : ('', 0)}
    autoreferences = ("user", )
    required_attributes = ("user", )
    
    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        self.user.prompt_flag = self.user.prompt_for_creds = False
        self.create("pride.gui.gui.Container", pack_mode="top") # top spacer
        field_space = self.create("pride.gui.gui.Container", pack_mode="top")
        field_space.create("pride.gui.gui.Container", pack_mode="left",
                           w_range=(0, .10)) # left spacer
        fields = [
                  [("username", {"entry_kwargs" : {"tip_bar_text" : "Enter your user name here"},
                                 "display_name" : "Username"})],
                  [("password", {"entry_kwargs" : {"tip_bar_text" : "Enter your password here",
                                                   "confidential" : True},
                                 "display_name" : "Password"})],
                  [#("register", {"button_text" : "register", "target_object" : self,
                    #             "entry_kwargs" : {"tip_bar_text" : "Sign up and register the supplied credentials before logging in"}
                    #                 }
                    ("auto_register", {"display_name" : "register"}
                   ),
                   ("login", {"button_text" : "login", "target_object" : self,
                              "entry_kwargs" : {"tip_bar_text" : "Log in with these credentials"}})
                  ],
                 ]

        field_space.create("pride.gui.widgets.form.Form", target_object=self.user,
                           fields=fields, w_range=(0, .5), pack_mode="left",
                           max_rows=5)
        display = self.status_display = field_space.create(Status_Display)
        text = "Log in to {}@({}:{})\n".format(self.service_name, *self.host_info)
        display.write_to(text)
        self.create("pride.gui.gui.Container", pack_mode="top") # bottom spacer

    def register(self):
        pass

    def login(self):
        user = self.user
        backup_flag = user.prompt_flag
        user.prompt_flag = False
        username = user.username # failed attempt will reset these to ''
        password = user.password #
        success = user.attempt_login()
        user.prompt_flag = backup_flag
        if success:
            self.user_password = ''
            self.status_display.write_to("Login success\n")
            self.parent_application.login_success(username)
        else:
            user.username = username; user.password = password
            self.status_display.write_to("Login failed\n")
            self.parent_application.login_failed()

def main():
    import pride.components.user
    import pride.gui.main
    import sys
    window = pride.objects[pride.gui.enable()]
    user = pride.components.user.User(auto_login=False, prompt_for_creds=False)
    kwargs = {"startup_programs" : (lambda *args, **kwargs: sys.exit(), )}
    gui = window.create(pride.gui.main.Gui, user=user, **kwargs)


if __name__ == "__main__":
    main()
