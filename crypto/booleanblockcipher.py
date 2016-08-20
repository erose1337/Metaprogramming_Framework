from utilities import rotate_left, slide, integer_to_bytes, bytes_to_integer, xor_subroutine, longs_to_bytes, bytes_to_longs

def mixRow(a):
    b = a & 0x80808080;
    
    # b |= b >> 1; # without multiply instruction
    # b |= b >> 3;
    # b >>= 3;
        
    b = (b >> 7) * 0x1B; # with multiply instruction

    b ^= (a << 1) & 0xFEFEFEFE;
    c = a ^ b;
    b ^= (c >>  8) | ((c << 24) & 0xFFFFFFFF);
    b ^= ((a <<  8) & 0xFFFFFFFF) | (a >> 24);
    return b ^ (a >> 16) ^ ((a << 16) & 0xFFFFFFFF);
    
def choice(a, b, c):
    return c ^ (a & (b ^ c))  
    
def nonlinear_mixing(a, b, c, d, bit_width=32):    
    a ^= mixRow(rotate_left(choice(b, c, d), 1, bit_width=bit_width))
    b ^= mixRow(rotate_left(choice(c, d, a), 3, bit_width=bit_width))
    c ^= mixRow(rotate_left(choice(d, a, b), 5, bit_width=bit_width))
    d ^= mixRow(rotate_left(choice(a, b, c), 7, bit_width=bit_width)) 
    return a, b, c, d            
            
def encrypt(data, key, rounds=2):    
    k1, k2, k3, k4 = bytes_to_longs(key)
    s1, s2, s3, s4 = bytes_to_longs(data)
        
    for round in range(1, rounds + 1):              
        
        s1, s2, s3, s4 = nonlinear_mixing(round ^ s1 ^ k1, 
                                          round ^ s2 ^ k2, 
                                          round ^ s3 ^ k3, 
                                          round ^ s4 ^ k4)
    
        k1, k2, k3, k4 = nonlinear_mixing(k1, k2, k3, k4)            
        
    return longs_to_bytes(s1 ^ k1, s2 ^ k2, s3 ^ k3, s4 ^ k4)    
            
def invert_nonlinear_mixing(a, b, c, d, bit_width=32):
    d ^= mixRow(rotate_left(choice(a, b, c), 7, bit_width=bit_width)) 
    c ^= mixRow(rotate_left(choice(d, a, b), 5, bit_width=bit_width))
    b ^= mixRow(rotate_left(choice(c, d, a), 3, bit_width=bit_width))
    a ^= mixRow(rotate_left(choice(b, c, d), 1, bit_width=bit_width))
    return a, b, c, d   
    
def decrypt(data, key, rounds=2):
    k1, k2, k3, k4 = bytes_to_longs(key)
    s1, s2, s3, s4 = bytes_to_longs(data)
        
    keys = []
    for round in range(1, rounds + 1):
        keys.append((k1, k2, k3, k4))
        k1, k2, k3, k4 = nonlinear_mixing(k1, k2, k3, k4)
    
    s1 ^= k1
    s2 ^= k2
    s3 ^= k3
    s4 ^= k4
    
    for round in reversed(range(1, rounds + 1)):
        k1, k2, k3, k4 = keys.pop(-1)
        
        s1, s2, s3, s4 = invert_nonlinear_mixing(s1, s2, s3, s4)
        s1 ^= k1 ^ round
        s2 ^= k2 ^ round
        s3 ^= k3 ^ round
        s4 ^= k4 ^ round        
    return longs_to_bytes(s1, s2, s3, s4)
    
def test_encrypt_decrypt():
    data = bytearray(16)
    key = bytearray(16)
    #data[3], data[7], data[11], data[15] = 0, 1, 1, 1
    #key[3] = 1
    data[-1] = 1
    key[-1] = 1
    rounds = 2
    ciphertext = encrypt(data, key, rounds)
    print "Ciphertext: \n{}".format(ciphertext)
    
    plaintext = decrypt(ciphertext, key, rounds)
    assert plaintext == data, (plaintext, data)
    
    
if __name__ == "__main__":
    #test_encrypt_decrypt()
    #test_encrypt_stream()
    test_encrypt_stream_metrics()
    