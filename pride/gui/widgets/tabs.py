import pride.gui.widgets.form

class Tabbed_Window(pride.gui.widgets.form.Scrollable_Window):

    defaults = {"include_new_tab_button" : True, "tab_targets" : tuple(),
                "new_window_type" : "pride.gui.gui.Container",
                "include_tab_delete_button" : True,
                "new_window_tab_text" : "New Window"}
    autoreferences = ("tab_bar", )

    def __init__(self, **kwargs):
        super(Tabbed_Window, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        if self.include_new_tab_button:
            fields = [[("new_tab", {"button_text" : '+',
                                    "scale_to_text" : True})]]
        else:
            fields = [[]]
        fields[0].extend([("select_tab", {"button_text" : _object.tab_text,
                                          "args" : (_object, )})
                          for _object in self.tab_targets])
        self.tab_bar = self.create(pride.gui.widgets.form.Form, pack_mode="top",
                                   fields=fields, target_object=self,
                                   h_range=(0, .05), max_rows=1)
        for _object in self.tab_targets:
            _object.hide()
        self.select_tab(self.tab_targets[0])

    def new_tab(self):
        tab_bar = self.tab_bar
        _object = self.main_window.create(self.new_window_type, text="debug text")
        fields = [("select_tab", {"args" : (_object, ),
                                  "button_text" : self.new_window_tab_text,
                                  "theme_profile" : "placeholder",
                                  "entry_kwargs" : {"theme_profile" : "placeholder",
                                                    "scale_to_text" : True}})]
        if self.include_tab_delete_button:
            fields.append(("delete_tab", {"args" : (_object, ),
                                          "button_text" : 'x',
                                          "theme_profile" : "placeholder",
                                          "entry_kwargs" : {"theme_profile" : "placeholder",
                                                            "scale_to_text" : True}})
                         )
        row = tab_bar.rows[0]
        for field_info in fields:
            tab_bar.create_field(field_info, row)

    def select_tab(self, _object):
        if _object.hidden:
            _object.show()
        else:
            _object.hide()
        _object.pack()
        for tab in self.tab_bar.fields_list:
            if tab.args[0] is _object:
                if _object.hidden:
                    tab.theme_profile = "placeholder"
                else:
                    tab.theme_profile = "indicator"

    def delete_tab(self, _object):
        _object.delete()
        found = []
        for field in self.tab_bar.fields_list:
            if field.args and field.args[0] == _object:
                found.append(field) # don't delete until after done iterating over fields list
        for field in found:
            field.delete()

    def delete(self):
        del self.tab_targets
        super(Tabbed_Window, self).delete()


def test_Tabbed_Window():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable(x=52, y=52)]
    window.create(pride.gui.main.Gui, startup_programs=(Tabbed_Window, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Tabbed_Window()
