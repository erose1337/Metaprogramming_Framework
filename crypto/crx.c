#include <stdio.h>
#include <string.h> // memset
#include "constructions.c"

#define WORDSIZE unsigned long long
#define ROUNDS 2

void crx_permutation(WORDSIZE* state)
{
    WORDSIZE a=state[0], b=state[1], c=state[2], d=state[3], t;    
    
    int round;    
    for (round = 0; round < ROUNDS; round++)
    {                                   
        t = d ^ (b & (c ^ d));
        a ^= ((t << 1) | (t >> (64 - 1)));
                                         
        t = a ^ (c & (d ^ a));           
        b ^= ((t << 2) | (t >> (64 - 2)));
                                         
        t = b ^ (d & (a ^ b));           
        c ^= ((t << 4) | (t >> (64 - 4)));
                                         
        t = c ^ (a & (b ^ c));           
        d ^= ((t << 8) | (t >> (64 - 8)));
                    
                    
        t = d ^ (b & (c ^ d));
        a ^= ((t << 16) | (t >> (64 - 16)));
                                          
        t = a ^ (c & (d ^ a));            
        b ^= ((t << 32) | (t >> (64 - 32)));
                                           
        t = b ^ (d & (a ^ b));             
        c ^= ((t << 48) | (t >> (64 - 48)));
                                           
        t = c ^ (a & (b ^ c));             
        d ^= ((t << 56) | (t >> (64 - 56)));
    }
    state[0] = a; state[1] = b; state[2] = c; state[3] = d;       
}
  
void print_state(WORDSIZE* state)
{
    int index;
    for (index = 0; index < 4; index++)
    {
        printf("%I64u ", state[index]);
    }
    printf("\n");
}

       
void test_crx_permutation()
{
    WORDSIZE state[4], key[4 * (ROUNDS + 1)];
    int index;
    for (index = 0; index < 4; index++)
    {
        state[index] = 0;    
    }
    state[0] = 1;
    for (index = 0; index < 4 * (ROUNDS + 1); index++)
    {
        key[index] = 0;
    }
    key[0] = 2;    
    crx_permutation(state);
    print_state(state);
    
    key_alternating_cipher(&crx_permutation, key, state, 2, 4);
    print_state(state);
}

int main()
{
    test_crx_permutation();    
    return 0;
}
    
    
    
    