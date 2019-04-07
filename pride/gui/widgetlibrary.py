import time

import pride
import pride.gui.gui as gui
import pride.gui
import pride.components.base as base
Instruction = pride.Instruction

import sdl2

FIELD_BACKGROUND_COLOR = (225, 225, 225, 200)

class Attribute_Modifier_Button(gui.Button):

    defaults = {"amount" : 0, "operation" : "",  "target" : None}

    verbosity = {"left_click" : 'v'}

    def left_click(self, mouse):
        reference, attribute = self.target
        instance = pride.objects[reference]
        old_value = getattr(instance, attribute)
        new_value = getattr(old_value, self.operation)(self.amount)
        setattr(instance, attribute, new_value)
        self.alert("Modified {}.{}; {}.{}({}) = {}".format(reference, attribute, old_value,
                                                           self.operation, self.amount,
                                                           getattr(instance, attribute)),
                   level=self.verbosity["left_click"])


class Instruction_Button(gui.Button):

    defaults = {"args" : tuple(), "kwargs" : None, "method" : '',
                "reference" : '', "priority" : 0.0, "callback" : None}

    def left_click(self, mouse):
        Instruction(self.reference, self.method,
                    *self.args, **self.kwargs or {}).execute(priority=self.priority,
                                                             callback=self.callback)


class Method_Button(gui.Button):

    defaults = {"args" : tuple(), "kwargs" : None, "method" : '', "target" : '',
                "scale_to_text" : True}

    def left_click(self, mouse):
        try:
            instance = self.target()
        except TypeError:
            instance = pride.objects[self.target]
        getattr(instance, self.method)(*self.args, **self.kwargs or {})


class Delete_Button(Method_Button):

    defaults = {"pack_mode" : "right", "text" : "x", "method" : "delete",
                "scale_to_text" : True}


class Exit_Button(Delete_Button):

    defaults = {"text" : "exit"}


class Popup_Button(gui.Button):

    defaults = {"popup_type" : '', "_popup" : None}

    def left_click(self, mouse):
        if self._popup:
            self.alert("Deleting: {}".format(self._popup), level=0)
            self._popup.delete()
        elif self.popup_type:
            self.alert("Creating: {}".format(self.popup_type), level=0)#'vv')
            popup = self._popup = self.create(self.popup_type)
            popup.pack()


class Objects_Explorer(pride.gui.gui.Application):

    def __init__(self, **kwargs):
        super(Objects_Explorer, self).__init__(**kwargs)
        references = self.application_window.create("pride.gui.gui.Container", pack_mode="left",
                                                             scroll_bars_enabled=True)
        viewer = self.object_attributes_viewer = self.application_window.create("pride.gui.gui.Container", pack_mode="right")
        viewer.current_object = viewer.create("pride.gui.pyobjecttest.Object_Button", objects["/Python"]).reference

        for key, item in pride.objects.items():
            references.create("pride.gui.pyobjecttest.Object_Button", item,
                              opener=viewer.reference, h_range=(20, 20),
                              wrap_text=False)


class Icon(pride.gui.gui.Button):

    defaults = {"h_range" : (0, 40), "w_range" : (0, 40), "pack_mode" : "grid"}
    required_attributes = ("popup_type", )

    def left_click(self, mouse):
        if mouse.clicks == 2:
            popup = self.parent.create(self.popup_type)
            popup.pack()


class Program_Icon(Icon):

    defaults = {"program" : '', "popup_type" : ''}

    required_attributes = ("program", )

    def left_click(self, mouse):
        if mouse.clicks == 2:
            popup = self.parent.create(self.popup_type, program=self.program)
            popup.pack()


class Homescreen(gui.Application):

    def __init__(self, **kwargs):
        super(Homescreen, self).__init__(**kwargs)
        self.application_window.create(Task_Bar, startup_components=("pride.gui.widgetlibrary.Date_Time_Button",
                                                  "pride.gui.widgetlibrary.Text_Box"))
        self.application_window.create(Icon, popup_type=Objects_Explorer, text="Objects Explorer")
        self.application_window.create(Program_Icon, popup_type="pride.gui.shell.Python_Shell",
                                       program="/User/Command_Line/Python_Shell", text="Python")
        self.application_window.create("pride.gui.text_editor.Shortcut")
        self.application_window.create(Icon, popup_type="pride.gui.chess.Chess", text="Chess")


class Task_Bar(gui.Container):

    defaults = {"pack_mode" : "top", "h_range" : (0, 20)}
    #predefaults= {"bound" : (0, 20)}

    #def _set_pack_mode(self, value):
    #    super(Task_Bar, self)._set_pack_mode(value)
    #    if self.pack_mode in ("right", "left", "left"):
    #        self._backup_w_range = self.w_range
    #        self.w_range = self.bound
    #        self.h_range = self._backup_h_range
    #    else:
    #        self._backup_h_range = self.h_range
    #        self.h_range = self.bound
    #        try:
    #            self.w_range = self._backup_w_range
    #        except AttributeError:
    #            pass
    #pack_mode = property(gui.Container._get_pack_mode, _set_pack_mode)

    def __init__(self, **kwargs):
        super(Task_Bar, self).__init__(**kwargs)
        parent_name = self.parent_name
        self.create(Indicator, text=parent_name)
        self.create(Delete_Button, target=parent_name)

 #   def pack(self, modifiers=None):

  #      super(Task_Bar, self).pack(modifiers)


class Text_Box(gui.Container):

    defaults = {"h" : 16, "pack_mode" : "left", "background_color" : FIELD_BACKGROUND_COLOR,
                "allow_text_edit" : True,  "editing" : False}

    def select(self, mouse):
        super(Text_Box, self).select(mouse)
        self.alert("Turning text input on", level='vv')
        self.allow_text_edit = True
        sdl2.SDL_StartTextInput()

    def deselect(self, mouse, next_active_object):
        super(Text_Box, self).deselect(mouse, next_active_object)
        self.alert("Disabling text input", level='vv')
        self.allow_text_edit = False
        sdl2.SDL_StopTextInput()

    #def draw_texture(self):
    #   # width, height = pride.gui.SCREEN_SIZE#self.texture.area
    #    area = self.area#(0, 0, width, height)
    #    self.draw("fill", area, color=self.background_color)
    #    self.draw("rect", area, color=self.color)
    #    if self.text:
    #        self.draw("text", self.area, self.text,
    #                  bg_color=self.background_color, color=self.text_color)


class Date_Time_Button(gui.Button):

    defaults = {"pack_mode" : "left", "refresh_interval" : 59.9}

    def __init__(self, **kwargs):
        super(Date_Time_Button, self).__init__(**kwargs)
        update = self.update_instruction = Instruction(self.reference, "update_time")
        self.update_time()

    def update_time(self):
        text = time.asctime()
        self.text = text[:-8] + text[-5:] # remove seconds
        self.update_instruction.execute(priority=self.refresh_interval)

    def delete(self):
        self.update_instruction.unschedule()
        super(Date_Time_Button, self).delete()


class Color_Palette(gui.Window):

    def __init__(self, **kwargs):
        super(Color_Palette, self).__init__(**kwargs)
        color_button = self.create("pride.gui.gui.Button", pack_mode="left")
        slider_container = self.create("pride.gui.gui.Container", pack_mode="left")

        button_name = color_button.reference
        for color in ('r', 'g', 'b'):
            slider_container.create("pride.gui.widgetlibrary.Scroll_Bar",
                                    target=(button_name, color))


class Scroll_Bar(gui.Container):

    defaults = {"pack_mode" : "right", "amount" : 5,
                "target" : '', "amount" : 0}
    required_attributes = ("target", "amount")

    def __init__(self, **kwargs):
        super(Scroll_Bar, self).__init__(**kwargs)
        kwargs = {"target" : self.target, "amount" : self.amount}
        if self.pack_mode in ("right", "left"): # horizontal packs on the left side
            self.w_range = (0, 8)
            kwargs["pack_mode"] = "top"
            self.create(Increment_Button, **kwargs)
            self.create(Decrement_Button, **kwargs)
        else:
            self.h_range = (0, 8)
            kwargs["pack_mode"] = "left"
            self.create(Increment_Button, **kwargs)
            self.create(Decrement_Button, **kwargs)


class Decrement_Button(Attribute_Modifier_Button):

    defaults = {"amount" : 10, "operation" : "__sub__", "h_range" : (0, 8),
                "w_range" : (0, 20), "text" : ''}


class Increment_Button(Attribute_Modifier_Button):

    defaults = {"amount" : 10, "operation" : "__add__", "h_range" : (0, 8),
                "w_range" : (0, 20), "text" : ''}


class Scroll_Indicator(gui.Button):

    defaults = {"movable" : True, "text" : ''}

    def pack(self, modifiers=None):
        if self.pack_mode in ("right", "left"):
            width = int(self.parent.w * .8)
            self.w_range = (width, width)
        else:
            height = int(self.parent.h * .8)
            self.h_range = (height, height)
        super(Scroll_Indicator, self).pack(modifiers)

    def draw_texture(self):
        super(Scroll_Indicator, self).draw_texture()
        self.draw("rect", (self.w / 4, self.h / 4,
                           self.w * 3 / 4, self.h * 3 / 4), color=self.color)


class Indicator(gui.Button):

    defaults = {"pack_mode" : "left",
                "line_color" : (255, 235, 155),
                "text" : ''}

    def __init__(self, **kwargs):
        super(Indicator, self).__init__(**kwargs)
        self.text = self.text or self.parent_name

    def draw_texture(self):
        super(Indicator, self).draw_texture()
        #x, y, w, h = self.parent.area
        self.draw("text", self.area, self.text, color=self.text_color, w=self.w,
                  center_text=self.center_text)


class Done_Button(gui.Button):

    defaults = {"w_range" : (0, 20), "h_range" : (0, 20), "pack_mode" : "right"}
    def left_click(self, mouse):
        callback_owner, method = self.callback
        getattr(pride.objects[callback_owner], method)()


class Prompt(Text_Box):

    defaults = {"use_done_button" : False}

    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        if self.use_done_button:
            self.create("pride.gui.widgetlibrary.Done_Button", callback=(self.reference, "_done_callback"))

    def handle_return(self):
        self.text = value
        callback_owner, method = self.callback
        getattr(pride.objects[callback_owner], method)(self.text)

    def _done_callback(self):
        self.handle_return()


class Dialog_Box(gui.Container):

    defaults = {"callback" : tuple()}
    required_attributes = ("callback", )

    def __init__(self, **kwargs):
        super(Dialog_Box, self).__init__(**kwargs)
        self.create("pride.gui.widgetlibrary.Text_Box", text=self.text,
                    allow_text_edit=False, pack_mode="top")
        self.user_text = self.create("pride.gui.widgetlibrary.Prompt",
                                     use_done_button=True, pack_mode="bottom",
                                     h_range=(0, 80), callback=(self.reference, "handle_input"))

    def handle_input(self, user_input):
        reference, method = self.callback
        getattr(pride.objects[reference], method)(user_input)


class Palette_Button(pride.gui.gui.Button):

    defaults = {"button_type" : ''}
    required_attributes = ("button_type", )

    def deselected(self, mouse, next_active_item):
        pride.objects[next_active_item].create(self.button_type)


class Palette(pride.gui.gui.Window):

    defaults = {"button_types" : tuple()}

    def __init__(self, **kwargs):
        super(Palette, self).__init__(**kwargs)
        for button_type in self.button_types:
            self.create(Palette_Button, button_type=button_type, pack_mode="top")


class Number_Display(pride.gui.gui.Button):

    predefaults = {"_numeric_value" : None}

    def _get_numeric_value(self):
        return self._numeric_value
    def _set_numeric_value(self, value):
        self._numeric_value = value
        self.text = bytes(value)
    numeric_value = property(_get_numeric_value, _set_numeric_value)


class Form(pride.gui.gui.Window):

    defaults = {"pack_mode" : "top", "available_points" : 0,
                "field_object_type" : "pride.gui.widgetlibrary.Number_Display"}

    mutable_defaults = {"entries" : dict}

    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)
        name_column = self.create("pride.gui.gui.Container", pack_mode="left")
        value_column = self.create("pride.gui.gui.Container", pack_mode="left")

        entries = self.entries
        for entry in sorted(entries.keys()):
            box = name_column.create("pride.gui.widgetlibrary.Text_Box", text=entry, allow_text_edit=False, pack_mode="top")
            value_box = value_column.create(self.field_object_type, numeric_value=entries[entry], pack_mode="top")
            value_box.create("pride.gui.widgetlibrary.Scroll_Bar", target=(value_box.reference, "numeric_value"), pack_mode="right", amount=1)


class Dropdown_Box(pride.gui.gui.Container):

    defaults = {"entry_h_range" : (20, 40), "selection" : None, "initial_value" : '',
                "menu_open" : False, "callback" : tuple()}

    def __init__(self, **kwargs):
        super(Dropdown_Box, self).__init__(**kwargs)
        self.entries = [self.create(entry_type, h_range=self.entry_h_range, callback=self.callback) for
                        entry_type in self.entry_types]
        initial_value = self.initial_value
        if initial_value:
            for entry in self.entries:
                if entry.selection_value == initial_value:
                    assert self.selection is None
                    self.selection = entry.selection_value
                else:
                    entry.hide()
        else:
            for entry in self.entries[1:]:
                entry.hide()
            self.selection = self.entries[0].selection_value

    def call_callback(self):
        if self.callback:
            reference, method_name = self.callback
            getattr(pride.objects[reference], method_name)(self.selection)

    def show_menu(self):
        self.menu_open = True
        for entry in self.entries:
            entry.always_on_top = True
            entry.show()

    def hide_menu(self, selection, _deselect=False):
        self.menu_open = False
        self.selection = selection.selection_value
        for entry in self.entries:
            entry.always_on_top = False
            if entry is not selection:
                entry.hide()
        if not _deselect:
            self.call_callback()


class Dropdown_Box_Entry(pride.gui.gui.Button):

    defaults = {"pack_mode" : "top", "selection_value" : None,
                "background_color" : FIELD_BACKGROUND_COLOR}

    def left_click(self, mouse, _deselect=False):
        dropdown_box = self.parent
        if not dropdown_box.menu_open:
            dropdown_box.show_menu()
        else:
            dropdown_box.hide_menu(self, _deselect)
            assert not self.hidden
            #self.show()
        self.pack()

    def deselect(self, mouse, next_active_object):
        if pride.objects[next_active_object] not in self.parent.entries:
            if self.parent.menu_open:
                self.left_click(mouse, True)

    @classmethod
    def from_info(cls, text, selection_value=''):
        selection_value = selection_value if selection_value else text
        return lambda **kwargs: cls(text=text, selection_value=selection_value, **kwargs)


class Dropdown_Field(pride.gui.gui.Container):

    defaults = {"field_name" : '', "entry_types" : tuple(), "callback" : tuple(),
                "orientation" : "side by side", "initial_value" : ''}
    required_attributes = ("field_name", "entry_types")
    allowed_values = {"orientation" : ("side by side", "stacked")}

    def _get_selection(self):
        return pride.objects[self.dropdown_box].selection
    def _set_selection(self, value):
        dropdown_box = pride.objects[self.dropdown_box]
        for entry in dropdown_box.entries:
            if entry.selection_value == value:
                entry.left_click(None)
                return dropdown_box.selection
        else:
            raise ValueError("Invalid selection '{}'".format(value))
    selection = property(_get_selection, _set_selection)

    def __init__(self, **kwargs):
        super(Dropdown_Field, self).__init__(**kwargs)
        if self.orientation == "side by side":
            pack_mode = "left"
        else:
            pack_mode = "top"
        if not self.callback:
            self.callback = (self.reference, "on_dropdown_selection")
        self.create("pride.gui.gui.Button", text=self.field_name, pack_mode=pack_mode)
        self.dropdown_box = self.create("pride.gui.widgetlibrary.Dropdown_Box",
                                        pack_mode=pack_mode, callback=self.callback,
                                        entry_types=self.entry_types,
                                        initial_value=self.initial_value).reference

    def on_dropdown_selection(self, selection):
        pass


class Spin_Field_Entry(pride.gui.gui.Container):

    defaults = {"text" : '0', "background_color" : FIELD_BACKGROUND_COLOR}

    def __init__(self, **kwargs):
        super(Spin_Field_Entry, self).__init__(**kwargs)
        self.create(pride.gui.widgetlibrary.Method_Button, target=self.reference,
                    method="increment_value", pack_mode="right", w_range=(0, 20),
                    text='+')
        self.create(pride.gui.widgetlibrary.Method_Button, target=self.reference,
                    method="decrement_value", pack_mode="right", w_range=(0, 20),
                    text='-')

    def increment_value(self):
        new_value = self.on_increment(self.text)
        self.text = str(new_value)
        if self.write_field_method:
            self.write_field_method(self.text)

    def decrement_value(self):
        new_value = self.on_decrement(self.text)
        self.text = str(new_value)
        if self.write_field_method:
            self.write_field_method(self.text)


class Spin_Field(pride.gui.gui.Container):

    defaults = {"field_name" : '',  "initial_value" : '',
                "field_entry_type" : Spin_Field_Entry, "write_field_method" : None}
    required_attributes = ("field_name", )

    def __init__(self, **kwargs):
        super(Spin_Field, self).__init__(**kwargs)
        if not getattr(self, "on_increment", False) or not getattr(self, "on_decrement", False):
            raise ValueError("on_increment/on_decrement not supplied to Spin_Field")
        prompt = self.create("pride.gui.gui.Container", text="{}:".format(self.field_name),
                             pack_mode="top")
        kwargs = {"pack_mode" : "top", "on_increment" : self.on_increment,
                  "on_decrement" : self.on_decrement, "write_field_method" : self.write_field_method}
        if self.initial_value:
            kwargs["text"] = str(self.initial_value)
        self.field = self.create(self.field_entry_type, **kwargs).reference


class Field_Entry(Text_Box):

    defaults = {"write_field_method" : None, "background_color" : FIELD_BACKGROUND_COLOR}
    required_attributes = ("write_field_method", )

    def deselect(self, mouse, next_active_object):
        super(Field_Entry, self).deselect(mouse, next_active_object)
        if self.text:
            self.write_field_method(self.text)

    def handle_return(self):
        self.deselect(None, None)


class Integer_Field_Entry(Field_Entry):

    defaults = {"background_color" : FIELD_BACKGROUND_COLOR}

    def text_entry(self, text):
        if self.allow_text_edit:
            try:
                int(text)
            except ValueError:
                pass
            else:
                self.text += text


class Field(pride.gui.gui.Container):

    defaults = {"field_name" : "", "write_field_method" : None, "initial_value" : '0',
                "field_entry_type" : Field_Entry, "orientation" : "side by side"}
    required_attributes = ("write_field_method", )
    allowed_values = {"orientation" : ("side by side", "stacked")}

    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        if self.orientation == "side by side":
            pack_mode = "left"
            scale_to_text = True
        else:
            pack_mode = "top"
            scale_to_text = False
        prompt = self.create("pride.gui.gui.Container", text="{}:".format(self.field_name),
                             scale_to_text=scale_to_text, pack_mode=pack_mode)
        field = self.create(self.field_entry_type, pack_mode=pack_mode, text=str(self.initial_value),
                            write_field_method=lambda value: self.write_field_method(self.field_name, value))


class Status_Indicator_Theme(pride.gui.gui.Theme):

    def draw_texture(self):
        x, y, w, h = area = self.area
        if not self._dont_draw:
            self.draw("fill", (x, y, w, h), color=self.background_color)
        for thickness in range(5):
            self.draw("rect", (x + thickness, y + thickness, w - (2 * thickness), h - (2 * thickness)),
                      color=(0, 0, 0, 255 / (thickness + 1)))


class Status_Indicator(pride.gui.gui.Container):

    defaults = {"w_range" : (0, 10), "pack_mode" : "left",
                "top_color" : (185, 85, 85, 235), "color" : (125, 105, 95, 255),
                "middle_color" : (85, 85, 185, 235), "_theme_type" : Status_Indicator_Theme,
                "bottom_color" : (85, 185, 85, 255), "theme_type" : "pride.gui.gui.Spacer_Theme",
                "_dont_draw" : True}

    def __init__(self, **kwargs):
        super(Status_Indicator, self).__init__(**kwargs)
        self.create("pride.gui.gui.Container", pack_mode="top",
                    theme_type="pride.gui.gui.Spacer_Theme")
        self.status_light = self.create("pride.gui.gui.Container", pack_mode="top",
                                        background_color=self.middle_color, theme_type=self._theme_type,
                                        _dont_draw=True).reference
        self.create("pride.gui.gui.Container", pack_mode="top",
                    theme_type="pride.gui.gui.Spacer_Theme")

    def enable_indicator(self):
        pride.objects[self.status_light]._dont_draw = False

    def disable_indicator(self):
        pride.objects[self.status_light]._dont_draw = True

    def change_color(self, color):
        pride.objects[self.status_light].background_color = color


class New_Tab_Button(Method_Button):

    defaults = {"pack_mode" : "left", "w_range" : (0, 40),
                "scale_to_text" : False}


class _Tab_Button(pride.gui.gui.Button):

    def left_click(self, mouse):
        self.parent.left_click(mouse)


class _Editable_Tab_Button(Text_Box):

    def left_click(self, mouse):
        super(_Editable_Tab_Button, self).left_click(mouse)
        self.parent.left_click(mouse)


class _Text_Only_Theme(pride.gui.gui.Theme):

    def draw_texture(self):
        if self.text:
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", self.area, self.text, w=self.w if self.wrap_text else None,
                      bg_color=self.text_background_color, color=self.text_color,
                      center_text=self.center_text)


class Tab_Button(Method_Button):

    defaults = {"pack_mode" : "left", "scale_to_text" : False,
                "include_delete_button" : True,
                "_tab_button_type" : _Tab_Button, "w_range" : (0, 200),
                "allow_text_edit" : True, "editing" : False}
    predefaults = {"_editable" : False}

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
            self.create(Method_Button, pack_mode="right", scale_to_text=True,
                        target=self.reference, method="delete_tab", text='x',
                        theme_type=_Text_Only_Theme, w_range=(0, 10))
        indicator = self.create(Status_Indicator)
        self.indicator = indicator.reference

    def delete_tab(self):
        # delete the tab
        # delete the associated window
        # remove the tab from tab_bar.tabs
        # select the previous tab in tab_bar if possible
        tabs = self.parent.tabs
        tabs.remove(self.reference)
        self.delete()
        pride.objects[self.window].delete()
        tabbed_window = self.parent.parent
        tabbed_window.window_listing.remove(self.window)
        try:
            tabbed_window.select_tab(tabs[-1])
        except IndexError:
            if tabs:
                raise

    def left_click(self, mouse):
        self.parent.parent.select_tab(self.reference)

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


class Tab_Bar(pride.gui.gui.Container):

    defaults = {"h_range" : (0, 40), "pack_mode" : "top", "label" : '',
                "tab_type" : Tab_Button}
    mutable_defaults = {"tabs" : list}

    def __init__(self, **kwargs):
        super(Tab_Bar, self).__init__(**kwargs)
        self.initialize_tabs()

    def initialize_tabs(self):
        if self.label:
            self.create("pride.gui.gui.Button", text=self.label,
                        scale_to_text=True, pack_mode="left")
        self.create(New_Tab_Button, text='+', target=self.parent.reference, method="new_tab")

    def new_tab(self, **kwargs):
        tab = self.create(self.tab_type, **kwargs).reference
        self.tabs.append(tab)
        return tab


class Tab_Switcher_Bar(Tab_Bar):

    defaults = {"tab_types" : tuple()}

    def initialize_tabs(self):
        if self.label:
            self.create("pride.gui.gui.Button", text=self.label,
                        scale_to_text=True, pack_mode="left")
        for tab_type in self.tab_types:
            self.tab_type = tab_type
            self.new_tab(scale_to_text=False)


class Tab_Switching_Window(pride.gui.gui.Window):

    defaults = {"tab_bar_type" : Tab_Switcher_Bar, "tab_types" : tuple(),
                "tab_bar_label" : '', "window_types" : tuple()}

    def __init__(self, **kwargs):
        super(Tab_Switching_Window, self).__init__(**kwargs)
        self.tab_bar = self.create(self.tab_bar_type, label=self.tab_bar_label,
                                   tab_types=self.tab_types)
        self.create_windows()

    def create_windows(self):
        tabs = self.tab_bar.tabs
        for index, window_type in reversed(enumerate(self.window_types)):
            window = self.create(window_type, tab=tabs[index])
            tab.window = window.reference
            if index:
                window.hide()
                tab.indicator.disable_indicator()
            else:
                tab.indicator.enable_indicator()

    def select_tab(self, selected_tab):
        for tab_reference in self.tab_bar.tabs:
            tab = pride.objects[tab_reference]
            if tab_reference != selected_tab:
                pride.objects[tab.window].hide()
                pride.objects[tab.indicator].disable_indicator()
                #pride.objects[tab.indicator].hide()
            else:
                window = pride.objects[tab.window]
                if window.hidden:
                    window.show()
                indicator = pride.objects[tab.indicator]
                indicator.enable_indicator()
                #if indicator.hidden:
                #    indicator.show()
        self.pack()


class Tabbed_Window(pride.gui.gui.Window):

    defaults = {"tab_bar_type" : Tab_Bar, "tab_type" : Tab_Button,
                "tab_bar_label" : '', "window_type" : "pride.gui.gui.Window"}
    mutable_defaults = {"window_listing" : list}

    def __init__(self, **kwargs):
        super(Tabbed_Window, self).__init__(**kwargs)
        self.tab_bar = self.create(self.tab_bar_type, label=self.tab_bar_label,
                                   tab_type=self.tab_type)

    def new_tab(self, window_kwargs=None, tab_kwargs=None):
        window_kwargs = window_kwargs if window_kwargs is not None else dict()
        tab_kwargs = tab_kwargs if tab_kwargs is not None else dict()
        window = self.create(self.window_type, **window_kwargs)
        self.window_listing.append(window.reference)
        tab_kwargs.setdefault("window", window.reference)
        new_tab = self.tab_bar.new_tab(**tab_kwargs)
        window.tab = new_tab
        self.select_tab(new_tab)
        return (new_tab, window)

    def select_tab(self, selected_tab):
        for tab_reference in self.tab_bar.tabs:
            tab = pride.objects[tab_reference]
            if tab_reference != selected_tab:
                pride.objects[tab.window].hide()
                pride.objects[tab.indicator].disable_indicator()
            else:
                window = pride.objects[tab.window]
                if window.hidden:
                    window.show()
                indicator = pride.objects[tab.indicator]
                indicator.enable_indicator()
        self.pack()
