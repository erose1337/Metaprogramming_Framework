#include <stdio.h>
#include <stdlib.h>

#define MASK16 0xFFFF
#define WORDSIZE16 unsigned short
#define WORDSIZE64 unsigned long long

inline WORDSIZE16 rotl16(WORDSIZE16 word, unsigned char amount){return ((word << amount) | (word >> (16 - amount))) & MASK16;}
inline WORDSIZE64 choice(WORDSIZE64 a, WORDSIZE64 b, WORDSIZE64 c){return c ^ (a & (b ^ c));} 
           
void permutation(WORDSIZE64* _state)
{           
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

    unsigned short * state = (unsigned short*)_state;
    
    WORDSIZE16 temp = 0;
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
}            

void add_key(WORDSIZE64* state, WORDSIZE64* key)
{
    int index;
    for (index = 0; index < 4; index++)
    {
        state[index] ^= key[index];
    }
}
        
        
void encrypt_block_256(unsigned char* message, unsigned char* _key)
{    
    unsigned long long* state =(unsigned long long*)message;
    unsigned long long* key = (unsigned long long*)_key;

    permutation(key);
    add_key(state, key);
    
    int round;
    for (round = 0; round < 16; round++)
    {                    
        permutation(state);
        
        permutation(key);  
        add_key(state, key);                
    }
}



// end of cipher code. begin testing + visualization stuff  
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
    inputs[1]  = 0;
    inputs[2]  = 0;
    inputs[3]  = 0;
              
    inputs[4]  = 0;
    inputs[5]  = 0;
    inputs[6]  = 0;
    inputs[7]  = 0;
              
    inputs[8]  = 0;
    inputs[9]  = 0;
    inputs[10] = 0;
    inputs[11] = 0;
    
    inputs[12] = 0;
    inputs[13] = 0;
    inputs[14] = 0;
    inputs[15] = 0;
    
    printf("Testing round function diffusion:\n");
    print_state_16x16(inputs);
    printf("\n");
    int round;    
    for (round = 0; round < 16; round++)
    {        
        unsigned long long* _inputs = (unsigned long long*)inputs;
        permutation(_inputs);
        print_state_16x16(inputs);
        printf("\nEnd of Round: %i\n", round);
    }   
}        

//void test_encrypt_performance() {
//	int index, index2;
//	WORDSIZE16 key[DATA_SIZE], round_keys[(rounds + 1) * DATA_SIZE];
//
//	WORD_TYPE* data = (WORD_TYPE*)malloc(DATA_SIZE * blocks * WORD_SIZE);
//	WORD_TYPE* plaintext = (WORD_TYPE*)malloc(DATA_SIZE * blocks * WORD_SIZE);
//
//	
//	
//	Stopwatch s;
//    
//	for (index2 = 0; index2 < measurements; index2++) {
//		for (index = 0; index < blocks; index++) {
//			crypt_stream(data, key, nonce, constants, data_byte_count / 8 / 4);
//		}        
//	}
//    
//    double timee = s.Lap();
//    
//    long long mega_bytes_of_data = (measurements * blocks * DATA_SIZE * WORD_SIZE) / (1024.0 * 1024.0);
//    printf("%.2f MB/s\n", (mega_bytes_of_data / timee));
//    //double bps = 100.0 * (blocks * DATA_SIZE * WORD_SIZE) / timee;
//	//printf("%.2f MB/s\n", bps / 1024.0 / 1024.0);
//}

int main()
{
    test_shuffle_and_shift();
    return 0;
}
