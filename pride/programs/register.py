import getpass
import argparse
import sys

import pride

_argparser = argparse.ArgumentParser()
_argparser.add_argument("service", help="The local-residing service to register with")
_argparser.add_argument("username")

class Registration(pride.components.base.Base):
    """ Launcher program for registering a new user with an
        Authenticated_Service. Dispatches the appropriate
        authenticated client to start registration. """
    defaults = {"name" : "registration", "username" : '',
                "authentication_client_name" : "pride.components.interpreter.Shell"}
    parser_args = ("username", )

    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)
        username = self.username or pride.objects["/User"].username
        client = pride.objects["/Python"].create(self.authentication_client_name,
                                                  auto_login=False,
                                                  username=username,
                                                  _register_callback=lambda status: sys.exit())
        client.register()

if __name__ == "__main__":
    registration = Registration(parse_args=True)
