import pprint
import ast

def dumps(*args):
    if len(args) == 1:
        args = args[0]
    return pprint.pformat(args)

def loads(serialized_data):
    if not isinstance(serialized_data, bytes):
        _type = type(serialized_data)
        message = "{} supplied (must be instance of {})"
        raise TypeError(message.format(_type, bytes))
    return ast.literal_eval(serialized_data)

def test_serializer():
    test_data = (0, 1.0, True, b"bytes", u"unicode", (0, 1, 2),
                 [x for x in range(4)],
                 dict((x, x) for x in range(4)))
    serialized = dumps(*test_data)
    deserialized = loads(serialized)
    assert deserialized == test_data, (pprint.pformat(test_data), '\n',
                                       pprint.pformat(deserialized))

if __name__ == "__main__":
    test_serializer()
