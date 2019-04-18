import getpass
import argparse
import sys

import pride

_argparser = argparse.ArgumentParser()
_argparser.add_argument("service", help="The local-residing service to register with")
_argparser.add_argument("username")

def register(service, username, password=None):
    print("Registering '{}' with local {} service".format(username, service))
    if password is None:
        password = getpass.getpass("Please enter the password ")
    success, message = pride.objects[service].register(username, password)
    if not success:
        raise ValueError("{} user {} already exists")

class Registration(pride.components.base.Base):
    """ Launcher program for registering a new user with an
        Authenticated_Service. Dispatches the appropriate
        authenticated client to start registration. """
    defaults = {"name" : "registration",
                "authentication_client_name" : "pride.components.interpreter.Shell"}

    parser_ignore = ("name", )

    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)
        client = pride.objects["/Python"].create(self.authentication_client_name,
                                                  parse_args=True, auto_login=False,
                                                  _register_results=sys.exit)
        client.register()

if __name__ == "__main__":
    #args, _  = _argparser.parse_known_args()
    #register(args.service, args.username)
    registration = Registration(parse_args=True)
