import pride.gui.gui
import pride.gui.widgetlibrary

class New_Tab_Button(pride.gui.widgetlibrary.Method_Button):

    defaults = {"pack_mode" : "left", "w_range" : (0, 40),
                "scale_to_text" : False}


class _Tab_Button(pride.gui.gui.Button):

    def left_click(self, mouse):
        self.parent.left_click(mouse)


class _Editable_Tab_Button(pride.gui.widgetlibrary.Text_Box):

    def left_click(self, mouse):
        super(_Editable_Tab_Button, self).left_click(mouse)
        self.parent.left_click(mouse)


class Tab_Button(pride.gui.gui.Button):

    defaults = {"pack_mode" : "left", "scale_to_text" : False,
                "include_delete_button" : True,
                "delete_tip" : "Close this window",
                "_tab_button_type" : _Tab_Button, "w_range" : (0, 200),
                "allow_text_edit" : True, "window_type" : None,
                "window" : None}
    predefaults = {"_editable" : False}
    autoreferences = ("delete_button", "indicator", "window")

    def _get_editable(self):
        return self._editable
    def _set_editable(self, value):
        if not value and self.allow_text_edit:
            self.allow_text_edit = False
            sdl2.SDL_StopTextInput()
        self._editable = value
    editable = property(_get_editable, _set_editable)

    def __init__(self, **kwargs):
        super(Tab_Button, self).__init__(**kwargs)
        if self.include_delete_button:
            kwargs = dict(pack_mode="right", scale_to_text=True,
                          target=self.reference, method="delete_tab", text='x',
                          theme_type="pride.gui.gui.Text_Only_Theme",
                          w_range=(0, 10), tip_bar_text=self.delete_tip,
                          theme_profile="placeholder")
            self.delete_button = self.create(pride.gui.widgetlibrary.Method_Button, **kwargs)
        indicator = self.create("pride.gui.widgetlibrary.Status_Indicator")
        self.indicator = indicator

    #def on_hover(self):
    #    super(Tab_Button, self).on_hover()
    #    if self.delete_button is not None:
    #        self.delete_button.theme_profile = "interactive"

    #def hover_ends(self):
    #    super(Tab_Button, self).hover_ends()
    #    if self.delete_button is not None:
    #        self.delete_button.theme_profile = "placeholder"

    def delete_tab(self):
        # delete the tab
        # delete the associated window
        # remove the tab from tab_bar.tabs
        # select the previous tab in tab_bar if possible
        tabs = self.parent.tabs
        tabs.remove(self)
        self.delete()
        self.window.delete()
        tabbed_window = self.parent.parent
        tabbed_window.window_listing.remove(self.window)
        try:
            tabbed_window.select_tab(tabs[-1])
        except IndexError:
            if tabs:
                raise

    def left_click(self, mouse):
        if self.window is None:
            self.window = self.parent.parent.initialize_window(self.window_type)
        self.parent.parent.select_tab(self)

    def select(self, mouse):
        super(Tab_Button, self).select(mouse)
        if self.editable:
            self.alert("Turning text input on", level='vv')
            self.allow_text_edit = True
            sdl2.SDL_StartTextInput()

    def deselect(self, mouse, next_active_object):
        super(Tab_Button, self).deselect(mouse, next_active_object)
        if self.editable:
            self.alert("Disabling text input", level='vv')
            self.allow_text_edit = False
            sdl2.SDL_StopTextInput()

    def handle_return(self):
        self.deselect(None, None)

    @classmethod
    def from_info(cls, **kwargs):
        def _callable(**_kwargs):
            _kwargs.update(kwargs)
            return cls(**_kwargs)
        return _callable


class Tab_Bar(pride.gui.gui.Container):

    defaults = {"h_range" : (0, 40), "pack_mode" : "top", "label" : '',
                "tab_type" : Tab_Button, "new_button_tip" : ''}
    mutable_defaults = {"tabs" : list}

    def __init__(self, **kwargs):
        super(Tab_Bar, self).__init__(**kwargs)
        self.initialize_tabs()

    def initialize_tabs(self):
        if self.label:
            self.create("pride.gui.gui.Container", text=self.label,
                        scale_to_text=True, pack_mode="left")
        self.create(New_Tab_Button, text='+', target=self.parent.reference,
                    method="new_tab", tip_bar_text=self.new_button_tip)

    def new_tab(self, **kwargs):
        tab = self.create(self.tab_type, **kwargs)
        self.tabs.append(tab)
        return tab


class Tab_Switcher_Bar(Tab_Bar):

    defaults = {"tab_types" : tuple()}

    def initialize_tabs(self):
        if self.label:
            self.create("pride.gui.gui.Container", text=self.label,
                        scale_to_text=True, pack_mode="left")
        for tab_type in self.tab_types:
            self.tab_type = tab_type
            self.new_tab(scale_to_text=False)


class Tab_Switching_Window(pride.gui.gui.Window):

    defaults = {"tab_bar_type" : Tab_Switcher_Bar, "tab_types" : tuple(),
                "tab_bar_label" : '', "window_types" : tuple()}
    autoreferences = ("tab_bar", )

    def __init__(self, **kwargs):
        super(Tab_Switching_Window, self).__init__(**kwargs)
        self.initialize_tabs_and_windows()

    def initialize_tabs_and_windows(self):
        self.tab_bar = self.create(self.tab_bar_type, label=self.tab_bar_label,
                                   tab_types=self.tab_types)
        self.create_windows()

    def create_windows(self):
        tabs = self.tab_bar.tabs
        for index, window_type in reversed(list(enumerate(self.window_types))):
            tab = tabs[index]
            tab.window_type = window_type
            if not index:
                tab.left_click(None)

    def initialize_window(self, window_type, **window_kwargs):
        window_kwargs = window_kwargs if window_kwargs is not None else dict()
        return self.create(window_type, **window_kwargs)

    def select_tab(self, selected_tab):
        for tab_reference in self.tab_bar.tabs:
            tab = tab_reference
            if tab_reference != selected_tab and tab.window is not None:
                tab.window.hide()
                tab.indicator.disable_indicator()
            elif tab.window is not None:
                window = tab.window
                if window.hidden:
                    window.show()
                indicator = tab.indicator
                indicator.enable_indicator()
        self.pack()


class Tabbed_Window(pride.gui.gui.Window):

    defaults = {"tab_bar_type" : Tab_Bar, "tab_type" : Tab_Button,
                "tab_bar_label" : '', "window_type" : "pride.gui.gui.Window",
                "new_button_tip" : ''}
    mutable_defaults = {"window_listing" : list}
    autoreferences = ("tab_bar", )

    def __init__(self, **kwargs):
        super(Tabbed_Window, self).__init__(**kwargs)
        self.initialize_tab_bar()

    def initialize_tab_bar(self):
        self.tab_bar = self.create(self.tab_bar_type, label=self.tab_bar_label,
                                   tab_type=self.tab_type,
                                   new_button_tip=self.new_button_tip)

    def new_tab(self, window_kwargs=None, tab_kwargs=None):
        tab_kwargs = tab_kwargs if tab_kwargs is not None else dict()
        window = self.initialize_window(self.window_type, **window_kwargs)
        tab_kwargs.setdefault("window", window)
        new_tab = self.tab_bar.new_tab(**tab_kwargs)
        window.tab = new_tab
        self.select_tab(new_tab)
        return (new_tab, window)

    def initialize_window(self, window_type, **window_kwargs):
        window_kwargs = window_kwargs if window_kwargs is not None else dict()
        window = self.create(self.window_type, **window_kwargs)
        self.window_listing.append(window)
        return window

    def select_tab(self, selected_tab):
        found = False
        for tab in self.tab_bar.tabs:
            if tab != selected_tab:
                tab.window.hide()
                tab.indicator.disable_indicator()
            else:
                if tab.window is None:
                    window = self.initialize_window(tab.window_type)
                window = tab.window
                if window.hidden:
                    window.show()
                indicator = tab.indicator
                indicator.enable_indicator()
                found = True
        assert found
        self.pack()
