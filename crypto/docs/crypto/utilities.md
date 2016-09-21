pride.crypto.utilities
==============



binary_form
--------------

**binary_form**(_string):

		 Returns the a string representation of the binary bits that constitute _string. 


brute_force
--------------

**brute_force**(output, function, test_bytes, prefix, postfix, joiner, string_slice):

		 usage: brute_force(output, function, test_bytes, 
                           prefix='', postfix='', 
                           joiner='') => input where function(input) == output
                           
        Attempt to find an input for function that produces output.
            - test_bytes should be an iterable of iterables which containing the symbols that 
              are to be tested 
                - i.e. [ASCII, ASCII], ['0123456789', 'abcdef']
                - symbols can be strings of any size
                    - [my_password_dictionary, my_password_dictionary], 
                        - my_password_dictionary can be an iterable of common words
            - prefix and postfix are any constant strings to prepend/append to each attempted input
            - joiner is the symbol to use when joining symbols for a test input
                - use '' (default) for test_bytes like [ASCII, ASCII]
                - use ' ' to test word lists [dictionary, dictionary]
                    - or have the word lists themselves include relevant spacing/punctuation
        Raises ValueError if no input was found that produces output.


byte_form
--------------

**byte_form**(bitstring):

		 Returns the ascii equivalent string of a string of bits. 


bytes_to_integer
--------------

**bytes_to_integer**(data):

				No documentation available


bytes_to_long_longs
--------------

**bytes_to_long_longs**(data):

				No documentation available


bytes_to_longs
--------------

**bytes_to_longs**(data):

				No documentation available


bytes_to_words
--------------

**bytes_to_words**(seed, wordsize):

				No documentation available


cast
--------------

**cast**(input_data, _type):

				No documentation available


find_cycle_length
--------------

**find_cycle_length**(function, *args, **kwargs):

				No documentation available


find_cycle_length_subroutine
--------------

**find_cycle_length_subroutine**(function, data, output_size, *args, **kwargs):

				No documentation available


find_long_cycle_length
--------------

**find_long_cycle_length**(max_size, chunk_size, function, _input, *args, **kwargs):

				No documentation available


find_long_cycle_length_subroutine
--------------

**find_long_cycle_length_subroutine**(max_size, chunk_size, function, _input, *args, **kwargs):

				No documentation available


generate_key
--------------

**generate_key**(size, wordsize):

				No documentation available


generate_s_box
--------------

**generate_s_box**(function):

				No documentation available


hamming_weight
--------------

**hamming_weight**(byte):

				No documentation available


high_order_byte
--------------

**high_order_byte**(byte, wordsize):

				No documentation available


integer_form
--------------

**integer_form**(_string):

				No documentation available


integer_to_bytes
--------------

**integer_to_bytes**(integer, _bytes):

				No documentation available


long_longs_to_bytes
--------------

**long_longs_to_bytes**(longs):

				No documentation available


longs_to_bytes
--------------

**longs_to_bytes**(longs):

				No documentation available


low_order_byte
--------------

**low_order_byte**(byte, wordsize):

				No documentation available


modular_addition
--------------

**modular_addition**(x, y, modulus):

				No documentation available


modular_subtraction
--------------

**modular_subtraction**(x, y, modulus):

				No documentation available


null_pad
--------------

**null_pad**(seed, size):

				No documentation available


pad_input
--------------

**pad_input**(hash_input, size):

				No documentation available


print_state_4x4
--------------

**print_state_4x4**(state, message):

				No documentation available


random_oracle_hash_function
--------------

**random_oracle_hash_function**(input_data, memo):

				No documentation available


replacement_subroutine
--------------

**replacement_subroutine**(bytearray1, bytearray2):

				No documentation available


rotate
--------------

**rotate**(input_string, amount):

				No documentation available


rotate_left
--------------

**rotate_left**(x, r, bit_width, _mask):

				No documentation available


rotate_right
--------------

**rotate_right**(x, r, bit_width, _mask):

				No documentation available


shift_left
--------------

**shift_left**(byte, amount, bit_width):

				No documentation available


shift_right
--------------

**shift_right**(byte, amount, bit_width):

				No documentation available


slide
--------------

**slide**(iterable, x):

		 Yields x bytes at a time from iterable 


words_to_bytes
--------------

**words_to_bytes**(state, wordsize):

				No documentation available


xor_parity
--------------

**xor_parity**(data):

				No documentation available


xor_subroutine
--------------

**xor_subroutine**(bytearray1, bytearray2):

				No documentation available


xor_sum
--------------

**xor_sum**(data):

				No documentation available
