import pride.gui.gui

class Login_Form(gui.Container):
        
    defaults = {"callback" : tuple(), "text" : "Please enter your username and password"}
    required_attributes = ("callback", )
    
    def __init__(self, **kwargs):
        super(Dialog_Box, self).__init__(**kwargs)
        self.create("pride.gui.widgetlibrary.Text_Box", text=self.text,
                    allow_text_edit=False, pack_mode="top")
        self.username_field = self.create("pride.gui.widgetlibrary.Text_Box",
                                          pack_mode="top", h_range=(0, 80))
        self.password_field = self.create(self.password_entry_field_type, callback=(self.reference, "handle_password"))
        
    def handle_password(self, password):
        username = self.username_field.text
        if username:
            reference, method_name = self.callback
            getattr(pride.objects[reference], method_name)(username, password)
        
        
class Lockscreen(pride.gui.gui.Window):
    
    def __init__(self, *args, **kwargs):
        super(Lockscreen, self).__init__(*args, **kwargs)
        login_form = self.create(Login_Form, pack_mode="main")
        
    def login(self, username, password):
        raise NotImplementedError()