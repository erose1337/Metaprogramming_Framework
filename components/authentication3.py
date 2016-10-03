import sys
import random
import hashlib
import os
import getpass

from pride import Instruction
import pride.components.rpc
import pride.functions.security
import pride.functions.decorators
import pride.functions.utilities
from pride.functions.security import hash_function
from pride.errors import SecurityError, UnauthorizedError             


# send session key to partner
# xor key with key sent by partner
#    - decrypt encrypted_session_secret via private key
#    - xor both session secrets together to obtain final session secret

remote_procedure_call = pride.components.rpc.remote_procedure_call       
                                
class Authenticated_Service(pride.components.rpc.RPC_Service):
   
    defaults = {# security related configuration options
                "iterations" : 100000, "password_hashing_algorithm" : "pbkdf2hmac",
                "sub_algorithm" : "sha512", "salt_size" : 16, "output_size" : 32,
                "session_id_size" : 16,
                
                # chooses whether or not to hash passwords for invalid registration attempts
                # if False and a registration request fails, the hashing step will be skipped
                "constant_time_registration" : True, 
                                   
                # registration should be disabled for security sensitive services (i.e. an interpreter)
                # if having arbitrary registered users is not security sensitive, then auto registration is safe
                "allow_login" : True, "allow_registration" : True,
                "login_success_message" : "Welcome to the {}, {}@{}",
                "login_failure_message" : "Failed to login to {} as {}@{}",
                "registration_success_message" : "Registered as '{}'@{}",                     
                "registration_failure_message" : "Failed to register as '{}'@{}"}
                
    verbosity = {"register" : "vv", "validate_success" : 'vvv',
                 "login" : "vv", "authentication_success" : "vv",
                 "login_success" : 'vv', "login_failure" : 'vv',
                 "authentication_failure" : "v", "validate_failure" : "vvv",                
                 "authentication_failure_already_logged_in" : 'v'}
    
    flags = {"current_session" : ('', None)} # session_id and peer name
     
    database_structure = {"Users" : ("identifier BLOB PRIMARY_KEY", 
                                     "verifier_hash BLOB", "salt BLOB")}
                              
    database_flags = {"primary_key" : {"Users" : "identifier"}}
    
    remotely_available_procedures = ("register", "login", "change_credentials", "logout")
    
    rate_limit = {"login" : 2, "register" : 2}       
    
    mutable_defaults = {"_rate" : dict, "ip_whitelist" : list, "ip_blacklist" : list,
                        "session_id" : dict}
                        
    inherited_attributes = {"database_structure" : dict, "database_flags" : dict,
                            "remotely_available_procedures" : tuple, "rate_limit" : dict}
    
    def _get_current_user(self):
        session_id = self.current_session[0]
        return self.session_id[session_id]
        
    def _del_current_user(self):
        id = self.current_session[0]
        del self.session_id[id]        
    current_user = property(_get_current_user, fdel=_del_current_user)
                           
    def register(self, identifier, password_verifier): 
        """ usage: 
                
                ...
                def get_credentials(self):
                    return self.username, self.password
                            
                @pride.functions.decorators.with_arguments_from(lambda self: ((self, ) + self.get_credentials(), {}))        
                @remote_procedure_call(callback_name="register_results")
                def register(self, username, password_hash): 
                    pass      
                                
            On success, inserts (identifier, hashed_password_verifier, salt) into database and returns register_success()
            On failure, returns register_failure() """
            
        identifier_in_use = self.database.query("Users", retrieve_fields=("identifier", ), 
                                                         where={"identifier" : identifier})
        salt = os.urandom(self.salt_size)
        if identifier_in_use:            
            if self.constant_time_registration:                
                verifier_hash = self._hash_password(password_verifier, salt)
            return self.register_failure(identifier)
        else:                        
            verifier_hash = self._hash_password(password_verifier, salt)        
            self.database.insert_into("Users", (identifier, verifier_hash, salt))
            return self.register_success(identifier)
        
    def change_credentials(self, new_identifier, new_password_verifier):        
        result = self.register(new_identifier, new_password_verifier)        
        if result[0]:            
            self.database.delete_from("Users", where={"identifier" : self.current_user})
        return result
    
    def register_success(self, username):            
        """ usage: called during register() when registration succeeds.
            returns: (success_flag, server_message, session_id)            
                - success_flag is True when registration succeeds 
                - server message is a string to be printed or used by the client"""                
        return True, self.registration_success_message.format(username, self.current_session[1])
    
    def register_failure(self, username):                
        """ usage: called during register() when registration fails.
            returns: (success_flag, server_message, session_id)
                - success_flag is False when registration fails
                - server message is a string to be print or used by the client"""                
        return False, self.registration_failure_message.format(username, self.current_session[1])
        
    def login(self, username, password):
        """ usage:
                
                ...
                def _login(self):                                
                    self._logging_in = True    
                    self.session.id = '0'
                    return (self, ) + self.get_credentials(), {}
                        
                @pride.functions.decorators.with_arguments_from(_login)
                @remote_procedure_call(callback_name="login_result")
                def login(self, username, password):
                    pass        
                
                ...
                
            Returns login_success() if username and password are verified
            Returns login_failure() otherwise"""
            
        try:
            correct_hash, salt = self.database.query("Users", retrieve_fields=("verifier_hash", "salt"), 
                                                            where={"identifier" : username})                                                                                  
        except ValueError:
            constant_time = self._hash_password("\x00", "\x00")
            return self.login_failure(username)
        else:
            password_hash = self._hash_password(password, salt)        
            if pride.functions.security.constant_time_comparison(password_hash, correct_hash):                
                return self.login_success(username)
            else:                
                return self.login_failure(username)
            
    def login_success(self, username):
        """ usage: called inside login() when an attempt succeeds
            returns: (success_flag, login_message, session_id)
                - success_flag is True when login succeeds
                - login_message is a string to be printed or used by the client                
                - session_id is a string of random bytes that identifies the client"""
        old_session_id, user_ip = self.current_session        
        session_id = os.urandom(self.session_id_size)
        
        self.current_session = (session_id, user_ip)
                    
        self.session_id[session_id] = username
                            
        self.alert("'{}' logged in successfully from {}".format(username, user_ip), level=self.verbosity["login_success"])
        
        return True, self.login_success_message.format(self.reference, username, user_ip), session_id
        
    def login_failure(self, username):
        """ usage: called inside login() when an attempt fails
            returns: (success_flag, login_message, session_id)
                - success_flag is False when login fails
                - login_message is a string to be printed or used by the client                
                - session_id is reset to '0'"""
                
        session_id, user_ip = self.current_session
        self.alert("'{}' failed to login".format(username), level=self.verbosity["login_failure"])
        return False, self.login_failure_message.format(self.reference, username, user_ip), '0'
        
    def _hash_password(self, password, salt):
        return pride.functions.security.hash_password(password, self.iterations, algorithm=self.password_hashing_algorithm, 
                                                                       sub_algorithm=self.sub_algorithm,
                                                                       salt=salt, output_size=self.output_size)   
    def logout(self):    
        """ usage:
        
            @pride.functions.decorators.call_if(logged_in=True) # don't call if not logged in
            @pride.functions.decorators.exit(_reset_login_flags)
            @remote_procedure_call(callback_name="logout_success")
            def logout(self): 
                pass
        
            Returns None. Forgets the current session associated with the currently logged in user."""
        del self.current_user     
        
    def validate(self, session_id, peername, method_name):
        """ Determines whether or not the peer with the supplied
            session id is allowed to call the requested method.

            Sets current_session attribute to (session_id, peername) if validation
            is successful. """
        if ((method_name not in self.remotely_available_procedures) or
            (peername[0] in self.ip_blacklist) or 
            (peername[0] not in self.ip_whitelist and self.ip_whitelist) or 
            (session_id == '0' and method_name not in ("register", "login")) or
            (session_id not in self.session_id and method_name not in ("register", "login")) or
            (method_name == "register" and not self.allow_registration) or
            (method_name == "login" and not self.allow_login)):            

            self.alert(self.validation_failure_string.format(peername[0] in self.ip_blacklist, 
                                                             peername[0] in self.ip_whitelist,
                                                             session_id in self.session_id,
                                                             method_name, 
                                                             method_name in self.remotely_available_procedures,
                                                             self.allow_login, self.allow_registration),
                       level=self.verbosity["validate_failure"])
            return False         
            
        if self.rate_limit and method_name in self.rate_limit:
            _new_connection = False
            try:
                self._rate[session_id][method_name].mark()
            except KeyError:
                latency = pride.components.datastructures.Latency("{}_{}".format(session_id, method_name))
                try:
                    self._rate[session_id][method_name] = latency
                except KeyError:
                    self._rate[session_id] = {method_name : latency}   
                    _new_connection = True
            if not _new_connection:
                current_rate = self._rate[session_id][method_name].last_measurement                
                if current_rate < self.rate_limit[method_name]:
                    message = "Rate of {} calls exceeded 1/{}s ({}); Denying request".format(method_name, 
                                                                                             self.rate_limit[method_name], 
                                                                                             current_rate)
                    self.alert(message, level=self.verbosity["validate_failure"])
                    return False
            
        self.alert("Authorizing: {} for {}".format(peername, method_name), 
                  level=self.verbosity["validate_success"])
        return True        
        
        
class Authenticated_Client(pride.components.rpc.RPC_Client):
    
    verbosity = {"register" : 0, "register_success" : 0, "register_failure" : 0,     
                 "login" : 0, "login_success" : 0, "login_failure" : 0,
                 "auto_login" : 'v', "logout" : 'v', "login_message" : 0,
                 "login_failed" : 0, "logout_success" : 0, "auto_register" : "vv",
                 "not_registered" : 0, "change_credentials" : 0, "invalid_password" : 0}
                 
    defaults = {"target_service" : "/Python/Authenticated_Service",
                "username_prompt" : "{}: Please provide the user name for {}@{}: ",
                "password_prompt" : "{}: Please provide the pass phrase or word for {}@{}: ",
                "auto_login" : True, "auto_register" : False,
                
                "username" : '', "password" : None, 
                  
                "registration_success_message" : "Registered with {}@{} as '{}'",                     
                "registration_failed_message" : "Failed to register with {}@{} as '{}'",
                
                "password_source" : "user_secret", "password_length" : 32}
        
    flags = {"_registering" : False, "logged_in" : False, "_logging_in" : False,
             "_username" : '', "_password_hash" : '', "_new_credentials" : None}       
    
    allowed_values = {"password_source" : ("user_secret", "user_password", "prompt_user")}
    
    def _get_password(self):                       
        if self.password_source == "prompt_user":            
            return getpass.getpass(self.password_prompt) if self._password is None else self._password
        elif self._password:
            return self._password
        elif self.password_source == "user_secret":
            method = "generate_strong_password"           
        elif self.password_source == "user_password":
            method = "generate_portable_password"
        return getattr(pride.objects["/User"], method)(self.target_service, self.username, self.password_length)                    
    def _set_password(self, value):
        self._password = value
        self.password_hash = ''                
    password = property(_get_password, _set_password)
    
    def _get_username(self):
        if not self._username:
            self._username = raw_input(self.username_prompt.format(self.reference,
                                                                   self.target_service,
                                                                   self.ip))
        return self._username
    def _set_username(self, value):         
        self._username = value        
    username = property(_get_username, _set_username)
                
    def __init__(self, **kwargs):
        super(Authenticated_Client, self).__init__(**kwargs)        
        self.password_prompt = self.password_prompt.format(self.reference, self.target_service, self.ip)
                              
        registered_users = pride.objects["/Python/Persistent_Storage"]["registered_users"]
        user_info = (self.target_service, self.ip, self.username)
        if user_info not in registered_users and self.auto_register:
            self.alert("Auto registering with {}@{} as {}".format(*user_info), level=self.verbosity["auto_register"])
            self.register()            
            
        elif self.auto_login:
            self.alert("Auto logging in", level=self.verbosity["auto_login"])
            self.login()
    
    def get_credentials(self):        
        return self.username, self.password
                
    @pride.functions.decorators.with_arguments_from(lambda self: ((self, ) + self.get_credentials(), {}))        
    @remote_procedure_call(callback_name="register_results")
    def register(self, username, password_hash): 
        pass                
        
    def register_results(self, server_response):
        self._registering = False  
        success, message = server_response
        self.alert("{}".format(message), level=0)
        if success:
            self.register_success()
        else:
            self.register_failure()                                                      
                    
    def register_success(self):
        self.alert(self.registration_success_message.format(self.target_service, self.ip, self.username), 
                   level=self.verbosity["register_success"])
        
        registered_users = pride.objects["/Python/Persistent_Storage"]["registered_users"]
        registered_users.append((self.target_service, self.ip, self.username))     
        pride.objects["/Python/Persistent_Storage"]["registered_users"] = registered_users

        if self.auto_login:
            self.login()
                
    def register_failure(self):
        self.alert(self.registration_failed_message.format(self.target_service, self.ip, self.username), 
                   level=self.verbosity["register_failure"])
                   
    def _login(self):                                
        self._logging_in = True    
        self.session.id = '0'
        return (self, ) + self.get_credentials(), {}
            
    @pride.functions.decorators.with_arguments_from(_login)
    @remote_procedure_call(callback_name="login_result")
    def login(self, username, password):
        pass
        
    def login_result(self, server_response):
        self._logging_in = False
        success, message, self.session.id = server_response
        if success:
            self.login_success(message)
        else:
            self.login_failure(message)
    
    def login_success(self, login_message):
        self.alert("{}".format(login_message, level=self.verbosity['login_success']))    
        self.logged_in = True        
        
        for instruction, callback in self._delayed_requests:
            self.alert("Making delayed request: {}".format((instruction.component_name, instruction.method)),
                      level=self.verbosity["delayed_request_sent"])
            self.session.execute(instruction, callback)
        self._delayed_requests = []
        
    def _reset_login_flags(self):
        self.logged_in = False
        self.session.id = '0'       
        
    def login_failure(self, server_response):        
        self.logged_in = False
        self.alert("{}".format(server_response, level=self.verbosity['login_failure']))
        
        if self.ip in ("localhost", "127.0.0.1"):
            registered_users = pride.objects["/Python/Persistent_Storage"]["registered_users"]               
            user_info = (self.target_service, self.ip, self.username)
            if user_info not in registered_users:
                if pride.components.shell.get_permission("{}: Attempt to register?: ".format(self.reference)):
                    self.register()
            else:
                self.alert("Invalid password", level=self.verbosity["invalid_password"])
                
    @pride.functions.decorators.call_if(logged_in=True)
    @pride.functions.decorators.exit(_reset_login_flags)
    @remote_procedure_call(callback_name="logout_success")
    def logout(self): 
        """ Logout self.username from the target service. If the user is logged in,
            the logged_in flag will be set to False and the session.id set to '0'.
            If the user is not logged in, this is a no-op. """
    
    def logout_success(self, server_response):
        self.alert("Logout success: {}".format(server_response), level=self.verbosity["logout_success"])        
        
    def handle_not_logged_in(self, instruction, callback):        
        if self.auto_login or pride.components.shell.get_permission("Login now? :"):
            self._delayed_requests.append((instruction, callback))
            if not self._logging_in:
                self.alert("Not logged in")       
                self.login()            
    
    def _get_new_credentials(self):
        backup = self.get_credentials()
        self.username, self.password = None, None
        self._new_credentials = username, password = self.username, self.password        
        self.username, self.password = backup
        return username, password
        
    @pride.functions.decorators.with_arguments_from(lambda self: ((self, ) + self._get_new_credentials(), {}))
    @remote_procedure_call(callback_name="change_credential_result")
    def change_credentials(self, new_identifier, new_password_verifier):
        pass        
        
    def change_credential_result(self, server_response):
        success, message = server_response
        self.alert("{}".format(message), level=0)
        old_credentials = self.username, self.password
        self.username, self.password = self._new_credentials            
        self._new_credentials = None
        
        if success:            
            registered_users = pride.objects["/Python/Persistent_Storage"]["registered_users"]
            registered_users.remove((self.target_service, self.ip, old_credentials[0]))     
            pride.objects["/Python/Persistent_Storage"]["registered_users"] = registered_users                
            
            self.register_success()
        else:              
            self.register_failure()
            self.username, self.password = old_credentials
        
        
    def delete(self):
        if self.logged_in:
            self.logout()
        super(Authenticated_Client, self).delete()
        
    def __getstate__(self):
        attributes = super(Authenticated_Client, self).__getstate__()
        del attributes["session"]
        attributes["objects"] = {}
        attributes["logged_in"] = False
        attributes["session_id"] = '0'
        return attributes
    
    def on_load(self, attributes):
        super(Authenticated_Client, self).on_load(attributes)        
        self.session = self.create("pride.components.rpc.Session", session_id='0', host_info=self.host_info)                               
                                       
        #if self.auto_login:
        #    self.alert("Auto logging in", level=self.verbosity["auto_login"])
        #    self.login()
                
def test_Authenticated_Service3():              
    service = Authenticated_Service()
    client = Authenticated_Client(target_service=service.reference, username="Authenticated_Service3_unit_test", auto_register=True, auto_login=True)
    client.logout()
    
    client.change_credentials()
    
if __name__ == "__main__":
    test_Authenticated_Service3()
    