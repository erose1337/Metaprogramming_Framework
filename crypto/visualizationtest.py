from utilities import slide

def print_state_4x64_256(inputs):    
    for word in inputs:
        print '\n'.join(slide(' '.join(list(format(word, 'b').zfill(64))), 32))
 
def print_state_4x32_128(inputs):
    for word in inputs:
        print("\n".join(slide(' '.join(list(format(word, 'b').zfill(32))), 16)))    
    
def print_state_16x16(inputs_16x16):    
    for word in inputs_16x16:
        print format(word, 'b').zfill(16)
        
def test_4x32_function(function, inputs, print_function=print_state_4x32_128):
    test_function(function, inputs, print_function)
            
def test_4x64_function(function, inputs, print_function=print_state_4x64_256):
    test_function(function, inputs, print_function)
    
def test_function(function, inputs, print_function):
    print("Testing {} with inputs: ".format(function))
    print_function(inputs)
    while not raw_input("any key+enter to finish, enter to continue: "):
        inputs = function(*inputs)
        print("\n")
        print_function(inputs) 