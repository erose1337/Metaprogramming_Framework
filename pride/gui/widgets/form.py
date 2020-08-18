import operator
import collections

import pride.gui.gui

import sdl2

# key codes used for hotkeys
UP_ARROW = 1073741906
DOWN_ARROW = 1073741905
RIGHT_ARROW = 1073741903
LEFT_ARROW = 1073741904
DELETE_KEY = "\x7f"

def field_info(field_name, **kwargs):
    return (field_name, kwargs)

class Scrollable_Window(pride.gui.gui.Window):

    defaults = {"vertical_slider_position" : "right",
                "horizontal_slider_position" : "bottom",
                "main_window_type" : "pride.gui.gui.Container",
                "slider_type" : "pride.gui.widgets.form.Slider_Field"}
    predefaults = {"_x_scroll_value" : 0, "_y_scroll_value" : 0}
    autoreferences = ("main_window", "vertical_slider", "horizontal_slider")
    mutable_defaults = {"vertical_slider_entry_kwargs" : lambda: {"orientation" : "stacked"},
                        "horizontal_slider_entry_kwargs" : dict}

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
        self.main_window = self.create(self.main_window_type, location="main")
        position = self.vertical_slider_position
        if position is not None:
            self.vertical_slider = \
            self.create(self.slider_type, location=position,
                        orientation="stacked", w_range=(0, .025),
                        name="y_scroll_value", minimum=0, maximum=0,
                        auto_create_id=False, target_object=self,
                        entry_kwargs=self.vertical_slider_entry_kwargs)
        position = self.horizontal_slider_position
        if position is not None:
            self.horizontal_slider = \
            self.create(self.slider_type, location=position,
                        orientation="side by side", h_range=(0, .025),
                        auto_create_id=False, target_object=self,
                        name="x_scroll_value", minimum=0, maximum=0,
                        entry_kwargs=self.horizontal_slider_entry_kwargs,)

    def handle_x_scroll(self, old_value, new_value):
        pass

    def handle_y_scroll(self, old_value, new_value):
        pass


class Form(Scrollable_Window):

    _ = "pride.gui.widgets.form."
    defaults = {"fields" : tuple(), "spinbox_type" : _ + "Spinbox", "row_location" : "top",
                "text_field_type" : _ + "Text_Field", "toggle_type" : _ + "Toggle",
                "dropdown_type" : _ + "Dropdown_Field", "row_h_range" : tuple(),
                "slider_type" : _ + "Slider_Field", "callable_type" : _  + "Callable_Field",
                "read_only" : False, "max_rows" : 4,
                "form_name" : '', "include_delete_button" : False}
    mutable_defaults = {"fields_list" : dict, "rows" : collections.OrderedDict,
                        "target_object" : lambda: None,
                        "default_row_kwargs" : dict, # defaults for each new row
                        "row_kwargs" : dict} # row_number : row_kwargs pairs
    hotkeys = {("\t", None) : "handle_tab"}

    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        self.create_subcomponents()

    def synchronize_fields(self):
        assert not self.deleted
        for field in self.fields_list.itervalues():
            field.entry.texture_invalid = True

    def check_if_selected(self, child, child_entry):
        _selected = False
        if (not _selected) and getattr(child, "include_incdec_buttons", False): # Spinbox
            _selected = (child.inc_button._selected or  child.dec_button._selected)
        if (not _selected) and getattr(child_entry, "include_incdec_buttons", False): # Slider
            _selected = (child_entry.inc_button.entry._selected or
                         child_entry.dec_button.entry._selected)
        if (not _selected) and getattr(child_entry, "include_minmax_buttons", False): # Slider
            _selected = (child_entry.max_button.entry._selected or
                         child_entry.min_button.entry._selected)
        if (not _selected) and (child_entry._selected or child._selected or
            getattr(child_entry, "continuum", child)._selected): # Slider
            _selected = True
        if not _selected: # Dropdown
            _selected = any((entry._selected for entry in
                             getattr(child_entry, "entries", tuple())))
        if not _selected and hasattr(child_entry, "fields_list"):
            _selected = any(self.check_if_selected(item, item.entry) for item in
                            child_entry.fields_list.itervalues())
        return _selected

    def handle_tab(self):
        values = self.fields_list.values()
        length = len(values)
        for index, child in enumerate(values):
            child_entry = child.entry
            selected = self.check_if_selected(child, child_entry)
            if selected:
                # lazily load the next row if there is one
                if index + 1 == length and len(self.rows) < len(self.fields):
                    row_count = len(self.rows)
                    self.handle_y_scroll(row_count, row_count + 1)
                    field = self.rows[row_count].children[0]
                else:
                    index = (index + 1) % length
                    field = values[index]
                entry = field.entry
                if entry.hidden:
                    slider = self.vertical_slider
                    if slider is not None:
                        slider.value = (slider.value + 1) % (len(self.rows) + 1 - self.max_rows)
                self.sdl_window.user_input.select_active_item(entry)
                name = getattr(field, "button_text", '') or field.display_name or field.name
                self.show_status("Selected: {}".format(name))
                break
        else:
            field = values[0]
            name = getattr(field, "button_text", '') or field.display_name or field.name
            self.show_status("Selected: {}".format(name))
            self.sdl_window.user_input.select_active_item(field.entry)

    def create_subcomponents(self):
        if self.form_name or self.include_delete_button:
            self.create_top_display()

        if self.target_object is None:
            self.target_object = self # can't use autoreferences because non-Base objects don't have a .reference attribute

        target_object = self.target_object; max_rows = self.max_rows
        for row_number, row_info in enumerate(self.fields):
            if row_number >= max_rows: # lazy loading on the rest of the rows
                break
            else:
                row = self.create_row(row_number)
                self.create_fields(row_number, row_info, row, target_object)

        #self.sort_rows()
        self.synchronize_scroll_bars()

    def sort_rows(self):
        raise NotImplementedError()
        # must sort after creating rows
        # .children may happen to contain window objects other than the fields
        # e.g. the mouse click animation
        window = self.main_window
        window.children[:] = sorted((child for child in window.children if
                                     hasattr(child, "row_number")),
                                    key=operator.attrgetter("row_number")) +\
                             [child for child in window.children if not
                              hasattr(child, "row_number")]

    def synchronize_scroll_bars(self):
        slider = self.vertical_slider
        if slider is not None:
            #print("new maximum", len(self.fields), self.max_rows, len(self.fields) - self.max_rows)
            slider.maximum = max(0, len(self.fields) - self.max_rows)
            slider.update_position_from_value()
            self.pack()
        else:
            self.alert("No slider")

    def create_fields(self, row_number, row_info, row, target_object):
        row_start_index = sum(len(_row) for _row in self.fields[:row_number])
        for field_index, field_info in enumerate(row_info):
            field_no = (row_start_index + field_index)
            self.create_field(field_no, field_info, row, target_object)

    def create_row(self, row_number):
        """ Should call `sort_rows` after creating rows """
        try:
            kwargs = self.row_kwargs[row_number]
        except KeyError:
            kwargs = self.default_row_kwargs.copy()
        kwargs = dict((key, value) for key, value in kwargs.items())
        kwargs.setdefault("row_number", row_number)
        kwargs.setdefault("location", self.row_location)
        kwargs.setdefault("h_range", self.row_h_range or (0, 1.0))

        window = self.main_window
        row = window.create("pride.gui.gui.Container", **kwargs)
        self.rows[row_number] = row
        return row

    def create_field(self, field_no, field_info, row, target_object=None):
        empty_entries = dict()
        name, entries = self._unpack(field_info, empty_entries)
        _target_object = entries.setdefault("target_object", self.target_object)
        field_type = self.determine_field_type(_target_object, name, entries)
        if self.read_only:
            entries.setdefault("editable", False)
        field = row.create(field_type, name=name, parent_form=self, **entries)
        # target_object must be removed from entries (and consequently from fields)
        # continued presence in .fields is a hanging reference that prevents proper deletion
        del entries["target_object"]
        #entries.clear()
        self.fields_list[field_no] = field
        return field

    def create_top_display(self):
        assert self.form_name or self.include_delete_button
        field = []
        if self.form_name:
            field.append(("form_name", {"editable" : False, "clickable" : False,
                                        "auto_create_id" : False,
                                        "entry_kwargs" : {"theme_profile" : "default",
                                                          "tip_bar_text" : self.tip_bar_text,
                                                          "clickable" : False}
                                        }
                         ))
        if self.include_delete_button:
            assert self.include_delete_button
            field.append(("handle_delete_button", {"button_text" : 'x',
                                                   "auto_create_id" : False,
                                                   "location" : "right"}))

        # form_name and include_delete_button being Falsey prevents further recursion
        self.create(Form, h_range=(0, .05), location="top", fields=[field],
                    form_name='', include_delete_button=False, target_object=self)

    def handle_y_scroll(self, old_value, new_value):
        super(Form, self).handle_y_scroll(old_value, new_value)
        max_rows = self.max_rows
        new_value = min(new_value, len(self.fields) - max_rows)
        rows = self.rows
        row_count = len(rows)
        #if new_value > (row_count - self.max_rows):
            # lazy load the next row(s)
        end_row = min(len(self.fields), new_value + max_rows)
        for row_number in range(new_value, end_row):
            if row_number not in self.rows:
                row = self.create_row(row_number)
                row_info = self.fields[row_number]
                self.create_fields(row_number, row_info, row, self.target_object)
        #self.sort_rows()
        self.set_row_visibility(new_value)

    def set_row_visibility(self, new_row_no):
        print("Showing rows {} - {}".format(new_row_no, new_row_no + self.max_rows))
        for row_number, row in self.rows.items():
            if (row_number >= new_row_no and
                row_number < new_row_no + self.max_rows):
                if row.hidden:
                    row.show()
                    row.pack()
            else:
                if not row.hidden:
                    row.hide()
                    row.pack()

    def handle_delete_button(self):
        self.delete()

    def _unpack(self, item, empty_entries):
        if isinstance(item, str):
            name = item
            entries = empty_entries
        elif len(item) == 1:
            name = item[0]
            entries = empty_entries
        else:
            name, entries = item
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
            if hasattr(value, "field_type"):
                field_type = value.field_type
            elif "values" in entries: # check for dropdowns before checking value
                field_type = self.dropdown_type
            elif "minimum" in entries and "maximum" in entries: # check here before checking for int/float
                field_type = self.slider_type
            elif isinstance(value, bool): # must compare for bool before comparing for int; bool is a subclass of int
                field_type = self.toggle_type
            elif isinstance(value, int) or isinstance(value, float):
                field_type = self.spinbox_type
            elif isinstance(value, str):
                field_type = self.text_field_type
            elif hasattr(value, "__call__"):
                field_type = self.callable_type
            #elif isinstance(value, tuple) or isinstance(value, list):
            #    field_type = "pride.gui.widgets.formext.Tabbed_Form"
        if field_type is None:
            message = "Unable to determine field_type for {}"
            raise ValueError(message.format((target_object, name, value, entries)))
        assert "field_type" not in entries
        return field_type

    def handle_value_changed(self, field, old_value, new_value):
        pass

    def delete(self):
        del self.target_object
        del self.rows
        del self.fields
        del self.fields_list
        super(Form, self).delete()

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
                       toggle1=False, toggle2=True, toggle3=False,
                       slider=32,  dropdown=None, callable=callable)

        _object["my text field"] = "texcellent!"
        fields = [[   "toggle",    "toggle1",    "toggle2",    "toggle3"      ],
                  [     "text",                       "my text field"         ],
                  [ "spinbox",    ("slider", {"minimum" : 0, "maximum" : 255})],
                  [("dropdown", {"values" : (None, 1, "test", 2.0, [True, ], #|   #| is just for appearance
                                             {"key" : "value pairs"})})       ],
                  [       ("callable", {"button_text" : "Press me!"})         ]
                 ]

        form_callable = lambda *args, **kwargs:\
            Form(*args, fields=fields, target_object=_object, **kwargs)
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


class Entry(pride.gui.gui.Button):

    defaults = {"location" : "right", "confidential" : False,
                "show_status_when_selected" : True}
    predefaults = {"parent_field" : None, "text_initialized" : False}
    autoreferences = ("parent_field", )

    def _get_text(self):
        return str(self.parent_field.value)
    def _set_text(self, value):
        if self.text_initialized:
            if self.allow_text_edit:
                if isinstance(self, Integer_Entry):
                    self.parent_field.value = int(value)
                else:
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

    def select(self):
        super(Entry, self).select()
        if self.show_status_when_selected:
            field = self.parent_field
            name = field.tip_name or getattr(field, "button_text", '') or field.display_name or field.name
            self.show_status("Selected: {}".format(name))


class Field(pride.gui.gui.Container):

    defaults = {"name" : '', "orientation" : "stacked", "entry_type" : Entry,
                "_value_initialized" : False,
                "editable" : True, "location" : "left", "auto_create_id" : True,
                "display_name" : '', "tip_name" : ''}
    mutable_defaults = {"entry_kwargs" : dict, "id_kwargs" : dict}
    predefaults = {"target_object" : None}
    #required_attributes = ("target_object", ) # target_object could be a list that starts out empty
    autoreferences = ("identifier", "parent_form")
    allowed_values = {"orientation" : ("stacked", "side by side")}

    def _get_value(self):
        try:
            return getattr(self.target_object, self.name)
        except (TypeError, AttributeError) as exception:
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
                except (TypeError, AttributeError) as exception:
                    assert hasattr(self, "target_object")
                    try: # duck typing might fail for mapping-like objects that don't restrict attribute assignment the way a dict does
                        self.target_object[self.name] = value
                    except TypeError:
                        if hasattr(self, "target_object") and hasattr(self, "name"):
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
        id_kwargs = self.id_kwargs
        orientation = self.orientation
        if orientation == "stacked":
            location = "top"
            id_kwargs.setdefault("scale_to_text", False)
            id_kwargs.setdefault("h_range", (0, .05))
        else:
            assert orientation == "side by side"
            location = "left"
        assert self.identifier is None
        if self.auto_create_id:
            self.create_id(location, **id_kwargs)
        self.create_entry(location)

    def create_id(self, location, **id_kwargs):
        id_kwargs.setdefault("tip_bar_text", self.tip_bar_text)
        self.identifier = self.create(pride.gui.gui.Container, location=location,
                                      text=self.display_name or self.name,
                                      **id_kwargs)

    def create_entry(self, location):
        kwargs = self.entry_kwargs
        kwargs.setdefault("location", location)
        self.entry = self.create(self.entry_type, parent_field=self, **kwargs)

    def handle_value_changed(self, old_value, new_value):
        if old_value == new_value:
            return False
        self.alert("Value changing from {} to {}".format(old_value, new_value),
                    level=self.verbosity["handle_value_changed"])
        return True

    def delete(self):
        del self.entry_kwargs
        del self.target_object
        super(Field, self).delete()


class Callable_Entry(Entry):

    hotkeys = {('\n', None) : "handle_return"}

    def _get_text(self):
        return self.parent_field.button_text
    def _set_text(self, value):
        field = self.parent_field
        try:
            value = field.button_text
        except AttributeError:
            if not hasattr(self, "parent_field"):
                raise
        self.text_initialized = False
        super(Callable_Entry, self)._set_text(value)
        if field is not None:
            #backup = getattr(field, "_backup_w_range", None)
            #if backup is None:
            #    field._backup_w_range = self.w_range
            field.w_range = self.w_range
            field.pack()

    text = property(_get_text, _set_text)

    def handle_return(self):
        parent_field = self.parent_field
        parent_field.value(*parent_field.args, **parent_field.kwargs)

    def left_click(self, mouse):
        parent_field = self.parent_field
        parent_field.value(*parent_field.args, **parent_field.kwargs)


class Callable_Field(Field):

    defaults = {"entry_type" : Callable_Entry, "orientation" : "side by side",
                "auto_create_id" : False, "button_text" : '', "args" : tuple()}
    mutable_defaults = {"entry_kwargs" : lambda: {"scale_to_text" : True},
                        "kwargs" : dict}

    def create_entry(self, location):
        super(Callable_Field, self).create_entry(location)
        self.entry.text = self.entry.text # .text may not get set, if so then scale_to_text wont happen

    def delete(self):
        del self.kwargs
        super(Callable_Field, self).delete()


class Text_Entry(Entry):

    defaults = {"h" : 16, "allow_text_edit" : False, "cursor_blink_rate" : 13,
                "cursor_symbol" : '_', "_cursor_offset" : 0}
    hotkeys = {(LEFT_ARROW, None) : "handle_left_arrow",
               (RIGHT_ARROW, None) : "handle_right_arrow",
               ("\b", None) : "handle_backspace", (DELETE_KEY, None) : "handle_delete_key"}

    def handle_left_arrow(self):
        self._cursor_offset = min(self._cursor_offset + 1, len(self.text))
        self.keep_cursor_visible() # keeps cursor visible while moving cursor

    def handle_right_arrow(self):
        self._cursor_offset = max(0, self._cursor_offset - 1)
        self.keep_cursor_visible()

    def handle_backspace(self):
        if self.allow_text_edit:
            offset = self._cursor_offset
            if offset:
                self.text = self.text[:-offset - 1] + self.text[-offset:]
            else:
                self.text = self.text[:-1]
            self.keep_cursor_visible()

    def handle_delete_key(self):
        if self.allow_text_edit:
            offset = self._cursor_offset
            if offset:
                if offset == 1:
                    self.text = self.text[:-offset]
                else:
                    self.text = self.text[:-offset] + self.text[-(offset - 1):]
                self._cursor_offset = max(0, offset - 1)
            self.keep_cursor_visible()

    def text_entry(self, text):
        if self.allow_text_edit:
            offset = self._cursor_offset
            if offset:
                text = self.text[:-offset] + text + self.text[-offset:]
            else:
                text = self.text + text
            self.text = text
            self.keep_cursor_visible()

    def keep_cursor_visible(self):
        self.disable_cursor(False)
        self.enable_cursor()

    def select(self):
        super(Text_Entry, self).select()
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
            self.purge_blink_instructions()

    def purge_blink_instructions(self):
        try:
            self.sdl_window.unschedule_postdraw_operation(self.wait_and_enable, self)
        except (KeyError, ValueError):
            pass
        try:
            self.sdl_window.unschedule_postdraw_operation(self.wait_and_disable, self)
        except (KeyError, ValueError):
            pass

    def deselect(self, next_active_object):
        super(Text_Entry, self).deselect(next_active_object)
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

        field = self.parent_field
        if field is not None:
            _min, _max = field.minimum, field.maximum
            assert value is not None
            value = int(value)
            if _min is not None:
                value = max(_min, value)
            if _max is not None:
                value = min(_max, value)
            value = str(value)
        super(Integer_Entry, self)._set_text(value)
    text = property(_get_text, _set_text)

    def increment_value(self, amount):
        parent_field = self.parent_field
        _min, _max = parent_field.minimum, parent_field.maximum
        value = int(parent_field.value or '0') + amount
        if _max is not None:
            value = min(_max, value)
        if _min is not None:
            value = max(_min, value)
        parent_field.value = value

    def decrement_value(self, amount):
        self.increment_value(-amount)


class Status_Light(pride.gui.gui.Container):

    defaults = {"location" : "top",
                "theme_profile" : "placeholder", "clickable" : False}

    def enable_indicator(self):
        self.theme_profile = "indicator"

    def disable_indicator(self):
        self.theme_profile = "placeholder"


class Toggle_Entry(Entry):

    defaults = {"status_light_type" : Status_Light}
    mutable_defaults = {"indicator_kwargs" : dict}
    autoreferences = ("status_light", )
    hotkeys = {('\n', None) : "handle_return"}

    def __init__(self, **kwargs):
        super(Toggle_Entry, self).__init__(**kwargs)
        self.create_subcomponents()

    def handle_return(self):
        self._toggle()

    def create_subcomponents(self):
        self.status_light = self.create(self.status_light_type, **self.indicator_kwargs)
        if self.parent_field.value:
            self.status_light.enable_indicator()
        else:
            self.status_light.disable_indicator()

    def left_click(self, mouse):
        super(Toggle_Entry, self).left_click(mouse)
        self._toggle()

    def _toggle(self):
        parent_field = self.parent_field
        parent_field.value = not parent_field.value
        if parent_field.value:
            self.status_light.enable_indicator()
        else:
            self.status_light.disable_indicator()


class _Dropdown_Callable_Entry(Callable_Entry):

    def deselect(self, next_active_object):
        super(_Dropdown_Callable_Entry, self).deselect(next_active_object)
        dropdown_callable = self.parent_field
        dropdown_entry = dropdown_callable.parent_form
        dropdown_field = dropdown_entry.parent_field
        if not pride.functions.utilities.isdescendant(next_active_object, dropdown_entry):
            if dropdown_field.menu_open:
                dropdown_field.close_menu(dropdown_field.value)


class _Dropdown_Callable(Callable_Field):

    defaults = {"entry_type" : _Dropdown_Callable_Entry}


class Dropdown_Entry(Form):

    defaults = {"callable_type" : _Dropdown_Callable}
    required_attributes = ("fields", )
    hotkeys = {(UP_ARROW, None) : "handle_up_arrow",
               (DOWN_ARROW, None) : "handle_down_arrow",
               ('\t', None) : None} # tab will cycle through dropdown options if this is not done
                                    # and it will cause tabbing to return back to the default field

    def handle_up_arrow(self):
        parent_field = self.parent_field
        rows = self.rows
        for index, row in rows.items():
            if not row.hidden:
                index = max(index - 1, 0)
                if index not in rows:
                    self.handle_y_scroll(index, index)
                parent_field.close_menu(self.fields_list[index].args[0])
                break

    def handle_down_arrow(self):
        parent_field = self.parent_field
        rows = self.rows
        end_row = len(self.fields) - 1
        for index, row in rows.items():
            if not row.hidden:
                index = min(index + 1, end_row)
                if index not in rows:
                    self.handle_y_scroll(index, index)
                parent_field.close_menu(self.fields_list[index].args[0])
                break


class Text_Field(Field):

    defaults = {"entry_type" : Text_Entry}


class Text_Display(Text_Field):

    defaults = {"editable" : False, "auto_create_id" : True}


class Spinbox(Field):

    defaults = {"entry_type" : Integer_Entry, "include_incdec_buttons" : False,
                "minimum" : None, "maximum" : None}
                # can only use either minimum or maximum but not both by default
                # must specify Spinbox type explicitly if min and max are used.
    mutable_defaults = {"entry_kwargs" : lambda: {"location" : "left"}}
    allowed_values = {"include_incdec_buttons" : (False, )} # not actually part of the interface

    def create_entry(self, location):
        container = self.create(pride.gui.gui.Container, location=location)
        entry = self.entry = container.create(self.entry_type, parent_field=self,
                                              tip_bar_text=self.tip_bar_text,
                                               **self.entry_kwargs)
        if self.editable:
            subcontainer = container.create(pride.gui.gui.Container, location="left",
                                            w_range=(0, .05))
            kwargs = {"target_entry" : entry, "location" : "top"}
            self.inc_button = subcontainer.create(Increment_Button, **kwargs)
            assert kwargs == {"target_entry" : entry, "location" : "top"}
            self.dec_button = subcontainer.create(Decrement_Button, **kwargs)
            self.include_incdec_buttons = True # this is used by Form tab selection feature

    def handle_value_changed(self, old_value, new_value):
        return super(Spinbox, self).handle_value_changed(int(old_value), int(new_value))


class Toggle(Field):

    defaults = {"entry_type" : Toggle_Entry}


class Dropdown_Field(Field):

    defaults = {"entry_type" : Dropdown_Entry, "orientation" : "side by side",
                "menu_open" : True, "values" : tuple(),
                "_backup_h_range" : None}
    mutable_defaults = {"entry_kwargs" : lambda: {"scale_to_text" : False}}
    required_attributes = ("values", )

    def create_entry(self, location):
        kwargs = self.entry_kwargs
        kwargs.setdefault("parent_field", self)
        if "fields" not in kwargs:
            kwargs.setdefault("location", location)
            #kwargs.setdefault("row_h_range", (32, 1.0))
            #kwargs.setdefault("max_rows", 8)
            # open towards the direction that has more room
            if (self.y + self.h) < self.sdl_window.h / 2:
                kwargs["row_location"] = "top"
            else:
                kwargs["row_location"] = "bottom"

            new_entry = lambda value: ("select_entry", {"button_text" : str(value),
                                                        "args" : (value, ),
                                                        "entry_kwargs" : {"scale_to_text" : False}})
            kwargs.setdefault("fields", [[new_entry(value)] for value in self.values])

        self.entry = self.create(self.entry_type, target_object=self, **kwargs)
        self.select_entry(self.values[0])

    def toggle_menu(self):
        if self.menu_open:
            self.close_menu()
        else:
            self.open_menu(None)

    def close_menu(self, value):
        entry = self.entry
        rows = entry.rows
        for row in rows.values():
            field = row.children[0]
            field.entry.always_on_top = False
            if field.args[0] is not value:
                row.hide()
            else:
                row.show()
                row.pack()
        entry.vertical_slider.maximum = 0
        entry.vertical_slider.pack()
        self.menu_open = False
        self.value = value
        if self._backup_h_range is not None:
            self.h_range = self._backup_h_range
            self._backup_h_range = None
            self.pack()

    def open_menu(self, selected_value):
        entry = self.entry
        max_rows = entry.max_rows
        rows = entry.rows
        for end, _row in rows.items():
            if _row.children[0].args[0] is selected_value:
                break
        else:
            end = max_rows
        end = max(max_rows, end + 1)
        beginning = max(0, end - max_rows)

        row_items = rows.items()
        for row_no, row in row_items:
            if row_no < beginning or row_no > end:
                row.children[0].entry.always_on_top = False
                row.hide()
            else:
                row.children[0].entry.always_on_top = True
                row.show()

        self.menu_open = True
        entry.vertical_slider.maximum = max(0, len(entry.fields) - max_rows)
        entry.vertical_slider.pack()

        self._backup_h_range = self.h_range
        self.h_range = ((end - beginning) * row.h_range[0],
                        self.h_range[1])
        self.pack()

    def select_entry(self, value):
        if not self.menu_open:
            self.open_menu(value)
        else:
            self.close_menu(value)


class Continuum(pride.gui.gui.Button):

    autoreferences = ("notch", "bar", "parent_field", "parent_entry")

    def __init__(self, **kwargs):
        super(Continuum, self).__init__(**kwargs)
        if self.orientation == "side by side":
            bar_location = "left"
            notch_kwargs = {"location" : "right", "w_range" : (0, .025)}
            self._adjustment_target = "w_range"
        else:
            bar_location = "top"
            notch_kwargs = {"location" : "bottom", "h_range" : (0, .025)}
            self._adjustment_target = "h_range"
        self.bar = bar = self.create(pride.gui.gui.Container, location=bar_location,
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
        left = entry.left; right = entry.right
        value = parent_field.value

        if left is None:
            left_size = 0
        else:
            left_size = getattr(left, size)
        if right is None:
            right_size = 0
        else:
            right_size = getattr(right,size)
        maximum = parent_field.maximum; minimum = parent_field.minimum
        width = (getattr(entry, size) - left_size) - right_size
        if value == maximum:
            new_size = width
        elif value == minimum:
            new_size = 0
        else:
            bucket_width = width / (float(maximum - minimum) + 1)
            new_size = int(bucket_width * parent_field.value)
        setattr(self.bar, "{}_range".format(size), (new_size, new_size))
        self.bar.pack()

    def left_click(self, mouse):
        super(Continuum, self).left_click(mouse)
        if not self.parent_field.editable:
            return
        # partition available space into n buckets
        # make notch w equal to bucket_width in size
        # find which bucket was clicked and assign that value
        # set width of bar to bucket_width * bucket_number
        #   aligns right edge of notch to right edge of selected bucket
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
        parent_field = self.parent_field; entry = parent_field.entry;
        left = entry.left; right = entry.right
        if left is None:
            left_size = 0
        else:
            left_size = getattr(left, size)
        if right is None:
            right_size = 0
        else:
            right_size = getattr(right, size)
        width = (getattr(entry, size) - left_size) - right_size
        maximum = parent_field.maximum; minimum = parent_field.minimum
        buckets = (maximum - minimum) + 1 # + 1 because minimum is a selectable choice (e.g. max = 1, min = 0)
        bucket_width = width / float(buckets)
        offset = getattr(mouse, coord) - getattr(entry, coord) - left_size
        value = max(min(int(offset / bucket_width), maximum), minimum)
        assert minimum <= value <= maximum
        before = parent_field.value
        parent_field.value = value

        if value == maximum:
            new_size = width
        elif value == minimum:
            new_size = 0
        else:
            new_size = int(bucket_width * value)
        bar = self.bar
        setattr(bar, "{}_range".format(size), (new_size, new_size))
        bar.pack()

    def mousemotion(self, x, y, x_change, y_change, mouse):
        if self.held:
            self.left_click(self._mousetuple(x, y))

    def _mousetuple(self, x, y, f=collections.namedtuple("mouse", ('x', 'y'))):
        return f(x, y)


class Endcap_Entry(Text_Entry):

    defaults = {"show_status_when_selected" : False}

    def left_click(self, mouse):
        super(Endcap_Entry, self).left_click(mouse)
        parent_field = self.parent_field
        slider_field = parent_field.target_object
        assert parent_field.name in ("minimum", "maximum")
        value = getattr(slider_field, parent_field.name)
        slider_field.value = value
        slider_field.update_position_from_value()


class Endcap(Text_Display):

    defaults = {"auto_create_id" : False, "entry_type" : Endcap_Entry}


class Slider_Entry(Entry):

    defaults = {"orientation" : "side by side", "include_incdec_buttons" : True,
                "include_minmax_buttons" : True, "hide_text" : False}
    autoreferences = ("left", "continuum", "right", "max_button", "min_button",
                      "inc_button", "dec_button")
    hotkeys = {(UP_ARROW, None) : "handle_up_arrow",
               (DOWN_ARROW, None) : "handle_down_arrow",
               (LEFT_ARROW, None) : "handle_left_arrow",
               (RIGHT_ARROW, None) : "handle_right_arrow"}

    def _get_text(self):
        if self.hide_text:
            #super(Slider_Entry, self)._get_text()
            return ''
        else:
            return super(Slider_Entry, self)._get_text()
    def _set_text(self, value):
        super(Slider_Entry, self)._set_text(value)
    text = property(_get_text, _set_text)

    def __init__(self, **kwargs):
        super(Slider_Entry, self).__init__(**kwargs)
        self.create_subcomponents()

    def handle_left_arrow(self):
        if self.orientation == "side by side":
            self.decrement_value()

    def handle_right_arrow(self):
        if self.orientation == "side by side":
            self.increment_value()

    def handle_up_arrow(self):
        if self.orientation == "stacked":
            self.decrement_value()

    def handle_down_arrow(self):
        if self.orientation == "stacked":
            self.increment_value()

    def create_subcomponents(self):
        parent_field = self.parent_field
        assert parent_field.minimum is not None and parent_field.maximum is not None

        orientation = self.orientation
        kwargs = dict()
        if orientation == "stacked":
            location = "top"
            kwargs["h_range"] = (0, .05)
            kwargs["entry_kwargs"] = {"scale_to_text" : False}
        else:
            location = "left"
            kwargs["w_range"] = (0, .08)
        if self.parent_field.editable:
            kwargs["show_status_when_selected"] = False

            include_minmax = self.include_minmax_buttons
            include_incdec = self.include_incdec_buttons
            if include_minmax and include_incdec:
                left = self.create(pride.gui.gui.Container, location=location, **kwargs)
                self.left = left
            else:
                left = None

            if include_minmax:
                if left is not None:
                    self.min_button = left.create(Endcap, location=location, name="minimum",
                                                target_object=parent_field, **kwargs)
                else:
                    self.min_button = self.left = self.create(Endcap, location=location, name="minimum",
                                                            target_object=parent_field, **kwargs)
            if include_incdec:
                if left is not None:
                    self.dec_button = left.create(Callable_Field,
                                                name="decrement_value",
                                                location=location,
                                                parent_field=parent_field,
                                                target_object=self,
                                                button_text='-', **kwargs)
                else:
                    self.dec_button = self.left =\
                    self.create(Callable_Field, name="decrement_value",
                                location=location, parent_field=parent_field,
                                target_object=self, button_text='-', **kwargs)

        self.continuum = self.create(Continuum, location=location,
                                     orientation=orientation, parent_entry=self,
                                     parent_field=parent_field)
        if self.parent_field.editable:
            if include_minmax and include_incdec:
                right = self.create(pride.gui.gui.Container, location=location,
                                    **kwargs)
                self.right = right
            else:
                right = None

            if include_incdec:
                if right is not None:
                    self.inc_button = self.right.create(Callable_Field,
                                                        name="increment_value",
                                                        location=location,
                                                        parent_field=parent_field,
                                                        target_object=self,
                                                        button_text='+', **kwargs)
                else:
                    self.inc_button = self.right =\
                    self.create(Callable_Field, name="increment_value",
                                location=location, parent_field=parent_field,
                                target_object=self, button_text='+', **kwargs)

            if include_minmax:
                if right is not None:
                    self.max_button = right.create(Endcap,
                                                target_object=parent_field,
                                                location=location,
                                                name="maximum", **kwargs)
                else:
                    self.max_button = self.right =\
                    self.create(Endcap, target_object=parent_field,
                                location=location, name="maximum", **kwargs)

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

    def handle_transition_animation_end(self):
        super(Slider_Field, self).handle_transition_animation_end()
        self.update_position_from_value()

    def update_position_from_value(self):
        self.entry.continuum.update_position_from_value()


if __name__ == "__main__":
    Form.unit_test()
