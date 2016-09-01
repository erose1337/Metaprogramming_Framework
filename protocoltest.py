class Authentication_Protocol(pride.base.Base):
    
    def register(self, username, password):
        raise NotImplementedError()
        
    def login(self, username, password):
        raise NotImplementedError()
    
    def login_success(self, username):
        raise NotImplementedError()
        
    def login_failure(self, username):
        raise NotImplementedError()
        
        
class Password_Based_Protocol_Client(Authenticated_Client):
    
    defaults = {"username" : '', "password" : None, "hash_password_clientside" : True,
                "iterations" : 100000, "password_hashing_algorithm" : "pbkdf2hmac",
                "sub_algorithm" : "sha512", "salt" : None, "salt_size" : 16, "output_size" : 32}    
    
    def _get_password(self):
        self.password = password = self._password or getpass.getpass(self.password_prompt.format(self))
        return password
                
    def _set_password(self, value):
        if self.remember_password:
            self._password = value
            pride.Instruction
        else:
            self._password = ''
            
    def _get_password_hash(self):
        return self._hash_password(self.password)
    password_hash = property(_get_password_hash)
        
    def get_credentials(self):
        return (self.username, 
                self.password_hash if self.hash_password_clientside else self.password)
            
    def register(self):
        return self.get_credentials()
        
    def register_success(self):
        self.alert("Registered successfully", level=self.verbosity["register_success"])
        
    def register_failure(self):
        self.alert("Registration failed", level=self.verbosity["register_failure"])
        
    def login(self):
        return self.get_credentials()
        
    def login_success(self, server_response):
        self.alert("Login success; Received server response: {}".format(server_response, level=self.verbosity['login_success']))
        
    def login_failure(self, server_response):
        self.alert("Login failure; Received server response: {}".format(server_response, level=self.verbosity['login_failure']))
        
    def _hash_password(self, password):
        return pride.security.hash_password(password, self.iterations, algorithm=self.password_hashing_algorithm, 
                                                                       sub_algorithm=self.sub_algorithm,
                                                                       salt=self.salt, salt_size=self.salt_size, 
                                                                       output_size=self.output_size)                        
    

class Password_Based_Protocol_Server(Authenticated_Service):
    
    defaults = {"iterations" : 100000, "password_hashing_algorithm" : "pbkdf2hmac",
                "sub_algorithm" : "sha512", "salt_size" : 16, "output_size" : 32} 
     
    remotely_available_procedures = ("register", "login")
    
    def register(self, username, password):
        salt = os.urandom(self.salt_size)
        password_hash = self._hash_password(password, salt)
        self.database.insert_into("Users", (username, password_hash, salt))
        return self.register_success(username)
        
    def register_success(self, username):
        return self.registration_success_message.format(username)
    
    def register_failure(self, username):
        return self.registration_failure_message.format(username)
        
    def login(self, username, password):      
        correct_hash, salt = self.database.query("Users", retrieve_fields=("password_hash", "salt"), 
                                                          where={"username" : username})                                                          
        password_hash = self._hash_password(password, salt)
        if pride.security.constant_time_comparison(password_hash, correct_hash):
            return self.login_success(username)
        else:
            return self.login_failure(username)
            
    def login_success(self, username):
        self.alert("'{}' logged in successfully".format(username), level=self.verbosity["login_success"])
        return True
        
    def login_failure(self, username):
        self.alert("'{}' failed to login".format(username), level=self.verbosity["login_failure"])
        return False         
        
    def _hash_password(self, password, salt):
        return pride.security.hash_password(password, self.iterations, algorithm=self.password_hashing_algorithm, 
                                                                       sub_algorithm=self.sub_algorithm,
                                                                       salt=salt, output_size=self.output_size)                        
    
def test_Password_Based_Protocol():
    
    
    