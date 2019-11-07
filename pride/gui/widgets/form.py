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
                try:
                    value = str(getattr(parent_field.target_object, parent_field.name))
                except AttributeError:
                    if not hasattr(parent_field, "target_object"):
                        raise
                    value = str(parent_field.target_object[parent_field.name])
                super(Entry, self)._set_text(value)
        else:
            super(Entry, self)._set_text(value)
            self.text_initialized = True
    text = property(_get_text, _set_text)


class Field(pride.gui.gui.Container):

    defaults = {"name" : '', "orientation" : "stacked", "entry_type" : Entry,
                "pack_mode" : "top", "balancer" : None, "_value_initialized" : False,
                "editable" : True, "pack_mode" : "left", "auto_create_id" : True,
                "display_name" : '', "scale_to_text" : True}
    mutable_defaults = {"entry_kwargs" : dict}
    predefaults = {"target_object" : None}
    required_attributes = ("target_object", )
    autoreferences = ("identifier", "displayer", "parent_form")
    allowed_values = {"orientation" : ("stacked", "side by side")}

    def _get_value(self):
        try:
            return getattr(self.target_object, self.name)
        except AttributeError as exception:
            try:
                return self.target_object[self.name]
            except TypeError:
                raise exception
    def _set_value(self, value):
        if self.editable:
            old_value = self.value
            if self.handle_value_changed(old_value, value):
                try:
                    setattr(self.target_object, self.name, value)
                except AttributeError as exception:
                    assert hasattr(self, "target_object")
                    try: # duck typing might fail for mapping-like objects that don't restrict attribute assignment the way a dict does
                        self.target_object[self.name] = value
                    except TypeError:
                        raise exception
                self.entry.texture_invalid = True # updates text later
                parent_form = self.parent_form
                if parent_form is not None:
                    parent_form.handle_value_changed(self, old_value, value)
    value = property(_get_value, _set_value)

    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        self.create_id_and_entry()

    def create_id_and_entry(self):
        id_kwargs = dict()
        orientation = self.orientation
        if orientation == "stacked":
            pack_mode = "top"
            scale_to_text = False
            id_kwargs["h_range"] = (0, .05)
        else:
            assert orientation == "side by side"
            pack_mode = "left"
            scale_to_text = self.scale_to_text
        assert self.identifier is None
        if self.auto_create_id:
            self.create_id(pack_mode, scale_to_text, **id_kwargs)
        self.create_entry(pack_mode)

    def create_id(self, pack_mode, scale_to_text, **id_kwargs):
        id_kwargs.setdefault("tip_bar_text", self.tip_bar_text)
        self.identifier = self.create(pride.gui.gui.Container, pack_mode=pack_mode,
                                      text=self.display_name or self.name,
                                      scale_to_text=scale_to_text, **id_kwargs)

    def create_entry(self, pack_mode):
        kwargs = self.entry_kwargs
        kwargs.setdefault("pack_mode", pack_mode)
        self.entry = self.create(self.entry_type, parent_field=self, **kwargs)

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

    def delete(self):
        del self.entry_kwargs
        del self.target_object
        super(Field, self).delete()


class Text_Entry(Entry):

    defaults = {"h" : 16, "allow_text_edit" : False, "cursor_blink_rate" : 13,
                "cursor_symbol" : '_'}

    def select(self, mouse):
        super(Text_Entry, self).select(mouse)
        if self.parent_field.editable:
            self.alert("Turning text input on", level='vv')
            self.allow_text_edit = True
            sdl2.SDL_StartTextInput()
            if not self.draw_cursor:
                self.enable_cursor()

    def wait_and_disable(self):
        if self._counter == self.cursor_blink_rate:
            self.disable_cursor()
        else:
            self._counter += 1
            self.sdl_window.schedule_postdraw_operation(self.wait_and_disable, self)

    def wait_and_enable(self):
        if self._counter == self.cursor_blink_rate:
            if not self.draw_cursor:
                self.enable_cursor()
        else:
            self._counter += 1
            self.sdl_window.schedule_postdraw_operation(self.wait_and_enable, self)

    def enable_cursor(self):
        assert self.draw_cursor == False
        assert not self.deleted
        self.sdl_window.schedule_postdraw_operation(self.wait_and_disable, self)
        self.texture_invalid = self.draw_cursor = True
        self._counter = 0

    def disable_cursor(self, reenable=True):
        assert not self.deleted
        self.draw_cursor = False
        self.texture_invalid = True
        if reenable:
            self.sdl_window.schedule_postdraw_operation(self.wait_and_enable, self)
            self._counter = 0
        else:
            try:
                self.sdl_window.unschedule_postdraw_operation(self.wait_and_enable, self)
            except (KeyError, ValueError):
                pass
            try:
                self.sdl_window.unschedule_postdraw_operation(self.wait_and_disable, self)
            except (KeyError, ValueError):
                pass

    def deselect(self, mouse, next_active_object):
        super(Text_Entry, self).deselect(mouse, next_active_object)
        self.alert("Disabling text input", level='vv')
        self.allow_text_edit = False
        sdl2.SDL_StopTextInput()
        self.disable_cursor(False)


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
        super(Decrement_Button, self).left_click(mouse)
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


class Status_Light(pride.gui.gui.Container):

    defaults = {"pack_mode" : "top",
                "theme_profile" : "placeholder", "clickable" : False}

    def enable_indicator(self):
        self.theme_profile = "hover"

    def disable_indicator(self):
        self.theme_profile = "placeholder"


class Toggle_Entry(Entry):

    defaults = {"status_light_type" : Status_Light}
    mutable_defaults = {"indicator_kwargs" : dict}
    autoreferences = ("status_light", )

    def __init__(self, **kwargs):
        super(Toggle_Entry, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        self.status_light = self.create(self.status_light_type, **self.indicator_kwargs)
        if self.parent_field.value:
            self.status_light.enable_indicator()
        else:
            self.status_light.disable_indicator()

    def left_click(self, mouse):
        super(Toggle_Entry, self).left_click(mouse)
        parent_field = self.parent_field
        parent_field.value = not parent_field.value
        if parent_field.value:
            self.status_light.enable_indicator()
        else:
            self.status_light.disable_indicator()


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

    def delete(self):
        del self.entries[:]
        super(Dropdown_Entry, self).delete()

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
        try:
            setattr(parent_field.target_object, parent_field.name, selected_entry.value)
        except AttributeError as exception:
            if not (hasattr(parent_field, "target_object") and
                    hasattr(parent_field, "name") and
                    hasattr(selected_entry, "value")):
                raise
            try:
                parent_field.target_object[parent_field.name] = selected_entry.value
            except TypeError:
                raise exception
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
    mutable_defaults = {"entry_kwargs" : lambda: {"pack_mode" : "left"}}

    def create_entry(self, pack_mode):
        container = self.create(pride.gui.gui.Container, pack_mode=pack_mode)
        entry = self.entry = container.create(self.entry_type, parent_field=self,
                                              tip_bar_text=self.tip_bar_text,
                                               **self.entry_kwargs)
        if self.editable:
            subcontainer = container.create(pride.gui.gui.Container, pack_mode="left",
                                            w_range=(0, .05))
            subcontainer.create(Increment_Button, target_entry=entry, pack_mode="top")
            subcontainer.create(Decrement_Button, target_entry=entry, pack_mode="top")

    def handle_value_changed(self, old_value, new_value):
        return super(Spinbox, self).handle_value_changed(int(old_value), int(new_value))

    def compute_cost(self, old_value, new_value):
        return new_value - old_value


class Toggle(Field):

    defaults = {"entry_type" : Toggle_Entry}

    def compute_cost(self, old_value, new_value):
        assert type(old_value) == type(new_value), (type(old_value), type(new_value), old_value, new_value)
        # True - False == 1; False - True == -1;
        return new_value - old_value


class Dropdown_Field(Field):

    defaults = {"entry_type" : Dropdown_Entry, "orientation" : "side by side"}
    mutable_defaults = {"entry_kwargs" : lambda: {"scale_to_text" : False}}

    def compute_cost(self, old_value, new_value):
        return 1


class Continuum(pride.gui.gui.Button):

    autoreferences = ("notch", "bar", "parent_field", "parent_entry")

    def __init__(self, **kwargs):
        super(Continuum, self).__init__(**kwargs)
        if self.orientation == "side by side":
            bar_pack_mode = "left"
            notch_kwargs = {"pack_mode" : "right", "w_range" : (0, .025)}
            self._adjustment_target = "w_range"
        else:
            bar_pack_mode = "top"
            notch_kwargs = {"pack_mode" : "bottom", "h_range" : (0, .025)}
            self._adjustment_target = "h_range"
        self.bar = bar = self.create(pride.gui.gui.Container, pack_mode=bar_pack_mode,
                                     clickable=False)
        self.notch = bar.create(pride.gui.gui.Container, clickable=False,
                                theme_profile="interactive", **notch_kwargs)

    def update_position_from_value(self):
        if self._adjustment_target == "w_range":
            size = 'w'
        else:
            assert self._adjustment_target == "h_range"
            size = 'h'

        parent_field = self.parent_field
        entry = parent_field.entry
        left = entry.left

        percent = float(parent_field.value) / parent_field.maximum
        width = (getattr(entry, size) - getattr(left, size)) - getattr(entry.right, size)
        offset = int(width * percent)
        setattr(self.bar, "{}_range".format(size), (offset, offset))
        self.bar.pack()

    def left_click(self, mouse):
        super(Continuum, self).left_click(mouse)
        if self._adjustment_target == "w_range":
            coord = 'x'
            size = 'w'
        else:
            assert self._adjustment_target == "h_range"
            coord = 'y'
            size = 'h'
        # unpack data
        # evaluate contextual meaning of data (build more data from relations between present data)
        # compute value based on data
        # ensure value fits the expected constraints
        # respond to computed value
        parent_field = self.parent_field
        entry = parent_field.entry
        left = entry.left
        width = (getattr(entry, size) - getattr(left, size)) - getattr(entry.right, size)

        offset = getattr(mouse, coord) - getattr(entry, coord) - getattr(left, size)
        offset = min(max(0, offset), width)
        percent = float(offset) / width; percent = max(0, min(1, percent));

        value = int(parent_field.maximum * percent)
        assert value <= parent_field.maximum
        assert value >= parent_field.minimum
        before = parent_field.value
        parent_field.value = value
        if parent_field.value != before: # insufficient balance can cause setting.value to fail
            new_size = int(percent * width)
            bar = self.bar
            setattr(bar, "{}_range".format(size), (new_size, new_size))
            bar.pack()

    def mousemotion(self, x, y, x_change, y_change):
        if self.held:
            self.left_click(self._mousetuple(x, y))

    def _mousetuple(self, x, y, f=collections.namedtuple("mouse", ('x', 'y'))):
        return f(x, y)


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

    defaults = {"orientation" : "side by side", "include_incdec_buttons" : True,
                "include_minmax_buttons" : True}
    autoreferences = ("left", "continuum", "right")

    def __init__(self, **kwargs):
        super(Slider_Entry, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        parent_field = self.parent_field
        assert parent_field.minimum is not None and parent_field.maximum is not None

        orientation = self.orientation
        kwargs = dict()
        if orientation == "stacked":
            pack_mode = "top"
            kwargs["h_range"] = (0, .05)
        else:
            pack_mode = "left"
            kwargs["w_range"] = (0, .08)

        include_minmax = self.include_minmax_buttons
        include_incdec = self.include_incdec_buttons
        left = self.create(pride.gui.gui.Container, pack_mode=pack_mode, **kwargs)
        self.left = left
        if include_minmax:
            left.create(Endcap, pack_mode=pack_mode, name="minimum",
                        target_object=parent_field, **kwargs)
        if include_incdec:
            left.create(Callable_Field, name="decrement_value", pack_mode=pack_mode,
                        parent_field=parent_field, target_object=self,
                        button_text='-', **kwargs)
        self.continuum = self.create(Continuum, pack_mode=pack_mode,
                                     orientation=orientation, parent_entry=self,
                                     parent_field=parent_field)
        right = self.create(pride.gui.gui.Container, pack_mode=pack_mode, **kwargs)
        self.right = right
        if include_incdec:
            self.right.create(Callable_Field, name="increment_value", pack_mode=pack_mode,
                        parent_field=parent_field, target_object=self,
                        button_text='+', **kwargs)
        if include_minmax:
            right.create(Endcap, target_object=parent_field, pack_mode=pack_mode,
                        name="maximum", **kwargs)

    def increment_value(self):
        parent_field = self.parent_field
        parent_field.value = min(parent_field.value + 1, parent_field.maximum)
        parent_field.update_position_from_value()

    def decrement_value(self):
        parent_field = self.parent_field
        parent_field.value = max(parent_field.value - 1, parent_field.minimum)
        parent_field.update_position_from_value()


class Slider_Field(Field):

    defaults = {"entry_type" : Slider_Entry}
    predefaults = {"_minimum" : 0, "_maximum" : 0}

    def _get_minimum(self):
        return self._minimum
    def _set_minimum(self, value):
        self._minimum = value
        if self.minimum == self.maximum:
            self.hide()
        else:
            self.show()
    minimum = property(_get_minimum, _set_minimum)

    def _get_maximum(self):
        return self._maximum
    def _set_maximum(self, value):
        self._maximum = value
        if self.minimum == self.maximum:
            self.hide()
        else:
            self.show()
    maximum = property(_get_maximum, _set_maximum)

    def compute_cost(self, old_value, new_value):
        return new_value - old_value

    def handle_transition_animation_end(self):
        super(Slider_Field, self).handle_transition_animation_end()
        self.update_position_from_value()

    def update_position_from_value(self):
        self.entry.continuum.update_position_from_value()


class Callable_Entry(Entry):

    def _get_text(self):
        return self.parent_field.button_text
    def _set_text(self, value):
        try:
            value = self.parent_field.button_text
        except AttributeError:
            if not hasattr(self, "parent_field"):
                raise
        self.text_initialized = False
        super(Callable_Entry, self)._set_text(value)
        if self.parent_field is not None:
            self.parent_field.w_range = self.w_range
    text = property(_get_text, _set_text)

    def left_click(self, mouse):
        parent_field = self.parent_field
        parent_field.value(*parent_field.args, **parent_field.kwargs)


class Callable_Field(Field):

    defaults = {"entry_type" : Callable_Entry, "orientation" : "side by side",
                "auto_create_id" : False, "button_text" : '', "args" : tuple()}
    mutable_defaults = {"entry_kwargs" : lambda: {"scale_to_text" : True},
                        "kwargs" : dict}

    def delete(self):
        del self.kwargs
        super(Callable_Field, self).delete()


class Scrollable_Window(pride.gui.gui.Window):

    defaults = {"vertical_slider_position" : "right",
                "horizontal_slider_position" : "bottom"}
    predefaults = {"_x_scroll_value" : 0, "_y_scroll_value" : 0}
    autoreferences = ("main_window", "vertical_slider", "horizontal_slider")

    def _get_y_scroll_value(self):
        return self._y_scroll_value
    def _set_y_scroll_value(self, new_value):
        old_value = self._y_scroll_value
        self._y_scroll_value = new_value
        self.handle_y_scroll(old_value, new_value)
    y_scroll_value = property(_get_y_scroll_value, _set_y_scroll_value)

    def _get_x_scroll_value(self):
        return self._x_scroll_value
    def _set_x_scroll_value(self, new_value):
        old_value = self._x_scroll_value
        self._x_scroll_value = new_value
        self.handle_x_scroll(old_value, new_value)
    x_scroll_value = property(_get_x_scroll_value, _set_x_scroll_value)

    def __init__(self, **kwargs):
        super(Scrollable_Window, self).__init__(**kwargs)
        self.main_window = self.create("pride.gui.gui.Container", pack_mode="main")
        position = self.vertical_slider_position
        if position is not None:
            self.vertical_slider = \
            self.create("pride.gui.widgets.form.Slider_Field", pack_mode=position,
                        orientation="stacked", w_range=(0, .025), target_object=self,
                        name="y_scroll_value", minimum=0, maximum=0,
                        auto_create_id=False,
                        entry_kwargs={"orientation" : "stacked"})
        position = self.horizontal_slider_position
        if position is not None:
            self.horizontal_slider = \
            self.create("pride.gui.widgets.form.Slider_Field", pack_mode=position,
                        orientation="side by side", h_range=(0, .025), target_object=self,
                        auto_create_id=False,
                        name="x_scroll_value", minimum=0, maximum=0)

    def handle_x_scroll(self, old_value, new_value):
        pass

    def handle_y_scroll(self, old_value, new_value):
        pass


class Form(Scrollable_Window):

    _ = "pride.gui.widgets.form."
    defaults = {"fields" : tuple(), "spinbox_type" : _ + "Spinbox",
                "text_field_type" : _ + "Text_Field", "toggle_type" : _ + "Toggle",
                "dropdown_type" : _ + "Dropdown_Field", "row_h_range" : tuple(),
                "slider_type" : _ + "Slider_Field", "callable_type" : _  + "Callable_Field",
                "target_object" : None, "balancer" : None, "_page_number" : 0,
                "include_balance_display" : True, "max_rows" : 4,
                "form_name" : '', "include_delete_button" : False}
    mutable_defaults = {"_fields_dict" : dict, "rows" : list}
    autoreferences = ("displayer", )

    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        if self.form_name or self.include_delete_button:
            # form_name and include_delete_button being Falsey prevents further recursion
            field = []
            if self.form_name:
                field.append(("form_name", {"editable" : False,
                                            "auto_create_id" : False}))
            if self.include_delete_button:
                assert self.include_delete_button
                field.append(("handle_delete_button", {"button_text" : 'x',
                                                       "auto_create_id" : False,
                                                       "pack_mode" : "right"}))

            self.create(Form, h_range=(0, .05), pack_mode="top", fields=[field],
                        form_name='', include_delete_button=False, target_object=self)

        if self.target_object is None:
            self.target_object = self # can't use autoreferences because non-Base objects don't have a .reference attribute

        balancer = self.balancer
        if balancer is not None and self.include_balance_display:
            self.create_balance_display()

        empty_entries = {"balancer" : balancer, "displayer" : self.displayer}
        target_object = self.target_object
        row_h_range = self.row_h_range or (0, 1.0)
        _fields_dict = self._fields_dict
        window = self.main_window
        max_rows = self.max_rows
        rows = self.rows
        for row_number, row in enumerate(self.fields):
            assert row
            container = window.create("pride.gui.gui.Container", pack_mode="top",
                                      h_range=row_h_range)
            rows.append(container)
            for item in row:
                name, entries = self._unpack(item, empty_entries)
                field_type = self.determine_field_type(target_object, name, entries)
                entries.setdefault("target_object", target_object)
                field = container.create(field_type, name=name, parent_form=self,
                                         **entries)
                # target_object must be removed from entries (and consequently from fields)
                # continued presence in .fields is a hanging reference that prevents proper deletion
                del entries["target_object"]
                _fields_dict[name] = field
            if row_number >= max_rows:
                container.hide()
        #del self.fields
        self.vertical_slider.maximum = max(0, len(rows) - max_rows)

    def handle_y_scroll(self, old_value, new_value):
        super(Form, self).handle_y_scroll(old_value, new_value)
        max_rows = self.max_rows
        rows = self.rows
        row_count = len(rows)
        for row_number, row in enumerate(rows):
            if row_number >= new_value and row_number < (new_value + max_rows):
                if row.hidden:
                    row.show()
                    row.pack()
            else:
                if not row.hidden:
                    row.hide()
                    row.pack()

    def handle_delete_button(self):
        self.delete()

    def create_balance_display(self):
        displayer = self.main_window.create(Text_Display, name="balance",
                                            target_object=self.balancer, pack_mode="top",
                                            h_range=(.05, .1), orientation="side by side")
        displayer.editable = False
        self.displayer = displayer

    def _unpack(self, item, empty_entries):
        if isinstance(item, str):
            name = item
            entries = empty_entries
        elif len(item) == 1:
            name = item[0]
            entries = empty_entries
        else:
            name, entries = item
            entries.setdefault("balancer", self.balancer)
            entries.setdefault("displayer", self.displayer)
        return name, entries

    def determine_field_type(self, target_object, name, entries):
        field_type = entries.pop("field_type", None)
        if field_type is None:
            try:
                value = getattr(target_object, name)
            except AttributeError as exception:
                try:
                    value = target_object[name]
                except TypeError:
                    raise exception
            if "minimum" in entries and "maximum" in entries: # check here before checking for int/float
                field_type = self.slider_type
            elif isinstance(value, bool): # must compare for bool before comparing for int; bool is a subclass of int
                field_type = self.toggle_type
            elif isinstance(value, int) or isinstance(value, float):
                field_type = self.spinbox_type
            elif isinstance(value, str):
                field_type = self.text_field_type
            elif "values" in entries:
                field_type = self.dropdown_type
            elif hasattr(value, "__call__"):
                field_type = self.callable_type
        assert field_type is not None
        assert "field_type" not in entries
        return field_type

    def handle_value_changed(self, field, old_value, new_value):
        pass

    def delete(self):
        del self.target_object
        del self.rows
        del self.fields
        del self._fields_dict
        super(Form, self).delete()

    def update_text(self, field_name):
        self._fields_dict[field_name].entry.texture_invalid = True

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

        def callable():
            print("Callable!")

        _object = dict(text='1', spinbox=2, toggle=True,
                                             toggle2=False, toggle3=True, toggle4=False,
                                             slider=32,  dropdown=None, callable=callable)
        #setattr(_object, "my text field", 'texcellent!') # can use spaces in field display name this way
        _object["my text field"] = "texcellent!"
        fields = [[   "toggle",    "toggle2",    "toggle3",    "toggle4"      ],
                  [     "text",                       "my text field"         ],
                  [ "spinbox",    ("slider", {"minimum" : 0, "maximum" : 255})],
                  [("dropdown", {"values" : (None, 1, "test", 2.0, [True, ], #|   #| is just for appearance
                                             {"key" : "value pairs"})})       ],
                  [       ("callable", {"button_text" : "Press me!"})         ]
                 ]

        balancer = Balancer(255, "Remaining Balance")
        form_callable = lambda *args, **kwargs:\
            Form(*args, balancer=balancer, fields=fields, target_object=_object, **kwargs)
        window.create(pride.gui.main.Gui, user=pride.objects["/User"],
                      startup_programs=(form_callable, ))
        assert _object["text"] == '1'
        assert _object["spinbox"] == 2
        assert _object["toggle"] == True
        assert _object["slider"] == 32
        assert _object["dropdown"] == None
        #assert _object.dropdown == 0
        #assert _object.text == '1'
        #assert getattr(_object, "my text field") == "texcellent!"
        ##assert _object.notaspinbox == '2', (_object.notaspinbox, type(_object.notaspinbox))
        #assert _object.spinbox == 2
        #assert _object.toggle == True


if __name__ == "__main__":
    Form.unit_test()
