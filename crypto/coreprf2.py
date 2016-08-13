from utilities import rotate_left

def micksRow(a):
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

def round_function(state, state2):
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
    # end decorrelation layer
    
    # recursive diffusion layer + mix the rows
    t ^= rotate_left(y ^ y2 ^ t2, 7, bit_width=32)
    #t ^= y ^ y2 ^ t2
    t = micksRow(t)
        
    y ^= rotate_left(t ^ y2 ^ t2, 23, bit_width=32)
    y = micksRow(y)
        
    t2 ^= rotate_left(y ^ y2 ^ t, 37, bit_width=32)
    t2 = micksRow(t2)
        
    y2 ^= rotate_left(y ^ t ^ t2, 47, bit_width=32)
    y2 = micksRow(y2)
        
    state =  (y << 32) | t        
    state2 = (y2 << 32)| t2     
    
    return state, state2
    
def test_round_function():
    from utilities import print_state_4x4, integer_to_bytes
    state, state2 = 0, 1
    
    state, state2 = round_function(state, state2)
    print_state_4x4(integer_to_bytes(state, 8) + integer_to_bytes(state2, 8))    
    print "State :\n{}".format(state)
    print "State2:\n{}".format(state2)
    
if __name__ == "__main__":
    test_round_function()
    
    