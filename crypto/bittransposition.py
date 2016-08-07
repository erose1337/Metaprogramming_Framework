from utilities import rotate_right

def bit_transposition(state, state_offset):
    output = bytearray(8)    
    for index in range(8):
        output[index] = 0
        for index2 in range(8): 
            byte = state[state_offset + index2]
            output[index] |= ((byte & 1) << index2) & 255
            state[state_offset + index2] = rotate_right(byte, 1)           
    state[state_offset:state_offset+8] = output[:]  
    
def bit_transposition_hackers_delight(A, m=1, n=1, B=list(bytearray(8))):   
   # Load the array and pack it into x and y. 

   x = (A[0]<<24)   | (A[m]<<16)   | (A[2*m]<<8) | A[3*m]; 
   y = (A[4*m]<<24) | (A[5*m]<<16) | (A[6*m]<<8) | A[7*m]; 
   #x = (A[3*m]<<24)   | (A[2*m]<<16)   | (A[1*m]<<8) | A[0]; 
   #y = (A[7*m]<<24) | (A[6*m]<<16) | (A[5*m]<<8) | A[4*m];   
   
   t = (y ^ (y >> 7)) & 0x00AA00AA;  y = y ^ t ^ (t << 7); 

   t = (x ^ (x >>14)) & 0x0000CCCC;  x = x ^ t ^ (t <<14); 
   t = (y ^ (y >>14)) & 0x0000CCCC;  y = y ^ t ^ (t <<14); 

   t = (x & 0xF0F0F0F0) | ((y >> 4) & 0x0F0F0F0F); 
   y = ((x << 4) & 0xF0F0F0F0) | (y & 0x0F0F0F0F); 
   x = t; 

   B[0]=x>>24;    B[n]=x>>16   & 255;    B[2*n]=(x>>8) & 255;  B[3*n]=x & 255; 
   B[4*n]=y>>24;  B[5*n]=y>>16 & 255;    B[6*n]=(y>>8) & 255;  B[7*n]=y & 255; 
      
   A[:] = B[:] 