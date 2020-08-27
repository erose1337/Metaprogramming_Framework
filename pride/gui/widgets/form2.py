# layout(
#        row_info(row_no,
#                 (field_info(field_name, **field_kwargs),
#                  field_info(...), ...),
#                 **row_kwargs)
#        row_info(...),
#        ...
#       )
import keyword # for kwlist
import tokenize
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

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
    return (dict((row[0], row) for row in rows), kwargs)

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

# if run as main, __builtins__ is a module
# otherwise, __builtins__ is a dictionary
try:
    FILTER_TOKENS = __builtins__.keys()
except AttributeError:
    FILTER_TOKENS = dir(__builtins__)
    assert FILTER_TOKENS != dir(dict)
FILTER_TOKENS += tuple(keyword.kwlist)

def double_check(program, filter=FILTER_TOKENS):
    flo = StringIO.StringIO(program)
    for _, token, _, _, _ in tokenize.generate_tokens(flo.readline):
        if token in filter:
            raise Warning("Found forbidden token '{}'".format(token))
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
    assert out[0][0] == row0, (out[0][0], row0)
    assert out[0][1] == row1, (out[0][1], row1)
    assert out[1]["w_range"] == (0, .25), out[1]["w_range"]

def test_compile_layout():
    import pprint
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
    import pprint
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
    import pprint
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

from pride.components import deep_update
import pride.gui.gui
import pride.gui.widgets
import pride.gui.widgets.form

class Scrollable_Window(pride.gui.gui.Window):

    defaults = {"vertical_slider_position" : "right",
                "horizontal_slider_position" : "bottom",
                "main_window_type" : "pride.gui.gui.Container",
                "slider_type" : "pride.gui.widgets.form.Slider_Field"}
    predefaults = {"_x_scroll_value" : 0, "_y_scroll_value" : 0}
    autoreferences = ("main_window", "vertical_slider", "horizontal_slider")
    mutable_defaults = {"vertical_slider_entry_kwargs" : lambda: {"orientation" : "stacked"},
                        "horizontal_slider_entry_kwargs" : dict}

    def _get_y_scroll_value(self):
        return self._y_scroll_value
    def _set_y_scroll_value(self, new_value):
        old_value = self._y_scroll_value
        self._y_scroll_value = new_value
        self.handle_y_scroll(old_value, new_value)
    y_scroll_value = property(_get_y_scroll_value, _set_y_scroll_value)

    def _get_x_scroll_value(self):
        return self._x_scroll_value
    def _set_x_scroll_value(self, new_value):
        old_value = self._x_scroll_value
        self._x_scroll_value = new_value
        self.handle_x_scroll(old_value, new_value)
    x_scroll_value = property(_get_x_scroll_value, _set_x_scroll_value)

    def __init__(self, **kwargs):
        super(Scrollable_Window, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        self.main_window = self.create(self.main_window_type, location="main")
        position = self.vertical_slider_position
        if position is not None:
            self.vertical_slider = \
            self.create(self.slider_type, location=position,
                        orientation="stacked", w_range=(0, .025),
                        name="y_scroll_value", minimum=0, maximum=0,
                        auto_create_id=False, target_object=self,
                        entry_kwargs=self.vertical_slider_entry_kwargs)
        position = self.horizontal_slider_position
        if position is not None:
            self.horizontal_slider = \
            self.create(self.slider_type, location=position,
                        orientation="side by side", h_range=(0, .025),
                        auto_create_id=False, target_object=self,
                        name="x_scroll_value", minimum=0, maximum=0,
                        entry_kwargs=self.horizontal_slider_entry_kwargs,)

    def handle_x_scroll(self, old_value, new_value):
        pass

    def handle_y_scroll(self, old_value, new_value):
        pass

# should not be an attribute of Form;
# otherwise it could be overwritten via kwargs when the Form is instantiated
# if the kwargs are controlled by an adversary (i.e. a malicious layout file)
# the field_type argument could be used to call any function

FIELD_TYPES = {"Dropdown" : "pride.gui.fields.Dropdown_Field",
               "Slider" : "pride.gui.fields.Slider",
               "Toggle" : "pride.gui.fields.Toggle",
               "Spinbox" : "pride.gui.fields.Spinbox",
               "Text_Field" : "pride.gui.fields.Text_Field",
               "Text_Display" : "pride.gui.fields.Text_Display",
               "Callable" : "pride.gui.fields.Callable_Field"}


class Row(pride.gui.gui.Container):

    mutable_defaults = {"fields" : list}

    def delete(self):
        del self.fields[:]
        super(Row, self).delete()


class Form(pride.gui.widgets.form.Scrollable_Window):

    defaults = {"target_object" : None}
    subcomponent_kwargs = {"row" : {"location" : "top",
                                    "h_range"  : (0, 1.0),
                                    "row_type" : "pride.gui.widgets.form2.Row"}}
    mutable_defaults = {"rows" : dict}

    def create_subcomponents(self):
        if self.target_object is None:
            self.target_object = self
        super(Form, self).create_subcomponents()

        _layout = self.layout
        for row_no in range(self.max_rows):
            self.create_row(_layout[row_no])

    def create_row(self, _row_info):
        kwargs = copy.deepcopy(self.row_kwargs)
        row_no, row_kwargs = _row_info[0], _row_info[-1]
        deep_update(kwargs, _row_info[-1])
        kwargs.setdefault("row_number", _row_info[0])
        _type = kwargs["row_type"]

        window = self.main_window
        row = window.create(_type, **kwargs)
        self.rows[row_no] = row

        for _field_info in _row_info[1:-1]:
            self.create_field(_field_info, row)

    def create_field(self, _field_info, row):
        field_name, field_kwargs = _field_info
        field_type = self.determine_field_type(target_object,
                                               field_name,
                                               field_kwargs)
        field_kwargs.setdefault("target_object", self.target_object)
        field = row.create(field_type, name=field_name, parent_form=self,
                           **field_kwargs)
        self.row.fields.append(field)

    def determine_field_type(self, target_object, name, entries):
        field_type = entries.get("field_type", None)
        if field_type is None:
            try:
                value = getattr(target_object, name)
            except AttributeError as exception:
                try:
                    value = target_object[name]
                except TypeError:
                    raise exception
            if hasattr(value, "field_type"):
                field_type = value.field_type
            elif "values" in entries: # check for dropdowns before checking value
                field_type = self.dropdown_type
            elif "minimum" in entries and "maximum" in entries: # check here before checking for int/float
                field_type = self.slider_type
            elif isinstance(value, bool): # must compare for bool before comparing for int; bool is a subclass of int
                field_type = self.toggle_type
            elif isinstance(value, int) or isinstance(value, float):
                field_type = self.spinbox_type
            elif isinstance(value, str):
                field_type = self.text_field_type
            elif hasattr(value, "__call__"):
                field_type = self.callable_type
            #elif isinstance(value, tuple) or isinstance(value, list):
            #    field_type = "pride.gui.widgets.formext.Tabbed_Form"
        if field_type is None:
            message = "Unable to determine field_type for {}"
            raise ValueError(message.format((target_object, name, value, entries)))
        if field_type not in FIELD_TYPES:
            message = "Requested field_type '{}' is unavailable"
            raise ValueError(message.format(field_type))
        return FIELD_TYPES[field_type]

    def delete(self):
        self.rows.clear()
        del self.target_object
        super(Form, self).delete()

def test_Form():
    import pride.gui.main
    _layout = layout(row_info(0,
                              field_info("test_bool"),
                              field_info("test_text"),
                              field_info("test_int")
                              h_range=(0, .2)),
                     row_info(1,
                              field_info("test_slider", minimum=0, maximum=100),
                              field_info("test_dropdown",
                                         values=(0, 1, 2, 3, 5, 8)))
                    )
    callable = lambda **kwargs: Form(layout=_layout)
    pride.gui.main.run_programs([callable])


if __name__ == "__main__":
    test_field_info()
    test_row_info()
    test_layout()
    test_compile_layout()
    test_compile_file()
    test_compile_filename()
    test_Form()
