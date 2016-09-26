#define rotate_left(x, amount)((x << amount | (x >> (32 - amount))))
    
#define choice(a, b, c)((c ^ (a & (b ^ c))))

#define iterate(permutation, a, b, c, d, iterations)\
({  unsigned int iteration;\
    for (iteration = 0; iteration < iterations; iteration++){\
        permutation(a, b, c, d);}\
})    
    
#define store(data, a, b, c, d)\
    ({data[0] = a; data[1] = b; data[2] = c; data[3] = d;})   
        
#define load(data, a, b, c, d)\
    ({a = data[0]; b = data[1]; c = data[2]; d=data[3];}) 
    