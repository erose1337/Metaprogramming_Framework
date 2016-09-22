#include "performancetesting.c" // for test_encrypt_performance_4x32

#define WORDSIZE32 unsigned long
#define ITERATIONS 2

#define rotate_left(x, amount)(x << amount | (x >> (32 - amount)))
    
#define choice(a, b, c)(c ^ (a & (b ^ c)))

#define nonlinear_mixing(a, b, c, d, rotate_amount1, rotate_amount2)\
({  a += b ^ c ^ d;\
    a = rotate_left(a, rotate_amount1);\
    a ^= choice(b, c, d);\
    a = rotate_left(a, rotate_amount2);\
})
    
#define permutation(a, b, c, d)\
({  nonlinear_mixing(a, b, c, d, 1, 11);\
    nonlinear_mixing(b, c, d, a, 2, 7);\
    nonlinear_mixing(c, d, a, b, 3, 15);\
    nonlinear_mixing(d, a, b, c, 5, 17);\
})                                                                                                   
        
#define iterate(permutation, a, b, c, d, iterations)\
({  unsigned int iteration;\
    for (iteration = 0; iteration < iterations; iteration++){\
        permutation(a, b, c, d);}\
})    
    
#define add_key(a, b, c, d, k0, k1, k2, k3)\
    ({a ^= k1; b ^= k1; c ^= k2; d ^= k3;})                       
    
#define store(data, a, b, c, d)\
    ({data[0] = a; data[1] = b; data[2] = c; data[3] = d;})   
        
#define load_abcd(data)\
    ({a = data[0]; b = data[1]; c = data[2]; d=data[3];})
    
#define load_key(key, k0, k1, k2, k3)\
    ({k0 = key[0]; k1 = key[1]; k2 = key[2]; k3 = key[3];})
    
#define load_round_key(round_key)\
    ({rk0 = round_key[0]; rk1 = round_key[1]; rk2 = round_key[2]; rk3 = round_key[3];})
        
void key_schedule(WORDSIZE32* key, WORDSIZE32* round_keys)
{    
    int key_number;           
    WORDSIZE32 a, b, c, d;
    WORDSIZE32 k0, k1, k2, k3; 
    load_key(key, k0, k1, k2, k3);  
    a = k0; b = k1; c = k2; d = k3;
    for (key_number = 0; key_number < 3; key_number++)
    {        
        permutation(a, b, c, d); 
        add_key(a, b, c, d, k0, k1, k2, k3);
        store(round_keys, a, b, c, d); 
        add_key(a, b, c, d, k0, k1, k2, k3); // remove key
        
        round_keys += 4;
    }
}
        
void encrypt(WORDSIZE32* data, WORDSIZE32* key)
{       
    WORDSIZE32 round_keys[12], a, b, c, d;
    load_abcd(data);
    key_schedule(key, round_keys);
        
    int key_number;
    for (key_number = 0; key_number < 3; key_number++)
    {        
        add_key(a, b, c, d, round_keys[(4 * key_number) + 0], round_keys[(4 * key_number) + 1], round_keys[(4 * key_number) + 2], round_keys[(4 * key_number) + 3]);   
        iterate(permutation, a, b, c, d, ITERATIONS);
    }
    add_key(a, b, c, d, round_keys[0], round_keys[1], round_keys[2], round_keys[3]);
    store(data, a, b, c, d);
}
 

int main()
{
    WORDSIZE32 data[4], key[4];
    encrypt(data, key);
    test_encrypt_performance_4x32(encrypt, 5000000);
}
