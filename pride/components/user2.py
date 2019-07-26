from os import urandom
import getpass

import pride.functions.security
import pride.components.asymmetric
import pride.components.shell
from pride.functions.persistence import save_data, load_data
from pride.functions.utilities import slide

def generate_identity(identifier=None, keypair=None, secret=None,
                      identifier_size=32, secret_size=32):
    """ usage: generate_identity(identifier=None, keypair=None, secret=None,
                                 identifier_size=32, secret_size=32) => identifier, keypair, secret

        Create a new identifier/keypair/secret.
        Pre-determined values may be passed in as arguments.
        If not, then the size of the generated parameters may be tuned.
        Asymmetric key pairs do not support alternative sizes"""
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
    return pride.functions.security.encrypt(message, encryption_key, mac_key)

def decrypt_identity(cryptogram, encryption_key, mac_key):
    serialized_data = pride.functions.security.decrypt(cryptogram, encryption_key, mac_key)
    identifier, private_key, public_key, secret = load_data(serialized_data)
    return private_key, public_key, secret

def store_identity(encryption_key, mac_key, identifier, private_key, public_key, secret, storage="/Python/Persistent_Storage"):
    """ usage: store_identity(encryption_key, mac_key, identifier, private_key, public_key, secret,
                              storage="/Python/Persistent_Storage") => None

        Encrypts the identifier/key pair/secret information and stores it in the object specified as storage.
        The storage object must support __getitem__ and __setitem__"""
    cryptogram = encrypt_identity(identifier, (private_key, public_key), secret, encryption_key, mac_key)
    pride.objects[storage]["/Users/{}".format(identifier)] = cryptogram

def load_identity(identifier, encryption_key, mac_key, storage="/Python/Persistent_Storage"):
    """ usage: load_identity(identifier, encryption_key, mac_key,
                             storage="/Python/Persistent_Storage") => private_key, public_key, secret

        Returns serialized private key, serialized public key, and secret bytes.
        Raises KeyError if identifier is not found."""
    cryptogram = pride.objects[storage]["/Users/{}".format(identifier)]
    return decrypt_identity(cryptogram, encryption_key, mac_key)


class User(pride.components.base.Base):
    """ Handles the master username and password, as well as derived cryptographic materials, and provides an interface for utilizing them. """

    defaults = {"kdf_hash_algorithm" : "sha256", "kdf_iterations" : 1000000,
                "encryption_key_size" : 32, "mac_key_size" : 32,
                "iv_size" : 12, "encryption_mode" : "GCM", "encryption_algorithm" : "AES",
                "mac_hash_algorithm" : "sha256",

                "username" : None, "private_key" : None, "public_key" : None, "secret" : None,
                "master_encryption_key" : None, "master_mac_key" : None,
                "data_encryption_key" : None, "data_mac_key" : None,
                "public_key" : None, "private_key" : None, "password" : None,

                "storage_reference" : "/Python/Persistent_Storage",
                "password_prompt" : "{}: Please enter the password for '{}': ",
                "auto_register" : False, "auto_login" : True}

    parser_args = ("username", )
    mutable_defaults = {"login_token" : dict}
    predefaults = {"_password" : None}
    verbosity = {"login_success" : "vv", "registering" : "vv"}


    def _get_password(self):
        if self._password is None:
            self._password = getpass.getpass(self.password_prompt.format(self.reference, self.username))
        return self._password
    def _set_password(self, value):
        self._password = value
    password = property(_get_password, _set_password)

    def _get_username(self):
        while self._username in (None, ''):
            self._username = raw_input("{}: Please provide username: ".format(self.reference))
        return self._username
    def _set_username(self, value):
        self._username = value
    username = property(_get_username, _set_username)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.auto_login:
            self.login()

    def login(self):
        while True:
            self.derive_master_keys()

            try:
                cryptogram = self.find_identity(self.username)
            except ValueError:
                self.username = self.password = None
                continue
            else:
                try:
                    private_key, public_key, secret = decrypt_identity(cryptogram, self.master_encryption_key, self.master_mac_key)
                except pride.functions.security.InvalidTag:
                    self.alert("Invalid password", level=0)
                    self.password = None
                    self.username = None
                else:
                    break

        self.private_key = pride.components.asymmetric.EC_Private_Key.deserialize(private_key)
        self.public_key = pride.components.asymmetric.EC_Public_Key.deserialize(public_key)
        self.secret = secret
        self.derive_data_keys(secret)

        self.add(self.private_key)
        self.add(self.public_key)
        self.alert("Logged in successfully", level=self.verbosity["login_success"])

    def attempt_login(self):
        self.derive_master_keys()

        try:
            cryptogram = self.find_identity(self.username)
        except ValueError:
            self.username = self.password = None
            return False
        else:
            try:
                private_key, public_key, secret = decrypt_identity(cryptogram, self.master_encryption_key, self.master_mac_key)
            except pride.functions.security.InvalidTag:
                self.password = self.username = None
                return False

        self.private_key = pride.components.asymmetric.EC_Private_Key.deserialize(private_key)
        self.public_key = pride.components.asymmetric.EC_Public_Key.deserialize(public_key)
        self.secret = secret
        self.derive_data_keys(secret)

        self.add(self.private_key)
        self.add(self.public_key)
        self.alert("Logged in successfully", level=self.verbosity["login_success"])
        return True

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
        kdf = pride.functions.security.key_derivation_function(
                algorithm=self.kdf_hash_algorithm, length=size1 + size2,
                salt=self.username, iterations=self.kdf_iterations)
                #salt needs to be changed to something that's actually random
        master_key = kdf.derive(self.password)

        self.master_encryption_key = master_key[:size1]
        self.master_mac_key = master_key[size1:size1 + size2]

    def derive_data_keys(self, secret):
        size1 = self.encryption_key_size
        size2 = self.mac_key_size
        kdf = pride.functions.security.hkdf_expand(self.kdf_hash_algorithm, size1 + size2,
                                                   info=self.username + ":" + "encryption and mac keys")
        keys = kdf.derive(secret)
        self.data_encryption_key = keys[:size1]
        self.data_mac_key = keys[size1:size1 + size2]

    def handle_not_registered(self, identifier):
        if self.auto_register or pride.components.shell.get_permission("{}: Register as '{}'? (y/n): ".format(self.reference, identifier)):
            if not self.auto_register:
                self.alert("Registering user '{}'".format(identifier), level=self.verbosity["registering"])
            self.store_new_identity(identifier)
        else:
            raise ValueError("{} not registered; Unable to continue".format(identifier))

    def store_new_identity(self, identifier):
        identifier, keypair, secret = generate_identity(identifier)
        store_identity(self.master_encryption_key, self.master_mac_key, identifier,
                       keypair[0], keypair[1], secret, storage=self.storage_reference)

    def forget_identity(self, identifier):
        #identifiers = pride.objects[self.storage_reference]
        #del identifiers["/Users/{}".format(identifier)]
        del pride.objects[self.storage_reference]["/_{}/{}".format(type(self), identifier)]

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
        return pride.functions.security.encrypt(data=data, key=self.data_encryption_key, mac_key=self.data_mac_key,
                                                iv=urandom(self.iv_size), extra_data=extra_data,
                                                algorithm=self.encryption_algorithm, mode=self.encryption_mode,
                                                return_mode=return_mode)

    def decrypt(self, packed_encrypted_data):
        """ Decrypts packed encrypted data as returned by encrypt. The Users
            encryption key is used to decrypt the data. """
        return pride.functions.security.decrypt(packed_encrypted_data, self.data_encryption_key, self.data_mac_key)

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
        return pride.functions.security.apply_mac(self.data_mac_key, data, self.mac_hash_algorithm)

    def verify(self, macd_data):
        """ Verifies data with the mac returned by authenticate. Data that is
            verified has two extremely probable guarantees: that it did indeed
            come from who an authorized party, and that it was not manipulated
            by unauthorized parties in transit.

            Returns data on successful verification; Returns False on failure. """
        return pride.functions.security.verify_mac(self.data_mac_key, macd_data, self.mac_hash_algorithm)

    def generate_tag(self, data):
        """ Generates a unique, unforgeable tag based on supplied data. """
        return pride.functions.security.generate_mac(self.data_mac_key, data, self.mac_hash_algorithm)

    def save_data(self, *args):
        """ Serializes and authenticates supplied arguments.
            To reload, use load_data. """
        package = pride.functions.persistence.save_data(*args)
        return self.authenticate(package)

    def load_data(self, package):
        """ Authenticate, then deserialize the supplied bytes.
            Returns the arguments that were passed to save_data."""
        packed_bytes = self.verify(package)
        if packed_bytes is not pride.functions.security.INVALID_TAG:
            return pride.functions.persistence.load_data(packed_bytes)
        else:
            raise InvalidTag()

    def hash(self, data):
        """ Hash data using the user objects specified hashing algorithm """
        hasher = pride.functions.security.hash_function(self.mac_hash_algorithm)
        hasher.update(data)
        return hasher.finalize()

    def generate_strong_password(self, client_program, username, password_size=32):
        """ Usage: user = pride.objects["/User"]
                   token = user.generate_strong_login_token(client_program, username, password_size)

            Generates a cryptographically strong password, derived from the identity secret material.
            This password is only available on the machine that /Python/Persistent_Storage resides on."""
        kdf = pride.functions.security.hkdf_expand(self.kdf_hash_algorithm, password_size,
                                                   info=client_program + ':' + username)
        return kdf.derive(self.secret)

    def generate_portable_password(self, client_program, username, password_size=32):
        """ Usage: user = pride.objects["/User"]
                   token = user.generate_portable_password(client_program, username, password_size)

            Generate a key stretched password for the target program and username, derived from the master password."""
        salt = client_program + username
        kdf = pride.functions.security.key_derivation_function(salt, algorithm=self.kdf_hash_algorithm,
                                                               length=password_size,
                                                               iterations=self.kdf_iterations)
        return kdf.derive(self.password)

    def sign(self, data):
        """ Signs a block of data using the Users private key """
        return self.private_key.sign(data)

    def get_derivation_description(self):
        iterations = ','.join(chunk for chunk in slide(str(reversed(str(self.kdf_iterations))), 3))
        return "PBKDF2-{} {} iterations".format(self.kdf_hash_algorithm, self.kdf_iterations)


class Session(User):
    """ An ID that only persists for one application execution. """
    verbosity = {"login_success" : "vvv", "registering" : "vvv"}

    def delete(self):
        self.forget_identity(self.username)
        super(Session, self).delete()

def test_User():
    user = User(username="test_User_unit_test")
    cryptogram = user.encrypt("Test data", "Extra test data")
    assert user.decrypt(cryptogram) == ("Test data", "Extra test data")

    saved = user.save_data(cryptogram)
    reloaded = user.load_data(saved)
    tagged = user.authenticate(saved)
    user.verify(tagged)
    user.hash(tagged)

    user.generate_tag(tagged)
    user.generate_strong_password("/Python/Data_Transfer_Service", "test_User_unit_test")
    user.generate_portable_password("/Python/Data_Transfer_Service", "test_User_unit_test")

    message = "sign here: "
    signature = user.private_key.sign(message)
    assert user.public_key.verify(signature, message)

    user.forget_identity(user.username)
    user.alert("Unit test passed", level=0)

if __name__ == "__main__":
    test_User()
