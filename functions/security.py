""" Provides security related functions such as encryption and decryption.
    Two backends are available: Ideally, the cryptography package has been
    installed, and that will be used. In situations where that is not feasible,
    usually due to permissions, the pride.cryptographyless module will be used
    instead. """
import os

from pride.functions.utilities import save_data, load_data
from pride.errors import SecurityError, InvalidPassword, InvalidTag, InvalidSignature
        
AEAD_MODES = ["GCM"]
INVALID_TAG = [] # just needs to be a unique object
    
try:                    
    import cryptography
except ImportError:
    # use an alternative file when the cryptography package is not installed    
    from cryptographyless import *        
        
else:
    import hashlib
    import cryptographyless
    
    del cryptography    
    from cryptography.exceptions import InvalidTag, InvalidSignature
    from cryptography.hazmat.primitives.hmac import HMAC
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.kdf.hkdf import HKDF, HKDFExpand
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.backends import openssl
    from cryptography.hazmat.primitives.constant_time import bytes_eq
    BACKEND = openssl.backend      
        
    def random_bytes(count):
        """ Generates count cryptographically secure random bytes """
        return os.urandom(count)         
        
    def hash_function(algorithm_name, backend=BACKEND):
        """ Returns a Hash object of type algorithm_name from 
            cryptography.hazmat.primitives.hashes """
        return hashes.Hash(getattr(hashes, algorithm_name.upper())(), backend=backend)
        
    def key_derivation_function(salt, algorithm="SHA256", length=32, 
                                iterations=100000, backend=BACKEND):
        """ Returns an key derivation function object from
            cryptography.hazmat.primitives.kdf.pbkdf2 """
        return PBKDF2HMAC(algorithm=getattr(hashes, algorithm.upper())(),
                          length=length, salt=salt, iterations=iterations,
                          backend=backend)
        
    def hkdf_expand(algorithm="SHA256", length=256, info='', backend=BACKEND):
        """ Returns an hmac based key derivation function (expand only) from
            cryptography.hazmat.primitives.hkdf. """
        return HKDFExpand(algorithm=getattr(hashes, algorithm.upper())(),
                          length=length, info=info, backend=BACKEND)
    
    def apply_mac(key, data, algorithm="SHA256", backend=BACKEND):
        """ Generates a message authentication code and prepends it to data.
            Mac and data are packed via pride.functions.utilities.save_data. 
            
            Applying a message authentication code facilitates the goals
            of authenticity and integrity. Note it does not protect
            confidentiality (i.e. encryption).
            
            Combining a mac with encryption is NOT straightforward;
            Authenticating/providing integrity of confidential data
            should preferably be accomplished via an appropriate
            block cipher mode of operation, such as GCM. If this is
            not possible, encrypt-then-mac is most secure solution in
            general. """
        return save_data(generate_mac(key, data, algorithm, backend), data)
                
    def generate_mac(key, data, algorithm="SHA256", backend=BACKEND):
        """ Returns a message authentication code for verifying the integrity and
            authenticity of data by entities that possess the key. 
            
            Note this is a lower level function then apply_mac and
            only returns the mac itself. 
            
            The mac is generated via HMAC with the specified algorithm and key. """
        hasher = HMAC(key, getattr(hashes, algorithm.upper())(), backend=backend)
        hasher.update(algorithm + '::' + data)
        return hasher.finalize()
                        
    def verify_mac(key, packed_data, algorithm="SHA256", backend=BACKEND):
        """ Verifies a message authentication code as obtained by apply_mac.
            Successful comparison indicates integrity and authenticity of the data. 
            Returns data is comparison succeeds; Otherwise returns pride.functions.security.INVALID_TAG. """        
        mac, data = load_data(packed_data)
        hasher = HMAC(key, getattr(hashes, algorithm.upper())(), backend=backend)
        hasher.update(algorithm + '::' + data)
        try:
            hasher.verify(mac)
        except InvalidSignature:
            return INVALID_TAG
        else:
            return data
                                
    def encrypt(data='', key='', mac_key='', iv=None, extra_data='', algorithm="AES", 
                mode="GCM", backend=BACKEND, iv_size=16, hash_algorithm="SHA256",
                return_mode="cryptogram"):
        """ Encrypts data with the specified key. Returns packed encrypted bytes.
            If an iv is not supplied a random one of iv_size will be generated.
            By default, the GCM mode of operation is used and the iv is 
            automatically included in the extra_data authenticated by the mode. 
            
            Note that not all algorithms may support all modes of operation
            with all backends. 
            
            A mac key is required when GCM mode is not in used. This function
            will refuse to encrypt data without authentication/integrity checks,
            as this is considered a serious flaw in security. 
            
            Technically speaking, 'iv' is not always the correct term for the
            parameter passed, depending on the mode of operation used. However,
            using two different fields for what are functionally the same would
            increase complexity needlessly. """
        assert data and key, "data" if not data else "key"
        if algorithm.lower() in hashlib.algorithms_guaranteed:
            return cryptographyless.encrypt(data, key, iv, extra_data, algorithm, mode,
                                            backend, iv_size, mac_key, hash_algorithm)
                                            
        header = algorithm + '_' + mode 
        if mode not in AEAD_MODES:
            if not mac_key:
                raise ValueError("Unable to authenticate data because no mac key was supplied for {} mode".format(header))        
            else:
                header += "_" + hash_algorithm
        else:
            header += "_" + "AEAD"
            
        if not iv and iv != 0: # 0 is a valid nonce for CTR mode.
            iv = random_bytes(iv_size)
            
        if mode != "ECB":
            mode_args = (iv, )
        else:
            mode_args = tuple()
        
        encryptor = Cipher(getattr(algorithms, algorithm)(key), 
                           getattr(modes, mode)(*mode_args), 
                           backend=BACKEND).encryptor()        
            
        if mode in AEAD_MODES:       
            encryptor.authenticate_additional_data(extra_data)            
        ciphertext = encryptor.update(data) + encryptor.finalize()          
                     
        if mode in AEAD_MODES:
            mac_tag = encryptor.tag
        else:
            mac_tag = generate_mac(mac_key, header + ciphertext + iv + extra_data, hash_algorithm) 
        
        if return_mode == "cryptogram":
            return save_data(header, ciphertext, iv, mac_tag, extra_data)
        else:
            assert return_mode == "values"
            return header, ciphertext, iv, mac_tag, extra_data
            
    def decrypt(packed_encrypted_data, key, mac_key='', backend=BACKEND):
        """ Decrypts packed encrypted data as returned by encrypt with the same key. 
            If extra data is present, returns plaintext, extra_data. If not,
            returns plaintext. Raises InvalidTag on authentication failure. """
        header, ciphertext, iv, tag, extra_data = load_data(packed_encrypted_data)        
        algorithm, mode, authentication_algorithm = header.split('_', 2)   
        if algorithm.lower() in hashlib.algorithms_guaranteed:
            return cryptographyless.decrypt(packed_encrypted_data, key, mac_key, backend)
            
        mode_args = (iv, tag) if mode in AEAD_MODES else (iv, )
        decryptor = Cipher(getattr(algorithms, algorithm)(key), 
                           getattr(modes, mode)(*mode_args), 
                           backend=BACKEND).decryptor()
        if mode in AEAD_MODES:
            decryptor.authenticate_additional_data(extra_data)
        else:
            if not mac_key:
                raise ValueError("mac_key not supplied for {} mode".format(header))
            if not verify_mac(mac_key, save_data(tag, header + ciphertext + iv + extra_data), authentication_algorithm):
                raise InvalidTag("Failed to authenticate data")
            
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        if extra_data:
            return (plaintext, extra_data)     
        else:
            return plaintext
            
    def hash_password(password, iterations, algorithm="pbkdf2hmac", sub_algorithm="sha256",
                                            salt=None, salt_size=16, output_size=32,
                                            backend=BACKEND):
        salt = os.urandom(salt_size) if salt is None else salt
        header = save_data(algorithm, sub_algorithm, iterations, salt_size, output_size)
        if algorithm == "pbkdf2hmac":          
            hasher = PBKDF2HMAC(algorithm=getattr(hashes, sub_algorithm.upper())(),
                                length=output_size, salt=salt, iterations=iterations,
                                backend=backend)
            
            return save_data(header, salt, hasher.derive(header + password))
        else:
            raise ValueError()
    
    def verify_hashed_password(password, header_salt_hash, backend=BACKEND):
        header, salt, correct_output = load_data(header_salt_hash)
        algorithm, sub_algorithm, iterations, salt_size, output_size = load_data(header)
        if algorithm == "pbkdf2hmac":            
            hasher = PBKDF2HMAC(algorithm=getattr(hashes, sub_algorithm.upper())(),
                                length=output_size, salt=salt, iterations=iterations,
                                backend=backend)
            output = hasher.derive(header + password)             
        else:
            return -1
        return constant_time_comparison(output, correct_output)    
        
    def constant_time_comparison(data1, data2):
        return bytes_eq(data1, data2)   
    
            
def test_packed_encrypted_data():
    data = "This is some fantastic test data"
    key = random_bytes(32)
    mac_key = random_bytes(16)
    for algorithm in ("AES", "Camellia"):
        for mode in ("CBC", "CTR", "GCM"):
            if algorithm == "Camellia" and mode in ("GCM", "CTR"): 
                continue
            packed_encrypted_data = encrypt(data, key, algorithm=algorithm, mode=mode, 
                                            mac_key=mac_key)                        
            plaintext = decrypt(packed_encrypted_data, key, mac_key=mac_key)            
            assert plaintext == data
    
def test_hash_password():
    password = "password"
    iterations = 100000
    _hash = hash_password(password, iterations)
    assert verify_hashed_password(password, _hash)   
    invalid_password = "passwore"
    assert not verify_hashed_password(invalid_password, _hash)    
    print "Passed hash_password/verify_password unit test"
    
if __name__ == "__main__":
    test_packed_encrypted_data()
    test_hash_password()
    