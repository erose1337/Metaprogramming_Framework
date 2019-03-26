import time

import pride
import pride.gui.gui as gui
import pride.gui
import pride.components.base as base
Instruction = pride.Instruction

import sdl2

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

    defaults = {"h" : 16, "pack_mode" : "left",
                "allow_text_edit" : True,  "editing" : False}

    def select(self, mouse):
        self.alert("Turning text input on", level='vv')
        self.allow_text_edit = True
        sdl2.SDL_StartTextInput()

    def deselect(self, mouse, next_active_object):
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

    defaults = {"entry_h_range" : (20, 40), "selection" : None,
                "menu_open" : False, "callback" : tuple()}

    def __init__(self, **kwargs):
        super(Dropdown_Box, self).__init__(**kwargs)
        self.entries = [self.create(entry_type, h_range=self.entry_h_range, callback=self.callback) for
                        entry_type in self.entry_types]
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
            entry.show()

    def hide_menu(self, selection):
        self.menu_open = False
        self.selection = selection.selection_value
        for entry in self.entries:
            if entry is not selection:
                entry.hide()


class Dropdown_Box_Entry(pride.gui.gui.Button):

    defaults = {"pack_mode" : "top", "selection_value" : None}

    def left_click(self, mouse):
        dropdown_box = self.parent
        if not dropdown_box.menu_open:
            dropdown_box.show_menu()
        else:
            dropdown_box.hide_menu(self)
            self.show()
        self.pack()
        dropdown_box.call_callback()


class Dropdown_Field(pride.gui.gui.Container):

    defaults = {"field_name" : '', "entry_types" : tuple(), "callback" : tuple(),
                "orientation" : "side by side"}
    required_attributes = ("field_name", "entry_types")
    allowed_values = {"orientation" : ("side by side", "stacked")}

    def _get_selection(self):
        return pride.objects[self.dropdown_box].selection
    selection = property(_get_selection)

    def __init__(self, **kwargs):
        super(Dropdown_Field, self).__init__(**kwargs)
        if self.orientation == "side by side":
            pack_mode = "left"
        else:
            pack_mode = "top"
        self.create("pride.gui.gui.Button", text=self.field_name, pack_mode=pack_mode)
        self.dropdown_box = self.create("pride.gui.widgetlibrary.Dropdown_Box",
                                        pack_mode=pack_mode, callback=self.callback,
                                        entry_types=self.entry_types).reference


class Spin_Field_Entry(pride.gui.gui.Container):

    defaults = {"text" : '0'}

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

    defaults = {"field_name" : '', "on_increment" : None, "on_decrement" : None,
                "initial_value" : '', "field_entry_type" : Spin_Field_Entry,
                "write_field_method" : None}
    required_attributes = ("field_name", "on_increment", "on_decrement")

    def __init__(self, **kwargs):
        super(Spin_Field, self).__init__(**kwargs)
        prompt = self.create("pride.gui.gui.Container", text="{}:".format(self.field_name),
                             pack_mode="top")
        kwargs = {"pack_mode" : "top", "on_increment" : self.on_increment,
                  "on_decrement" : self.on_decrement, "write_field_method" : self.write_field_method}
        if self.initial_value:
            kwargs["text"] = self.initial_value
        self.field = self.create(self.field_entry_type, **kwargs).reference


class Field_Entry(Text_Box):

    defaults = {"write_field_method" : None}
    required_attributes = ("write_field_method", )

    def deselect(self, mouse, next_active_object):
        super(Field_Entry, self).deselect(mouse, next_active_object)
        if self.text:
            self.write_field_method(self.text)

    def handle_return(self):
        self.deselect(None, None)


class Integer_Field_Entry(Field_Entry):

    def text_entry(self, text):
        if self.allow_text_edit:
            try:
                int(text)
            except ValueError:
                pass
            else:
                self.text += text


class Field(pride.gui.gui.Container):

    defaults = {"field_name" : "", "write_field_method" : None,
                "field_entry_type" : Field_Entry}
    required_attributes = ("write_field_method", )

    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        prompt = self.create("pride.gui.gui.Container", text="{}:".format(self.field_name),
                             w_range=(0, 120), pack_mode="left")
        field = self.create(self.field_entry_type, pack_mode="left",
                            write_field_method=lambda value: self.write_field_method(self.field_name, value))


class New_Tab_Button(Method_Button):

    defaults = {"pack_mode" : "left", "w_range" : (0, 40),
                "scale_to_text" : False}


class Tab_Button(Method_Button):

    defaults = {"pack_mode" : "left"}


class Tab_Bar(pride.gui.gui.Container):

    defaults = {"h_range" : (0, 40)}

    def __init__(self, **kwargs):
        super(Tab_Bar, self).__init__(**kwargs)
        self.create(New_Tab_Button, target=self.target, method=self.method,
                    text='+')
