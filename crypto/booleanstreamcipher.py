from utilities import rotate_left

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
    
def choice(b, c, d):
    return d ^ (b & (c ^ d))  
    
def nonlinear_mixing(t, y, t2, y2):
    t ^= rotate_left(choice(y, t2, y2), 1, bit_width=32) # has problems related to hamming weight
    y ^= rotate_left(choice(t2, y2, t), 3, bit_width=32)
    t2 ^= rotate_left(choice(y2, t, y), 5, bit_width=32)
    y2 ^= rotate_left(choice(t, y, t2), 7, bit_width=32)
    
    #t ^= mixRow(rotate_left(choice(y, t2, y2), 1, bit_width=32)) # fills out the fastest
    #y ^= mixRow(rotate_left(choice(t2, y2, t), 3, bit_width=32))
    #t2 ^= mixRow(rotate_left(choice(y2, t, y), 5, bit_width=32))
    #y2 ^= mixRow(rotate_left(choice(t, y, t2), 7, bit_width=32))
    
    #t ^= rotate_left(mixRow(choice(y, t2, y2)), 1, bit_width=32)
    #y ^= rotate_left(mixRow(choice(t2, y2, t)), 3, bit_width=32)
    #t2 ^= rotate_left(mixRow(choice(y2, t, y)), 5, bit_width=32)
    #y2 ^= rotate_left(mixRow(choice(t, y, t2)), 7, bit_width=32)       
    
    #t ^= rotate_left(choice(y, t2, y2), 1, bit_width=32)
    #t = mixRow(t)
    #y ^= rotate_left(choice(t2, y2, t), 3, bit_width=32)
    #y = mixRow(y)
    #t2 ^= rotate_left(choice(y2, t, y), 5, bit_width=32)
    #t2 = mixRow(t2)
    #y2 ^= rotate_left(choice(t, y, t2), 7, bit_width=32)
    #y2 = mixRow(y2)
    
    #t ^= mixRow(choice(y, t2, y2))
    #y ^= mixRow(choice(t2, y2, t))
    #t2 ^= mixRow(choice(y2, t, y))
    #y2 ^= mixRow(choice(t, y, t2))
    
    return t, y, t2, y2
    
def test_nonlinear_mixing():
    from utilities import print_state_4x4, integer_to_bytes
    def to_bytes(t, y, t2, y2):
        return integer_to_bytes(t, 4) + integer_to_bytes(y, 4) + integer_to_bytes(t2, 4) + integer_to_bytes(y2, 4)
    t, y, t2, y2 = (0, 0, 0, 1)
    output = nonlinear_mixing(t, y, t2, y2)
    from pride.datastructures import Average
    hamming_weight = Average(size=2 ** 16)
    for sample in range(2 ** 8):
        for chunk in range(2 ** 8):        
            hamming_weight.add(sum(format(word, 'b').zfill(32).count('1') for word in output))
            output = nonlinear_mixing(*output)
            
            #print sample, chunk, max(hamming_weight.values)
        message = "Hamming weight (min/avg/max): {}".format(hamming_weight.range)
        print message
        #print_state_4x4(to_bytes(*output), message)
        #if raw_input("Enter any character+enter to end, enter to continue: "):
        #    break
        #else:
        #    output = nonlinear_mixing(*output)
        
    
if __name__ == "__main__":
    test_nonlinear_mixing()
    