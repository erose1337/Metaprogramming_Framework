import pride.gui.form
from pride.components import Component
from pride.gui.form import row_info, field_info

def add_field_to_row(_row_info, _field_info):
    return row_info(_row_info[0],
                    *(_row_info[1] + (_field_info, )),
                    **_row_info[2])

def tab_info(**tab_kwargs):
    return field_info("select_tab", **tab_kwargs)

class Tab_Bar(pride.gui.form.Form):

    defaults = {"include_new_tab_button" : False, "tab_info" : tuple(),
                "pack_mode" : "top"}
    subcomponents = {"vertical_slider" : Component(location=None),
                     "horizontal_slider" :
                                     Component("pride.gui.fields.Slider_Field"),
                     "new_tab_button" :
                            Component("pride.gui.fields.Callable_Field",
                                      name="create_new_tab", button_text='+',
                                      location="right")}

    def create_subcomponents(self):
        super(Tab_Bar, self).create_subcomponents()
        try:
            row = self.layout[0][0]
        except KeyError:
            self.layout[0][0] = row_info(0)

        if self.include_new_tab_button:
            _field_info = field_info("new_tab", **self.new_tab_button_kwargs)
            self.add_field_to_row(_row_info, _field_info)

        for _field_info, _object in self.tab_info:
            _field_info["args"] = (_object, )
            self.add_field_to_row(_field_info, row)

    def add_field_to_row(self, _row_info, _field_info):
        _row_info = self.layout[0][0]
        self.layout[0][0] = add_field_to_row(_row_info, _field_info)


def test_Tab_Bar():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable(x=52, y=52)]
    window.create(pride.gui.main.Gui, startup_programs=(Tab_Bar, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Tab_Bar()
