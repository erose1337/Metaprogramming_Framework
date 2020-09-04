from pride.functions.utilities import resolve_string
from pride.gui.form import Form

class Remote_Form(Form):

    def deep_filter(self, key, value, _type,
                    layout_name=None, row_no=None, field_name=None):
        if key not in _type.interface[1]:
            self.raise_error("'{}' not in {} interface",
                             layout_name, row_no, field_name,
                             (key, _type.__name__))
        try:
            component, _kwargs = key.rsplit('_', 1)
        except ValueError:
            pass
        else:

            if _kwargs == "kwargs" and component in _type.subcomponents:
                sub_type = _type.subcomponents[component]["type"]
                if (sub_type not in pride.gui.fields.ENTRIES and
                    sub_type not in pride.gui.fields.FIELDS):
                    self.raise_error("Invalid type '{}'".format(sub_type),
                                     layout_name, row_no, field_name)
                sub_type = resolve_string(sub_type)
                for subkey, subvalue in value.items():
                    if subkey == "type":
                        continue
                    self.deep_filter(subkey, subvalue, sub_type,
                                     layout_name, row_no, field_name)

    def create_subcomponents(self):
        api_controlled_values = dir(self)
        form_vars = self.form_vars = []
        for key, value in self.layout[-1].items():
            if key in api_controlled_values:
                if key not in self.interface[1]:
                    raise Warning("Filter failed to catch '{}' {}".format(key, value))
            else:
                form_vars.append(key)

        _layout = self.layout
        form_kwargs = _layout[1]
        interface = self.interface[1]
        for key, value in form_kwargs.items():
            if key not in form_vars:
                self.deep_filter(key, value, type(self),
                                 form_kwargs.get("layout_name", None))
        super(Remote_Form, self).create_subcomponents()

    def create_row(self, _row_info):
        untrusted_kwargs = _row_info[-1]
        row_type = self.row_kwargs["type"]
        if row_type not in ("pride.gui.form.Row", ):
            self.raise_error("Invalid row_type '{}'".format(row_type))

        row_type = pride.functions.utilities.resolve_string(row_type)
        for key, value in untrusted_kwargs.items():
            self.deep_filter(key, value, row_type,
                             row_no=_row_info[0])
        return super(Remote_Form, self).create_row(_row_info)

    def create_field(self, _field_info, row):
        untrusted_kwargs = _field_info[-1]
        f_name = _field_info[0]
        target_object = self.target_object
        row_no = row.row_number
        if not hasattr(target_object, f_name):
            self.raise_error("target_object has no attribute '{}'",
                             row=row.row_number, field=f_name,
                             args=(f_name, ))

        if (f_name not in target_object.interface[0] and
            f_name not in target_object.interface[1] and
            f_name not in self.form_vars):
            message = "Attempted to create field for non-interface attribute {}"
            self.raise_error(message, row=row.row_number, field=f_name,
                             args=(f_name, ))

        field_type = self.determine_field_type(self.target_object,
                                               f_name,
                                               untrusted_kwargs)
        if field_type not in ("pride.gui.fields.Dropdown_Field",
                              "pride.gui.fields.Slider_Field",
                              "pride.gui.fields.Toggle",
                              "pride.gui.fields.Spinbox",
                              "pride.gui.fields.Text_Field",
                              "pride.gui.fields.Text_Display",
                              "pride.gui.fields.Callable_Field",
                              "pride.gui.fields.Dropdown_Callable",
                              "pride.gui.tabs.Tab"):
            self.raise_error("Requested field_type '{}' is unavailable",
                             row=row_no, field=f_name,
                             args=(field_type, ))

        field_type = resolve_string(field_type)
        for key, value in untrusted_kwargs.items():
            self.deep_filter(key, value, field_type,
                             row_no=row_no, field_name=f_name)
        return super(Remote_Form, self).create_field(_field_info, row)

    def raise_error(self, text, layout_name=None, row=None, field=None,
                    args=tuple()):
        message = ''
        layout_name = getattr(self, "layout_name", layout_name)
        if layout_name is not None:
            message += "\nlayout: {}\n".format(layout_name)
            message += ('-' * min(79, len(message))) + '\n'
        if row is not None:
            message += "Row: {}; ".format(row)
        if field is not None:
            message += "Field: {}".format(field)
        if row or field:
            message += '\n'
        message += text.format(*args)
        raise ValueError(message)

def test_Remote_Form():
    import pride.gui.main
    from pride.gui.form import layout, row_info, field_info

    _layout = layout(row_info(0,
                              field_info("test_bool"),
                              field_info("test_text"),
                              field_info("test_int"),
                              h_range=(0, .2)),
                     row_info(1,
                              field_info("test_slider", minimum=0, maximum=100),
                              field_info("test_dropdown",
                                         orientation="stacked",
                                         values=(0, 1, 2, 3, 5, 8, 13, 21,
                                                 34, 55, 89, 144)),
                              field_info("delete",
                                         button_text="Delete (Test Callable)"),
                              h_range=(0, .3)),
                     row_info(2), row_info(3), row_info(4),
                     row_info(5, field_info("test_bool")),
                     test_bool=True, test_text="Text", test_int=0,
                     test_slider=50, test_dropdown=0,
                     layout_name="Remote_Form test layout")

    class Test_Form(Remote_Form):

        defaults = {"layout" : _layout}

        def test_callable(self):
            self.alert("test_callable")


    pride.gui.main.run_programs([Test_Form])

if __name__ == "__main__":
    test_Remote_Form()
