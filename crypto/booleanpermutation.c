#include <stdio.h>
#include <stdlib.h>

#define MASK16 0xFFFF
#define WORDSIZE16 unsigned short
#define WORDSIZE64 unsigned long long

WORDSIZE16 rotl16(word, amount){return ((word << amount) | (word >> (16 - amount))) & MASK16;}
WORDSIZE64 choice(a, b, c){return c ^ (a & (b ^ c));} 
           
void round_function(WORDSIZE16* state)
{   WORDSIZE16 temp = 0;
    temp = state[0];

    state[0]  = rotl16(state[11], 11);
    state[11] = rotl16(state[8] , 8 );
    state[8]  = rotl16(state[13], 13);
    state[13] = rotl16(state[10], 10);
    state[10] = rotl16(state[14], 14);
    state[14] = rotl16(state[2] , 2 );
    state[2]  = rotl16(state[4] , 4 );
    state[4]  = rotl16(state[12], 12);
    state[12] = rotl16(state[1] , 1 );
    state[1]  = rotl16(state[5] , 5 );
    state[5]  = rotl16(state[6] , 6 );
    state[6]  = rotl16(state[9] , 9 );
    state[9]  = rotl16(state[3] , 3 );
    state[3]  = rotl16(state[15], 15);
    state[15] = rotl16(state[7] , 7 );
    state[7]  = rotl16(temp     , 0 );
    
    unsigned long long* _state = (unsigned long long*)state;
    unsigned long long a, b, c, d;
    a = _state[0];
    b = _state[1];
    c = _state[2];
    d = _state[3];
        
    a ^= choice(b, c, d);
    b ^= choice(c, d, a);
    c ^= choice(d, a, b);
    d ^= choice(a, b, c);   
    
    _state[0] = a;
    _state[1] = b;
    _state[2] = c;
    _state[3] = d;
}    
  
#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c"
#define WORD_TO_BINARY(byte)  \
  (byte & 0x8000 ? '1' : '0'), \
  (byte & 0x4000 ? '1' : '0'), \
  (byte & 0x2000 ? '1' : '0'), \
  (byte & 0x1000 ? '1' : '0'), \
  (byte & 0x0800 ? '1' : '0'), \
  (byte & 0x0400 ? '1' : '0'), \
  (byte & 0x0200 ? '1' : '0'), \
  (byte & 0x0100 ? '1' : '0'), \
  (byte & 0x0080 ? '1' : '0'), \
  (byte & 0x0040 ? '1' : '0'), \
  (byte & 0x0020 ? '1' : '0'), \
  (byte & 0x0010 ? '1' : '0'), \
  (byte & 0x0008 ? '1' : '0'), \
  (byte & 0x0004 ? '1' : '0'), \
  (byte & 0x0002 ? '1' : '0'), \
  (byte & 0x0001 ? '1' : '0') 
  
void print_state_16x16(WORDSIZE16* state)
{       
    unsigned short* _shorts = (unsigned short*)state;
    int index;
    for (index = 0; index < 16; index++)
    {
        printf(BYTE_TO_BINARY_PATTERN "\n", WORD_TO_BINARY(_shorts[index]));
    }
}

void test_shuffle_and_shift()
{
    WORDSIZE16 inputs[16];    
    inputs[0]  = 1;
    inputs[1]  = 1;
    inputs[2]  = 1;
    inputs[3]  = 1;
              
    inputs[4]  = 1;
    inputs[5]  = 1;
    inputs[6]  = 1;
    inputs[7]  = 1;
              
    inputs[8]  = 1;
    inputs[9]  = 1;
    inputs[10] = 1;
    inputs[11] = 1;
    
    inputs[12] = 1;
    inputs[13] = 1;
    inputs[14] = 1;
    inputs[15] = 1;
    
    printf("Testing round function diffusion:\n");
    print_state_16x16(inputs);
    printf("\n");
    int round;    
    for (round = 0; round < 16; round++)
    {
        round_function(inputs);
        print_state_16x16(inputs);
        printf("\nEnd of Round: %i\n", round);
    }   
}        

int main()
{
    test_shuffle_and_shift();
}
