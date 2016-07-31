from utilities import bytes_to_integer, integer_to_bytes, replacement_subroutine

def mick_sponge_64(state, mask=0xFFFFFFFFFFFFFFFF):    
    spunj = bytes_to_integer(state)
    PS = [3, 5, 11, 17, 23, 41, 47, 53, 59, 61]
    PD = [1078, 300, 90, 480, 3334, 86, 670, 2268, 122, 2068]    
    m = 0xFFFFFFFFFFFFFFFF    
    for i in range(10):
        m -= PD[i]
        spunj = (spunj * m) % mask
        spunj = (spunj << PS[i]) | (spunj >> (64 - PS[i]))
        spunj = (spunj + m) % mask    
    replacement_subroutine(state, integer_to_bytes(spunj, 8))

def test_mick_sponge_64():
    from sponge import sponge_factory
    from metrics import test_hash_function
    hash_function = sponge_factory(mick_sponge_64, rate=1, capacity=7)
    test_hash_function(hash_function)
    
if __name__ == "__main__":
    test_mick_sponge_64()
    