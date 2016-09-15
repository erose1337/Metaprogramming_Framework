from permutation3 import permutation_subroutine, invert_permutation_subroutine
from utilities import xor_subroutine

def cipher(data, public_key, permutation=permutation_subroutine, rounds=2):  
    """ Cipher construction with 2 inputs and 2 outputs.
        Inputs: 
            - Plaintext
            - Key, potentially publicly known            
        Outputs:
            - Ciphertext
            - Decryption key
            
        Encipher data in such a way that the key used to encrypt is not the same key used to decrypt.
        Generates a private decryption key for each processed message. """            
    private_key = public_key[:]
    for round in range(rounds):
        xor_subroutine(data, private_key)
        permutation(data)
        
        xor_subroutine(private_key, data)
        permutation(private_key)
    xor_subroutine(data, private_key)    
    return private_key
    
def decipher(data, private_key, invert_permutation=invert_permutation_subroutine, rounds=2):
    """ Decryption component of the constructions with 2 Inputs and 2 Outputs.
        Inputs:
            - Ciphertext
            - Private decryption key
        Outputs:
            - Plaintext
            - Public encryption key
        
        Decipher ciphertext using private_key. 
        Produces the associated public key alongside the plaintext, which can be used for verification. """            
    public_key = private_key[:]
    xor_subroutine(data, public_key)
    for round in range(rounds):
        invert_permutation(public_key)
        xor_subroutine(public_key, data)
        
        invert_permutation(data)
        xor_subroutine(data, public_key)
    return public_key # is now == public_key again (if all went well)
    
def encrypt(data, public_key):
    return cipher(data, public_key)    
    
def decrypt(ciphertext, private_key, public_key):
    _public_key = decipher(ciphertext, private_key)
    if _public_key == public_key:
        return ciphertext # is now == plaintext
    else:
        return -1
        
def test_encrypt_decrypt():
    data = bytearray(16)    
    public_key = bytearray(16)
    data[0] = 1
    plaintext = data[:]
    
    private_key = encrypt(data, public_key)
    ciphertext = data[:]
    print [byte for byte in ciphertext]
    print [byte for byte in private_key]
    _plaintext = decrypt(ciphertext, private_key, public_key)
    assert plaintext == _plaintext, (plaintext, _plaintext)
    
        
    private_key = encrypt(data, public_key)
    ciphertext = data[:]
    print [byte for byte in private_key]
    invalid_plaintext = decrypt(ciphertext, public_key, public_key) # cannot decrypt with the public key
    assert invalid_plaintext == -1, invalid_plaintext
    print [byte for byte in ciphertext]
    
if __name__ == "__main__":
    test_encrypt_decrypt()
    