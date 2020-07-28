""" Notice that each field in the form has a identifier/label and an entry for a value.
    The presentation and behavior of a field can be customized. Specifically:

    - The presence of an identifier (auto_create_id)
    - The text of the identifier (display_name)
    - The `orientation` ("stacked" or "side by side")
    - If the field is editable
    - If the field should wrap a target_object other than the parent Forms target

    The vertical size of the rows can also be constrained.
    The number of visible rows can be set.
    Scroll bars appear on the form when there are more rows than `max_rows`.

    New field types are introduced.
    The `alert` method is introduced."""

import pride.gui.widgets.form
field_info = pride.gui.widgets.form.field_info


class Test_Form(pride.gui.widgets.form.Form):


    defaults = {"fields" : (
                            (field_info("test_field1", orientation="side by side",
                                        display_name="Text Field"),
                             field_info("boolean_field", auto_create_id=False)),
                            (field_info("numeric_attribute", editable=False), ),
                            (field_info("dropdown_attribute",
                                        values=("another string",
                                                0,
                                                1,
                                                None,
                                                True,
                                                ('a', 'b', 'c', 1, 2, 3)
                                                )
                                       ), ),
                            (field_info("callable_button", button_text="Call me!",
                                        args=("assign callable args here",),
                                        kwargs={"demonstration" : True}), ),
                            (field_info("slider_field", minimum=0, maximum=100), ),
                           ),
            "test_field1" : "test string", "boolean_field" : False,
            "numeric_attribute" : 0, "dropdown_attribute" : 0,
            "slider_field" : 50,
            "max_rows" : 3,
            "row_h_range" : (0, .33)} # minimum of 0 pixels
                                      # maximum of 33% of the total window height

    def callable_button(self, argument, demonstration=False):
        """ Called when a user clicks the button that says "Call me!" """
        # the `alert` method writes text to stdout and the logfile, prefixed with the components name
        self.alert("callable_button with {} {}".format(argument, demonstration))


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
