aes_procedures
==============



addRoundKey
--------------

**addRoundKey**(state, key):

				No documentation available


aes_encrypt
--------------

**aes_encrypt**(state, key):

				No documentation available


aes_round
--------------

**aes_round**(state, key):

				No documentation available


bytes_to_integer
--------------

**bytes_to_integer**(data):

				No documentation available


core
--------------

**core**(word, iteration):

		Key schedule core.


createRoundKey
--------------

**createRoundKey**(expandedKey, roundKeyPointer):

		Create a round key.
    Creates a round key from the given expanded key and the
    position within the expanded key.
    


expandKey
--------------

**expandKey**(key, size, expandedKeySize):

		Rijndael's key expansion.

    Expands an 128,192,256 key into an 176,208,240 bytes key

    expandedKey is a char list of large enough size,
    key is the non-expanded key.
    


getRconValue
--------------

**getRconValue**(num):

		Retrieves a given Rcon Value


integer_to_bytes
--------------

**integer_to_bytes**(integer, _bytes):

				No documentation available


mixColumns
--------------

**mixColumns**(state, mode):

				No documentation available


mixColumns_subroutine
--------------

**mixColumns_subroutine**(state, mode):

				No documentation available


rotate
--------------

**rotate**(word):

		 Rijndael's key schedule rotate operation.

    Rotate a word eight bits to the left: eg, rotate(1d2c3a4f) == 2c3a4f1d
    Word is an char list of size 4 (32 bits overall).
    


shiftRows
--------------

**shiftRows**(state, invert):

				No documentation available


subBytes
--------------

**subBytes**(state, s_box):

				No documentation available


test_mixColumn2
--------------

**test_mixColumn2**():

				No documentation available


test_mixColumns_subroutine
--------------

**test_mixColumns_subroutine**():

				No documentation available


test_mixcolumn
--------------

**test_mixcolumn**():

				No documentation available
