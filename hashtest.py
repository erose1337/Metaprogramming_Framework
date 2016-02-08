import itertools   
import binascii

# helper functions

def pack_data(*args): # copied from pride.utilities
    sizes = []
    for arg in args:
        sizes.append(str(len(arg)))
    return ' '.join(sizes + [args[0]]) + ''.join(str(arg) for arg in args[1:])
    
def unpack_data(packed_bytes, size_count):
    """ Unpack a stream according to its size header """
    sizes = packed_bytes.split(' ', size_count)
    packed_bytes = sizes.pop(-1)
    data = []
    for size in (int(size) for size in sizes):
        data.append(packed_bytes[:size])
        packed_bytes = packed_bytes[size:]
    return data
    
def binary_form(_string):
    """ Returns the a string representation of the binary bits that constitute _string. """
    try:
        return ''.join(format(ord(character), 'b').zfill(8) for character in _string)
    except TypeError:        
        bits = format(_string, 'b')
        bit_length = len(bits)
        if bit_length % 8:
            bits = bits.zfill(bit_length + (8 - (bit_length % 8)))                
        return bits
        
def byte_form(bitstring):
    """ Returns the ascii equivalent string of a string of bits. """
    try:
        _hex = hex(int(bitstring, 2))[2:]
    except TypeError:
        _hex = hex(bitstring)[2:]
        bitstring = binary_form(bitstring)
    try:
        output = binascii.unhexlify(_hex[:-1 if _hex[-1] == 'L' else None])
    except TypeError:
        output = binascii.unhexlify('0' + _hex[:-1 if _hex[-1] == 'L' else None])
        
    if len(output) == len(bitstring) / 8:
        return output
    else:
        return ''.join(chr(int(bits, 2)) for bits in slide(bitstring, 8))
        
_type_resolver = {"bytes" : byte_form, "binary" : binary_form, "int" : lambda bits: int(bits, 2)}
    
def cast(input_data, _type):
    return _type_resolver[_type](input_data)
    
def rotate(input_string, amount):
    """ Rotate input_string by amount. Amount may be positive or negative.
        Example:
            
            >>> data = "0001"
            >>> rotated = rotate(data, -1) # shift left one
            >>> print rotated
            >>> 0010
            >>> print rotate(rotated, 1) # shift right one, back to original
            >>> 0001 """
    if not amount or not input_string:            
        return input_string    
    else:
        amount = amount % len(input_string)
        return input_string[-amount:] + input_string[:-amount]
        
def slide(iterable, x=16):
    """ Yields x bytes at a time from iterable """
    slice_count, remainder = divmod(len(iterable), x)
    for position in range((slice_count + 1 if remainder else slice_count)):
        _position = position * x
        yield iterable[_position:_position + x]   
            
def prime_generator():
    """ Generates prime numbers in successive order. """
    primes = [2]
    yield 2
    for test_number in itertools.count(3, 2):
        for prime in primes:
            if not test_number % prime:
                break
        else:
            yield test_number
            primes.append(test_number)

generator = prime_generator()
PRIMES = [next(generator) for count in range(2048)]
del generator          
# end of helper functions
                                                
def unpack_factors(bits, initial_power=0, initial_output=1, power_increment=1):   
    """ Unpack encoded (prime, power) pairs and compose them into an integer.
        Each contiguous 1-bit increments the exponent of the current prime.
        Each zero advances to the next prime and composes the current prime and
        exponent into the output.
        
        For example:
            
            11001101
            
        Is interpreted to mean:
            
            (2 ** 2) * (3 ** 0) * (5 ** 2) * (7 ** 1)
            
        The bits that previously represented the number 205 are composed and 
        result in the integer 700. """    
    if '1' not in bits:
        return 0 
    variables = iter(PRIMES)#prime_generator()
    variable = next(variables)
    power = initial_power
    output = initial_output   
    last_bit = len(bits) - 1
    for bit in bits[:-1]:
        if bit == '1':
            power += power_increment
        else:                        
            output *= variable ** power
            power = initial_power        
            variable = next(variables)              
    if bits[-1] == '1':
        power += power_increment    
    output *= variable ** power       
    return output                       
                            
def mixing_subroutine(_bytes):    
    byte_length = len(_bytes)
    key = (45 + sum(_bytes)) * byte_length * 2    
    for counter, byte in enumerate(_bytes):
        psuedorandom_byte = pow(251, key ^ byte ^ (_bytes[(counter + 1) % byte_length] * counter), 257) % 256
        _bytes[counter % byte_length] = psuedorandom_byte ^ (counter % 256)        
    return _bytes
    
def confusion_shuffle(input_data):
    output = binary_form(bytes(input_data))             
    for index, byte in enumerate(bytearray(input_data)):
        output = rotate(output[:index * 8], (index + 1) * (1 + byte)) + output[index * 8:]  
    return byte_form(output)
    
def sponge_function(hash_input, key='', output_size=32, capacity=32, rate=32, 
                    mix_state_function=mixing_subroutine):  
    state_size = capacity + rate
    state = bytearray(state_size)
    if key:
        for index, value in enumerate(bytearray(key)):
            state[index % rate] ^= value
        mix_state_function(state)
    
    hash_input += '1'
    while len(hash_input) < rate: # expanding small inputs is good for diffusion/byte bias
        hash_input = byte_form(unpack_factors(binary_form(hash_input)))
        
    for _bytes in slide(hash_input, rate):
        for index, byte in enumerate(bytearray(_bytes)):
            state[index] ^= byte
        mix_state_function(state)
    
    mix_state_function(state)
    output = state[:rate]
    while len(output) < output_size:
        mix_state_function(state)
        output += state[:rate]
    return bytes(output[:output_size])
           
def sponge_encryptor(hash_input, key='', capacity=32, rate=32, 
                     mix_state_function=mixing_subroutine):  
    state_size = capacity + rate
    state = bytearray(state_size)
    if key:
        for index, value in enumerate(bytearray(key)):
            state[index % rate] ^= value
        mix_state_function(state)
    
    hash_input += '1'
    while len(hash_input) < rate: # expanding small inputs is good for diffusion/byte bias
        hash_input = byte_form(unpack_factors(binary_form(hash_input)))
        
    for _bytes in slide(hash_input, rate):
        for index, byte in enumerate(bytearray(_bytes)):
            state[index] ^= byte
        mix_state_function(state)
    
    mix_state_function(state)        
    input_block = yield None        
    while input_block is not None:
        for index, value in enumerate(bytearray(input_block)):
            state[index] ^= value     
        input_block = yield state[:len(input_block)]         
        mix_state_function(state)        
    yield state[:rate]
    
def sponge_decryptor(hash_input, key='', capacity=32, rate=32, 
                     mix_state_function=mixing_subroutine):      
    state_size = capacity + rate
    state = bytearray(state_size)
    if key:
        for index, value in enumerate(bytearray(key)):
            state[index % rate] ^= value
        mix_state_function(state)
    
    hash_input += '1'
    while len(hash_input) < rate: # expanding small inputs is good for diffusion/byte bias
        hash_input = byte_form(unpack_factors(binary_form(hash_input)))
        
    for _bytes in slide(hash_input, rate):
        for index, byte in enumerate(bytearray(_bytes)):
            state[index] ^= byte
        mix_state_function(state)
    
    mix_state_function(state)        
    input_block = yield None       
    while input_block is not None:
        last_block = state[:len(input_block)]
        for index, value in enumerate(bytearray(input_block)):
            state[index] ^= value     
        input_block = yield state[:len(input_block)]
        for index, value in enumerate(last_block):
            state[index] ^= value           
        mix_state_function(state)    

    yield state[:rate]
                        
def invert_mixing_function(_bytes):
    import itertools
    length = len(_bytes)
    recovered = bytearray()
    for counter, psuedorandom_byte in enumerate(_bytes):
        psuedorandom_byte ^= (counter % 256)
            
        reform_state = lambda byte: (45 + sum(recovered) + byte) * length * 2
        possible_inputs = []
        unknown_bytes = length - len(recovered)
        for byte in xrange(256):
            possible_state = reform_state(byte)
            for increment in xrange(unknown_bytes * 256):                
                if pow(251, (increment + possible_state) ^ byte, 257) % 256 == psuedorandom_byte:
                    possible_inputs.append(byte)
                    break                         
        
        if not possible_inputs:    
            print "Failed to find any possible inputs"
            raise Exception()
        elif len(possible_inputs) == 1:
            recovered.append(possible_inputs[0])
        else:
            print "ambiguous recovery: ", psuedorandom_byte, possible_inputs
    return recovered
    
def xor_compression(data, state_size=64):    
    output = bytearray('\x00' * state_size)
    for _bytes in slide(data, state_size):
        for index, byte in enumerate(bytearray(_bytes)):
            output[index] ^= byte
    return bytes(output)                              
             
class Hash_Object(object):
                        
    def __init__(self, hash_input='', output_size=32, capacity=32, rate=32, state=None):  
        self.rate = rate
        self.capacity = capacity
        self.output_size = output_size        
        self.state = ''
        if state is not None:
            self.state = state
        
        if hash_input:
            if self.state:
                self.update(hash_input)
            else:
                self.state = self.hash(hash_input)
        
    def hash(self, hash_input, key=''):
        return sponge_function(hash_input, key, self.output_size, self.capacity, self.rate)
       
    def update(self, hash_input):
        self.state = xor_compression(self.state + self.hash(hash_input), self.state_size)
        
    def digest(self):
        return self.state

    def copy(self):
        return Hash_Object(output_size=self.output_size, capacity=self.state_size, 
                           rate=self.rate, state=self.state)

# test functions        
            
def test_hash_object():
    hasher = Hash_Object("Test data")
    assert hasher.digest() == sponge_function("Test data")
    
def test_encrypt_decrypt():
    message = "I am an awesome test message, for sure :)"
    key = "Super secret key"
    ciphertext = encrypt(message, key, '0')
    assert decrypt(ciphertext, key) == message
        
def test_chain_cycle(state="\x00\x00", key=""):
    state = bytearray(key + state)
    size = len(state)
    outputs = [bytes(state)]
    import itertools
    import random
    max_length = 0
    for cycle_length in itertools.count():
        mixing_subroutine(state)   
        #  assert len(state) == 2, len(state)
        #state, key = state[:1], bytes(state[1:])                
        output = bytes(state)
        if not state[0]:
            state = bytearray(confusion_shuffle(state))
           #  print index, len(state), state[index], len(mixing_subroutine(bytearray(state[index])))
      #  print cycle_length
        if output in outputs:
            max_length = max(max_length, len(outputs))
            #break
            print "Cycle length: ", cycle_length, max_length, len(outputs)
            outputs = [output]
        else:
     #       print cycle_length, len(output)
            outputs.append(output)            
    #print "Cycle length: ", cycle_length, len(outputs)
    
def test_permutation():
    _input = "\x00"
    outputs = []
    max_cycle = 0
    best_initial_state = 0
    for initial_state in xrange(256):  
        outputs = []
        for y in xrange(256):
            _input = mixing_subroutine(_input)
            outputs.append(_input)  
                
        start = cycle = outputs.pop()
        for cycle_length, output in enumerate(reversed(outputs)):
            if output == start:                
                break
            cycle += output
        outputs.append(start)
        
        if cycle_length > max_cycle:
            best = (cycle_length, initial_state, len(set(outputs)))
            max_cycle = cycle_length
            _outputs = outputs
    print best# [char for char in reversed(cycle)]
    #print
    print [char for char in _outputs], "\n"
    print set(''.join(chr(x) for x in xrange(256))).difference(_outputs)
            
def test_mixing_function2():
    data = "\x00"
    outputs = [data]
    while True:
        data = mixing_function2(data)
        if data in outputs:
            break
        outputs.append(data)
    print len(outputs)
    
def encrypt(data, key, iv, extra_data='', block_size=32):
    sponge = sponge_encryptor(extra_data + iv, key, rate=block_size)
    next(sponge)
    ciphertext = ''
    for _bytes in slide(data, block_size):
        ciphertext += sponge.send(_bytes)
    mac_tag = sponge.send(None)
    return pack_data("EHC0_EHC0", ciphertext, iv, mac_tag, extra_data)
    
def decrypt(data, key, block_size=32):
    header, ciphertext, iv, mac_tag, extra_data = unpack_data(data, 5)
    sponge = sponge_decryptor(extra_data + iv, key, rate=block_size)
    next(sponge)
    plaintext = ''
    for _bytes in slide(ciphertext, block_size):
        plaintext += sponge.send(_bytes)
    _mac_tag = sponge.send(None)

    if _mac_tag != mac_tag:
        raise ValueError("Invalid mac tag")
    else:
        if extra_data:
            return plaintext, extra_data
        else:
            return plaintext
    
def test_duplex():
    sponge = sponge_encryptor("testing", "key")    
    next(sponge)
    message = "This is an excellent message!"
    output = ''
    for _bytes in slide(message, 32):
        output += sponge.send(_bytes)
    mac_tag = sponge.send(None)
    
    sponge = sponge_decryptor("testing", "key")
    next(sponge)
    _message = ''
    for _bytes in slide(output, 32):
        _message += sponge.send(_bytes)
    _mac_tag = sponge.send(None)
    assert _message == message
    assert mac_tag == _mac_tag    
    
    #print mac_tag
    #print
    #print output
    #print
    #print _message
    
if __name__ == "__main__":
    from hashtests import test_hash_function
    #test_duplex()
    test_encrypt_decrypt()
    #test_hash_function(sponge_function)
    #test_chain_cycle()