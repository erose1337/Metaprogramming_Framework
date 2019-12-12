import pride.gui.widgets.form

class Tab_Button_Entry(pride.gui.widgets.form.Callable_Entry):

    defaults = {"_end_hover_set_profile" : '', "_already_constructed" : False,
                "use_lazy_loading" : True}

    def left_click(self, mouse):
        parent_field = self.parent_field
        if self.use_lazy_loading and not self._already_constructed:
            parent_field.args = (parent_field.args[0](), ) + parent_field.args[1:]
            self._already_constructed = True
        parent_field.value(self, *parent_field.args, **parent_field.kwargs)
        _object = self.parent_field.args[0]
        if _object.hidden:
            self._end_hover_set_profile = "interactive"
        else:
            self._end_hover_set_profile = "indicator"

    def handle_return(self):
        parent_field = self.parent_field
        parent_field.value(self, *parent_field.args, **parent_field.kwargs)

    def hover_ends(self):
        super(Tab_Button_Entry, self).hover_ends()
        new_profile = self._end_hover_set_profile
        if new_profile:
            self.theme_profile = new_profile
            self._end_hover_set_profile = ''


class Tab_Button_Field(pride.gui.widgets.form.Callable_Field):

    defaults = {"entry_type" : Tab_Button_Entry}


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
                                          "args" : (_object, ),
                                          "field_type" : Tab_Button_Field})
                          for _object in self.tab_targets])
        self.tab_bar = self.create(pride.gui.widgets.form.Form, pack_mode="top",
                                   fields=fields, target_object=self,
                                   h_range=(0, .05), max_rows=1)

    def new_tab(self, new_tab_button):
        tab_bar = self.tab_bar
        _object = self.main_window.create(self.new_window_type, text="debug text")
        fields = [("select_tab", {"args" : (_object, ),
                                  "button_text" : self.new_window_tab_text,
                                  "theme_profile" : "placeholder",
                                  "entry_kwargs" : {"theme_profile" : "placeholder",
                                                    "scale_to_text" : True},
                                  "field_type" : Tab_Button_Field})]
        if self.include_tab_delete_button:
            fields.append(("delete_tab", {"args" : (_object, ),
                                          "button_text" : 'x',
                                          "theme_profile" : "placeholder",
                                          "entry_kwargs" : {"theme_profile" : "placeholder",
                                                            "scale_to_text" : True}})
                         )
        row = tab_bar.rows[0]
        for field_info in fields:
            field = tab_bar.create_field(field_info, row)
            if field.name == "select_tab":
                self._set_color(field.entry, field.args[0])

    def select_tab(self, tab, _object):
        if _object.hidden:
            _object.show()
        else:
            _object.hide()
        _object.pack()
        self._set_color(tab, _object)
        #self.sdl_window.schedule_postdraw_operation(lambda: self._set_color(tab, _object), self)

    def _set_color(self, tab, _object):
        if _object.hidden:
            tab.theme_profile = "interactive"
        else:
            tab.theme_profile = "indicator"

    def delete_tab(self, delete_button, _object):
        _object.delete()
        delete_button.parent_field.delete()
        for field in self.tab_bar.fields_list:
            if field.args and field.args[0] == _object:
                field.delete() # modifies list that is being iterated over
                break          # won't matter if we don't do anything further with it

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
