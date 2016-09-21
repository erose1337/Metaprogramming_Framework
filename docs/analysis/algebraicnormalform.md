algebraicnormalform
==============


Translate sbox to ANF Boolean functions.
The size of the input sbox should be $2^n$.


InputError
--------------

	Raise this exception when the size of sbox is not $2^n$.


Method resolution order: 

	(<class 'algebraicnormalform.InputError'>,
	 <type 'exceptions.Exception'>,
	 <type 'exceptions.BaseException'>,
	 <type 'object'>)

components
--------------

**components**(x):

		
    A little tricky here.
    Find out which entries of the sbox should be considered.
    Return a list containing the indices of such entries.
    


count_terms
--------------

**count_terms**(sbox):

				No documentation available


print_anf
--------------

**print_anf**(sbox):

		Print out the ANF equations.


sbox2anf
--------------

**sbox2anf**(sbox):

		
    The core function of Sbox2ANF module.
    Calculate every coefficient of the ANF Boolean functions.
    Return a nested list containing the computed coefficients.
    
