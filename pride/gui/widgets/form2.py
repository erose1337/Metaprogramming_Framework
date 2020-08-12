# layout(
#        row_info(row_no,
#                 (field_info(field_name, **field_kwargs),
#                  field_info(...), ...),
#                 **row_kwargs)
#        row_info(...),
#        ...
#       )
import pprint

TEST_LAYOUT = """\
layout(row_info(0,
                field_info("test_string"),
                field_info("test_bool"),
                h_range=(0, .1)),
      row_info(1,
               field_info("test_int"),
               field_info("test_dropdown", values=(1, '2'))
               ),
      w_range=(0, .25)
     )"""

def layout(*rows, **kwargs):
    return (dict((row[0], row[1:]) for row in rows), kwargs)

def row_info(row_no, *field_infos, **row_kwargs):
    return (row_no, field_infos, row_kwargs)

def field_info(field_name, **kwargs):
    return (field_name, kwargs)

def compile_layout(layout_str):
    _globals = {"layout" : layout,
                "row_info" : row_info,
                "field_info" : field_info}
    _locals = dict()
    program = "__compile_layout_output = {}".format(layout_str)
    double_check(program)
    exec program in _locals, _globals
    return _globals["__compile_layout_output"]

def double_check(program):
    forbidden = ("setattr", "getattr", "delattr", "dir", "__dict__")
    for item in forbidden:
        if item in program:
            raise Warning("Found forbidden token '{}'".format(item))
    # cannot simply filter '.' because it is needed for floating point numbers
    # if the symbol to the right of the '.' is a numeral, then
    # it cannot be a name, as names may not start with numbers.
    if '.' in program:
        index = 0
        end = len(program)
        while index != end:
            try:
                index = program.index('.', index + 1)
            except ValueError:
                break
            if not program[index + 1].isdigit():
                raise Warning("Found an attempted attribute access")

def compile_file(_file):
    return compile_layout(_file.read())

def compile_filename(filename):
    with open(filename, 'r') as _file:
        output = compile_file(_file)
    return output

def test_field_info():
    field_name = "test name"
    kwargs = dict()
    out = field_info(field_name, **kwargs)
    assert out[0] == field_name
    assert out[1] == kwargs

def test_row_info():
    field1 = field_info("test_field1")
    field2 = field_info("test_field2")
    out = row_info(0,
                   field1,
                   field2,
                   h_range=(0, .1))
    assert out[0] == 0, out[0]
    assert out[1][0] == field1, (out[1][0], field1)
    assert out[1][1] == field2, (out[1][1], field2)
    assert out[2]["h_range"] == (0, .1), out[2]["h_range"]

def test_layout():
    row0 = row_info(0,
                    field_info("test_string"),
                    field_info("test_bool"),
                    h_range=(0, .1))
    row1 = row_info(1, field_info("test_int"),
                       field_info("test_dropdown", values=(1, '2')))

    out = layout(row0, row1, w_range=(0, .25))
    assert out[0][0] == row0[1:], (out[0][0], row0[1:])
    assert out[0][1] == row1[1:], (out[0][1], row1[1:])
    assert out[1]["w_range"] == (0, .25), out[1]["w_range"]

def test_compile_layout():
    row0 = row_info(0,
                    field_info("test_string"),
                    field_info("test_bool"),
                    h_range=(0, .1))
    row1 = row_info(1,
                    field_info("test_int"),
                    field_info("test_dropdown", values=(1, '2')))
    out1 = layout(row0, row1, w_range=(0, .25))

    _layout = TEST_LAYOUT
    out2 = compile_layout(_layout)
    assert out1 == out2, '\n' + pprint.pformat((out1, out2))

def test_compile_file():
    row0 = row_info(0,
                    field_info("test_string"),
                    field_info("test_bool"),
                    h_range=(0, .1))
    row1 = row_info(1,
                    field_info("test_int"),
                    field_info("test_dropdown", values=(1, '2')))
    out1 = layout(row0, row1, w_range=(0, .25))

    with open("_form2test.txt", 'w+') as _file:
        _file.write(TEST_LAYOUT)
        _file.seek(0)
        out2 = compile_file(_file)
    assert out1 == out2, '\n' + pprint.pformat((out1, out2))

def test_compile_filename():
    row0 = row_info(0,
                    field_info("test_string"),
                    field_info("test_bool"),
                    h_range=(0, .1))
    row1 = row_info(1,
                    field_info("test_int"),
                    field_info("test_dropdown", values=(1, '2')))
    out1 = layout(row0, row1, w_range=(0, .25))

    with open("_form2test.txt", 'w') as _file:
        _file.write(TEST_LAYOUT)
        _file.seek(0)
    out2 = compile_filename("_form2test.txt")
    assert out1 == out2, '\n' + pprint.pformat((out1, out2))

if __name__ == "__main__":
    test_field_info()
    test_row_info()
    test_layout()
    test_compile_layout()
    test_compile_file()
    test_compile_filename()
