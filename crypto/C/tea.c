#include <stdint.h>
#include <stdio.h>
#include <time.h>

void encrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0=v[0], v1=v[1], sum=0, i;           /* set up */
    uint32_t delta=0x9e3779b9;                     /* a key schedule constant */
    uint32_t k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */
    for (i=0; i < 32; i++) {                       /* basic cycle start */
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
    }                                              /* end cycle */
    v[0]=v0; v[1]=v1;
}

void time_test()
{
    uint32_t v[2];
    v[0] = 1;
    v[1] = 2;
    
    uint32_t k[4];
    k[0] = 0;
    k[1] = 1;
    k[2] = 2;
    k[3] = 3;
    
    unsigned long index, blocks = (1024 * 1024 * 1024) / 64;
    clock_t begin = clock();
    for (index = 0; index < blocks; index++)
    {
        encrypt(v, k);
    }
    clock_t end = clock();
    
    double time_taken = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Time taken: %.2fs\n", time_taken);
}

int main()
{
    time_test();
    return 0;
}