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

import pride.functions.decorators
import pride.components.rpc
import pride.components.asymmetric
 
def generate_identity(identifier=None, keypair=None, secret=None,
                      identifier_size=32, keypair_size=4096, secret_size=32):
    if identifier is None:
        identifier = urandom(identifier_size)
    if keypair is None:
        keypair = pride.components.asymmetric.generate_ec_keypair()
    if secret is None:
        secret = urandom(secret_size)
        
    return identifier, keypair, secret
    
def encrypt_identity(identitifier, keypair, secret, encryption_key, mac_key, encrypted_public_key=False):   
    private_key, public_key  = keypair
    if encrypted_public_key:
        public_key = encrypt(public_key, encryption_key)
    private_key = encrypt(private_key, encryption_key)
    secret = encrypt(secret, encryption_key)
    mac = HMAC(identifier + private_key + public_key + secret, mac_key)
    return private_key, public_key, secret, mac
  
def decrypt_identity(identifier, keypair, secret, mac, 
                     encryption_key, mac_key, encrypted_public_key=False):    
    private_key, public_key  = keypair
    _mac = HMAC(identifier + private_key + public_key + secret, mac_key)
    if _mac != mac:
        return -1
    if encrypted_public_key:
        public_key = decrypt(public_key, encryption_key)
    private_key = decrypt(private_key, encryption_key)
    secret = decrypt(secret, encryption_key)
    return private_key, public_key, secret
    
    
class Identity_Service(pride.components.rpc.RPC_Service):
    
    database_structure = {"Users" : ("identifier BLOB PRIMARY_KEY UNIQUE",
                                     "private_key BLOB", "public_key BLOB", "secret BLOB")}                
    remotely_available_procdures = ("store_identity", "retrieve_identity")
    
    def store_identity(self, identifier, private_key, public_key, secret, mac):
        self.database.insert_into("Users", (identifier, private_key, public_key, secret, mac))
        return "Stored successfully"
        
    def retrieve_identity(self, identifier, contents="all"):
        if contents == "all":
            fields = ("private_key", "public_key", "secret")        
        else:
            fields = ("public_key", )
        return self.database.query("Users", retrieve_fields=fields,
                                            where={"identifier" : identifier})                                                   
        
    
class Identity(pride.components.rpc.RPC_Client):
            
    defaults = {"target_service" : "/Identity_Service",
                "identifier" : None, "keypair" : None, "secret" : None,
                "encryption_key" : None, "mac_key" : None, "keypair" : None,
                "encrypt_public_key" : True}
                
    def _generate_credentials(self):
        identifier, keypair, secret = generate_identity(self.identifier, self.keypair, self.secret)
        private_key, public_key, secret, mac = encrypt_identity(identifier, keypair, secret, 
                                                                self.encryption_key, self.mac_key, 
                                                                self.encrypt_public_key)
        return (self, identifier, private_key, public_key, secret, mac), {}
    
    @pride.functions.decorators.with_arguments_from(_generate_credentials)
    @pride.components.rpc.remote_procedure_call(callback_name="store_results")
    def store_identity(self, identifier, private_key, public_key, secret, mac):
        pass
        
    def store_results(self, result):
        self.alert("{}".format(result), 0)
            
    def _get_identifier(self):
        return (self, self.identifier), {}
        
    @pride.functions.decorators.with_arguments_from(_get_identifier)
    @pride.components.rpc.remote_procedure_call(callback_name="retrieve_results")
    def retrieve_identity(self, identifier, contents="all"):
        pass
        
    def retrieve_results(self, response):
        self.alert("{}".format(response), level=0)
        
        
def test_Identity_Service():
    service = Identity_Service()
    identity = Identity(identifier="Ella-land rocks!")
    
    identity.store_identity()
    identity.retrieve_identity()
    
if __name__ == "__main__":
    test_Identity_Service()
    