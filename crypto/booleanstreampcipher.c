#include <stdlib.h>
#include <stdio.h>

#define WORDSIZE unsigned long long
#define ROUNDS 1

#ifndef memcpy_s
void memcpy_s(WORDSIZE* s1, WORDSIZE* s2, size_t n)
{
    unsigned int index;
    for (index = 0; index < n; index++)
    {
        s1[index] = s2[index];
    }
}
#endif

WORDSIZE rotate_left(WORDSIZE word64, int amount)
{    
    return ((word64 << amount) | (word64 >> (64 - amount)));
}

void xor_subroutine(WORDSIZE* data1, WORDSIZE* data2, WORDSIZE size)
{
    WORDSIZE index = 0;
    for (index = 0; index < size; index++)
    {
        data1[index] ^= data2[index];
    }
}

WORDSIZE choice(WORDSIZE a, WORDSIZE b, WORDSIZE c)
{
    return c ^ (a & (b ^ c));
}
       
WORDSIZE nonlinear_mixing(WORDSIZE b, WORDSIZE c, WORDSIZE d, int rotation_amount)
{
    return rotate_left(choice(b, c, d), rotation_amount);      
}
   
void _stream_cipher(WORDSIZE* nonce, WORDSIZE* key, WORDSIZE* keystream, WORDSIZE* constants, WORDSIZE block_count)
{ 
    WORDSIZE block = 0;
    int round = 0;
    
    WORDSIZE k1 = key[0];
    WORDSIZE k2 = key[1];
    WORDSIZE k3 = key[2];
    WORDSIZE k4 = key[3];
    
    WORDSIZE s1 = nonce[0];
    WORDSIZE s2 = nonce[1];
    WORDSIZE s3 = nonce[2];
    WORDSIZE s4 = nonce[3];       
    
    for (block = 0; block < block_count; block++)
    {
        for (round = 0; round < ROUNDS; round++)
        {
            s1 ^= k1 ^ constants[round ^ 3];
            s2 ^= k2 ^ constants[round ^ 5];
            s3 ^= k3 ^ constants[round ^ 7];
            s4 ^= k4 ^ constants[round ^ 13];
            
            s1 ^= nonlinear_mixing(s2, s3, s4, 3);
            s2 ^= nonlinear_mixing(s3, s4, s1, 5);
            s3 ^= nonlinear_mixing(s4, s1, s2, 7);
            s4 ^= nonlinear_mixing(s1, s2, s3, 13);
            
            k1 ^= constants[round ^ 17];
            k2 ^= constants[round ^ 19];
            k3 ^= constants[round ^ 23];
            k4 ^= constants[round ^ 29];
            
            k1 ^= nonlinear_mixing(k2, k3, k4, 17);
            k2 ^= nonlinear_mixing(k3, k4, k1, 19);
            k3 ^= nonlinear_mixing(k4, k1, k2, 23);
            k4 ^= nonlinear_mixing(k1, k2, k3, 29);
        }   
        s1 ^= k1;
        s2 ^= k2;
        s3 ^= k3;
        s4 ^= k4;
        printf("pre memcpy\n");
        memcpy_s(keystream + 0, &s1, sizeof(s1));
        memcpy_s(keystream + 1, &s2, sizeof(s2));
        memcpy_s(keystream + 2, &s3, sizeof(s3));
        memcpy_s(keystream + 3, &s4, sizeof(s4));     
        printf("Post memcpy\n");
    }
}
    
void crypt_stream(WORDSIZE* plaintext, WORDSIZE* key, WORDSIZE* nonce, WORDSIZE* constants, WORDSIZE blocks)
{
    printf("Allocating memory\n");
    WORDSIZE* keystream = (WORDSIZE*)malloc(blocks * 32 * sizeof(WORDSIZE)); 
    if (keystream == NULL)
    {
        printf("Failed to allocate memory\n");
    }
    printf("Entering stream cipher\n");
    _stream_cipher(nonce, key, keystream, constants, blocks);  
    printf("combining with keystream\n");
    xor_subroutine(plaintext, keystream, blocks);
    printf("after xor\n");
    free(keystream);
    printf("Freed keystream\n");
}    
       
void test_crypt_stream()
{
    WORDSIZE message[4], key[4], nonce[4], _message[4], constants[256];
    int index = 0;
    for (index = 0; index < 4; index++)
    {
        message[index] = 0;
        _message[index] = 0;
        key[index] = 0;
        nonce[index] = 0;
    }
    for (index = 0; index < 256; index++)
    {
        constants[index] = index;
    }
    //nonce[-1] = 1
    //message[1] = 2
    printf("Encrypting\n");    
    crypt_stream(message, key, nonce, constants, 1);
    printf("Decrypting\n");

    for (index = 0; index < 4; index++)
    {
        printf("%I64u\n", message[index]);        
    }    
    printf("\n");
    
    crypt_stream(message, key, nonce, constants, 1);
    printf("....Done\n");
    for (index = 0; index < 4; index++)
    {
        if (message[index] != _message[index])
        {
            printf("Failed\n");
        }
        else
        {
            printf("%I64u", message[index]);
        }
    }    
    printf("\n");
}

int main()
{
    test_crypt_stream();
    return 0;
}
    