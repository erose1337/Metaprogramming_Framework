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
    
def opcode_counter(function):
    return len(function.func_code.co_code)
    
def test_opcode_counter():
    mix_count = opcode_counter(mixRow)
    choice_count = opcode_counter(choice)
    rotate_count = opcode_counter(rotate_left)
    print "Mix operation count: {} (per word)".format(mix_count)
    print "Choice operation count: {} (per word)".format(choice_count)
    print "Rotate operation count: {} (per word)".format(rotate_count)
    print "Total Operations in nonlinear_mixing: {} (".format((mix_count + choice_count + rotate_count) * 4)
    
def round_function(state1, state2):    
    x = (((state2 >> 24) & 255) << 24) | (((state1 >> 40) & 255) << 16) | (((state1 >> 32) & 255) << 8) | ((state2 >> 56) & 255)
    y = (((state2 >> 32) & 255) << 24) | (((state1 >> 48) & 255) << 16) | (((state2 >> 8) & 255) << 8) | (state1 & 255)      
    
    t = (y ^ (y >> 7)) & 0x00AA00AA;  y = y ^ t ^ (t << 7);    
    t = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t ^ (t <<14); 
    t = (y ^ (y >>14)) & 0x0000CCCC;  y = y ^ t ^ (t <<14); 
    
    t = (x & 0xF0F0F0F0) | ((y >> 4) & 0x0F0F0F0F); 
    y = ((x << 4) & 0xF0F0F0F0) | (y & 0x0F0F0F0F); 
            
    # bottom half
    x =  (((state2 >> 40) & 255) << 24) | (((state1 >> 24) & 255) << 16) | (((state2 >> 48) & 255) << 8) | (state2 & 255)
    y2 = (((state1 >> 8) & 255) <<24)  | (((state2 >> 16) & 255) << 16) | (((state1 >> 16) & 255) << 8) | ((state1 >> 56) & 255)      
    
    t2 = (y2 ^ (y2 >> 7)) & 0x00AA00AA;  y2 = y2 ^ t2 ^ (t2 << 7); 
    
    t2 = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t2 ^ (t2 <<14); 
    t2 = (y2 ^ (y2 >>14)) & 0x0000CCCC;  y2 = y2 ^ t2 ^ (t2 <<14); 
    
    t2 = (x & 0xF0F0F0F0) | ((y2 >> 4) & 0x0F0F0F0F); 
    y2 = ((x << 4) & 0xF0F0F0F0) | (y2 & 0x0F0F0F0F);                    
    # end decorrelation layer
    
    # non linear layer + mix the rows       
    t ^= mixRow(rotate_left(choice(y, t2, y2), 1, bit_width=32))
    y ^= mixRow(rotate_left(choice(t2, y2, t), 3, bit_width=32))
    t2 ^= mixRow(rotate_left(choice(y2, t, y), 5, bit_width=32))
    y2 ^= mixRow(rotate_left(choice(t, y, t2), 7, bit_width=32))                    
    
    return t, y, y2, t2        
    
def test_sbox_stats():        
    sbox1, sbox2, sbox3, sbox4 = [bytearray() for count in range(4)]
    a, b, c, d = 0, 0, 0, 1
    for counter in range(256):
    #    for round in range(2):
    #        state1, state2 = ((a << 32) | b), ((c << 32) | d)
    #        a, b, c, d = round_function(state1, state2)
        #a, b, c, d = nonlinear_mixing(a, b, c, d)
        sbox1.append(integer_to_bytes(a, 4)[3])
        sbox2.append(integer_to_bytes(b, 4)[3])
        sbox3.append(integer_to_bytes(c, 4)[3])
        sbox4.append(integer_to_bytes(d, 4)[3])
    from cryptanalysis import summarize_sbox
    for sbox in (sbox1, sbox2, sbox3, sbox4):
        summarize_sbox(sbox)
        
        
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
    
def encrypt_stream(plaintext, key, nonce, rounds=2):        
    data = bytearray(plaintext)
    data_size = len(data)
    output = bytearray()  
    
    _stream_cipher(bytearray(nonce), bytearray(key), output, data_size, rounds)    
    xor_subroutine(data, output)    
    return bytes(data)
       
def test_encrypt_stream():
    message = bytearray(16)    
    key = bytearray(16)
    nonce = bytearray(16)    
    nonce[-1] = 1
    message[1] = 1
    _message = message[:]
    
    encrypt_stream(message, key, nonce)
        
    #print "Ciphertext: {}\n{}".format(len(message), [byte for byte in message])
    
    encrypt_stream(message, key, nonce)
    assert message == _message, (message, _message)
    
def test_encrypt_stream_metrics():
    from metrics import test_stream_cipher
    test_stream_cipher(encrypt_stream, bytearray(16), bytearray(16))
        
if __name__ == "__main__":
    #test_encrypt_stream()
    #test_encrypt_stream_metrics()
    #test_opcode_counter()
    test_sbox_stats()
    