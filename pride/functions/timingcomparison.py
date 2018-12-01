import pride.functions.decorators

def timing_comparison(*functions, **kwargs):
    iterations = kwargs.get("iterations", 1)
    for function, args, kwargs in functions:
        print pride.functions.decorators.Timed(function, iterations)(*args, **kwargs)

# test accessing global versus accessing an attribute; global is faster        
TEST = "this is a test string"
def global_access():
    for x in xrange(10000):
        TEST
 
class _Test(object):
    def __init__(self):
        self.TEST = "this is a test string"
        
def attribute_access():
    t = _Test()
    for x in xrange(10000):
        t.TEST
          
#timing_comparison((global_access, tuple(), {}), (attribute_access, tuple(), {}))        
      
def number_of_set_bits(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24
    
def number_of_set_bits_sum(x):
    return sum( [x&(1<<i)>0 for i in range(8)] )

#timing_comparison((number_of_set_bits, (127, ), {}), (number_of_set_bits_sum, (127, ), {}))
    
def inplace_add_inplace_and(a, b):
    a += b
    a &= 255
    
def reallocate_add_and(a, b):
    a = (a + b) & 255
    
#timing_comparison((inplace_add_inplace_and, (1, 10), {}), (reallocate_add_and, (1, 10), {}), iterations=1000000)

def list_replace(_list, index, value):
    _list[index] = value
    
def bytearray_replace(_bytearray, index, value):
    _bytearray[index] = value
    
#timing_comparison((list_replace, ([0] * 256, 128, 65536), {}), 
#                  (bytearray_replace, ([0] * 256, 128, 255), {}), iterations=100000) 

def _func(byte):
    _func.state ^= byte
    return _func.state
        
def xor_sum(data1):       
    _func.state = 0    
    return map(_func, data1)[-1]
    
def xor_sum2(data1):
    xor_sum2.state = 0
    for byte in data1:
        xor_sum2.state ^= byte
    return xor_sum2.state
    
#timing_comparison((xor_sum, (range(256), ), {}), (xor_sum2, (range(256), ), {}),
#                  iterations=10000)
                  
def extract_number_from_string(data):
    return [int(s) for s in data.split() if s.isdigit()]
    
def extract_number_from_string2(data, numbers=set("0123456789")):
    return [int(s) for s in data if s in numbers]
    
def slide1(iterable, x=1):
    """ Yields x bytes at a time from iterable """
    slice_count, remainder = divmod(len(iterable), x)
    for position in range((slice_count + 1 if remainder else slice_count)):
        _position = position * x
        yield iterable[_position:_position + x]      
    
def slide_iter(iterable, x=1):
    size = len(iterable)
    return (iterable[position * x:(position * x) + x] for position in range((size / x) + (1 if (size % x) else 0)))
    
def test_slide_timing():       
    iterable = [x for x in range(1024 * 1024 * 48)]
    TEST_SIZE = 16
    def test_slide1(iterable):
        for chunk in slide(iterable, TEST_SIZE):
            pass
    def test_slide_iter(iterable):
        for chunk in slide(iterable, TEST_SIZE):
            pass
    timing_comparison((test_slide1, (iterable, ), {}),
                      (test_slide_iter, (iterable, ), {}))
    
    
if __name__ == "__main__":
    #timing_comparison((extract_number_from_string, ("h3110 23 cat 444.4 rabbit 11 2 dog", ), {}),
    #                  (extract_number_from_string2, ("h3110 23 cat 444.4 rabbit 11 2 dog", ), {}),
    #                  iterations=10000)
    test_slide_timing()
    