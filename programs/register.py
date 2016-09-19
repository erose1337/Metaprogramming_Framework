import contextlib
import sys

import pride
import pride.objectlibrary.shell
import pride.errors
import pride.functions.utilities
        
class Registration(pride.objectlibrary.base.Base):
    """ Launcher program for registering a new user with an 
        Authenticated_Service. Dispatches the appropriate 
        authenticated client to start registration. """
    defaults = {"name" : "registration",                 
                "authentication_client_name" : "pride.objectlibrary.interpreter.Shell"}
    
    parser_ignore = ("name", )

    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)
        client = pride.objects["/Python"].create(self.authentication_client_name,
                                                  parse_args=True, auto_login=False,
                                                  _register_results=sys.exit)        
        client.register()                   
        
if __name__ == "__main__":
    #import pride.objectlibrary.user
  #  pride.Instruction("/User", "create", Registration, parse_args=True).execute(priority=.011)    
    #user = pride.objectlibrary.user.User()
    #python = pride.objectlibrary.interpreter.Python()
    registration = Registration(parse_args=True)