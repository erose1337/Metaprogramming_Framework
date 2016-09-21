sponge
==============



Hash_Object
--------------

	No documentation available


Method resolution order: 

	(<class 'sponge.Hash_Object'>, <type 'object'>)

- **hash**(self, hash_input, key):

				No documentation available


- **digest**(self):

				No documentation available


- **copy**(self):

				No documentation available


- **update**(self, hash_input):

				No documentation available


absorb
--------------

**absorb**(data, state, rate, mixing_subroutine, replacement_subroutine):

				No documentation available


cast
--------------

**cast**(input_data, _type):

				No documentation available


decrypt
--------------

**decrypt**(data, key, iv, mixing_subroutine, rate, **kwargs):

				No documentation available


decryption_mode
--------------

**decryption_mode**(state, rate, output_size, mode_of_operation, absorb_mode):

				No documentation available


encrypt
--------------

**encrypt**(data, key, iv, mixing_subroutine, rate, **kwargs):

				No documentation available


encryption_mode
--------------

**encryption_mode**(state, rate, output_size, mixing_subroutine, absorb_mode):

				No documentation available


example_mixing_subroutine
--------------

**example_mixing_subroutine**(_bytes):

				No documentation available


pad_input
--------------

**pad_input**(hash_input, size):

				No documentation available


prng_mode
--------------

**prng_mode**(state, rate, output_size, mixing_subroutine, absorb_mode):

				No documentation available


psuedorandom_data
--------------

**psuedorandom_data**(quantity, seed, key, mixing_subroutine, rate):

				No documentation available


replacement_subroutine
--------------

**replacement_subroutine**(bytearray1, bytearray2):

				No documentation available


slide
--------------

**slide**(iterable, x):

		 Yields x bytes at a time from iterable 


sponge_factory
--------------

**sponge_factory**(mixing_subroutine, key, output_size, capacity, rate, mode_of_operation, absorb_mode):

		 usage: sponge_factory(mixing_subroutine, key='', output_size=32,
                              capacity=32, rate=32, 
                              mode_of_operation=variable_length_hash,
                              absorb_mode=xor_subroutine) => sponge function
                              
        Returns a sponge function that uses the supplied mixing subroutine as
        the permutation that mixes the internal state.
        
        mixing_subroutine should accept one required argument, an bytearray of 
        capacity + rate length, and should return nothing.
        
        key is an optional argument that will be absorbed into the state before
        any data is absorbed
        
        output_size, capacity, and rate should be integers. 
        
        mode_of_operation should be one of: variable_length_hash, prng_mode,
        encryption_mode, or decryption_mode. 
        
            - Note: it is simplest to use the encrypt/decrypt/psuedorandom_data 
                    helper functions for when something other then a hash is desired
                    
        absorb_mode should be either xor_subroutine or replacement_subroutine 


sponge_function
--------------

**sponge_function**(hash_input, key, output_size, capacity, rate, mixing_subroutine, mode_of_operation, absorb_mode):

				No documentation available


symmetric_primitive_factory
--------------

**symmetric_primitive_factory**(mixing_subroutine, **kwargs):

				No documentation available


test_encrypt_decrypt
--------------

**test_encrypt_decrypt**():

				No documentation available


test_example_mixer_stats
--------------

**test_example_mixer_stats**():

				No documentation available


test_hash
--------------

**test_hash**():

				No documentation available


test_hash_object
--------------

**test_hash_object**():

				No documentation available


test_psuedorandom_data
--------------

**test_psuedorandom_data**():

				No documentation available


variable_length_hash
--------------

**variable_length_hash**(state, rate, output_size, mixing_subroutine, absorb_mode):

				No documentation available


xor_subroutine
--------------

**xor_subroutine**(bytearray1, bytearray2):

				No documentation available
