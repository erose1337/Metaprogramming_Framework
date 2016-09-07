from utilities import slide

def rotl16(word, amount, _mask=0xFFFF):
    amount %= 16
    return ((word << amount) | (word >> (16 - amount))) & _mask 
    
def choice(a, b, c):
    return c ^ (a & (b ^ c))  
    
def shuffle_and_shift(a, b, c, d, word_0=0xFFFF000000000000, word_1=0x0000FFFF00000000, word_2=0x00000000FFFF0000, word_3=0x000000000000FFFF):   
    temp = a
    tempb = b
    tempc = c
    register0 = (rotl16((d & word_0)    >> 48, 0 ) << 48) | (rotl16((b & word_3)    << 0 , 1 ) << 32) | (rotl16((b & word_2)    >> 16, 2 ) << 16) | rotl16((c & word_0) >> 48, 3 )
    register1 = (rotl16((temp & word_3) >> 0 , 4 ) << 48) | (rotl16((c & word_2)    >> 16, 5 ) << 32) | (rotl16((b & word_1)    >> 32, 6 ) << 16) | rotl16((d & word_3) >> 0 , 7 )
    register2 = (rotl16((c & word_3)    >> 0 , 8 ) << 48) | (rotl16((d & word_1)    >> 32, 9 ) << 32) | (rotl16((temp & word_0) >> 48, 10) << 16) | rotl16((d & word_2) >> 16, 11)
    register3 = (rotl16((tempb & word_0)>> 48, 12) << 48) | (rotl16((temp & word_1) >> 32, 13) << 32) | (rotl16((tempc & word_1)>> 32, 14) << 16) | rotl16((temp & word_2) >> 16, 15)
    return register0, register1, register2, register3          
      
def shuffle_bytes_and_shift_rows(_state):

    temp = _state[0]

    _state[0]  = rotl16(_state[11], 0 )
    _state[11] = rotl16(_state[8] , 11)
    _state[8]  = rotl16(_state[13], 8 )
    _state[13] = rotl16(_state[10], 13)
    _state[10] = rotl16(_state[14], 10)
    _state[14] = rotl16(_state[2] , 14)
    _state[2]  = rotl16(_state[4] , 2 )
    _state[4]  = rotl16(_state[12], 4 )
    _state[12] = rotl16(_state[1] , 12)
    _state[1]  = rotl16(_state[5] , 1 )
    _state[5]  = rotl16(_state[6] , 5 )
    _state[6]  = rotl16(_state[9] , 6 )
    _state[9]  = rotl16(_state[3] , 9 )
    _state[3]  = rotl16(_state[15], 3 )
    _state[15] = rotl16(_state[7] , 15)
    _state[7]  = rotl16(temp      , 7 )

    
def mix_quarters(a, b, c, d):   
    a ^= choice(b, c, d)
    b ^= choice(c, d, a)
    c ^= choice(d, a, b)
    d ^= choice(a, b, c)   
    return a, b, c, d
    
def shuffle_mix(a, b, c, d):    
    a, b, c, d = shuffle_and_shift(a, b, c, d)
    a, b, c, d = mix_quarters(a, b, c, d)
    return a, b, c, d
       
def print_state_4x64(inputs_4x64):    
    for word in inputs_4x64:
        print '\n'.join(slide(format(word, 'b').zfill(64), 16))
            
def test_shuffle_and_shift():
    inputs = [1 | (1 << 16) | (1 << 32) | (1 << 48), 0, 0, 0]   
    inputs[0] = 1
    print("Testing shuffle and shift: ")
    print_state_4x64(inputs)
    while not raw_input("any key+enter to finish, enter to continue: "):
        inputs = shuffle_and_shift(*inputs)
        print("\n")
        print_state_4x64(inputs)  
        
def test_shuffle_mix():
    inputs = [1 | (1 << 16) | (1 << 32) | (1 << 48), 0, 0, 0]               
    print("Testing shuffle mix: ")
    print_state_4x64(inputs)
    while not raw_input("any key+enter to finish, enter to continue: "):
        inputs = shuffle_mix(*inputs)
        print("\n")
        print_state_4x64(inputs)  

if __name__ == "__main__":
    test_shuffle_mix()
    