#define WORDSIZE32 unsigned long
#define ROUNDS 2

void permutation(WORDSIZE32* state)
{
    WORDSIZE32 a=state[0], b= state[1], c=state[2], d=state[3];
     
    int round;    
    for (round = 0; round < ROUNDS; round++)
    {
        //a = rotl32(a + (b ^ c ^ d), 1);
        //b = rotl32(b + (a ^ c ^ d), 3);
        //c = rotl32(c + (a ^ b ^ d), 5);
        //d = rotl32(d + (a ^ b ^ c), 7);
        //
        //a = rotl32(a ^ choice(b, c, d), 11);
        //b = rotl32(a ^ choice(c, d, a), 17);
        //c = rotl32(a ^ choice(d, a, b), 23);
        //d = rotl32(a ^ choice(a, b, c), 29); 
        
        a += b ^ c ^ d;
        a = (a << 1) | (a >> 31); // rotl32
    
        b += a ^ c ^ d;
        b = (b << 3) | (b >> (29));
        
        c += a ^ b ^ d;
        c = (c << 5) | (c >> (27));
        
        d += a ^ b ^ c;
        d = (d << 7) | (d >> (25));                    
                        
        
        
        a ^= d ^ (b & (c ^ d)); // choice(b, c, d)
        a = (a << 11) | (a >> (21));
            
        b ^= a ^ (c & (d ^ a)); 
        b = (b << 17) | (b >> (15));
            
        c ^= b ^ (d & (a ^ b)); 
        c = (c << 23) | (c >> (9));
            
        d ^= c ^ (a & (b ^ c)); 
        d = (d << 29) | (d >> (3));     
    }
    
    state[0] = a; state[1] = b; state[2] = c; state[3] = d;
}
    
int main()
{
    return 0;
}