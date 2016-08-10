from utilities import bytes_to_integer, integer_to_bytes, rotate_left

#def decorrelation_layer(state, offset):
#    # top half   
#    
#    x = (state[11 + offset]<<24) | (state[5 + offset]<<16) | (state[4 + offset]<<8) | state[15 + offset]
#    y = (state[12 + offset]<<24) | (state[6 + offset]<<16) | (state[9 + offset]<<8) | state[0  + offset]       
#    
#    t = (y ^ (y >> 7)) & 0x00AA00AA;  y = y ^ t ^ (t << 7); 
#    
#    t = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t ^ (t <<14); 
#    t = (y ^ (y >>14)) & 0x0000CCCC;  y = y ^ t ^ (t <<14); 
#    
#    t = (x & 0xF0F0F0F0) | ((y >> 4) & 0x0F0F0F0F); 
#    y = ((x << 4) & 0xF0F0F0F0) | (y & 0x0F0F0F0F); 
#            
#     # bottom half
#    x =  (state[13 + offset]<<24) | (state[3  + offset]<<16) | (state[14 + offset]<<8) | state[8 + offset] 
#    y2 = (state[1  + offset]<<24) | (state[10 + offset]<<16) | (state[2  + offset]<<8) | state[7 + offset]       
#    
#    t2 = (y2 ^ (y2 >> 7)) & 0x00AA00AA;  y2 = y2 ^ t2 ^ (t2 << 7); 
#    
#    t2 = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t2 ^ (t2 <<14); 
#    t2 = (y2 ^ (y2 >>14)) & 0x0000CCCC;  y2 = y2 ^ t2 ^ (t2 <<14); 
#    
#    t2 = (x & 0xF0F0F0F0) | ((y2 >> 4) & 0x0F0F0F0F); 
#    y2 = ((x << 4) & 0xF0F0F0F0) | (y2 & 0x0F0F0F0F); 
#            
#    state[0 + offset]=t>>24;  state[1 + offset]=t>>16 & 255; state[2 + offset]=(t>>8) & 255; state[3 + offset]=t & 255; 
#    state[4 + offset]=y>>24;  state[5 + offset]=y>>16 & 255; state[6 + offset]=(y>>8) & 255; state[7 + offset]=y & 255; 
#
#    state[8  + offset]=t2>>24;  state[9  + offset]=t2>>16 & 255; state[10 + offset]=(t2>>8) & 255; state[11 + offset]=t2 & 255; 
#    state[12 + offset]=y2>>24;  state[13 + offset]=y2>>16 & 255; state[14 + offset]=(y2>>8) & 255; state[15 + offset]=y2 & 255; 
    
def choice(b, c, d):
    return d ^ (b & (c ^ d))
    
def decorrelation_layer(state, state2):
    # top half   
    # the strange ordering applies shuffle_bytes h
#    x = (state2[3]<<24) | (state[5]<<16) | (state[4] <<8) | state2[7]
#    y = (state2[4]<<24) | (state[6]<<16) | (state2[1]<<8) | state[0]       
 
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
    #state[0]=t>>24;  state[1]=t>>16 & 255; state[2]=(t>>8) & 255; state[3]=t & 255; 
    #state[4]=y>>24;  state[5]=y>>16 & 255; state[6]=(y>>8) & 255; state[7]=y & 255; 

    state2 = y2 | t2
    #state2[0]=t2>>24;  state2[1]=t2>>16 & 255; state2[2]=(t2>>8) & 255; state2[3]=t2 & 255; 
    #state2[4]=y2>>24;  state2[5]=y2>>16 & 255; state2[6]=(y2>>8) & 255; state2[7]=y2 & 255; 
    
    return state, state2
    
def prp(top, bottom, key, index, mask=0xFFFFFFFFFFFFFFFF, rotations=21):
# Addition tends to flip more of the low order bits then the high order bits
#     - This will tend to break xor differentials in the affected bits
#     - 
#     
# Rotate moves bits to a new location
#     - Does not break xor or additive differentials by itself
#     - 
# 
#     
# Xor flips all bits evenly
#     - Further xor will not break xor differentials
#     - Rotate and xor will not break xor differentials
#     
# Boolean functions
#     - requires multiple inputs (3 for choice and majority functions)
#     
    key ^= top     
    top = rotate_left((top + key + index) & mask, rotations, bit_width=64)    
    key ^= top
    
    key ^= bottom
    bottom = (bottom + (top >> 32)) & mask
    #bottom = choice(bottom, index, key)
    #bottom ^= rotate_left(top, (index ^ rotations), bit_width=64)
    bottom ^= rotate_left(top, index, bit_width=64) #^ rotate_left(key, index, bit_width=64)
    key ^= bottom
            
    return top, bottom, key
    
def test_prp():
    a, b, c, d = 1, 0, 0, 0
    key = a ^ b ^ c ^ d
    
    
    counter = 1
    while True:
        a, b, = decorrelation_layer(a, b)
        a, b, key = prp(a, b, key, counter)
      
        b, c = decorrelation_layer(b, c)
        b, c, key = prp(b, c, key, counter + 1)
        
        c, d = decorrelation_layer(c, d)
        c, d, key = prp(c, d, key, counter + 2)
        
        d, a = decorrelation_layer(d, a)
        d, a, key = prp(d, a, key, counter + 3)
        print format(a, 'b').zfill(64).count('1') + format(b, 'b').zfill(64).count('1') + format(c, 'b').zfill(64).count('1') + format(d, 'b').zfill(64).count('1')
        print "\n{}".format(''.join(bytes(integer_to_bytes(word, 8)) for word in (a, b, c, d)))
        if raw_input(''):
            break
    
    
def cube_prf(state, rounds=1):    
    a, b, c, d = (bytes_to_integer(state[offset:offset + 8]) for offset in range(0, 32, 8))    
    data_xor = a ^ b ^ c ^ d 
   # a, d = decorrelation_layer(a, d)
    
    for round in range(rounds):
        
        #print a, b, data_xor
        a, b = decorrelation_layer(a, b)                
        a, b, data_xor = prp(a, b, data_xor, round)
            
        b, c = decorrelation_layer(b, c)
        b, c, data_xor = prp(b, c, data_xor, round + 1)
        
    
        c, d = decorrelation_layer(c, d)
        c, d, data_xor = prp(c, d, data_xor, round + 2)
        
    
        d, a = decorrelation_layer(d, a)
        d, a, data_xor = prp(d, a, data_xor, round + 3)
    
    state[:] = bytearray(''.join(bytes(integer_to_bytes(quadword, 8)) for quadword in (a, b, c, d)))
    
def test_cube_prf():
    state = range(32)
        
    while not raw_input(''):
        cube_prf(state)
        print bytearray(state)
        
if __name__ == "__main__":
    test_cube_prf()
    #test_prp()
    