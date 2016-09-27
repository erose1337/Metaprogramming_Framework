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
    
def generate_identity(identifier=None, keypair=None, secret=None,
                      identifier_size=32, keypair_size=4096, secret_size=32):
    if identifier is None:
        identifier = urandom(identifier_size)
    if keypair is None:
        keypair = generate_public_private_keypair(keypair_size)
    if secret is None:
        secret = urandom(secret_size)
        
    return idenitifier, keypair, secret
    
def encrypt_identity(identitifier, public_key, private_key, secret, encryption_key, mac_key, encrypted_public_key=False):   
    if encrypted_public_key:
        public_key = encrypt(public_key, encryption_key)
    private_key = encrypt(private_key, encryption_key)
    secret = encrypt(secret, encryption_key)
    mac = HMAC(identifier + public_key + private_key + secret, mac_key)
    return public_key, private_key, secret, mac
  
def decrypt_identity(identifier, public_key, private_key, secret, mac, 
                     encryption_key, mac_key, encrypted_public_key=False):    
    _mac = HMAC(identifier + public_key + private_key + secret, mac_key)
    if _mac != mac:
        return -1
    if encrypted_public_key:
        public_key = decrypt(public_key, encryption_key)
    private_key = decrypt(private_key, encryption_key)
    secret = decrypt(secret, encryption_key)
    return public_key, private_key, secret
    
    
class Identity_Service(pride.authentication3.Authenticated_Service):
    
    database_structure = {"Users", ("identifier BLOB UNIQUE PRIMARY_KEY",
                                    "public_key BLOB", "private_key BLOB", "secret BLOB")}                                    
    remote_available_procdures = ("retrieve_identity", )
    
    def register(self, identifier, public_key, private_key, secret, mac):
        self.database.insert_into("Users", (identifier, public_key, private_key, secret, mac))
    
    def retrieve_identity(self, identifier, contents="all"):
        if contents == "all":
            fields = ("public_key", "private_key", "secret")        
        else:
            fields = ("public_key", )
        return self.database.query("Users", retrieve_fields=("public_key", ),
                                            where={"identifier" : identifier})                                                   
        
    
class Identity(pride.authentication3.Authenticated_Client):
            
    def _generate_credentials(self):
        identifier, keypair, secret = generate_identity(self.identifier, self.keypair, self.secret)
        public_key, private_key, 
        return (self, self.identifier, self.public_key,), {}
        
    @pride.decorators.with_arguments_from(_get_identifier)
    @pride.authentication3.remote_procedure_call(callback_name="retrieve_results")
    def retrieve_identity(self, identifier, contents="all"):
        pass
        
    def retrieve_results(self, response):
        self.alert("{}".format(response), level=0)
        
        
def test_Identity_Service():
    service = Identity_Service()
    identity = Identity(identifier="Ella-land rocks!")
    
if __name__ == "__main__":
    test_Identity_Service()
    