from utilities import bytes_to_integer, integer_to_bytes

# 0 1 2 3  4 5  6  7   8  9 10 11 12 13 14 15 
# 8 6 5 15 1 13 10 9   14 12 2 4  7  0  14 3

def decorrelation_layer(state1, state2, transposition_table):    
    state = bytearray(16)
    for index, byte in enumerate(integer_to_bytes(state1, 8) + integer_to_bytes(state2, 8)):
        state[transposition_table[index]] = byte
    
    state1, state2 = bytes_to_integer(state[:8]), bytes_to_integer(state[8:])
    # top half   
    # the strange ordering applies shuffle_bytes before the bit permutation         
    
    
    x = (((state2 >> 24) & 255) << 24) | (((state1 >> 40) & 255) << 16) | (((state1 >> 32) & 255) << 8) | ((state2 >> 56) & 255)
    y = (((state2 >> 32) & 255) << 24) | (((state1 >> 48) & 255) << 16) | (((state2 >> 8) & 255) << 8) | (state2 & 255)    
    
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
    
    return ((y << 32) | t), ((y2 << 32) | t2)
    
def test_for_fixed_points():
    state = bytearray(16)
    for index in range(16):    
        for shift in range(8):
            state[index] = 1 << shift            
            state1, state2 = bytes_to_integer(state[:8]), bytes_to_integer(state[8:])
            assert format(state1, 'b').zfill(64).count('1') in (1, 0), format(state1, 'b').zfill(64)
            assert format(state2, 'b').zfill(64).count('1') in (1, 0), format(state2, 'b').zfill(64)
            
            state1, state2 = decorrelation_layer(state1, state2)
            assert format(state1, 'b').zfill(64).count('1') in (1, 0), format(state1, 'b').zfill(64)
            assert format(state2, 'b').zfill(64).count('1') in (1, 0), format(state2, 'b').zfill(64)
            
            _state = integer_to_bytes(state1, 8) + integer_to_bytes(state2, 8)
            if _state[index] == 1 << shift:
                print "Fixed point in decorrelation layer at: {} {}".format(index, shift)
            
            state[index] = 0
            
    
# 865F1CA9 EB2470D3
# 07E15B82 3AD6FC49
# 2EF5C19A B468073D
# 0734C1AF DE6B2895
#          
# 7CE9215F B6D048A3
# 4A168F7C 30ED59B2
# 2FC156AD E8340B97
# F4589721 A30E6CDB
    
if __name__ == "__main__":
    test_for_fixed_points()
    