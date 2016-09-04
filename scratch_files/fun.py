import itertools
import hashlib
import random

import pride.base

class _Object(pride.base.Base):
    
    defaults = pride.base.Base.defaults.copy()
    
    def __add__(self, other_self):
        self_class, other_class = self.__class__, other_self.__class__
        
        new_name = '_'.join((self_class.__name__, other_class.__name__))
        
        new_class_attributes = self_class.__dict__.copy()
        new_class_attributes.update(other_class.__dict__)
        
        new_class = type(new_name, tuple(set((self_class, other_class))),
                         new_class_attributes)
                         
        new_self_attributes = self.__dict__.copy()
        new_self_attributes.update(other_self.__dict__)
        return new_class(**new_self_attributes)
        
        
STANDARD_OPERATORS = ("+=", "-=", "*=", "/=", "//=", "**=", "%=",
                      "&=", "^=", "<<=", ">>=")
        
def compile_function(source, function_name):    
    namespace = {}
    exec compile(source, 'generate_function', 'exec') in namespace, namespace
    return namespace.pop(function_name)
    
def generate_function(input0=0, input1=0, operation_count=0,
                      operators=STANDARD_OPERATORS,
                      operations=tuple()):
    hash_string = hashlib.sha1(':'.join(str(item) for item in 
                              (input0, input1, operation_count, 
                              operators, operations))).hexdigest()                     
    input0 = input0 or random.randint(1, 8)
    input1 = input1 or random.randint(1, 8)
    function_name = "generated_function{}".format(hash_string)    
    source = "def {}(input0={}, input1={}):\n".format(function_name, input0, input1)
    inputs = ("input0", "input1")
    for count in xrange(operation_count or random.randint(1, 6)):
        operator = random.choice(operators)
        source += "    {} {} {}\n".format(random.choice(inputs), 
                                          operator, 
                                          random.choice(inputs))
    source += "    return input0, input1"
    print "Created: \n", source
    return compile_function(source, function_name)   
        
def generate_function2(_inputs, operation_count=0, operators=STANDARD_OPERATORS, operations=tuple()):
    source = "def {}(" + ''.join("input{}={}, ".format(count, argument) for count, argument in enumerate(_inputs)) + "):\n"
    operations = operations or (operators[random.randint(0, len(operators))] for operation in range(operation_count))
    for operation in operations:
        source += "    input{} {} input{}\n".format(random.choice(_inputs), operation, random.choice(_inputs))
    source += "    return " + ''.join("input{}, ".format(index) for index, _input in enumerate(_inputs))
    source = source.format("function_name")
    print("Created:\n{}".format(source))
    return compile_function(source, "function_name")
    
def generate_function_combinations(input_count, operation_count, operator_list, _hash=hash):
    _inputs = range(input_count)
    for _inputs in itertools.product(*(_inputs for count in _inputs)):
        print _inputs
        for operations in itertools.product(*(operator_list for count in range(operation_count))):
            name = _hash(str(_inputs) + str(operations))
            source = "def function_{}(".format(name) + ''.join("input{}, ".format(count) for count in _inputs) + "):\n"    
            for operation in operations:
                source += "    input0 {} input1\n".format(operation)
            source += "    return " + ''.join("input{}, ".format(index) for index in range(input_count))
            source = source.format("function_name")
        print("Created:\n{}".format(source))
    #return compile_function(source, "function_name")
    
def generate_arx_functions(input_count, operation_count):
    _inputs = [0 for count in range(input_count)]
    operators = ("+=", "^=", "<<=", ">>=")
    
        
if __name__ == "__main__":    
    object1 = _Object(thisisatest=1)
    object2 = _Object(again=None)
    
    object3 = object1 + object2
    print object3.__dict__
    print object3.__class__.__mro__
    
    new_function = generate_function()
    new_function2 = generate_function2((0, 1, 2, 3), 3)
    generate_function_combinations(4, 3, ("+=", "^=", "<<=", ">>="))
    