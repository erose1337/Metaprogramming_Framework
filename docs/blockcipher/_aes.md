_aes
==============



AES
--------------

	AES funtions for a single block
    


Method resolution order: 

	(<class '_aes.AES'>, <type 'object'>)

- **core**(self, word, iteration):

		Key schedule core.


- **aes_invRound**(self, state, roundKey):

				No documentation available


- **aes_invMain**(self, state, expandedKey, nbrRounds):

				No documentation available


- **decrypt**(self, iput, key, size):

				No documentation available


- **mixColumn**(self, column, isInv):

				No documentation available


- **createRoundKey**(self, expandedKey, roundKeyPointer):

		Create a round key.
        Creates a round key from the given expanded key and the
        position within the expanded key.
        


- **galois_multiplication**(self, a, b):

		Galois multiplication of 8 bit characters a and b.


- **rotate**(self, word):

		 Rijndael's key schedule rotate operation.

        Rotate a word eight bits to the left: eg, rotate(1d2c3a4f) == 2c3a4f1d
        Word is an char list of size 4 (32 bits overall).
        


- **getSBoxInvert**(self, num):

		Retrieves a given Inverted S-Box Value


- **subBytes**(self, state, isInv):

				No documentation available


- **encrypt**(self, iput, key, size):

				No documentation available


- **shiftRows**(self, state, isInv):

				No documentation available


- **addRoundKey**(self, state, roundKey):

		Adds (XORs) the round key to the state.


- **getSBoxValue**(self, num):

		Retrieves a given S-Box Value


- **getRconValue**(self, num):

		Retrieves a given Rcon Value


- **aes_main**(self, state, expandedKey, nbrRounds):

				No documentation available


- **expandKey**(self, key, size, expandedKeySize):

		Rijndael's key expansion.

        Expands an 128,192,256 key into an 176,208,240 bytes key

        expandedKey is a char list of large enough size,
        key is the non-expanded key.
        


- **mixColumns**(self, state, isInv):

				No documentation available


- **shiftRow**(self, state, statePointer, nbr, isInv):

				No documentation available


- **aes_round**(self, state, roundKey):

				No documentation available


AESModeOfOperation
--------------

	Handles AES with plaintext consistingof multiple blocks.
    Choice of block encoding modes:  OFT, CFB, CBC
    


Method resolution order: 

	(<class '_aes.AESModeOfOperation'>, <type 'object'>)

- **convertString**(self, string, start, end, mode):

				No documentation available


- **encrypt**(self, stringIn, mode, key, size, IV):

				No documentation available


- **decrypt**(self, cipherIn, originalsize, mode, key, size, IV):

				No documentation available


append_PKCS7_padding
--------------

**append_PKCS7_padding**(s):

		return s padded to a multiple of 16-bytes by PKCS7 padding


decryptData
--------------

**decryptData**(key, data, mode):

		decrypt `data` using `key`

    `key` should be a string of bytes.

    `data` should have the initialization vector prepended as a string of
    ordinal values.
    


encryptData
--------------

**encryptData**(key, data, mode):

		encrypt `data` using `key`

    `key` should be a string of bytes.

    returned cipher is a string of bytes prepended with the initialization
    vector.

    


generateRandomKey
--------------

**generateRandomKey**(keysize):

		Generates a key from random data of length `keysize`.    
    The returned key is a string of bytes.    
    


strip_PKCS7_padding
--------------

**strip_PKCS7_padding**(s):

		return s stripped of PKCS7 padding


testStr
--------------

**testStr**(cleartext, keysize, modeName):

		Test with random key, choice of mode.
