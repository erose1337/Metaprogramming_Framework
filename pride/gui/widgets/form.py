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

# Balanced Form
# =============
# A Balanced Form is a form that limits the range/selection of field values according to some cost function and an available balance.
# For example, in an RPG game, a character may have a given number of XP points. These points can be spent to increment stats.
# - The "balance" is the currently available XP
# - The cost function determines how much XP it takes to increment some stat
# - Balance is spent to increment some stat
# - Insufficient balance prevents the player from being able to increment stats
#
# Balanced Forms define their own cost function and behavior when an attempt is made to change a value.
# The default behavior is to simply dis-allow the change if the balance is insufficient, otherwise allow the change.

import pride.gui.gui

import sdl2


class Entry(pride.gui.gui.Button):

    defaults = {"pack_mode" : "right"}
    predefaults = {"parent_field" : None, "text_initialized" : False}
    autoreferences = ("parent_field", )

    def _get_text(self):
        return str(self.parent_field.value)
    def _set_text(self, value):
        if self.text_initialized:
            if self.allow_text_edit:
                # apparently there's no need to set actual .text attribute on the entry
                self.parent_field.value = value
            else:
                parent_field = self.parent_field
                super(Entry, self)._set_text(str(getattr(parent_field.target_object, parent_field.name)))
        else:
            super(Entry, self)._set_text(value)
            self.text_initialized = True
    text = property(_get_text, _set_text)


class Field(pride.gui.gui.Container):

    defaults = {"name" : '', "orientation" : "stacked", "entry_type" : Entry,
                "pack_mode" : "top", "balancer" : None, "_value_initialized" : False,
                "editable" : True, "pack_mode" : "left", "auto_create_id" : True}
    predefaults = {"target_object" : None}
    required_attributes = ("target_object", )
    autoreferences = ("identifier", )
    allowed_values = {"orientation" : ("stacked", "side by side")}

    def _get_value(self):
        return getattr(self.target_object, self.name)
    def _set_value(self, value):
        setattr(self.target_object, self.name, value)
        self.entry.texture_invalid = True # updates text later
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
        if self.auto_create_id:
            self.create_id(pack_mode, scale_to_text, **id_kwargs)
        self.create_entry(pack_mode)

    def create_id(self, pack_mode, scale_to_text, **id_kwargs):
        self.identifier = self.create(pride.gui.gui.Container, text=self.name,
                                      pack_mode=pack_mode, scale_to_text=scale_to_text,
                                      **id_kwargs)

    def create_entry(self, pack_mode):
        self.entry = self.create(self.entry_type,
                                 pack_mode=pack_mode, tip_bar_text=self.tip_bar_text,
                                 parent_field=self)

    def handle_value_changed(self, old_value, new_value):
        #assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value) # int changing to long would trigger this
        assert old_value != new_value
        balancer = self.balancer
        if balancer is not None:
            balance = self.balancer.get_balance()
            cost = self.compute_cost(old_value, new_value) # maybe self.cost_model.compute_cost instead ?
        else:
            balance = None
            cost = 0
        if balancer is None or balance is None or cost <= balancer.get_balance():
            self.alert("Value changing from {} to {} (initialized: {})".format(old_value, new_value, self._value_initialized),
                        level=self.verbosity["handle_value_changed"])
            if balancer is not None and balance is not None and self._value_initialized:
                balancer.spend(cost)
            self.assign_value(new_value)
            return True
        else:
            return False

    def assign_value(self, new_value):
        assert self.target_object is not None
        setattr(self.target_object, self.name, new_value)

    def compute_cost(self, old_value, new_value):
        assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value)
        raise NotImplementedError()


class Text_Entry(Entry):

    defaults = {"h" : 16, "allow_text_edit" : False}

    #def _get_text(self):
    #    return super(Text_Entry, self)._get_text()
    #def _set_text(self, value):
    #    if self.text_initialized:
    #        parent_field = self.parent_field
    #        setattr(parent_field.target_object, parent_field.name, value)
    #    else:
    #        self.first_set = True
    #    super(Text_Entry, self)._set_text(value)
    #text = property(_get_text, _set_text)

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


class Integer_Entry(Text_Entry):

    def _get_text(self):
        return super(Integer_Entry, self)._get_text()
    def _set_text(self, value):
        try:
            int(value)
        except TypeError: # value can be None
            pass
        except ValueError: # have to remove any non-decimal-numeric characters
            value = ''.join(item for item in value if item in "0123456789")
            if not value:
                value = '0'
        super(Integer_Entry, self)._set_text(value)
    text = property(_get_text, _set_text)

    def increment_value(self, amount):
        parent_field = self.parent_field
        target_object = parent_field.target_object
        attribute = parent_field.name
        value = getattr(target_object, attribute)
        setattr(target_object, attribute, value + amount)

    def decrement_value(self, amount):
        parent_field = self.parent_field
        target_object = parent_field.target_object
        attribute = parent_field.name
        value = getattr(target_object, attribute)
        setattr(target_object, attribute, value - amount)


class Toggle_Entry(Entry):

    def left_click(self, mouse):
        parent_field = self.parent_field
        parent_field.value = not parent_field.value


class _Dropdown_Entry(Entry):

    defaults = {"pack_mode" : "bottom", "h_range" : (.05, 1.0)}
    predefaults = {"use_auto_direction" : True, "_pack_mode" : "top"}

    def _get_pack_mode(self):
        return self._pack_mode
    def _set_pack_mode(self, value):
        if self.use_auto_direction:
            if (self.y + self.h) < self.sdl_window.h / 2:
                value = "bottom"
            else:
                value = "top"
        self._pack_mode = value
    pack_mode = property(_get_pack_mode, _set_pack_mode)

    def left_click(self, mouse):
        super(_Dropdown_Entry, self).left_click(mouse)
        self.parent.toggle_menu(self)

    def deselect(self, mouse, next_active_object):
        self.parent.deselect(mouse, next_active_object)


class Dropdown_Entry(Entry):

    defaults = {"pack_mode" : "top", "menu_open" : False,
                "entry_type" : _Dropdown_Entry, "_initialized_already" : False}

    def __init__(self, **kwargs):
        super(Dropdown_Entry, self).__init__(**kwargs)
        self.initialize_entries()

    def initialize_entries(self):
        assert not self._initialized_already
        self.entries = [self.create(self.entry_type, value=value) for value in self.value]
        self.hide_menu(self.entries[0], _initialized_already=False)
        self.text = ''
        self._initialized_already = True

    def left_click(self, mouse):
        super(Dropdown_Entry, self).left_click(mouse)
        self.show_menu()

    def deselect(self, mouse, next_active_object):
        if pride.objects[next_active_object] not in self.entries:
            if self.menu_open:
                self.hide_menu(self.selected_entry)
                #for entry in self.entries:
                #    entry.always_on_top = False
                #    if entry.value != self.value:
                #        entry.hide()
                #    elif type(entry.value) != type(self.value):
                #        entry.hide() # to prevent something like 1 == True from happening, where 1 and True are both entries
                #    else:
                #        entry.show()
                #self.menu_open = False
                #self.pack()

    def toggle_menu(self, selected_entry):
        if not self.menu_open:
            #assert hasattr(self, "entry")
            self.show_menu()
        else:
            self.hide_menu(selected_entry)
        self.pack()

    def show_menu(self):
        self.menu_open = True
        for entry in self.entries:
            entry.always_on_top = True
            entry.show()
            entry.texture_invalid = True
    #    self.pack() # Setting entry.texture_invalid seems to work better? (fixes a bug)

    def hide_menu(self, selected_entry, _initialized_already=True):
        self.menu_open = False
        for entry in self.entries:
            entry.always_on_top = False
            if entry is not selected_entry:
                entry.hide()
            elif entry.hidden:
                entry.show()

        parent_field = self.parent_field
        setattr(parent_field.target_object, parent_field.name, selected_entry.value)
        self.pack()
        self.selected_entry = selected_entry
        assert not selected_entry.hidden


class Text_Field(Field):

    defaults = {"entry_type" : Text_Entry}

    def compute_cost(self, old_value, new_value):
        assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value)
        old_value = len(old_value)
        new_value = len(new_value)
        return new_value - old_value


class Text_Display(Text_Field):

    defaults = {"editable" : False, "auto_create_id" : True}


class Spinbox(Field):

    defaults = {"entry_type" : Integer_Entry}

    def create_entry(self, pack_mode):
        container = self.create(pride.gui.gui.Container, pack_mode=pack_mode)
        subcontainer = container.create(pride.gui.gui.Container, pack_mode="right",
                                        w_range=(0, .05))
        entry = self.entry = container.create(self.entry_type,
                                              tip_bar_text=self.tip_bar_text,
                                              parent_field=self)
        subcontainer.create(Increment_Button, target_entry=entry, pack_mode="top")
        subcontainer.create(Decrement_Button, target_entry=entry, pack_mode="top")

    def handle_value_changed(self, old_value, new_value):
        return super(Spinbox, self).handle_value_changed(int(old_value), int(new_value))

    def assign_value(self, new_value):
        assert isinstance(new_value, int) or isinstance(new_value, long), (new_value, type(new_value))
        assert self.target_object is not None
        setattr(self.target_object, self.name, new_value)

    def compute_cost(self, old_value, new_value):
        #assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value) # int/long strike again
        return new_value - old_value


class Toggle(Field):

    defaults = {"entry_type" : Toggle_Entry}

    def compute_cost(self, old_value, new_value):
        assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value)
        # True - False == 1; False - True == -1;
        return new_value - old_value


class Dropdown_Field(Field):

    defaults = {"entry_type" : Dropdown_Entry, "orientation" : "side by side"}

    def handle_value_changed(self, old_value, new_value):
        self.alert("Value changed from {} to {}".format(old_value, new_value),
                   level=self.verbosity["handle_value_changed"])
        do_change = False
        if self.balancer is not None:
            balance = self.balancer.get_balance()
            if balance is not None:
                cost = self.compute_cost(old_value, new_value)
                if cost <= balance:
                    do_change = True
            else:
                do_change = True
        else:
            do_change = True
        if do_change:
            self.assign_value(new_value)

    def assign_value(self, new_value):
        assert self.target_object is not None
        setattr(self.target_object, self.name, new_value)

    def compute_cost(self, old_value, new_value):
        return 0


class Form(pride.gui.gui.Window):

    defaults = {"fields" : tuple(), "spinbox_type" : Spinbox,
                "text_field_type" : Text_Field, "toggle_type" : Toggle,
                "dropdown_type" : Dropdown_Field, "target_object" : None,
                "balance" : None, "balance_name" : "balance"}
    autoreferences = ("displayer", )

    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        if self.balance is not None:
            displayer = self.create(Text_Field, name=self.balance_name,
                                    target_object=self.balance, pack_mode="top",
                                    h_range=(.05, .1), orientation="side by side")
            displayer.editable = False
            self.displayer = displayer
        spinbox = self.spinbox_type
        text_field = self.text_field_type
        toggle = self.toggle_type
        dropdown = self.dropdown_type
        target_object = self.target_object
        for row in self.fields:
            container = self.create("pride.gui.gui.Container", pack_mode="top")
            for name, entries in row:
                field_type = entries.pop("field_type", None)
                value = getattr(target_object, name)
                if field_type is None:
                    if isinstance(value, bool): # must compare for bool before comparing for int; bool is a subclass of int
                        field_type = toggle
                    elif isinstance(value, int) or isinstance(value, float):
                        field_type = spinbox
                    elif isinstance(value, str):
                        field_type = text_field
                    elif isinstance(value, tuple) or isinstance(value, list):
                        field_type = dropdown

                entries.setdefault("balancer", self)
                assert field_type is not None
                assert "field_type" not in entries
                field = container.create(field_type, name=name,
                                         target_object=target_object,
                                         **entries)

    def get_balance(self):
        return self.balance

    def spend(self, amount):
        assert amount <= self.balance
        self.balance -= amount
        displayer = self.displayer
        if displayer is not None:
            backup = displayer.editable
            displayer.editable = True
            displayer.text = str(self.balance)
            displayer.editable = backup

    def earn(self, amount):
        assert amount >= 0
        self.balance += amount

    def display_balance(self, amount):
        displayer = self.displayer
        if displayer is not None:
            backup = displayer.editable
            displayer.editable = True
            displayer.text = str(self.balance)
            displayer.editable = backup

    @classmethod
    def from_file(cls, filename):
        form_info = cefparser.parse_filename(filename)
        print form_info
        raise NotImplementedError()

    @classmethod
    def unit_test(cls):
        import pride.gui.main
        import pride.components.base

        _object = pride.components.base.Base(text='1', text2='Excellent', spinbox=2,
                                             toggle=True)
        setattr(_object, "text box1", 'texcellent!'); setattr(_object, "text box2", '')
        balance = None#pride.components.base.Base(balance=10, name="Remaining Balance")
        window = pride.objects[pride.gui.enable()]
        fields = [[("toggle", dict())],
                  [("text box1", dict()), ("text box2", dict())]]
#        [#[("Dropdown", {"value" : (0, 1, 2, False, 1.0, [1, 2, 3])})],
#        [("text", dict()), ("text2", dict()),
#       #  ("NotASpinbox", {"field_type" : "pride.gui.widgets.form.Text_Field"}),
#         ("spinbox", dict()),
#         ("toggle", dict())]]

        form_callable = lambda *args, **kwargs:\
            Form(*args,
                 balance=balance,
                 fields=fields,
                 target_object=_object,
                 **kwargs)
        window.create(pride.gui.main.Gui, user=pride.objects["/User"],
                      startup_programs=(form_callable, ))
        #assert _object.dropdown == 0
        assert _object.text == '1'
        assert getattr(_object, "text2") == "Excellent"
        #assert _object.notaspinbox == '2', (_object.notaspinbox, type(_object.notaspinbox))
        assert _object.spinbox == 2
        assert _object.toggle == True

if __name__ == "__main__":
    Form.unit_test()
