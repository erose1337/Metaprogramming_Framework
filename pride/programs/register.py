import sys

import pride.components.base
import pride.components.user

class Service_Registration(pride.components.base.Base):
    """ Registers a new 'user' (not a `User` object) with an Authenticated_Service.
        Some services may not have `register` enabled as remotely callable procedure.
        This program facilitates registration with such services locally.
        This is primarily used to set up accounts for the remote shell.
        This is written as a Base object instead of as a function so that the built-in argument parsing can be used.
        """
    defaults = {"name" : "registration", "username" : '', "password" : '',
                "authentication_client_name" : "pride.components.interpreter.Shell"}
    parser_args = ("username", "password")

    def __init__(self, **kwargs):
        super(Service_Registration, self).__init__(**kwargs)
        username = self.username or pride.objects["/User"].username
        password = self.password or pride.objects["/User"].password
        client = pride.objects["/Python"].create(self.authentication_client_name,
                                                  auto_login=False,
                                                  username=username, password=password,
                                                  _register_callback=sys.exit)#lambda status: sys.exit())
        client.register()


class User_Registration(pride.components.user.User):

    defaults = {"auto_register" : True}
    required_attributes = ("username", "password")
    parser_args = ("username", "password")

    def store_new_identity(self, identifier):
        super(User_Registration, self).store_new_identity(identifier)
        self.alert("Registered new User '{}'".format(identifier))
        sys.exit()


if __name__ == "__main__":
    Service_Registration(parse_args=True)
    #User_Registration(parse_args=True)
