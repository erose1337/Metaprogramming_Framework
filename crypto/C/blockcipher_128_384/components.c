#include "constants.c"
#include "functions.c"

#define nonlinear_mixing(a, b, c, d, rotate_amount1, rotate_amount2)({\
    a += b ^ c ^ d;\
    a = rotate_left(a, rotate_amount1);\
    a ^= choice(b, c, d);\
    a = rotate_left(a, rotate_amount2);})
    
#define permutation(a, b, c, d)({\
    nonlinear_mixing(a, b, c, d, 1, 11);\
    nonlinear_mixing(b, c, d, a, 2, 7);\
    nonlinear_mixing(c, d, a, b, 3, 15);\
    nonlinear_mixing(d, a, b, c, 5, 17);})                                                                                                
            
#define choice_swap(key, a, b)({\
    _t = a;\
    a = choice(key, a, b);\
    b = choice(key, b, _t);})
    
#define shuffle_words(a, b, c, d, key, key_number)({\
    choice_swap(key[(4 * key_number) + 0], a, b);\
    choice_swap(key[(4 * key_number) + 1], c, d);\
    choice_swap(key[(4 * key_number) + 2], a, c);\
    choice_swap(key[(4 * key_number) + 3], b, d);})   
            
#define add_key(a, b, c, d, keys, key_number)({\
    a ^= keys[(4 * key_number) + 0];\
    b ^= keys[(4 * key_number) + 1];\
    c ^= keys[(4 * key_number) + 2];\
    d ^= keys[(4 * key_number) + 3];})   
    