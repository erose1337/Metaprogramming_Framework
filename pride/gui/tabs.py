import operator # for itemgetter

import pride.gui.form
import pride.gui.fields
from pride.functions.utilities import slide
from pride.gui.form import layout, row_info, field_info


class Tab_Entry(pride.gui.fields.Callable_Entry):

    defaults = {"_end_hover_set_profile" : '', "_already_constructed" : False,
                "use_lazy_loading" : True, "_just_constructed" : False}

    def left_click(self, mouse):
        parent_field = self.parent_field
        if self.use_lazy_loading and not self._already_constructed:
            self.lazy_load_object()

        parent_field.value(self, *parent_field.args, **parent_field.kwargs)
        _object = self.parent_field.args[0]
        if _object.hidden:
            self._end_hover_set_profile = "interactive"
        else:
            self._end_hover_set_profile = "indicator"

    def lazy_load_object(self):
        parent_field = self.parent_field
        callable = parent_field.args[0]
        tab_ref = callable.tab_reference
        assert not self._already_constructed
        _object = callable()
        _object.tab_reference = tab_ref
        parent_field.args = (_object, ) + parent_field.args[1:]
        self._just_constructed = self._already_constructed = True

    def handle_return(self):
        parent_field = self.parent_field
        parent_field.value(self, *parent_field.args, **parent_field.kwargs)

    def hover_ends(self):
        super(Tab_Entry, self).hover_ends()
        new_profile = self._end_hover_set_profile
        if new_profile:
            self.theme_profile = new_profile
            self._end_hover_set_profile = ''


class Tab(pride.gui.fields.Callable_Field):

    defaults = {"entry_type" : Tab_Entry, "editable" : True,
                "include_delete_button" : True}
    subcomponents = {"tab_delete_button" :
                          {"type" : "pride.gui.fields.Callable_Field",
                           "button_text" : 'x',
                           "theme_profile" : "placeholder",
                           "name" : "delete_tab",
                           "entry_kwargs" : {"theme_profile" : "placeholder",
                                             "scale_to_text" : True}}}

    def create_subcomponents(self):
        super(Tab, self).create_subcomponents()
        if self.include_delete_button:
            tabbed_window = self.parent
            while not hasattr(tabbed_window, "delete_tab"):
                tabbed_window = tabbed_window.parent
            self.create("pride.gui.fields.Callable_Field",
                        target_object=tabbed_window, args=(self, ),
                        **self.tab_delete_button_kwargs)


class Tab_Bar(pride.gui.form.Form):

    interface = (("select_tab", ), ("select_tab", ))

    def select_tab(self, tab, _object):
        tabbed_window = self.target_object
        tabbed_window.select_tab(tab, _object)

    def add_field(self, _field_info, row):
        row_no = row.row_number
        _layout = self.layout
        _row_info = _layout[0][row_no]
        _layout[0][row_no] = row_info(row_no,
                                      *(_row_info[1] + (_field_info, )),
                                      **_row_info[2])
        return self.create_field(_field_info, row)

    def delete_field(self, field, row):
        row_no = row.row_number
        row_offset = row.fields.index(field)

        _layout = self.layout
        _row_info = _layout[0][row_no]
        _field_info = _row_info[1][row_offset]
        del _field_info[1]["target_object"]

        row.fields.remove(field)
        field.delete()

        _layout[0][row_no] = row_info(row_no,
                                      *(info for i, info in
                                        enumerate(_row_info[1]) if
                                        i != row_offset),
                                      **_row_info[2])

    def delete_row(self, row):
        row_no = row.row_number
        del self.rows[row.row_number]
        row.delete()
        del self.layout[0][row_no]
        if row_no == self.y_scroll_value:
            self.y_scroll_value = max(0, self.y_scroll_value - 1)
        self.synchronize_scroll_bars()

    def add_row(self, _row_info):
        row_no = _row_info[0]
        #assert row_no not in self.layout[0]
        self.layout[0][row_no] = _row_info
        return self.create_row(_row_info)


class Tabbed_Window(pride.gui.form.Scrollable_Window):

    defaults = {"include_new_tab_button" : True, "tab_targets" : tuple(),
                "new_window_type" : "pride.gui.gui.Container",
                "tab_bar_label" : '',
                "include_label" : False,
                "tabs_per_row" : 8,
                "top_bar_type" : "pride.gui.gui.Container",
                "new_tab_button_type" : "pride.gui.fields.Callable_Field"}
    autoreferences = ("tab_bar", "top_bar")
    interface = (("new_tab", ), ("new_tab", ))
    subcomponents = {"top_bar" : {"location" : "top",
                                        "h_range" : (0, .05)},
                           "tab_bar" : {"location" : "left",
                                        "entry_kwargs" : {"orientation" :
                                                                      "stacked",
                                                     "include_minmax_buttons" :
                                                                         False},
                                        "form_name" : '', "max_rows" : 1,
                                        "vertical_slider_kwargs" :
                                            {"include_minmax_buttons" : False}},
                           "new_tab_button" : {"location" : "left",
                                               "button_text" : '+',
                                               "name" : "new_tab",
                                               "entry_kwargs" :
                                                      {"scale_to_text" : False,
                                                       "w_range" : (0, .05)}},
                           "tab" : {"button_text" : "New Window",
                                    "theme_profile" : "placeholder",
                                    "field_type" : "Tab",
                                    "entry_kwargs" : {"scale_to_text" : True,
                                                  "use_lazy_loading" : True}},
                          "tab_bar_row" : dict()}

    def create_subcomponents(self):
        super(Tabbed_Window, self).create_subcomponents()
        self.create_topbar()

        if self.include_new_tab_button:
            self.create_new_tab_button()

        _layout = self.create_tab_layout()
        offset = 0
        if self.include_label:
            offset += 1
            self.create_tab_bar_label()
        self.create_tab_bar(_layout, offset)

    def create_topbar(self):
        kwargs = self.top_bar_kwargs
        self.top_bar = self.create(self.top_bar_type, **kwargs)

    def create_new_tab_button(self):
        self.top_bar.create(self.new_tab_button_type,
                            target_object=self, **self.new_tab_button_kwargs)

    def create_tab_layout(self):
        rows = []
        _kwargs = self.tab_kwargs
        tab_bar_row_kwargs = self.tab_bar_row_kwargs
        for row_no, row in enumerate(slide(self.tab_targets,
                                           self.tabs_per_row)):
            fields = []
            for _object in row:
                tab_kwargs = _kwargs.copy()
                tab_kwargs.setdefault("w_range", (0, 1.0 / self.tabs_per_row))
                tab_kwargs["args"] = (_object, )
                tab_kwargs.update(getattr(_object, "tab_kwargs", dict()))
                fields.append(field_info("select_tab", **tab_kwargs))

            rows.append(row_info(row_no, *fields,
                                 **tab_bar_row_kwargs))
        return layout(*rows)

    def create_tab_bar_label(self):
        _layout = layout(row_info(0,
                                  field_info("tab_bar_label",
                                             hoverable=False, editable=False,
                                             location="left",
                                             text=self.tab_bar_label,
                                             scale_to_text=True)))
        self.top_bar.create("pride.gui.form.Form", layout=_layout,
                            location="left")

    def create_tab_bar(self, _layout, offset):
        kwargs = self.tab_bar_kwargs
        kwargs["layout"] = _layout
        kwargs["target_object"] = self
        window = self.top_bar
        self.tab_bar = window.create(Tab_Bar, **kwargs)

        tabs = self.tab_bar.fields
        for tab_no, target in enumerate(self.tab_targets):
            target.tab_reference = tabs[tab_no].reference

        if self.tab_targets:
            first_tab = tabs[offset]
            try:
                self._set_color(first_tab.entry, self.tab_targets[0])
            except AttributeError:
                first_tab.entry.lazy_load_object()
                self._set_color(first_tab.entry, first_tab.args[0])
                first_tab.entry._just_constructed = False

        if not tabs:
            self.tab_bar.hide()

    def new_tab(self):
        tab_bar = self.tab_bar
        if tab_bar.hidden:
            tab_bar.show()
        _object = self.main_window.create(self.new_window_type,
                                          parent_form=tab_bar)
        kwargs = self.tab_kwargs.copy()
        kwargs["entry_kwargs"]["use_lazy_loading"] = False
        kwargs["target_object"] = self
        kwargs["args"] = (_object, )
        _field_info = field_info("select_tab", **kwargs)

        # find the first row that is not full
        tabs_per_row = self.tabs_per_row
        for row in sorted(tab_bar.rows.values()):
            if len(row.children) < tabs_per_row:
                break
        else: # there are no non-full rows
            row_no = len(tab_bar.rows)
            row_kwargs = self.tab_bar_row_kwargs.copy()
            _row_info = row_info(row_no, **row_kwargs)
            row = tab_bar.add_row(_row_info)

        field = tab_bar.add_field(_field_info, row)
        self._set_color(field.entry, field.args[0])

        _object.tab_reference = field.reference

        tab_bar.load_rows()
        tab_bar.synchronize_scroll_bars()

    def select_tab(self, tab, _object):
        #if not hasattr(_object, "hidden"):
        #    if tab.use_lazy_loading and not tab._already_constructed:
        #        tab.lazy_load_object()
        #        _object = tab.parent_field.args[0]

        if not tab._just_constructed:
            if _object.hidden:
                _object.show()
            else:
                _object.hide()
            _object.pack()
        else:
            tab._just_constructed = False
        self._set_color(tab, _object)
        #self.sdl_window.schedule_postdraw_operation(lambda: self._set_color(tab, _object), self)

    def _set_color(self, tab, _object):
        if _object.hidden:
            tab.theme_profile = "interactive"
        else:
            tab.theme_profile = "indicator"

    def delete_tab(self, tab):
        row = tab.parent
        tab_bar = self.tab_bar
        tab_bar.delete_field(tab, row)

        _object = tab.args[0]
        _object.delete()

        if not row.children:
            tab_bar.delete_row(row)

        if not tab_bar.fields:
            tab_bar.hide()

    def delete(self):
        super(Tabbed_Window, self).delete()
        del self.tab_targets


def test_Tabbed_Window():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable(x=52, y=52)]
    window.create(pride.gui.main.Gui, startup_programs=(Tabbed_Window, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Tabbed_Window()
