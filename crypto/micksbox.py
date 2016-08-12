import itertools

def mick_prp(x, magic1=3, magic2=5, magic3=11, mask=0xFF):
    a = (x * magic1) & mask 
    b = (x * magic2) & mask 
    c = (x * magic3) & mask 
    return (a & b) ^ (b & c) ^ (c & a)
    
primitive_roots_modulo_256 = [3,5,11,13,19,21,27,29,35,37,43,45,51,53,59,61,67,69,75,77,83,85,91,93,99,101,
                              107,109,115,117,123,125,131,133,139,141,147,149,155,157,163,165,171,173,179,181,187,189,
                              195,197,203,205,211,213,219,221,227,229,235,237,243,245,251,253]    
def test_mick_prp():
    from cryptanalysis import summarize_sbox
    for combination in itertools.combinations(primitive_roots_modulo_256, 3):
        sbox = [mick_prp(byte, *combination) for byte in range(256)]
        print '\n' + str(combination)
        summarize_sbox(sbox)
    
if __name__ == "__main__":
    test_mick_prp()
    