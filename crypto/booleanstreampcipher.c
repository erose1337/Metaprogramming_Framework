from utilities import xor_subroutine, rotate_left, bytes_to_words, integer_to_bytes

#DEFINE WORDSIZE unsigned long long
#DEFINE ROUNDS 1

WORDSIZE choice(WORDSIZE a, WORDSIZE b, WORDSIZE c):
    return c ^ (a & (b ^ c))
        
WORDSIZE nonlinear_mixing(WORDSIZE b, WORDSIZE c, WORDSIZE d): 
    return rotate_left(choice(b, c, d), 1, bit_width=64)        
    
void _stream_cipher(WORDSIZE* nonce, WORDSIZE* key, WORDSIZE* output, WORDSIZE* constants)
{ 
    k1, k2, k3, k4 = bytes_to_long_longs(key)
    s1, s2, s3, s4 = bytes_to_long_longs(nonce)
    
    for (block = 0; block < block_count; block++)
    {
        for (round = 0; round < ROUNDS; round++)
        {
            s1 ^= k1 ^ constants[round ^ 3];
            s2 ^= k2 ^ constants[round ^ 5];
            s3 ^= k3 ^ constants[round ^ 7];
            s4 ^= k4 ^ constants[round ^ 13];
            
            s1 ^= nonlinear_mixing(s2, s3, s4);
            s2 ^= nonlinear_mixing(s3, s4, s1);
            s3 ^= nonlinear_mixing(s4, s1, s2);
            s4 ^= nonlinear_mixing(s1, s2, s3);
            
            k1 ^= constants[round ^ 17];
            k2 ^= constants[round ^ 19];
            k3 ^= constants[round ^ 23];
            k4 ^= constants[round ^ 29];
            
            k1 ^= nonlinear_mixing(k2, k3, k4);
            k2 ^= nonlinear_mixing(k3, k4, k1);
            k3 ^= nonlinear_mixing(k4, k1, k2);
            k4 ^= nonlinear_mixing(k1, k2, k3);
        }   
        s1 ^= k1;
        s2 ^= k2;
        s3 ^= k3;
        s4 ^= k4;
        memcpy_s(output + 0, &s1, sizeof(s1));
        memcpy_s(output + 1, &s2, sizeof(s2));
        memcpy_s(output + 2, &s3, sizeof(s3));
        memcpy_s(output + 3, &s4, sizeof(s4));                     
    }
    
def crypt_stream(plaintext, key, nonce, rounds=16):        
    data = bytearray(plaintext)
    data_size = len(data)
    output = bytearray()  
    
    _stream_cipher(bytearray(nonce), bytearray(key), output, data_size, rounds)    
    xor_subroutine(data, output)    
    return bytes(data)
       
def test_crypt_stream():
    message = bytearray(32)    
    key = bytearray(32)
    nonce = bytearray(32)    
    nonce[-1] = 1
    message[1] = 2
    _message = message[:]
    
    crypt_stream(message, key, nonce)
        
    #print "Ciphertext: {}\n{}".format(len(message), [byte for byte in message])
    
    crypt_stream(message, key, nonce)
    assert message == _message, (message, _message)
    
def test_crypt_stream_metrics():
    from metrics import test_stream_cipher
    test_stream_cipher(crypt_stream, bytearray(32), bytearray(32))
        
if __name__ == "__main__":
    test_crypt_stream()
    test_crypt_stream_metrics()        
    