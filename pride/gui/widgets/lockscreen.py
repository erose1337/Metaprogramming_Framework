import pride.components.user
import pride.gui.gui
import pride.gui.widgetlibrary


class Confidential_Entry(pride.gui.widgetlibrary.Field_Entry):

    defaults = {"symbol" : '*', #"constant_length_field" : True,
                "_confidential_text" : ''}

    #def __init__(self, **kwargs):
    #    super(Confidential_Entry, self).__init__(**kwargs)
    #    self.create("pride.gui.widgetlibrary.Method_Button", method="toggle_constant_length",
    #                target=self.reference)

    def text_entry(self, text):
        if self.allow_text_edit:
            self._confidential_text += text
            self.text = self.symbol * 16
            #else:
            #self.text += self.symbol * len(text)

    def deselect(self, mouse, next_active_object):
        super(Confidential_Entry, self).deselect(mouse, next_active_object)
        if self.text:
            self.write_field_method(self._confidential_text)

    def handle_backspace(self):
        if self.allow_text_edit:
            self._confidential_text = self._confidential_text[:-1]
            if not self._confidential_text:
                self.text = ''


class Username_Password_Field(pride.gui.gui.Container):

    defaults = {"username" : '', "user_password" : ''}
    autoreferences = ("username_field", "password_field", "autoregister")

    def __init__(self, **kwargs):
        super(Username_Password_Field, self).__init__(**kwargs)
        self.username_field = self.create("pride.gui.widgetlibrary.Field",
                                          field_name="Username", initial_value='',
                                          tip_bar_text="Enter your user name here",
                                          pack_mode="top",
                                          write_field_method=self._set_username,
                                          orientation="stacked")
        self.password_field = self.create("pride.gui.widgetlibrary.Field",
                                          field_entry_type=Confidential_Entry,
                                          field_name="Password", initial_value='',
                                          tip_bar_text="Enter your password here",
                                          pack_mode="top",
                                          write_field_method=self._set_password,
                                          return_method=self.submit_credentials,
                                          orientation="stacked")
        buttons_field = self.create("pride.gui.gui.Container", pack_mode="top",
                                    h_range=(0, .10))
        self.autoregister = buttons_field.create("pride.gui.widgets.buttons.Toggle", text="auto register",
                                                 state=False, pack_mode="left", scale_to_text=True)
        buttons_field.create("pride.gui.widgetlibrary.Method_Button", text="Submit",
                             method="submit_credentials", target=self.reference,
                             scale_to_text=False, pack_mode="left")

    def _set_password(self, field_name, value):
        self.user_password = value

    def _set_username(self, field_name, value):
        self.username = value

    def submit_credentials(self):
        user = self.user
        text = "Computing: {}\n".format(user.get_derivation_description())
        self.parent_application.status_display.text += text
        self.parent_application.parent_application.show_status("Attempting login...")
        pride.objects[self.sdl_window].run()
        user.username = self.username
        user.password = self.user_password
        user.auto_register = self.autoregister.state
        success = user.attempt_login()
        if success:
            self.user_password = ''
            self.parent_application.login_success()
        else:
            self.parent_application.login_failed()


class Status_Display(pride.gui.gui.Container):

    defaults = {"center_text" : False, "scale_to_text" : False}


class Login_Screen(pride.gui.gui.Application):

    defaults = {"user" : None, "startup_components" : tuple(),
                "tip_bar_enabled" : False, "service_name" : '',
                "host_info" : ('', 0)}
    required_attributes = ("user", "service_name", "host_info")
    autoreferences = ("field_space", "top_spacer", "bottom_spacer", "status_display")

    def __init__(self, **kwargs):
        super(Login_Screen, self).__init__(**kwargs)
        window = self.application_window
        self.top_spacer = window.create("pride.gui.gui.Container", pack_mode="top")
        self.field_space = field_space = window.create("pride.gui.gui.Container", pack_mode="top")
        field_space.create("pride.gui.gui.Container", pack_mode="left",
                           w_range=(0, .10))
        field_space.create(Username_Password_Field, pack_mode="left", user=self.user,
                           w_range=(0, .50))

        text = "Log in to {}@({}:{})\n".format(self.service_name, *self.host_info)
        self.status_display = field_space.create(Status_Display, pack_mode="left",
                                                 text=text, theme_profile="interactive")
        self.bottom_spacer = window.create("pride.gui.gui.Container", pack_mode="top")
        self.parent_application.show_status("Login Screen")

    def login_success(self):
        self.top_spacer.delete()
        self.field_space.delete()
        self.bottom_spacer.delete()
        self.parent_application.login_success(self.user.username)

    def login_failed(self):
        self.parent_application.show_status("Login attempt failed")
        display = self.status_display
        display.text = text = display.text + "Login attempt failed\n"

        if text.count("\n") > self.h / 43:
            display.text = '\n'.join(text.split('\n')[-self.h / 43:])

def main():
    if "/SDL_Window" not in pride.objects:
        window = pride.objects[pride.gui.enable()]
    else:
        window = pride.objects["/SDL_Window"]
    user = pride.components.user.User(auto_login=False, auto_register=True)
    window.create(Login_Screen, user=user)

if __name__ == "__main__":
    main()
