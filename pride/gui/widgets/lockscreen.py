import pride.components.user
import pride.gui.gui

class Username_Password_Field(pride.gui.gui.Container):

    defaults = {"username" : '', "user_password" : ''}
    autoreferences = ("username_field", "password_field")

    def __init__(self, **kwargs):
        super(Username_Password_Field, self).__init__(**kwargs)
        self.username_field = self.create("pride.gui.widgetlibrary.Field",
                                          field_name="Username", initial_value='',
                                          tip_bar_text="Enter your user name here",
                                          pack_mode="top",
                                          write_field_method=self._set_username,
                                          orientation="stacked")
        self.password_field = self.create("pride.gui.widgetlibrary.Field",
                                          field_name="Password", initial_value='',
                                          tip_bar_text="Enter your password here",
                                          pack_mode="top",
                                          write_field_method=self._set_password,
                                          orientation="stacked")
        buttons_field = self.create("pride.gui.gui.Container", pack_mode="top",
                                    h_range=(0, .10))
        buttons_field.create("pride.gui.widgetlibrary.Method_Button", text="Submit",
                             method="submit_credentials", target=self.reference,
                             scale_to_text=False, pack_mode="left")

    def _set_password(self, field_name, value):
        self.user_password = value

    def _set_username(self, field_name, value):
        self.username = value

    def submit_credentials(self):
        self.parent_application.parent_application.show_status("Attempting login...")
        self.user.username = self.username
        self.user.password = self.user_password
        success = self.user.attempt_login()
        if success:
            self.user_password = ''
            self.parent_application.login_success()
        else:
            self.parent_application.login_failed()


class Login_Screen(pride.gui.gui.Application):

    defaults = {"user" : None, "startup_components" : tuple(),
                "tip_bar_enabled" : False}
    required_attributes = ("user", )
    autoreferences = ("field_space", "top_spacer", "bottom_spacer")

    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        window = self.application_window
        self.top_spacer = window.create("pride.gui.gui.Container", pack_mode="top")
        self.field_space = field_space = window.create("pride.gui.gui.Container", pack_mode="top")
        field_space.create("pride.gui.gui.Container", pack_mode="left",
                           w_range=(0, .10))
        field_space.create(Username_Password_Field, pack_mode="left", user=self.user,
                           w_range=(0, .50))
        field_space.create("pride.gui.gui.Container", pack_mode="left")
        self.bottom_spacer = window.create("pride.gui.gui.Container", pack_mode="top")
        self.parent_application.show_status("Login Screen")

    def login_success(self):
        self.top_spacer.delete()
        self.field_space.delete()
        self.bottom_spacer.delete()
        self.parent_application.login_success(self.user.username)

    def login_failed(self):
        self.parent_application.show_status("Login attempt failed")

def main():
    if "/SDL_Window" not in pride.objects:
        window = pride.objects[pride.gui.enable()]
    else:
        window = pride.objects["/SDL_Window"]
    user = pride.components.user.User(auto_login=False, auto_register=True)
    window.create(Login_Screen, user=user)

if __name__ == "__main__":
    main()
