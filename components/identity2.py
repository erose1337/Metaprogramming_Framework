 #generate master symmetric encryption and MAC key from password via slow hashing
 #generate random public/private keypair (identity keys)
 #generate random symmetric secret
 #generate identifier string associated with identity
 #
 #Using master encryption key, encrypt private key and optionally the associated public key, along with the symmetric secret
 #generate MAC via HMAC(identifier | (potentially encrypted) public key | encrypted private key | encrypted symmetric secret, 
 #                      MAC key)
 #
 #upload MAC, identifier, public key, encrypted private key, and encrypted symmetric secret to server
 #  
 #
 #--login steps:
 #   
 #   retrieve encrypted keys from server by sending identifier
 #   generate master symmetric keys from password
 #   verify MAC
 #   decrypt keys
 #   derive encryption/MAC keys from symmetric secret

from os import urandom
import getpass

import pride.functions.decorators
import pride.functions.security
import pride.components.rpc
import pride.components.asymmetric
import pride.components.shell
from pride.functions.persistence import save_data, load_data
encrypt = pride.functions.security.encrypt
decrypt = pride.functions.security.decrypt

def generate_identity(identifier=None, keypair=None, secret=None,
                      identifier_size=32, secret_size=32):
    if identifier is None:
        identifier = urandom(identifier_size)
    if keypair is None:
        keypair = pride.components.asymmetric.generate_ec_keypair()
    if secret is None:
        secret = urandom(secret_size)
        
    return identifier, keypair, secret
    
def encrypt_identity(identifier, keypair, secret, encryption_key, mac_key):   
    private_key, public_key  = keypair[0].serialize(), keypair[1].serialize()
    message = save_data(identifier, private_key, public_key, secret)    
    return encrypt(message, encryption_key, mac_key)
  
def decrypt_identity(cryptogram, encryption_key, mac_key):    
    serialized_data = decrypt(cryptogram, encryption_key, mac_key)
    identifier, private_key, public_key, secret = load_data(serialized_data)
    return private_key, public_key, secret
    
def store_identity(encryption_key, mac_key, identifier, private_key, public_key, secret, storage="/Python/Persistent_Storage"):
    cryptogram = encrypt_identity(identifier, (private_key, public_key), secret, encryption_key, mac_key)    
    pride.objects[storage]["/Users/{}".format(identifier)] = cryptogram
    
def load_identity(identifier, encryption_key, mac_key, storage="/Python/Persistent_Storage"):    
    cryptogram = pride.objects[storage]["/Users/{}".format(identifier)]
    return decrypt_identity(cryptogram, encryption_key, mac_key)
        

class User(pride.base.Base):
    
    defaults = {"kdf_hash_algorithm" : "sha256", "kdf_iteration_count" : 100000,
                "login_token_size" : 32, "encryption_key_size" : 32, "mac_key_size" : 32,

                "identifier" : None, "private_key" : None, "public_key" : None, "secret" : None,
                "master_encryption_key" : None, "master_mac_key" : None, 
                "data_encryption_key" : None, "data_mac_key" : None, 
                "public_key" : None, "private_key" : None,
                "login_to_services" : tuple(),
                
                "storage_reference" : "/Python/Persistent_Storage",
                "password_prompt" : "{}: Please enter the password: "}
    
    mutable_defaults = {"login_token" : dict}
    flags = {"_password" : None}
    verbosity = {"login_success" : 'v'}
    
    def _get_password(self):
        if self._password is None:
            self._password = getpass.getpass(self.password_prompt)
        return self._password
    def _set_password(self, value):
        self._password = value
    password = property(_get_password, _set_password)
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password_prompt = self.password_prompt.format(self.reference)
        self.login()
        self.alert("Logged in successfully", level=self.verbosity["login_success"])
        
    def login(self):        
        self.derive_master_keys()
        
        cryptogram = self.find_identity(self.identifier)                
        private_key, public_key, secret = decrypt_identity(cryptogram, self.master_encryption_key, self.master_mac_key)                    
        
        self.private_key = pride.components.asymmetric.EC_Private_Key.deserialize(private_key)    
        self.public_key = pride.components.asymmetric.EC_Public_Key.deserialize(public_key)
        
        self.derive_login_tokens(secret)
        self.derive_data_keys(secret)        
        
    def find_identity(self, identifier):
        try:
            cryptogram = pride.objects[self.storage_reference]["/Users/{}".format(identifier)]            
        except KeyError:    
            if self.storage_reference not in pride.objects:
                raise
            else:
                self.handle_not_registered(identifier)    
                cryptogram = pride.objects[self.storage_reference]["/Users/{}".format(identifier)]            
        return cryptogram
        
    def derive_master_keys(self):
        size1, size2 = self.encryption_key_size, self.mac_key_size        
        kdf = invoke("pride.functions.security.key_derivation_function", 
                     algorithm=self.kdf_hash_algorithm, length=size1 + size2, 
                     salt=self.identifier, iterations=self.kdf_iteration_count)                
        master_key = kdf.derive(self.password)
        
        self.master_encryption_key = master_key[:size1]
        self.master_mac_key = master_key[size1:size1 + size2]
        
    def derive_login_tokens(self, secret):
        kdf_hash_algorithm = self.kdf_hash_algorithm
        login_token_size = self.login_token_size
        for service in self.login_to_services:
            kdf = pride.functions.security.hkdf_expand(kdf_hash_algorithm, login_token_size,
                                                       info=self.identifier + ":" + service)                                                               
            self.login_token[service] = kdf.derive(secret)
            
    def derive_data_keys(self, secret):
        size1 = self.encryption_key_size
        size2 = self.mac_key_size
        kdf = pride.functions.security.hkdf_expand(self.kdf_hash_algorithm, size1 + size2, 
                                                   info=self.identifier + ":" + "encryption and mac keys")
        keys = kdf.derive(secret)
        self.data_encryption_key = keys[:size1]
        self.data_mac_key = keys[size1:size1 + size2]
        
    def store_new_identity(self, identifier):
        identifier, keypair, secret = generate_identity(identifier)
        store_identity(self.master_encryption_key, self.master_mac_key, identifier,
                       keypair[0], keypair[1], secret, storage=self.storage_reference)
        
    def handle_not_registered(self, identifier):
        if pride.components.shell.get_permission("{}: Register as '{}'? (y/n): ".format(self.reference, identifier)):
            self.store_new_identity(identifier)
        else:
            raise NotImplementedError()
                
                
def test_User():
    user = User(identifier="localhost", login_to_services=("/Python/Interpreter", ))
    
    
if __name__ == "__main__":
    test_User()
    