import pride.gui.widgets.tabs

API = ("tab_info", "Tabbed_form", )

def tab_info(tab_name, _type, **tab_kwargs):
    return (tab_name, _type, tab_kwargs)

class Tabbed_Form(pride.gui.widgets.tabs.Tabbed_Window):

    defaults = {"include_new_tab_button" : False,
                "form_type" : "pride.gui.widgets.form.Form"}
    tabs = tuple() # [tab_info("tab1", callable)]

    def create_subcomponents(self):
        if getattr(self, "fields", False):
            self.main_window.create(self.form_type, fields=self.fields,
                                    parent_form=self, target_object=self,
                                    location="main")

        tab_targets = self.tab_targets = []
        for name, _type, tab_kwargs in self.tabs:

            def callable(self=self, name=name, _type=_type):
                instance = self.main_window.create(_type)
                setattr(self, name, instance)
                return instance

            tab_kwargs.setdefault("button_text", name)
            callable.tab_kwargs = tab_kwargs
            tab_targets.append(callable)

        super(Tabbed_Form, self).create_subcomponents()

def test_Tabbed_Form():
    import pride.gui.main
    import pride.gui.widgets.form
    field_info = pride.gui.widgets.form.field_info

    class Test_Form(pride.gui.widgets.form.Form):

        defaults = {"test_value" : True, "integer" : 0,
                    "fields" : [[field_info("test_value"),
                                 field_info("integer")]],
                    "row_kwargs" : {0 : {"h_range" : (0, .1)}}}


    class test_Tabbed_Form(Tabbed_Form):

        tabs = (tab_info("form1", Test_Form, button_text="form1"), )


    pride.gui.main.run_programs([test_Tabbed_Form])

if __name__ == "__main__":
    test_Tabbed_Form()
