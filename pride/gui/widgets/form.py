# Forms
# =====
#
# A *Form* has
# ------
# - a name
# - a sequence of *Fields*
#
# A Field has
# -------
# - a name
# - an initial value
# - optional extra entries as needed
#
#
# A template form:
#
# Form Name
# ====
#
# Field Name
# -----------
# - initial_value: None
# - entry1: value1
# - entry2: value2

import pride.gui.gui

import sdl2


class Entry(pride.gui.gui.Button):

    defaults = {"value" : None, "pack_mode" : "right"}
    predefaults = {"_value" : None}

    def _get_value(self):
        return self._value
    def _set_value(self, value):
        old_value = self._value
        self._value = value
        self.text = str(value)
        self.parent.handle_value_changed(old_value, value)
    value = property(_get_value, _set_value)


class Field(pride.gui.gui.Container):

    defaults = {"name" : '', "orientation" : "stacked", "entry_type" : Entry,
                "pack_mode" : "top"}
    predefaults = {"_value" : None}
    autoreferences = ("identifier", )
    allowed_values = {"orientation" : ("stacked", "side by side")}

    def _get_value(self):
        try:
            return self.entry.value
        except AttributeError:
            if hasattr(self, "entry"):
                raise
            return self._value
    def _set_value(self, value):
        try:
            self.entry.value = value
        except AttributeError:
            self._value = value
    value = property(_get_value, _set_value)

    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        self.create_id_and_entry()

    def create_id_and_entry(self):
        id_kwargs = dict()
        if self.orientation == "stacked":
            pack_mode = "top"
            scale_to_text = False
            id_kwargs["h_range"] = (0, .10)
        elif self.orientation == "side by side":
            pack_mode = "left"
            scale_to_text = True
        assert self.identifier is None
        self.identifier = self.create(pride.gui.gui.Container, text=self.name,
                                      pack_mode=pack_mode, scale_to_text=scale_to_text,
                                      **id_kwargs)
        self.entry = self.create(self.entry_type, value=self.value,
                                 pack_mode=pack_mode, tip_bar_text=self.tip_bar_text)

    def handle_value_changed(self, old_value, new_value):
        self.alert("Value changed from {} to {}".format(old_value, new_value),
                   level=self.verbosity["handle_value_changed"])
        #raise NotImplementedError()


class Text_Entry(Entry):

    defaults = {"h" : 16, "allow_text_edit" : False}

    def select(self, mouse):
        super(Text_Entry, self).select(mouse)
        self.alert("Turning text input on", level='vv')
        self.allow_text_edit = True
        sdl2.SDL_StartTextInput()

    def deselect(self, mouse, next_active_object):
        super(Text_Entry, self).deselect(mouse, next_active_object)
        self.alert("Disabling text input", level='vv')
        self.allow_text_edit = False
        sdl2.SDL_StopTextInput()


class Increment_Button(pride.gui.gui.Button):

    defaults = {"increment" : 1, "text" : '+'}
    autoreferences = ("target_entry", )

    def left_click(self, mouse):
        super(Increment_Button, self).left_click(mouse)
        self.target_entry.increment_value(self.increment)


class Decrement_Button(pride.gui.gui.Button):

    defaults = {"increment" : 1, "text" : '-'}
    autoreferences = ("target_entry", )

    def left_click(self, mouse):
        self.target_entry.decrement_value(self.increment)


class Integer_Entry(Entry):

    def _get_value(self):
        return int(super(Integer_Entry, self)._get_value())

    def __init__(self, **kwargs):
        super(Integer_Entry, self).__init__(**kwargs)
        container = self.create(pride.gui.gui.Container, pack_mode="right",
                                w_range=(0, .10))
        container.create(Increment_Button, target_entry=self, pack_mode="top")
        container.create(Decrement_Button, target_entry=self, pack_mode="top")

    def increment_value(self, amount):
        self.value += amount

    def decrement_value(self, amount):
        self.value -= amount


class Toggle_Entry(Entry):

    def left_click(self, mouse):
        self.value = not self.value


class _Dropdown_Entry(Entry):

    defaults = {"pack_mode" : "top", "h_range" : (.05, 1.0)}

    def left_click(self, mouse):
        super(_Dropdown_Entry, self).left_click(mouse)
        self.parent.toggle_menu(self)

    def deselect(self, mouse, next_active_object):
        self.parent.deselect(mouse, next_active_object)


class Dropdown_Entry(Entry):

    defaults = {"pack_mode" : "top", "menu_open" : False,
                "entry_type" : _Dropdown_Entry}

    def _get_value(self):
        return self._value
    def _set_value(self, value):
        old_value = self._value
        self._value = value
        self.text = ''
        self.parent.handle_value_changed(old_value, value)
    value = property(_get_value, _set_value)

    def __init__(self, **kwargs):
        super(Dropdown_Entry, self).__init__(**kwargs)
        self.entries = [self.create(self.entry_type, value=value) for value in self.value]
        self.hide_menu(self.entries[0])

    def left_click(self, mouse):
        super(Dropdown_Entry, self).left_click(mouse)
        self.show_menu()

    def deselect(self, mouse, next_active_object):
        if pride.objects[next_active_object] not in self.entries:
            if self.menu_open:
                for entry in self.entries:
                    entry.always_on_top = False
                    if entry.value != self.value:
                        entry.hide()
                    elif type(entry.value) != type(self.value):
                        entry.hide() # to prevent something like 1 == True from happening, where 1 and True are both entries
                self.menu_open = False
                self.pack()

    def toggle_menu(self, selected_entry):
        if not self.menu_open:
            self.show_menu()
        else:
            self.hide_menu(selected_entry)
        self.pack()

    def show_menu(self):
        self.menu_open = True
        for entry in self.entries:
            entry.always_on_top = True
            entry.show()
        self.pack()

    def hide_menu(self, selected_entry):
        self.menu_open = False
        for entry in self.entries:
            entry.always_on_top = False
            if entry != selected_entry:
                entry.hide()
            elif entry.hidden:
                entry.show()
        self.value = selected_entry.value
        self.pack()

    def handle_value_changed(self, old_value, value):
        pass


class Text_Field(Field):

    defaults = {"entry_type" : Text_Entry}


class Spinbox(Field):

    defaults = {"entry_type" : Integer_Entry}


class Toggle(Field):

    defaults = {"entry_type" : Toggle_Entry}


class Dropdown_Field(Field):

    defaults = {"entry_type" : Dropdown_Entry}


class Form(pride.gui.gui.Window):

    defaults = {"fields" : tuple(), "spinbox_type" : Spinbox,
                "text_field_type" : Text_Field, "toggle_type" : Toggle,
                "dropdown_type" : Dropdown_Field}

    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        spinbox = self.spinbox_type
        text_field = self.text_field_type
        toggle = self.toggle_type
        dropdown = self.dropdown_type
        for row in self.fields:
            container = self.create("pride.gui.gui.Container", pack_mode="top")
            for name, entries in row:
                value = entries["value"]
                if isinstance(value, bool): # must compare for bool before comparing for int; bool is a subclass of int
                    field_type = toggle
                elif isinstance(value, int) or isinstance(value, float):
                    field_type = spinbox
                elif isinstance(value, str):
                    field_type = text_field
                elif isinstance(value, tuple) or isinstance(value, list):
                    field_type = dropdown
                container.create(field_type, name=name, pack_mode="left", **entries)

    @classmethod
    def from_file(cls, filename):
        form_info = cefparser.parse_filename(filename)
        print form_info
        raise NotImplementedError()

    @classmethod
    def unit_test(cls):
        import pride.gui.main

        window = pride.objects[pride.gui.enable()]
        form_callable = lambda *args, **kwargs: Form(*args,
                                                fields=[[("Test1", {"value" : '1'}), ("Test1-b", {"value" : "Excellent"})],
                                                        [("Test4", {"value" : (0, 1, 2, False, 1.0, [1, 2, 3])}),
                                                         ("Test2", {"value" : 2}),
                                                         ("Test3", {"value" : True})]],
                                                **kwargs)
        window.create(pride.gui.main.Gui, user=pride.objects["/User"],
                      startup_programs=(form_callable, ))

if __name__ == "__main__":
    Form.unit_test()
