import copy

import pride.gui.form
import pride.gui.fields
from pride.components import Component
from pride.gui.form import row_info, field_info

import sdl2

def add_field_to_row(_row_info, _field_info):
    return row_info(_row_info[0],
                    *(_row_info[1] + (_field_info, )),
                    **_row_info[2])


class New_Tab_Button_Entry(pride.gui.fields.Callable_Entry):

    def left_click(self, mouse):
        shift_is_held = sdl2.SDL_GetModState()
        if sdl2.KMOD_SHIFT & shift_is_held:
            self.parent_field.kwargs["mode"] = 1
        else:
            self.parent_field.kwargs["mode"] = 0
        super(New_Tab_Button_Entry, self).left_click(mouse)


class New_Tab_Button(pride.gui.fields.Callable_Field):

    subcomponents = {"entry" :
                              Component("pride.gui.tabs2.New_Tab_Button_Entry")}


class Tab_Button_Entry(pride.gui.fields.Callable_Entry):

    def left_click(self, mouse):
        shift_is_held = sdl2.SDL_GetModState()
        if sdl2.KMOD_SHIFT & shift_is_held:
            self.parent_field.kwargs["mode"] = 1
        else:
            self.parent_field.kwargs["mode"] = 0
        super(Tab_Button_Entry, self).left_click(mouse)


class Tab_Button(pride.gui.fields.Callable_Field):

    defaults = {"include_delete_button" : True}
    subcomponents = {"entry" : Component("pride.gui.tabs2.Tab_Button_Entry"),
                     "delete_button" :
                      Component("pride.gui.fields.Callable_Field",
                                name="delete", button_text='x',
                                location="right",
                                entry_kwargs={"theme_profile" : "placeholder"})}

    def create_subcomponents(self):
        super(Tab_Button, self).create_subcomponents()
        if self.include_delete_button:
            self.create(self.delete_button_type, target_object=self,
                        **self.delete_button_kwargs)

    def delete(self):
        window_object = self.args[0]
        tab_bar = self.parent_form
        if self.selected:
            tab_bar._deselect_tab(self, window_object)
        tab_bar.tabs.remove(self)
        window_object.delete()
        super(Tab_Button, self).delete()


class Tab_Bar(pride.gui.form.Form):

    defaults = {"include_new_tab_button" : True, "tab_info" : tuple(),
                "pack_mode" : "top", "h_range" : (0, .075), "max_tabs" : 9}
    mutable_defaults = {"open_tabs" : list, "tabs" : list}
    subcomponents = {"vertical_slider" : Component(location=None),
                     "horizontal_slider" :
                                     Component(location="bottom"),
                     "new_tab_button" :
                          Component(field_type="pride.gui.tabs2.New_Tab_Button",
                                    name="create_new_tab", button_text='+',
                                    location="right"),
                     "tab" : Component(field_type="pride.gui.tabs2.Tab_Button",
                                       location="left",
                                       button_text="New Window"),
                     "new_window" : Component("pride.gui.gui.Container",
                                              location="bottom")}

    def create_subcomponents(self):
        try:
            row = self.layout[0][0]
        except KeyError:
            row = self.layout[0][0] = row_info(0)

        if self.include_new_tab_button:
            _field_info = field_info("create_new_tab",
                                     **self.new_tab_button_kwargs)
            self.add_field(_field_info)

        for _field_info, _object in self.tab_info:
            _field_info["args"] = (_object, )
            self.add_field(_field_info)
        super(Tab_Bar, self).create_subcomponents()

    def add_field(self, _field_info):
        _row_info = self.layout[0][0]
        self.layout[0][0] = add_field_to_row(_row_info, _field_info)

    def create_new_tab(self, mode=0):
        window = self.parent.main_window
        window_object = window.create(self.new_window_type,
                                      **self.new_window_kwargs)

        tab_kwargs = copy.deepcopy(self.tab_kwargs)
        tab_kwargs["args"] = (window_object, )
        tab_kwargs["selected"] = True
        tab_field = field_info("select_tab", **tab_kwargs)
        self.add_field(tab_field)

        tab = self.create_field(tab_field, self.rows[0])
        tab.entry.theme_profile = "indicator"
        window_object.tab_reference = tab.reference
        self.open_tabs.append(tab)
        self.tabs.append(tab)

        if mode == 0:
            self.deselect_other_tabs(tab)

        if len(self.tabs) > self.max_tabs:
            self.x_scroll_value += 1

    def handle_x_scroll(self, old, new):
        tabs = self.tabs
        max_tabs = self.max_tabs
        value = new
        end = min(len(tabs), value + max_tabs)

        opened = []
        for tab in tabs[value:end]:
            tab.show()
            tab.pack()
            opened.append(tab)
        for tab in (tab for tab in tabs if tab not in opened):
            tab.hide()

        self.synchronize_scroll_bars()

    def synchronize_scroll_bars(self):
        slider = self.horizontal_slider
        if slider is not None:
            slider.maximum = max(0, len(self.tabs) - self.max_tabs)
            slider.update_position_from_value()
            slider.entry.texture_invalid = True
            self.pack()

    def select_tab(self, window_object, mode=0):
        tab = pride.objects[window_object.tab_reference]
        tab.selected = not tab.selected
        if mode == 0:
            # open only the selected tab
            # hide all other open tabs
            self.deselect_other_tabs(tab)
        else:
            if mode != 1:
                raise ValueError("Invalid mode {} not in (0, 1)".format(mode))
            # open the selected tab in addition to others

        if tab.selected:
            self._select_tab(tab, window_object)
        else:
            self._deselect_tab(tab, window_object)

    def deselect_other_tabs(self, tab):
        for other_tab in self.open_tabs[:]: # open_tabs is modified in the loop
            if other_tab is tab or other_tab.name != "select_tab":
                continue
            self._deselect_tab(other_tab, other_tab.args[0])

    def _select_tab(self, tab, window_object):
        tab.selected = True
        tab.entry.theme_profile = "indicator"
        if window_object.hidden:
            window_object.show()
        self.pack()
        self.open_tabs.append(tab)

    def _deselect_tab(self, tab, window_object):
        tab.selected = False
        tab.entry.theme_profile = "interactive"
        if not window_object.hidden:
            window_object.hide()
        self.pack()
        self.open_tabs.remove(tab)

    def delete(self):
        del self.open_tabs
        del self.tabs
        super(Tab_Bar, self).delete()


class Tabbed_Window(pride.gui.form.Scrollable_Window):

    subcomponents = {"vertical_slider" : Component(location=None),
                     "horizontal_slider" : Component(location=None),
                     "tab_bar" : Component("pride.gui.tabs2.Tab_Bar")}

    def create_subcomponents(self):
        super(Tabbed_Window, self).create_subcomponents()
        self.create_tab_bar()

    def create_tab_bar(self):
        self.tab_bar = self.create(self.tab_bar_type, **self.tab_bar_kwargs)


def test_Tab_Bar():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable(x=52, y=52)]
    window.create(pride.gui.main.Gui, startup_programs=(Tabbed_Window, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Tab_Bar()
