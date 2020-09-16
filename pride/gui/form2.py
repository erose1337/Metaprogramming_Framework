import pprint

import pride.gui.fields
from pride.functions.utilities import resolve_string
from pride.gui.form import Form
from pride.components import Component

ENTRIES = ("pride.gui.fields.Callable_Entry",
           "pride.gui.fields.Text_Entry",
           "pride.gui.fields.Dropdown_Entry",
           "pride.gui.fields.Spinbox_Entry",
           "pride.gui.fields.Toggle_Entry",
           "pride.gui.fields.Slider_Entry",
           "pride.gui.fields.Callable_Entry",
           "pride.gui.fields.Image_Entry",
           "pride.gui.fields.Media_Entry")

FIELDS = ("pride.gui.fields.Callable_Field",
          "pride.gui.fields.Text_Field",
          "pride.gui.fields.Dropdown_Field",
          "pride.gui.fields.Spinbox",
          "pride.gui.fields.Toggle",
          "pride.gui.fields.Slider_Field",
          "pride.gui.fields.Dropdown_Callable",
          "pride.gui.fields.Image_Field",
          "pride.gui.fields.Media_Field")


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
                sub_type = _type.subcomponents[component].type
                if (sub_type not in ENTRIES and sub_type not in FIELDS):
                    self.raise_error("Invalid type '{}'".format(sub_type),
                                     layout_name, row_no, field_name)
                sub_type = resolve_string(sub_type)
                for subkey, subvalue in value.items():
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
        row_type = self.row_type
        if row_type not in ("pride.gui.form.Row", ):
            self.raise_error("Invalid row_type '{}'".format(row_type))

        row_type = resolve_string(row_type)
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
        if field_type not in FIELDS:
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
    from pride.gui.form import (layout, row_info, field_info,
                                load_resource_data, generate_manifest)

    images_dir = pride.site_config.IMAGES_DIRECTORY
    image_filename = os.path.join(images_dir, "testimage.png")
    image_data = load_resource_data(image_filename)

    audio_dir = pride.site_config.GUI_RESOURCES_DIRECTORY
    audio_filename = os.path.join(audio_dir, "testaudio.ogg")
    audio_data = load_resource_data(audio_filename)

    manifest_data = {"/images/testimage.png" : image_data,
                     "/audio/testaudio.ogg" : audio_data}
    manifest = generate_manifest(manifest_data)
    resource_filename = os.path.join(pride.site_config.RESOURCE_DIRECTORY,
                                     manifest["/images/testimage.png"])
    with open(resource_filename, "wb") as _file:
        _file.write(image_data)
        _file.flush()
    with open(os.path.join(pride.site_config.RESOURCE_DIRECTORY,
                           manifest["/audio/testaudio.ogg"]), "wb") as _file:
        _file.write(audio_data)
        _file.flush()

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
                     row_info(2,
                              field_info("test_image",
                                    field_type="pride.gui.fields.Image_Field")),
                     row_info(3,
                              field_info("test_audio",
                                    field_type="pride.gui.fields.Media_Field")),
                     row_info(4),
                     row_info(5, field_info("test_bool")),
                     test_bool=True, test_text="Text", test_int=0,
                     test_slider=50, test_dropdown=0,
                     test_image="/images/testimage.png",
                     test_audio="/audio/testaudio.ogg",
                     manifest=manifest, layout_name="Form2 test layout")

    class Test_Form(Remote_Form):

        defaults = {"layout" : _layout}

        def test_callable(self):
            self.alert("test_callable")


    pride.gui.main.run_programs([Test_Form])

if __name__ == "__main__":
    test_Remote_Form()
