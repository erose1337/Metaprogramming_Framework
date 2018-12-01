rng
==============



Stream_Cipher
--------------

	No documentation available


Method resolution order: 

	(<class 'rng.Stream_Cipher'>, <type 'object'>)

- **encrypt**(self, data, seed, tag):

				No documentation available


- **test_metrics**(cls, *args, **kwargs):

				No documentation available


- **decrypt**(self, data, seed, tag):

				No documentation available


- **random_bytes**(self, quantity, seed, tweak):

				No documentation available


Stream_Cipher2
--------------

	No documentation available


Method resolution order: 

	(<class 'rng.Stream_Cipher2'>, <class 'rng.Stream_Cipher'>, <type 'object'>)

- **encrypt**(self, data, seed, tag, tweak):

				No documentation available


- **crypt**(self, data, key, tweak, start, direction):

				No documentation available


- **decrypt**(self, data, seed, tag, tweak):

				No documentation available


- **substitute_bytes**(self, data, tweak, start, direction):

				No documentation available


null_pad
--------------

**null_pad**(seed, size):

				No documentation available


random_bytes
--------------

**random_bytes**(count, seed, key, tweak, output_size):

		 Generates count random bytes using random_number_generator using the 
        supplied/default seed, key, tweak, and output_size. 


random_number_generator
--------------

**random_number_generator**(key, seed, output_size, tweak):

		 Psuedorandom number generator. Operates by randomly shuffling the
        set of 256 elements according to an internal state array.
        
        One round consists of a permutation of the set array along with a
        randomizing of the internal state array. 
        
        Each output byte is obtained by selecting a byte from the state in
        a random location determined by the set.
        
        Output size is configurable to allow for a tunable security capacity,
        similar to a cryptographic sponge function. 
        
        Internally, two states are used: The main state array, and an 8-bit
        byte. The 8-bit byte contributes to diffusion and avalanche


random_number_generator_subroutine
--------------

**random_number_generator_subroutine**(key, seed, tweak, output, output_size):

		 Identical to random_number_generator; This uses less allocations and is more performant. 


shuffle_extract
--------------

**shuffle_extract**(data, key, state):

		 State update and round key extraction function. 


sponge
--------------

**sponge**(input_data, output_bytes, rate):

				No documentation available


test_random_number_generator
--------------

**test_random_number_generator**():

				No documentation available


test_shuffle_extract
--------------

**test_shuffle_extract**():

				No documentation available


test_stream_cipher2
--------------

**test_stream_cipher2**():

				No documentation available


xor_subroutine
--------------

**xor_subroutine**(bytearray1, bytearray2):

				No documentation available


xor_sum
--------------

**xor_sum**(data):

				No documentation available
