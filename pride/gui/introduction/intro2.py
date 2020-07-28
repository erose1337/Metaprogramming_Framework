""" This example shows how to create a Form.
    A Form can receive a variety of input types from a user.
    A basic Form consists of fields such as:

    - Text fields
    - Dropdown fields
    - Sliders
    - Spinboxes
    - Toggles
    - Programmable buttons

    Forms are created by specifying information about the fields.

    The `main` function has been modified to create a form when starting by setting the `startup_programs` attribute.

    The `defaults` dictionary is also introduced.

    A Form is a wrapper around a python object.
    By default (as in the following example) the wrapped object will be the Form object itself.
        - The `target_object` attribute controls what object is wrapped.
    Fields in the form are linked with the corresponding attributes on the wrapped object.
    When a user modifies a field, it modifies the value of that attribute on the wrapped object.

    This example creates a form that is laid out like so:

        -----------------------------------------
        |text field      | boolean field        |
        |                | (an on/off button)   |
        |---------------------------------------|
        |          integer field                |
        |           (a spinbox)                 |
        ----------------------------------------
     """
import pride.gui.widgets.form
field_info = pride.gui.widgets.form.field_info


class Test_Form(pride.gui.widgets.form.Form):

    # the class `defaults` dictionary is used to set a new objects attributes
    # each key:value in the `defaults` dictionary is set as an attribute on a newly created object

    # the "fields" attribute is an iterable (in this case tuple) of iterables
    # each sub-tuple represents a row in the form
    # the field_info items in each sub-tuple represent a field in that row
    # fields support a variety of keyword arguments for adjusting their presentation and/or behavior
    defaults = {"fields" : (
                             (field_info("test_field1"), field_info("boolean_field")),
                             (field_info("numeric_attribute"), )
                           ),
                "test_field1" : "test string", "boolean_field" : False,
                "numeric_attribute" : 0}


def main():
    import pride
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable()]
    window.create(pride.gui.main.Gui,
                  startup_programs=(Test_Form, ),
                  user=pride.objects["/User"]
                  )

if __name__ == "__main__":
    main()
