import itertools
import random
from os import urandom

from pride.decorators import Timed
from pride.datastructures import Average
from pride.utilities import shell
from utilities import cast, binary_form
import pride.crypto

ASCII = ''.join(chr(x) for x in range(256))
TEST_OPTIONS = {"avalanche_test" : True, "randomness_test" : True, "bias_test" : True,
                "period_test" : True, "performance_test" : True, "randomize_key" : False}                 
         
def hamming_distance(str1, str2):
  return sum(itertools.imap(str.__ne__, cast(str1, "binary"), cast(str2, "binary")))
  
def print_hamming_info(output1, output2):    
    output1_binary = binary_form(output1)
    output2_binary = binary_form(output2)
    _distance = hamming_distance(binary_form(output1), binary_form(output2))
    bit_count = len(output1_binary)
    print "bit string length: ", bit_count
    print "Hamming weights: ", output1_binary.count('1'), output2_binary.count('1')
    print "Hamming distance and ratio (.5 is ideal): ", _distance, _distance / float(bit_count)
    
def test_avalanche(hash_function, blocksize=16):        
    print "Testing diffusion/avalanche... "
    beginning = "\x00" * (blocksize - 2)
    _bytes = ''.join(chr(byte) for byte in range(256))
    import pride.datastructures
    ratio = pride.datastructures.Average(size=65535)
    for byte in _bytes:  
        last_output = hash_function(beginning + byte + _bytes[0])
        for byte2 in _bytes[1:]:
            next_input = beginning + byte + byte2
            next_output = hash_function(next_input)
            distance = hamming_distance(last_output, next_output)
            ratio.add(distance)
            last_output = next_output
            
            #input1 = beginning + byte + byte2
            #output1 = hash_function(input1)                      
            
            #byte2 = chr((ord(byte2) + 1) % 256)
            #if byte2 == byte:
            #    continue
            #input2 = beginning + byte + byte2                        
            #output1 = hash_function(input1)
            #output2 = hash_function(input2)            
            #distance = hamming_distance(output1, output2)
            #ratio.add(distance)
    minimum, average, maximum = ratio.range
    bit_count = float(len(cast(last_output, "binary")))
    print "Minimum Hamming distance and ratio: ", minimum / bit_count
    print "Average Hamming distance and ratio: ", average / bit_count
    print "Maximum Hamming distance and ratio: ", maximum / bit_count    
    
def test_randomness(random_bytes):    
    size = len(random_bytes)
    print "Testing randomness of {} bytes... ".format(size)    
    with open("./random_data/Test_Data_{}.bin".format(size), 'wb') as _file:
        _file.write(random_bytes)
        _file.flush()    
    print "Data generated; Running ent..."
    shell("./ent/ent.exe ./random_data/Test_Data_{}.bin".format(size))
    
    #outputs = dict((x, random_bytes.count(chr(x))) for x in xrange(256))
    #average = Average(values=tuple(random_bytes.count(chr(x))for x in xrange(256)))
    #print "Randomness distribution (min, average, max): (~4100 is good): ", average.range
    #import pprint
    #pprint.pprint(sorted(outputs.items()))
        
def test_period(hash_function, blocksize=16, test_size=2):
    output = '\x00' * blocksize
    outputs = ['']    
    cycle_lengths = []
    print "Testing period with output truncated to {} byte: ".format(test_size)
    last_marker = 0
    for cycle_length in itertools.count():                
        output = hash_function(output)
        if output[:test_size] in outputs:            
            #print "cycled after {} with {} byte output: ".format(cycle_length - last_marker, test_size)
            cycle_lengths.append(cycle_length - last_marker)
            last_marker = cycle_length
            if len(cycle_lengths) == 100:
                break
        outputs.append(output[:test_size])
    average = Average(values=cycle_lengths)
    print "Minimum/Average/Maximum cycle lengths: ", average.range
    
def test_bias(hash_function, byte_range=slice(0, 16)):
    biases = [[] for x in xrange(byte_range.stop)]    
    outputs2 = []   
    print "Testing for byte bias..."
    for byte1 in range(256):
        for byte2 in range(256):
            output = hash_function(chr(byte1) + chr(byte2))
            for index, byte in enumerate(output[byte_range]):
                biases[index].append(ord(byte))            
            outputs2.extend(output[byte_range])        
    print "Byte bias: ", len(output), [len(set(_list)) for _list in biases]   
    print "Symbols out of 256 that appeared anywhere: ", len(set(outputs2))
       
def test_collisions(hash_function, output_size=3):      
    outputs = {}        
    print "Testing for collisions with output of {} bytes... ".format(output_size)
    for count, possibility in enumerate(itertools.product(ASCII, ASCII)):
        hash_input = ''.join(possibility)        
        hash_output = hash_function(hash_input)[:output_size]
        if hash_output in outputs:
            print "Collision after: ", count, "; Output size: ", output_size
            break
        else:
            outputs[hash_output] = hash_input
    else:
        print "No collisions after {} inputs with output size {}".format(count, output_size), len(set(outputs))
    
def test_compression_performance(hash_function):    
    print "Time testing compression function..."
    print Timed(hash_function, 10)("Timing test for input" * 1000)
    
def test_prng_performance(hash_function):    
    print "Testing time to generate 1024 * 1024 bytes... "
    print Timed(hash_function, 1)('', output_size=1024 * 1024)
    
def test_hash_function(hash_function, avalanche_test=True, randomness_test=True, bias_test=True,
                       period_test=True, performance_test=True, randomize_key=False, collision_test=True,
                       compression_test=True):
    if avalanche_test:
        test_avalanche(hash_function)
    if randomness_test:
        test_randomness(hash_function('', output_size=1024 * 1024))
    if period_test:
        test_period(hash_function)    
    if bias_test:
        test_bias(hash_function)
    if collision_test:
        test_collisions(hash_function)
    if compression_test:
        test_compression_performance(hash_function)
    if performance_test:
        test_prng_performance(hash_function)
    
def test_block_cipher(cipher, blocksize=16, avalanche_test=True, randomness_test=True, bias_test=True,
                      period_test=True, performance_test=True, randomize_key=False, keysize=None):
    _cipher = cipher("\x00" * (keysize if keysize is not None else blocksize), "cbc")
    key = "\x00" * keysize if not randomize_key else urandom(keysize or blocksize)
    
    if avalanche_test:
        test_function = lambda data: _cipher.encrypt(data, key)
        test_avalanche(test_function)
               
    if randomness_test:
        random_bytes = _cipher.encrypt("\x00" * 1024 * 1024 * 1, key)        
        test_randomness(random_bytes)
    
    if bias_test:
        test_function = lambda byte: _cipher.encrypt(("\x00" * 14) + byte, key)
        test_bias(test_function)
     
    if period_test:
        test_function = lambda data: _cipher.encrypt(data, key)
        test_period(test_function)
        
    if performance_test:
        test_function = lambda data, output_size: _cipher.encrypt("\x00" * output_size, key)
        test_prng_performance(test_function)
    
def test_random_metrics(test_options):
    from metrics import test_block_cipher
    from utilities import replacement_subroutine
        
    class Random_Cipher(pride.crypto.Cipher):
        
        def __init__(self, *args):
            super(Random_Cipher, self).__init__(*args)
            self.blocksize = 16
            
        def encrypt_block(self, plaintext, key):
            replacement_subroutine(plaintext, urandom(len(plaintext)))
            
    Random_Cipher.test_metrics(**test_options)

def test_aes_metrics(test_options):        
    from pride.security import encrypt as aes_encrypt
    from pride.security import random_bytes
    from utilities import replacement_subroutine
        
    class Aes_Cipher(pride.crypto.Cipher):
        
        key = random_bytes(16)
        
        def __init__(self, *args):
            super(Aes_Cipher, self).__init__(*args)
            self.blocksize = 16
            
        def encrypt_block(self, plaintext, key):
            ciphertext = aes_encrypt(bytes(plaintext), bytes(key), bytes(key), mode="ECB", return_mode="values")[1]  
            replacement_subroutine(plaintext, bytearray(ciphertext))
            
    test_block_cipher(Aes_Cipher, **test_options) 
    
def test_sha_metrics():
    from hashlib import sha256
    test_avalanche(lambda data: sha256(data).digest())
    
if __name__ == "__main__":
    options = dict((key, not value) for key, value in TEST_OPTIONS.items())
    options["period_test"] = True
    options["randomize_key"] = False
    #test_aes_metrics(options)
    #test_sha_metrics()
    test_random_metrics(TEST_OPTIONS)
    