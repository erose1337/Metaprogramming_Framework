import pride.gui.widgets.form
from pride.functions.utilities import slide

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
                "include_tab_delete_button" : True, "tab_bar_label" : '',
                "new_window_tab_text" : "New Window", "include_label" : False,
                "tab_bar_title_text" : '', "tabs_per_row" : 16}
    autoreferences = ("tab_bar", )

    def __init__(self, **kwargs):
        super(Tabbed_Window, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        fields = [[("select_tab", {"button_text" : _object.tab_text,#getattr(_object,
                                                        #   "tab_text", ''),
                                   "args" : (_object, ),
                                   "field_type" : Tab_Button_Field})
                   for _object in row] for
                        row in slide(self.tab_targets, self.tabs_per_row)]
        if self.include_new_tab_button:
            entry = ("new_tab", {"button_text" : '+', "scale_to_text" : True})
            if fields:
                fields[0].insert(0, entry)
            else:
                fields.append([entry])
        if self.include_label:
            entry = ("tab_bar_label", {"hoverable" : False,
                                       "field_type" : "pride.gui.gui.Window",
                                       "pack_mode" : "left",
                                       "text" : self.tab_bar_label,
                                       "scale_to_text" : True
                                       })
            if fields:
                fields[0].insert(0, entry)
            else:
                fields.append([entry])
        kwargs = {"orientation" : "stacked", "include_minmax_buttons" : False}
        self.tab_bar = self.create(pride.gui.widgets.form.Form, pack_mode="top",
                                   fields=fields, target_object=self,
                                   form_name=self.tab_bar_title_text,
                                   vertical_slider_entry_kwargs=kwargs,
                                   h_range=(0, .05), max_rows=1)

    def new_tab(self):
        tab_bar = self.tab_bar
        _object = self.main_window.create(self.new_window_type)
        fields = [("select_tab", {"args" : (_object, ),
                                  "button_text" : self.new_window_tab_text,
                                  "theme_profile" : "placeholder",
                                  "entry_kwargs" : {"theme_profile" : "placeholder",
                                                    "scale_to_text" : True,
                                                    "use_lazy_loading" : False},
                                  "field_type" : Tab_Button_Field})]
        if self.include_tab_delete_button:
            fields.append(("delete_tab", {"args" : (_object, ),
                                          "button_text" : 'x',
                                          "theme_profile" : "placeholder",
                                          "entry_kwargs" : {"theme_profile" : "placeholder",
                                                            "scale_to_text" : True}})
                         )
        # find the first row that is not full
        tabs_per_row = self.tabs_per_row
        for row in tab_bar.rows:
            if len(row.children) < tabs_per_row:
                break
        else: # there are no non-full rows
            row, _ = tab_bar.create_row()

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

    def delete_tab(self, _object):
        _object.delete()
        fields = [field for field in self.tab_bar.fields_list if
                  getattr(field, "args", False) and field.args[0] == _object]
        for field in fields: # will be delete button and tab button
            field.delete()   # delete would modify fields_list during iteration and cause bugs
        row = field.parent
        if not row.children:
            self.tab_bar.rows.remove(row)
            row.delete()

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
