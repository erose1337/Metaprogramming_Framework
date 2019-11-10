import pride.gui.gui

class Status_Display(pride.gui.gui.Container):

    defaults = {"center_text" : False, "scale_to_text" : False}

    def write_to(self, text):
        self.text += text


class Login_Screen(pride.gui.gui.Window):

    defaults = {"user" : None, "service_name" : '', "host_info" : ('', 0)}
    hotkeys = {("\t", None) : "handle_tab"}

    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        self.create("pride.gui.gui.Container", pack_mode="top") # top spacer
        field_space = self.create("pride.gui.gui.Container", pack_mode="top")
        field_space.create("pride.gui.gui.Container", pack_mode="left",
                           w_range=(0, .10)) # left spacer
        fields = [
                  [("username", {"entry_kwargs" : {"tip_bar_text" : "Enter your user name here"}})],
                  [("password", {"entry_kwargs" : {"tip_bar_text" : "Enter your password here",
                                                   "confidential" : True}})],
                  [("auto_register", {"entry_kwargs" : {"indicator_kwargs" : {"pack_mode" : "right"}},
                                      "display_name" : "First time?",
                                      "tip_bar_text" : "if True: Sign up and register the supplied credentials before logging in"}),
                   ("login", {"button_text" : "Login", "target_object" : self,
                              "entry_kwargs" : {"tip_bar_text" : "Log in with these credentials"}})],
                 ]

        field_space.create("pride.gui.widgets.form.Form", target_object=self.user,
                           fields=fields, w_range=(0, .5), pack_mode="left",
                           max_rows=5)
        display = self.status_display = field_space.create(Status_Display, pack_mode="left")
        text = "Log in to {}@({}:{})\n".format(self.service_name, *self.host_info)
        display.write_to(text)
        self.create("pride.gui.gui.Container", pack_mode="top") # bottom spacer

    def handle_tab(self):
        pass

    def login(self):
        user = self.user
        username = user.username # failed attempt will reset these to ''
        password = user.password #
        backup_flag = user.prompt_flag
        user.prompt_flag = False
        success = user.attempt_login()
        user.prompt_flag = backup_flag
        if success:
            self.user_password = ''
            self.parent_application.login_success(username)
            self.status_display.write_to("Login success")
        else:
            user.username = username; user.password = password
            self.parent_application.login_failed()
            self.status_display.write_to("Login failed")

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
