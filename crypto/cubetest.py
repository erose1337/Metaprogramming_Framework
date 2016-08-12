from utilities import bytes_to_integer, integer_to_bytes, rotate_left
    
def decorrelation_layer(state, state2):
    # top half   
    # the strange ordering applies shuffle_bytes before the bit permutation
 
    x = (((state2 >> 24) & 255) << 24) | (((state >> 40) & 255) << 16) | (((state >> 32) & 255) << 8) | ((state2 >> 56) & 255)
    y = (((state2 >> 32) & 255) << 24) | (((state >> 48) & 255) << 16) | (((state2 >> 8) & 255) << 8) | (state & 255)    
    
    t = (y ^ (y >> 7)) & 0x00AA00AA;  y = y ^ t ^ (t << 7);    
    t = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t ^ (t <<14); 
    t = (y ^ (y >>14)) & 0x0000CCCC;  y = y ^ t ^ (t <<14); 
    
    t = (x & 0xF0F0F0F0) | ((y >> 4) & 0x0F0F0F0F); 
    y = ((x << 4) & 0xF0F0F0F0) | (y & 0x0F0F0F0F); 
            
     # bottom half
    x =  (((state2 >> 40) & 255) << 24) | (((state >> 24) & 255) << 16) | (((state2 >> 48) & 255) << 8) | (state2 & 255)
    y2 = (((state >> 8) & 255) <<24)  | (((state2 >> 16) & 255) << 16) | (((state >> 16) & 255) << 8) | ((state >> 56) & 255)      
    
    t2 = (y2 ^ (y2 >> 7)) & 0x00AA00AA;  y2 = y2 ^ t2 ^ (t2 << 7); 
    
    t2 = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t2 ^ (t2 <<14); 
    t2 = (y2 ^ (y2 >>14)) & 0x0000CCCC;  y2 = y2 ^ t2 ^ (t2 <<14); 
    
    t2 = (x & 0xF0F0F0F0) | ((y2 >> 4) & 0x0F0F0F0F); 
    y2 = ((x << 4) & 0xF0F0F0F0) | (y2 & 0x0F0F0F0F); 
            
    state =  y | t        
    state2 = y2 | t2          
    return state, state2
    
def prp(top, bottom, key, index, mask=0xFFFFFFFFFFFFFFFF, rotations=21):
    key ^= top ^ bottom
    top = rotate_left((top + key + index) & mask, rotations, bit_width=64)    

    bottom = (bottom + (top >> 32)) & mask    
    bottom ^= rotate_left(top, index, bit_width=64) 
    key ^= top ^ bottom
            
    return top, bottom, key
            
def cube_prf(state, rounds=1):    
    a, b, c, d = (bytes_to_integer(state[offset:offset + 8]) for offset in range(0, 32, 8))    
    data_xor = a ^ b ^ c ^ d 
    data_xord = data_xorc = data_xorb = data_xora = data_xor
    a, c = decorrelation_layer(a, c)
    for round in range(rounds):         
        
        a, b = decorrelation_layer(a, b)                
        c, d = decorrelation_layer(c, d)
                
        b, c = decorrelation_layer(b, c)        
        d, a = decorrelation_layer(d, a)    
            
        a, b, data_xora = prp(a, b, data_xora, round)                                                   
        c, d, data_xorc = prp(c, d, data_xorc, round + 2)                       

        b, c, data_xorb = prp(b, c, data_xorb, round + 1)                
        d, a, data_xord = prp(d, a, data_xord, round + 3)                           

    state[:] = integer_to_bytes(a, 8) + integer_to_bytes(b, 8) + integer_to_bytes(c, 8) + integer_to_bytes(d, 8)    
    
def test_cube_prf():
    from sponge import sponge_factory
    cube_hash = sponge_factory(cube_prf, rate=32, capacity=0, output_size=32)
    
    from metrics import test_hash_function
    test_hash_function(cube_hash, avalanche_test=False, randomness_test=False)
        
if __name__ == "__main__":    
    test_cube_prf()
        