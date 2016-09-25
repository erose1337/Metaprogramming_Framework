import sys
import getpass
from os import urandom

import pride.components.base
import pride.functions.security
import pride.components.shell
import pride.functions.persistence

class InvalidUsername(BaseException): pass

class User(pride.components.base.Base):
    """ A User object for managing secure information and client accounts.
        A user is capable of performing manipulation of secure data,
        including encryption and decryption. The user object is responsible
        for deriving and holding keys required for such manipulation. """
    defaults = {# security configuration options    
                # these may need to update with time. If so the site_config file can be used instead of changing this dictionary.
                "hash_function" : "SHA256", "kdf_iteration_count" : 100000, 
                "salt_size" : 16, "key_length" : 32, "iv_size" : 12,
                
                # these will probably be updated less frequently
                "encryption_mode" : "GCM", "encryption_algorithm" : "AES",
                
                # login/key derivation can be bypassed by supplying keys directly
                # note that encryption key, salt, and mac key must be supplied to
                # skip the login/key derivation process
                # filesystem_key is used to access nonindexable files in /Python/File_System
                "encryption_key" : bytes(), "salt" : bytes(), "mac_key" : bytes(),
                "file_system_key" : bytes(),
                
                # similarly, username may be assigned instead of prompted. 
                "username" : '', 
                
                # These may be changed for specific application needs
                "hkdf_mac_info_string" : "{} Message Authentication Code Key",
                "hkdf_encryption_info_string" : "{} Encryption Key",
                "hkdf_file_system_info_string" : "{} File_System key",
                "password_prompt" : "{}: Please provide the pass phrase or word: ",
                
                # the salt and verifier file are stored in the /Python/File_System
                # nonindexable files have the filename hashed upon storing/search
                "salt_filetype" : "pride.components.fileio.Database_File",
                "verifier_filetype" : "pride.components.fileio.Database_File",
                "verifier_indexable" : False,
                
                "open_command_line" : True}
    
    parser_ignore = ("mac_key", "encryption_key", "hkdf_mac_info_string", 
                     "hkdf_encryption_info_string", "hkdf_file_system_info_string",
                     "password_prompt", "iv_size", "verifier_filetype",
                     "salt_indexable", "kdf_iteration_count",
                     "encryption_mode", "encryption_algorithm", "verifier_indexable",
                     "salt_size", "salt_filetype", "salt", "file_system_key")
    
    flags = {"_password_verifier_size" : 32, "_reset_encryption_key" : False,
             "_reset_file_system_key" : False, "_reset_mac_key" : False}
    
    verbosity = {"password_verified" : 'v', "invalid_password" : 0, "login_success" : 0}
    
    def _get_password(self):
        return getpass.getpass(self.password_prompt.format(self.reference))
    password = property(_get_password)
    
    def _get_username(self):
        if not self._username:
            username_prompt = "{}: Please provide a username: ".format(self.reference)
            self._username = raw_input(username_prompt, must_reply=True)
        return self._username
    def _set_username(self, value):
        self._username = value
    username = property(_get_username, _set_username)   
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)        
        
        login_success = self.encryption_key and self.mac_key and self.file_system_key and self.salt
        while not login_success:                
            try:
                self.login()
            except (InvalidUsername, pride.functions.security.InvalidTag): # failed to open password verifier file
                self.username = ''
                if self._reset_encryption_key:
                    self.encryption_key = bytes()
                if self._reset_mac_key:
                    self.mac_key = bytes()
                self.alert("Login failed", level=self.verbosity["invalid_password"])
                continue
            else:
                login_success = True      
        assert self.encryption_key and self.mac_key and self.file_system_key and self.salt
        self.alert("Logged in successfully", level=self.verbosity["login_success"])
        if self.open_command_line:
            self.create("pride.components.shell.Command_Line")       
                        
    def login(self):
        """ Attempt to login as username using a password. Upon success, the
            users encryption and mac key are derived and stored in memory.
            Upon failure, the prompt is repeated. """                
        if not self.salt:
            with self.create(self.salt_filetype, # uses Database_Files by default
                             "{}_salt.bin".format(self.username), 
                             "a+b", indexable=True) as _file:                 
                _file.seek(0)
                salt = _file.read(self.salt_size)
                if not salt:
                    salt = urandom(self.salt_size)
                    _file.write(salt)
            self.salt = salt
        else:
            salt = self.salt 
            
        kdf = invoke("pride.functions.security.key_derivation_function", 
                     algorithm=self.hash_function, length=key_length, 
                     salt=salt, iterations=self.kdf_iteration_count)
        master_key = kdf.derive(self.username + ':' + self.password)
        
        hkdf_options = {"algorithm" : self.hash_function, "length" : key_length}      
        
        if not self.file_system_key:
            hkdf_options["info"] = self.hkdf_file_system_info_string.format(self.username + salt)
            file_system_kdf = invoke("pride.functions.security.hkdf_expand", **hkdf_options)
            self.file_system_key = file_system_kdf.derive(master_key)       
            self._reset_file_system_key = True            
        if not self.encryption_key:
            hkdf_options["info"] = self.hkdf_encryption_info_string.format(self.username + salt)
            encryption_kdf = invoke("pride.functions.security.hkdf_expand", **hkdf_options)
            self.encryption_key = encryption_kdf.derive(master_key)                
            self._reset_encryption_key = True
        if not self.mac_key:
            hkdf_options["info"] = self.hkdf_mac_info_string.format(self.username + salt)        
            mac_kdf = invoke("pride.functions.security.hkdf_expand", **hkdf_options)
            self.mac_key = mac_kdf.derive(master_key)
            self._reset_mac_key = True
          
        try:
            with self.create(self.verifier_filetype, file_name, 'rb') as _file:
                keys = self.decrypt(_file.read())
                self.data_encryption_key = keys[:self.keysize]
                self.private_key = keys[self.keysize:]
        except IOError:
            message = "{}: username '{}' does not exist. Create it?: (y/n) ".format(self, self.username)
            if pride.components.shell.get_permission(message):
                with self.create(self.verifier_filetype, file_name, "wb") as _file:
                    _file.write(os.u
                    
            
    def encrypt(self, data, extra_data='', return_mode="cryptogram"):
        """ usage: pride.objects["/User"].encrypt(data, extra_data='', 
                                                  return_mode="cryptogram") => cryptogram or unpacked cryptogram
        
            Encrypt and authenticates the supplied data; 
            Authenticates, but does not encrypt, any extra_data. 
            
            The data is encrypted using the Users encryption key. 
            
            If return_mode == "cryptogram", returns packed encrypted bytes. 
            If return_mode == "values", returns unpacked header, ciphertext, iv, mac_tag, extra_data.
            
            Default cipher and mode of operation is AES-256-GCM.
            Modes not recognized as providing authenticity or integrity (i.e. CTR) will be authenticated via HMAC."""        
        return pride.functions.security.encrypt(data=data, key=self.encryption_key, mac_key=self.mac_key, 
                                      iv=urandom(self.iv_size), extra_data=extra_data, 
                                      algorithm=self.encryption_algorithm, mode=self.encryption_mode,
                                      return_mode=return_mode)
                                      
    def decrypt(self, packed_encrypted_data):
        """ Decrypts packed encrypted data as returned by encrypt. The Users 
            encryption key is used to decrypt the data. """
        return pride.functions.security.decrypt(packed_encrypted_data, self.encryption_key, self.mac_key)
    
    def authenticate(self, data):
        """ Returns tagged data.
            
            Authenticates and provides integrity to a piece of data. 
            Authentication and integrity are generally requirements for any data
            that must be secured. Returns a message authentication code.
            
            Note that User.encrypt uses AES-GCM mode, which authenticates
            data and extra_data automatically. 
            
            Combining encryption and authentication is not simple. This method 
            should be used ONLY in conjunction with unencrypted data, unless 
            you are certain you know what you are doing. """        
        return pride.functions.security.apply_mac(self.mac_key, data, self.hash_function)
        
    def verify(self, macd_data):
        """ Verifies data with the mac returned by authenticate. Data that is 
            verified has two extremely probable guarantees: that it did indeed
            come from who an authorized party, and that it was not manipulated 
            by unauthorized parties in transit. 
            
            Returns data on successful verification; Returns False on failure. """
        return pride.functions.security.verify_mac(self.mac_key, macd_data, self.hash_function)
    
    def generate_tag(self, data):
        """ Generates a unique, unforgeable tag based on supplied data. """
        return pride.functions.security.generate_mac(self.mac_key, data, self.hash_function)
        
    def save_data(self, *args):
        package = pride.functions.persistence.save_data(*args)
        return self.authenticate(package)
        
    def load_data(self, package):
        packed_bytes = self.verify(package)        
        if packed_bytes is not pride.functions.security.INVALID_TAG:
            return pride.functions.persistence.load_data(packed_bytes)
        else:            
            return packed_bytes # == INVALID_TAG
    
    def hash(self, data):
        """ Hash data using the user objects specified hashing algorithm """
        hasher = pride.functions.security.hash_function(self.hash_function)    
        hasher.update(data)
        return hasher.finalize()
        
        
class Session(User): 

    verbosity = {"login_success" : "vvvv"}
    defaults = {"open_command_line" : False}
    required_attributes = ("username", "encryption_key", "mac_key", "file_system_key", "salt")    

        
def test_User():
    import pride    
    user = pride.objects["/User"]
    data = "This is some test data!"
    packed_encrypted_data = user.encrypt(data)
    assert user.decrypt(packed_encrypted_data) == data
    
    saved = user.save_data(data, packed_encrypted_data)
    _data, _packed_encrypted_data = user.load_data(saved)
    assert _data == data
    assert _packed_encrypted_data == packed_encrypted_data
    
    user.hash(_data)
    user.alert("Passed unit test", level=0)
    raise SystemExit()
    
if __name__ == "__main__":
    test_User()
    