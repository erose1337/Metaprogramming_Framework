from utilities import rotate_right, print_state_4x4, hamming_weight, modular_subtraction, xor_sum

def bit_transposition_involution(state, state_offset):
    output = bytearray(8)    
    for index in range(8):
        output[index] = 0
        for index2 in range(8): 
            byte = state[state_offset + index2]
            output[index] |= ((byte & 1) << index2) & 255
            state[state_offset + index2] = rotate_right(byte, 1)           
    state[state_offset:state_offset+8] = output[:]  
    
def bit_transposition_hackers_delight(A, state_offset):   
    # Load the array and pack it into x and y. 
    
    x = (A[0 + state_offset]<<24)   | (A[1 + state_offset]<<16)   | (A[2 + state_offset]<<8) | A[3 + state_offset]; 
    y = (A[4 + state_offset]<<24) | (A[5 + state_offset]<<16) | (A[6 + state_offset]<<8) | A[7 + state_offset];    
    
    t = (y ^ (y >> 7)) & 0x00AA00AA;  y = y ^ t ^ (t << 7); 
    
    t = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t ^ (t <<14); 
    t = (y ^ (y >>14)) & 0x0000CCCC;  y = y ^ t ^ (t <<14); 
    
    t = (x & 0xF0F0F0F0) | ((y >> 4) & 0x0F0F0F0F); 
    y = ((x << 4) & 0xF0F0F0F0) | (y & 0x0F0F0F0F); 
        
    A[0 + state_offset]=t>>24;  A[1 + state_offset]=t>>16 & 255; A[2 + state_offset]=(t>>8) & 255; A[3 + state_offset]=t & 255; 
    A[4 + state_offset]=y>>24;  A[5 + state_offset]=y>>16 & 255; A[6 + state_offset]=(y>>8) & 255; A[7 + state_offset]=y & 255; 

    

def shuffle_bytes(_state):

    temp = _state[0]

    _state[0] = _state[11]
    _state[11] = _state[8]
    _state[8] = _state[13]
    _state[13] = _state[10]
    _state[10] = _state[14]
    _state[14] = _state[2]
    _state[2] = _state[4]
    _state[4] = _state[12]
    _state[12] = _state[1]
    _state[1] = _state[5]
    _state[5] = _state[6]
    _state[6] = _state[9]
    _state[9] = _state[3]
    _state[3] = _state[15]
    _state[15] = _state[7]
    _state[7] = temp
    
def decorrelation_layer(state):
    shuffle_bytes(state)
    #bit_transposition_involution(state, 0)
    #bit_transposition_involution(state, 8)
    bit_transposition_hackers_delight(state, 0)
    bit_transposition_hackers_delight(state, 8)
    
def polarize_state(state):
    #bit_transposition_involution(state, 0)
    bit_transposition_hackers_delight(state, 0)
    
#def H(a, b, m=255): # NORX H function
#    return ((a ^ b) ^ ((a & b) << 1)) & m
    
def prp(state):
    decorrelation_layer(state)
    key = xor_sum(state)
    for index, byte in enumerate(state): 
        key ^= byte
        state[index] = (key + byte + index) & 255
        key ^= state[index]    
#    mixColumns_subroutine(state)
      
def test_prf_sponge():
    import sponge
    from metrics import test_hash_function
    hasher = sponge.sponge_factory(prp, rate=8, capacity=8, output_size=8)
    test_hash_function(hasher)
    
#def test_prp():
#    state = [0 for number in range(16)]
#    state[0] = 1
#   # polarize_state(state)
#    while not raw_input(''):
#        prp(state)
#        print state
        

    
    
#def visualize_bits():
#    state = range(16)
#    bits = range(128)
#    
#    def visualize_bit_transposition(state, _slice, offset):
#        for index in range(8):
#            for index2 in range(8):
#                temp[index]
#        state[_slice] = [[row[index2 + offset][index] for index2 in range(8)] for index in range(8)]
                
def _test_decorrelation_layer(state):    
    bit_transposition_involution(state, 0)
            
    states = [state[:]]
    while True:
        #print_state_4x4(state, "Before: ")
        shuffle_bytes(state)
        bit_transposition_involution(state, 0)
        bit_transposition_involution(state, 8)
            
        #print_state_4x4(state, "After: ")
        if state in states:                   
      #  if raw_input(''):
            break
        else:            
            states.append(state[:])
    return len(states)    
        #print_state_4x4(state)
        #if raw_input(''):
        #    break
          
def test_bit_transposition():
    data = range(16)
    _sum = sum(hamming_weight(byte) for byte in data)
    _data = data[:]
    #print_state_4x4(data, "Before: ")
    bit_transposition_involution(data, 0)
    #print_state_4x4(data, "After: ")
    rotated = data[:]
    bit_transposition_involution(data, 0)
    assert data == _data
    bit_transposition_involution(data, 8)
    #print_state_4x4(data, "Bottom transposed: ")
    bit_transposition_involution(data, 8)
    assert data == _data
    
    
    
    
    print_state_4x4(data, "Before: ")
    bit_transposition_hackers_delight(data, 0)
    _sum_after = sum(hamming_weight(byte) for byte in data)
    assert _sum == _sum_after, (_sum, _sum_after)
    print_state_4x4(data, "After: ")
    #assert data == rotated, (data, rotated)
    bit_transposition_hackers_delight(data, 0)
    print_state_4x4(data, "Reverted: ")
    _sum_after = sum(hamming_weight(byte) for byte in data)
    assert _sum == _sum_after, (_sum, _sum_after)    
    #assert data == _data
    
    data = _data[:]
    print_state_4x4(data, "Bottom before: ")
    bit_transposition_hackers_delight(data, 8)
    print_state_4x4(data, "Bottom after: ")
    _sum_after = sum(hamming_weight(byte) for byte in data)
    assert _sum == _sum_after, (_sum, _sum_after)  
    
    
def test_decorrelation_layer_period():    
    import os
    for number1 in range(256):
        for number2 in range(256):
            #state = [x for x in range(14)] + [number1, number2]
            state = bytearray(os.urandom(16))
            count = _test_decorrelation_layer(state)
            print count
            
if __name__ == "__main__":
    #test_decorrelation_layer_period()    
    test_bit_transposition()
    #test_prp()
    #test_prf_sponge()
    