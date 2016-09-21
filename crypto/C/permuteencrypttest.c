#define WORDSIZE32 unsigned long
#define ROUNDS 2

#define rotate_left(x, amount)(x << amount | (x >> (32 - amount)))
    
#define choice(a, b, c)(c ^ (a & (b ^ c)))

#define horizontal_mixing(a, b, c, d, rotate_amount)\
({  a += b ^ c ^ d;\
    a = rotate_left(a, rotate_amount);\
})   

#define vertical_mixing(a, b, c, d, rotate_amount)\
({  a ^= choice(b, c, d);\
    a = rotate_left(a, rotate_amount);\
})
    
#define round_function(a, b, c, d)\
({  horizontal_mixing(a, b, c, d, 1 ); \
    vertical_mixing(a, b, c, d, 11); \
    \
    horizontal_mixing(b, a, c, d, 2 ); \
    vertical_mixing(b, a, c, d, 7); \
    \
    horizontal_mixing(c, a, b, d, 3 ); \
    vertical_mixing(c, a, b, d, 13); \
    \
    horizontal_mixing(d, a, b, c, 5 ); \
    vertical_mixing(d, a, b, c, 17);\
})                                                                                                        
                                 
#define add_key(a, b, c, d, k0, k1, k2, k3)\
    ({a ^= k1; b ^= k1; c ^= k2; d ^= k3;})                       
    
#define store(data, a, b, c, d)\
    ({data[0] = a; data[1] = b; data[2] = c; data[3] = d;})   
        
#define load_abcd(data)\
    ({a = data[0]; b = data[1]; c = data[2]; d=data[3];})
    
#define load_key(key, k0, k1, k2, k3)({k0 = key[0]; k1 = key[1]; k2 = key[2]; k3 = key[3];})
    
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
        round_function(a, b, c, d);
        add_key(a, b, c, d, k0, k1, k2, k3); // F(x) ^ x
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
        
    int round, key_number;
    for (key_number = 0; key_number < 3; key_number++)
    {        
        add_key(a, b, c, d, round_keys[(4 * key_number) + 0], round_keys[(4 * key_number) + 1], round_keys[(4 * key_number) + 2], round_keys[(4 * key_number) + 3]);                
        for (round = 0; round < ROUNDS; round++)
        {                    
            round_function(a, b, c, d);                 
        }
    }    
    add_key(a, b, c, d, round_keys[0], round_keys[1], round_keys[2], round_keys[3]);
    store(data, a, b, c, d);
}

int main()
{
    WORDSIZE32 data[4], key[4];
    encrypt(data, key);
}