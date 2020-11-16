import sys

import pride.components.base
import pride.components.user
import pride.functions.contextmanagers

class Service_Registration(pride.components.base.Base):
    """ Registers a new 'user' (not a `User` object) with an Authenticated_Service.
        Some services may not have `register` enabled as remotely callable procedure.
        This program facilitates registration with such services locally.
        This is primarily used to set up accounts for the remote shell.
        This is written as a Base object instead of as a function so that the built-in argument parsing can be used.
        """
    defaults = {"name" : "registration", "username" : '', "password" : '',
                "target_service" : "/Program/Interpreter",
                "auto_exit" : True}
    parser_args = ("username", "password")
    verbosity = {"registration_success" : 0, "registration_failure" : 0}

    def __init__(self, **kwargs):
        super(Service_Registration, self).__init__(**kwargs)

        if "/User" not in pride.objects:
            msg = "/User not found; probable cause: Program not run using pride"
            msg += "\nRun using python -m pride.main yourmodule.py ..."
            raise SystemExit(msg)
        username = self.username
        user = pride.objects["/User"]
        if not username:
            username = user.username

        service_name = self.target_service
        password = self.password
        if not password:
            password = user.generate_strong_password(service_name, username)

        service = pride.objects[service_name]
        with pride.functions.contextmanagers.backup(service, "allow_registration"):
            service.allow_registration = True
            success = service.register(username, password)
        if success:
            message = "Successfully registered '{}' with {}"
            self.alert(message.format(username, service_name),
                       level=self.verbosity["registration_success"])
        else:
            message = "Failed to register '{}' with {}"
            self.alert(message.format(username, service_name),
                       level=self.verbosity["registration_failure"])
        if self.auto_exit:
            raise SystemExit()

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
