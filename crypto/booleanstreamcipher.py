from utilities import xor_subroutine, longs_to_bytes, bytes_to_longs
from ciphercomponents import choice_rotate_mixRow as nonlinear_mixing
                   
def _stream_cipher(nonce, key, output, data_size, rounds, wordsize=32):
    k1, k2, k3, k4 = bytes_to_longs(key)
    s1, s2, s3, s4 = bytes_to_longs(nonce)
    wordsize /= 8 # wordsize in bytes
    for block in range((data_size / wordsize / 4) + (data_size % wordsize)):
        for round in range(1, rounds + 1):                          
            s1, s2, s3, s4 = nonlinear_mixing(round ^ s1 ^ k1, 
                                              round ^ s2 ^ k2, 
                                              round ^ s3 ^ k3, 
                                              round ^ s4 ^ k4)                                                
            k1, k2, k3, k4 = nonlinear_mixing(k1, k2, k3, k4)                                              
        output.extend(longs_to_bytes(s1 ^ k1, s2 ^ k2, s3 ^ k3, s4 ^ k4))            
    
def crypt_stream(plaintext, key, nonce, rounds=2):        
    data = bytearray(plaintext)
    data_size = len(data)
    output = bytearray()  
    
    _stream_cipher(bytearray(nonce), bytearray(key), output, data_size, rounds)    
    xor_subroutine(data, output)    
    return bytes(data)
       
def test_crypt_stream():
    message = bytearray(16)    
    key = bytearray(16)
    nonce = bytearray(16)    
    nonce[-1] = 1
    message[1] = 2
    _message = message[:]
    
    crypt_stream(message, key, nonce)
        
    #print "Ciphertext: {}\n{}".format(len(message), [byte for byte in message])
    
    crypt_stream(message, key, nonce)
    assert message == _message, (message, _message)
    
def test_crypt_stream_metrics():
    from metrics import test_stream_cipher
    test_stream_cipher(crypt_stream, bytearray(16), bytearray(16))
        
if __name__ == "__main__":
    test_crypt_stream()
    test_crypt_stream_metrics()        
    