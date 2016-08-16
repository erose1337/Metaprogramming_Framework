from utilities import rotate_left, bytes_to_integer, integer_to_bytes

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

def polarize(state):
    x = (((state >> 24) & 255) << 24) | (((state >> 16) & 255) << 16) | (((state >> 8) & 255) << 8) | (state & 255)
    y = (((state >> 56) & 255) << 24) | (((state >> 48) & 255) << 16) | (((state >> 40) & 255) << 8) | ((state >> 32) & 255)    
    
    t = (y ^ (y >> 7)) & 0x00AA00AA;  y = y ^ t ^ (t << 7);    
    t = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t ^ (t <<14); 
    t = (y ^ (y >>14)) & 0x0000CCCC;  y = y ^ t ^ (t <<14); 
    
    t = (x & 0xF0F0F0F0) | ((y >> 4) & 0x0F0F0F0F); 
    y = ((x << 4) & 0xF0F0F0F0) | (y & 0x0F0F0F0F); 
    
    return (y << 32) | t
    
def choice(b, c, d):
    return d ^ (b & (c ^ d))    
    
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
    
    # non linear layer + mix the rows
    
    ## t y t2 y2
    #t ^= choice(y, t2, y2)
    #t = micksRow(t)
    #
    #y ^= choice(t2, y2, t)
    #y = micksRow(y)
    #
    #t2 ^= choice(y2, t, y)
    #t2 = micksRow(t2)
    #
    #y2 ^= choice(t, y, t2)
    #y2 = micksRow(y2)               
    
    
    t ^= micksRow(choice(y, t2, y2))
    y ^= micksRow(choice(t2, y2, t))
    t2 ^= micksRow(choice(y2, t, y))
    y2 ^= micksRow(choice(t, y, t2))
    
    #t ^= micksRow(y ^ t2 ^ y2)
    #y ^= micksRow(t2 ^ y2 ^ t)
    #t2 ^= micksRow(y2 ^ t ^ y)
    #y2 ^= micksRow(t ^ y ^ t2)
    
    state =  (y << 32) | t        
    state2 = (y2 << 32)| t2     
    
    return state, state2
    
def prf(state, state2):    
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
    
    # non linear layer + mix the rows
    ## t y t2 y2
    t ^= choice(y, t2, y2) 
  #  t = micksRow(t ^ y ^ t2 ^ y2)    
    y ^= choice(t2, y2, t)
  #  y = micksRow(t ^ y ^ t2 ^ y2)    
    t2 ^= choice(y2, t, y)
  #  t2 = micksRow(t ^ y ^ t2 ^ y2)   
    y2 ^= choice(t, y, t2) 
  #  y2 = micksRow(t ^  y ^ t2 ^ y2)
    
    t ^=  micksRow(t ^ y ^ y2 ^ t2)
    y ^=  micksRow(t ^ y ^ y2 ^ t2)
    t2 ^= micksRow(t ^ y ^ y2 ^ t2)
    y2 ^= micksRow(t ^ y ^ y2 ^ t2)
    
    state =  (y << 32) | t        
    state2 = (y2 << 32)| t2     
    
    return state, state2
    
def get_output_difference(function, input1, input2):    
    output1 = function(input1)
    output2 = function(input2)
    
    output1_bits = ''.join(format(byte, 'b').zfill(8) for byte in output1)
    output2_bits = ''.join(format(byte, 'b').zfill(8) for byte in output2)    
    return _get_difference(output1, output2)        
    
def binary_form(bytestring):
    return ''.join(format(byte, 'b').zfill(8) for byte in bytestring)
    
def _get_difference(output1, output2):  
    output1_bits = binary_form(output1)
    output2_bits = binary_form(output2)
    input_differences = b''
    
    for index, bit in enumerate(output1_bits):          
        if bit != output2_bits[index]:
            input_differences += '1'
        else:
            input_differences += '0'
    return input_differences        
    
def print_active_sbox_info():
    rounds = 1
    input1 = bytearray(16)
    input2 = bytearray(16)
    input1[-1] = 1
    
    def test_function(state):
        state1, state2 = bytes_to_integer(state[:8]), bytes_to_integer(state[8:16])
        state1, state2 = round_function(state1, state2)
        state[:] = integer_to_bytes(state1, 8) + integer_to_bytes(state2, 8)
        return state
        
    for round in range(rounds):
        input_difference = _get_difference(input1, input2)
        print "Input difference: {}/{}".format(input_difference.count('1'), len(input_difference))
        output_difference = get_output_difference(test_function, input1, input2)
        print "Active bits: {}/{}".format(output_difference.count('1'), len(output_difference))                   
            
def test_round_function():
    from utilities import print_state_4x4, integer_to_bytes
    state, state2 = 1, 0
    
    state = polarize(state)
    state, state2 = round_function(state, state2)
    print_state_4x4(integer_to_bytes(state, 8) + integer_to_bytes(state2, 8))    
    print "State :\n{}".format(state)
    print "State2:\n{}".format(state2)
        
if __name__ == "__main__":
    test_round_function()
    #print_active_sbox_info()
    