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
import collections

import pride.gui.gui

import sdl2

class Balancer(object):

    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def get_balance(self):
        return self.balance

    def spend(self, amount):
        self.balance -= amount

    def earn(self, amount):
        self.balance += amount


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
    autoreferences = ("identifier", "displayer")
    allowed_values = {"orientation" : ("stacked", "side by side")}

    def _get_value(self):
        return getattr(self.target_object, self.name)
    def _set_value(self, value):
        if self.editable:
            if self.handle_value_changed(self.value, value):
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
        id_kwargs.setdefault("tip_bar_text", self.tip_bar_text)
        self.identifier = self.create(pride.gui.gui.Container, text=self.name,
                                      pack_mode=pack_mode, scale_to_text=scale_to_text,
                                      **id_kwargs)

    def create_entry(self, pack_mode):
        self.entry = self.create(self.entry_type, pack_mode=pack_mode, parent_field=self)

    def handle_value_changed(self, old_value, new_value):
        if old_value == new_value:
            return False
        balancer = self.balancer
        if balancer is not None:
            balance = self.balancer.get_balance()
            cost = self.compute_cost(old_value, new_value) # maybe self.cost_model.compute_cost instead ?

        if balancer is None or cost <= balance:
            self.alert("Value changing from {} to {}".format(old_value, new_value),
                        level=self.verbosity["handle_value_changed"])
            if balancer is not None:
                balancer.spend(cost)
                self.displayer.entry.texture_invalid = True
            return True
        else:
            return False

    def compute_cost(self, old_value, new_value):
        assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value)
        raise NotImplementedError()


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


class Integer_Entry(Text_Entry):

    def _get_text(self):
        return super(Integer_Entry, self)._get_text()
    def _set_text(self, value):
        if value and value[-1] == '-':
            value = value[:-1]
            sign = -1
        else:
            sign = 1
        try:
            int(value)
        except TypeError: # value can be None
            pass
        except ValueError: # have to remove any non-decimal-numeric characters
            value = ''.join(item for item in value if item in "0123456789")
            if not value:
                value = '0'

        value = value.lstrip('0')
        if not value: # remove leading zeros
            value = '0'
        if sign:
            value = str(sign * int(value))
        assert value
        super(Integer_Entry, self)._set_text(value)
    text = property(_get_text, _set_text)

    def increment_value(self, amount):
        parent_field = self.parent_field
        parent_field.value = int(parent_field.value or '0') + amount

    def decrement_value(self, amount):
        parent_field = self.parent_field
        parent_field.value = int(parent_field.value or '0') - amount


class Toggle_Entry(Entry):

    def left_click(self, mouse):
        parent_field = self.parent_field
        parent_field.value = not parent_field.value


class _Dropdown_Entry(Entry):

    defaults = {"pack_mode" : "bottom", "h_range" : (.05, 1.0)}
    predefaults = {"use_auto_direction" : True, "_pack_mode" : "top"}

    def _get_text(self):
        return str(self.value)
    def _set_text(self, value):
        super(_Dropdown_Entry, self)._set_text(value)
    text = property(_get_text, _set_text)

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

    def _get_text(self):
        return ''
    def _set_text(self, value):
        super(Dropdown_Entry, self)._set_text(value)
    text = property(_get_text, _set_text)

    def __init__(self, **kwargs):
        super(Dropdown_Entry, self).__init__(**kwargs)
        self.initialize_entries()

    def initialize_entries(self):
        assert not self._initialized_already
        self.entries = [self.create(self.entry_type, value=value) for value in self.parent_field.values]
        self.hide_menu(self.entries[0], _initialized_already=False)
        self._initialized_already = True

    def left_click(self, mouse):
        super(Dropdown_Entry, self).left_click(mouse)
        self.show_menu()

    def deselect(self, mouse, next_active_object):
        if pride.objects[next_active_object] not in self.entries:
            if self.menu_open:
                self.hide_menu(self.selected_entry)

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
            entry.texture_invalid = True

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

    #def handle_value_changed(self, old_value, new_value):
    #    self.alert("Value changed from {} to {}".format(old_value, new_value),
    #               level=self.verbosity["handle_value_changed"])
    #    do_change = False
    #    if self.balancer is not None:
    #        balance = self.balancer.get_balance()
    #        if balance is not None:
    #            cost = self.compute_cost(old_value, new_value)
    #            if cost <= balance:
    #                do_change = True
    #        else:
    #            do_change = True
    #    else:
    #        do_change = True
    #    return do_change

    def compute_cost(self, old_value, new_value):
        return 1


class Continuum(pride.gui.gui.Button):

    autoreferences = ("notch", "bar", "parent_field", "parent_entry")

    def __init__(self, **kwargs):
        super(Continuum, self).__init__(**kwargs)
        self.bar = bar = self.create(pride.gui.gui.Container, pack_mode="left",
                                     clickable=False)
        self.notch = bar.create(pride.gui.gui.Container, pack_mode="right",
                                w_range=(0, .025), clickable=False,
                                theme_profile="interactive")

    def handle_area_change(self, old_area):
        super(Continuum, self).handle_area_change(old_area)
        self.update_position_from_value()

    def update_position_from_value(self):
        parent_field = self.parent_field
        entry = parent_field.entry
        left = entry.left

        percent = float(parent_field.value) / parent_field.maximum
        width = (entry.w - left.w) - entry.right.w
        offset = int(width * percent)

        self.bar.w_range = (offset, offset)
        self.bar.pack()

    def left_click(self, mouse):
        # unpack data
        # evaluate contextual meaning of data (build more data from relations between present data)
        # compute value based on data
        # ensure value fits the expected constraints
        # respond to computed value
        parent_field = self.parent_field
        entry = parent_field.entry
        left = entry.left
        width = (entry.w - left.w) - entry.right.w

        offset = mouse.x - entry.x - left.w; offset = min(max(0, offset), width);
        percent = float(offset) / width; percent = max(0, min(1, percent));

        value = int(parent_field.maximum * percent)
        assert value <= parent_field.maximum
        assert value >= parent_field.minimum
        before = parent_field.value
        parent_field.value = value
        if parent_field.value != before: # insufficient balance can cause setting.value to fail
            self.bar.w_range = (int(percent * width), int(percent * width))
            self.bar.pack()

    def mousemotion(self, x, y, x_change, y_change):
        if self.held:
            self.left_click(self._mousetuple(x))

    def _mousetuple(self, x, f=collections.namedtuple("mouse", 'x')):
        return f(x)


class Endcap_Entry(Text_Entry):

    def left_click(self, mouse):
        super(Endcap_Entry, self).left_click(mouse)
        parent_field = self.parent_field
        slider_field = parent_field.target_object
        assert parent_field.name in ("minimum", "maximum")
        value = getattr(slider_field, parent_field.name)
        slider_field.value = value
        slider_field.update_position_from_value()


class Endcap(Text_Display):

    defaults = {"auto_create_id" : False, "w_range" : (0, .05),
                "entry_type" : Endcap_Entry}


class Slider_Entry(Entry):

    autoreferences = ("left", "continuum", "right")

    def __init__(self, **kwargs):
        super(Slider_Entry, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        parent_field = self.parent_field
        assert parent_field.minimum is not None and parent_field.maximum is not None
        self.left = self.create(Endcap, pack_mode="left", target_object=parent_field,
                                name="minimum")
        self.continuum = self.create(Continuum, pack_mode="left",
                                     parent_field=parent_field, parent_entry=self)
        self.right = self.create(Endcap, pack_mode="right", target_object=parent_field,
                                 name="maximum")


class Slider_Field(Field):

    defaults = {"entry_type" : Slider_Entry}

    def compute_cost(self, old_value, new_value):
        return new_value - old_value

    def update_position_from_value(self):
        self.entry.continuum.update_position_from_value()


class Form(pride.gui.gui.Window):

    defaults = {"fields" : tuple(), "spinbox_type" : Spinbox,
                "text_field_type" : Text_Field, "toggle_type" : Toggle,
                "dropdown_type" : Dropdown_Field, "target_object" : None,
                "balancer" : None, "include_balance_display" : True}
    autoreferences = ("displayer", )
    required_attributes = ("target_object", )

    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        balancer = self.balancer
        if balancer is not None and self.include_balance_display:
            displayer = self.create(Text_Display, name="balance",
                                    target_object=balancer, pack_mode="top",
                                    h_range=(.05, .1), orientation="side by side")
            displayer.editable = False
            self.displayer = displayer
        else:
            displayer = None
        spinbox = self.spinbox_type
        text_field = self.text_field_type
        toggle = self.toggle_type
        dropdown = self.dropdown_type
        empty_entries = {"balancer" : balancer, "displayer" : displayer}
        target_object = self.target_object
        for row in self.fields:
            container = self.create("pride.gui.gui.Container", pack_mode="top")
            for item in row:
                if isinstance(item, str):
                    name = item
                    entries = empty_entries
                elif len(item) == 1:
                    name = item[0]
                    entries = empty_entries
                else:
                    name, entries = item
                    entries.setdefault("balancer", balancer)
                    entries.setdefault("displayer", displayer)

                field_type = entries.pop("field_type", None)
                if field_type is None:
                    value = getattr(target_object, name)
                    if "minimum" in entries and "maximum" in entries: # check here before checking for int/float
                        field_type = Slider_Field
                    elif isinstance(value, bool): # must compare for bool before comparing for int; bool is a subclass of int
                        field_type = toggle
                    elif isinstance(value, int) or isinstance(value, float):
                        field_type = spinbox
                    elif isinstance(value, str):
                        field_type = text_field
                    elif "values" in entries:
                        field_type = dropdown
                assert field_type is not None
                assert "field_type" not in entries
                field = container.create(field_type, name=name,
                                         target_object=target_object,
                                         **entries)

    @classmethod
    def from_file(cls, filename):
        form_info = cefparser.parse_filename(filename)
        print form_info
        raise NotImplementedError()

    @classmethod
    def unit_test(cls):
        import pride.gui.main
        import pride.components.base
        window = pride.objects[pride.gui.enable()]

        _object = pride.components.base.Base(text='1', spinbox=2, toggle=True,
                                             slider=128,  dropdown=None)
        setattr(_object, "my text field", 'texcellent!') # can use spaces in field display name this way
        fields = [[                     "toggle"                              ],
                  [     "text",                       "my text field"         ],
                  [ "spinbox",    ("slider", {"minimum" : 0, "maximum" : 255})],
                  [("dropdown", {"values" : (None, 1, "test", 2.0, [True, ], #|   #| is just for appearance
                                             {"key" : "value pairs"})})       ]
                 ]

        balancer = Balancer(255, "Remaining Balance")
        form_callable = lambda *args, **kwargs:\
            Form(*args,
                 balancer=balancer,
                 fields=fields,
                 target_object=_object,
                 **kwargs)
        window.create(pride.gui.main.Gui, user=pride.objects["/User"],
                      startup_programs=(form_callable, ))
        #assert _object.dropdown == 0
        assert _object.text == '1'
        assert getattr(_object, "my text field") == "texcellent!"
        #assert _object.notaspinbox == '2', (_object.notaspinbox, type(_object.notaspinbox))
        assert _object.spinbox == 2
        assert _object.toggle == True

if __name__ == "__main__":
    Form.unit_test()
