metrics
==============



binary_form
--------------

**binary_form**(_bytes):

				No documentation available


hamming_distance
--------------

**hamming_distance**(str1, str2):

				No documentation available


print_hamming_info
--------------

**print_hamming_info**(output1, output2):

				No documentation available


slide
--------------

**slide**(iterable, x):

		 Yields x bytes at a time from iterable 


test_aes_metrics
--------------

**test_aes_metrics**(test_options):

				No documentation available


test_avalanche_hash
--------------

**test_avalanche_hash**(hash_function, blocksize):

				No documentation available


test_avalanche_of_key
--------------

**test_avalanche_of_key**(encrypt_method, iv, keysize):

				No documentation available


test_avalanche_of_seed
--------------

**test_avalanche_of_seed**(encrypt_method, key, seedsize, seedname):

				No documentation available


test_bias
--------------

**test_bias**(hash_function, byte_range):

				No documentation available


test_bias_of_data
--------------

**test_bias_of_data**(random_data):

				No documentation available


test_block_cipher
--------------

**test_block_cipher**(encrypt_method, key, iv, avalanche_test, randomness_test, bias_test, period_test, performance_test, randomize_key, blocksize, performance_test_sizes):

		 Test statistical metrics of the supplied cipher. cipher should be a 
        pride.crypto.Cipher object or an object that supports an encrypt method
        that accepts plaintext bytes and key bytes and returns ciphertext bytes


test_cipher_performance
--------------

**test_cipher_performance**(performance_test_sizes, encrypt_method, key, seed):

				No documentation available


test_collisions
--------------

**test_collisions**(hash_function, output_size):

				No documentation available


test_compression_performance
--------------

**test_compression_performance**(hash_function, test_message):

				No documentation available


test_fixed_zero_point
--------------

**test_fixed_zero_point**(hash_function):

				No documentation available


test_for_involution
--------------

**test_for_involution**(encrypt_function, blocksize, key, iv):

				No documentation available


test_hash_function
--------------

**test_hash_function**(hash_function, avalanche_test, randomness_test, bias_test, period_test, performance_test, randomize_key, collision_test, compression_test):

		 Test statistical metrics of the given hash function. hash_function 
        should be a function that accepts one string of bytes as input and returns
        one string of bytes as output. 


test_period
--------------

**test_period**(hash_function, blocksize, test_size):

				No documentation available


test_permutation
--------------

**test_permutation**(permutation, state_size, avalanche_test, randomness_test, bias_test, period_test, performance_test):

				No documentation available


test_prng_performance_hash
--------------

**test_prng_performance_hash**(hash_function):

				No documentation available


test_prng_performance_permutation
--------------

**test_prng_performance_permutation**(permutation, state_size):

				No documentation available


test_random_metrics
--------------

**test_random_metrics**():

				No documentation available


test_randomness
--------------

**test_randomness**(random_bytes):

				No documentation available


test_sha_metrics
--------------

**test_sha_metrics**():

				No documentation available


test_stream_cipher
--------------

**test_stream_cipher**(encrypt_method, key, seed, avalanche_test, randomness_test, bias_test, period_test, performance_test, randomize_key, rate, performance_test_sizes):

				No documentation available
