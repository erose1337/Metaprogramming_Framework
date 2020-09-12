import copy

import pride.gui.form
import pride.gui.fields
from pride.components import Component, deep_update
from pride.gui.form import row_info, field_info

import sdl2

def add_field_to_row(_row_info, _field_info):
    return row_info(_row_info[0],
                    *(_row_info[1] + (_field_info, )),
                    **_row_info[2])

def tab_info(object_or_lazy_loaded, **kwargs):
    kwargs["field_type"] = "pride.gui.tabs.Tab_Button"
    needs_load = kwargs.setdefault("needs_load", True)
    if needs_load:
        _type, kwargs2 = object_or_lazy_loaded
        def create_object(window, _type=_type, kwargs2=kwargs2):
            return window.create(_type, **kwargs2)
        kwargs["args"] = (create_object, )
    else:
        kwargs["args"] = (object_or_lazy_loaded, )
    return field_info("select_tab", **kwargs)

def lazy_loaded(_type, **kwargs):
    return (_type, kwargs)


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
                              Component("pride.gui.tabs.New_Tab_Button_Entry")}


class Tab_Button_Entry(pride.gui.fields.Callable_Entry):

    def left_click(self, mouse):
        tab = self.parent_field
        tab_bar = tab.parent_form
        tabbed_window = tab_bar.parent
        if tab.needs_load:
            window_object = tab.args[0](tabbed_window.main_window)
            window_object.tab_reference = tab.reference
            tab.args = (window_object, )
            tab.selected = tab.needs_load = False
            window_object.hide()
        else:
            window_object = tab.args[0]
            if getattr(window_object, "tab_reference", None) is None:
                window_object.tab_reference = tab.reference
                tab.selected = False

        shift_is_held = sdl2.SDL_GetModState()
        if sdl2.KMOD_SHIFT & shift_is_held:
            self.parent_field.kwargs["mode"] = 1
        else:
            self.parent_field.kwargs["mode"] = 0
        super(Tab_Button_Entry, self).left_click(mouse)


class Tab_Button(pride.gui.fields.Callable_Field):

    defaults = {"include_delete_button" : False}
    subcomponents = {"entry" : Component("pride.gui.tabs.Tab_Button_Entry"),
                     "delete_button" :
                      Component("pride.gui.fields.Callable_Field",
                                name="delete", button_text='x',
                                location="right", theme_profile="placeholder",
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
        tab_bar.x_scroll_value = max(0, tab_bar.x_scroll_value - 1)
        window_object.delete()
        super(Tab_Button, self).delete()


class Tab_Bar(pride.gui.form.Form):

    defaults = {"include_new_tab_button" : True, "tab_info" : tuple(),
                "pack_mode" : "top", "h_range" : (0, .06), "max_tabs" : 9}
    mutable_defaults = {"open_tabs" : list, "tabs" : list}
    subcomponents = {"vertical_slider" : Component(location=None),
                     "horizontal_slider" :
                                     Component(location="bottom",
                                               h_range=(0, .0175)),
                     "new_tab_button" :
                          Component(field_type="pride.gui.tabs.New_Tab_Button",
                                    name="create_new_tab", button_text='+',
                                    location="right"),
                     "tab" : Component(field_type="pride.gui.tabs.Tab_Button",
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

        for _field_info in self.tab_info:
            self.add_field(_field_info)
        super(Tab_Bar, self).create_subcomponents()
        self.tabs = [field for field in self.rows[0].fields if
                     field.name == "select_tab"]
        self.x_scroll_value = max(0, len(self.tabs) - self.max_tabs)

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
        tab_kwargs["include_delete_button"] = True
        tab_kwargs["needs_load"] = False
        tab_field = field_info("select_tab", **tab_kwargs)
        self.add_field(tab_field)

        tab = self.create_field(tab_field, self.rows[0])
        tab.entry.theme_profile = "indicator"
        window_object.tab_reference = tab.reference
        self.open_tabs.append(tab)
        self.tabs.append(tab)

        if mode == 0:
            self.deselect_other_tabs(tab)

        self.x_scroll_value = max(0, len(self.tabs) - self.max_tabs)

    def handle_x_scroll(self, old, new):
        tabs = self.tabs
        max_tabs = self.max_tabs
        value = max(0, min(self.horizontal_slider.maximum, new))
        end = min(len(tabs), value + max_tabs)

        opened = []
        for tab in tabs[value:end + 1]:
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
            window_object.pack()
        self.pack()
        self.open_tabs.append(tab)

    def _deselect_tab(self, tab, window_object):
        tab.selected = False
        tab.entry.theme_profile = "interactive"
        if not window_object.hidden:
            window_object.hide()
        self.pack()
        self.parent.pack()
        self.open_tabs.remove(tab)

    def delete(self):
        del self.open_tabs
        del self.tabs
        super(Tab_Bar, self).delete()


class Tabbed_Window(pride.gui.form.Scrollable_Window):

    subcomponents = {"vertical_slider" : Component(location=None),
                     "horizontal_slider" : Component(location=None),
                     "tab_bar" : Component("pride.gui.tabs.Tab_Bar")}

    def create_subcomponents(self):
        super(Tabbed_Window, self).create_subcomponents()
        self.create_tab_bar()

    def create_tab_bar(self):
        self.tab_bar = self.create(self.tab_bar_type, **self.tab_bar_kwargs)

    @classmethod
    def from_tab_info(cls, *tab_infos, **kwargs):
        tab_bar_kwargs = kwargs.setdefault("tab_bar_kwargs", dict())
        tab_bar_kwargs.setdefault("tab_info", tuple())
        tab_bar_kwargs["tab_info"] += tab_infos
        def callable(cls=cls, _kwargs=kwargs, **kwargs2):
            deep_update(_kwargs, kwargs2)
            return cls(**_kwargs)
        return callable


def test_Tab_Bar():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable(x=52, y=52)]

    # there are 3 separate types of tabs:
    # - a tab associated with a pre-existing window object
    #       - tab_info(window_object, **tab_kwargs)
    # - a tab associated with a not-yet created window object
    #       - tab_info(lazy_loaded(type, **window_object_kwargs), **tab_kwargs)
    # - a new tab button that creates a given type of window
    #       - class ...(Tabbed_Window):
    #           subcomponents = {"tab_bar" : Component(new_window_type=type)}
    other = window.create("pride.gui.gui.Container", text="other space")
    other.hide()
    pre_existing = tab_info(other, button_text="Other tab", needs_load=False)

    lazily_loaded = tab_info(lazy_loaded("pride.gui.gui.Container",
                                         text="Test space"),
                             button_text="Test tab")

    # cannot pass instances in via subcomponents
    # values in subcomponents are deep copied
    # the following will not work ----------------------------------------------
    #class Test_Window(Tabbed_Window):
    #
    #    subcomponents = {"tab_bar" : Component(tab_info=(pre_existing,
    #                                                     lazily_loaded))}
    # --- end non working example ----------------------------------------------
    # use from_tab_info kwargs to customize subcomponents as necessary
    program = Tabbed_Window.from_tab_info(pre_existing, lazily_loaded)

    window.create(pride.gui.main.Gui, startup_programs=(program, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Tab_Bar()
