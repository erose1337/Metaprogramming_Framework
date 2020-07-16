import copy
from math import ceil

import pride.components.base
import pride.gui.widgets.form
import pride.gui.widgets.tabs
from pride.functions.utilities import slide
field_info = pride.gui.widgets.form.field_info

class _Text_Entry(pride.gui.widgets.form.Text_Entry): pass


class _Text_Field(pride.gui.widgets.form.Text_Field):

    defaults = {"entry_type" : _Text_Entry}
    autoreferences = ("parent_window", )

    def handle_value_changed(self, old_value, new_value):
        super(_Text_Field, self).handle_value_changed(old_value, new_value)
        if len(new_value) < len(old_value):
            self.parent_window.handle_backspace()
        else:
            data = new_value[len(old_value):]
            self.parent_window.write_to(data)


class Scrollable_Text_Window(pride.gui.widgets.form.Scrollable_Window):

    defaults = {"text_field" : '', "line_count" : 24, "_current_line" : ''}
    mutable_defaults = {"input_history" : list, "lines" : list,
                        "vertical_slider_entry_kwargs" :\
                            lambda: {"orientation" : "stacked",
                                     "include_minmax_buttons" : False,
                                     "hide_text" : True}}
    hotkeys = {('\n', None) : "handle_return"}
    autoreferences = ("_form", )

    def __init__(self, **kwargs):
        super(Scrollable_Text_Window, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        window = self.main_window
        fields = [[field_info("text_field", auto_create_id=False,
                              field_type=_Text_Field, parent_window=self,
                              entry_kwargs={"center_text" : False,
                                            "hoverable" : False,
                                            "_formext_fix" : True, # conspries with Minimal_Themes draw_texture to fix a text jittering bug
                                            "font" : "Hack-Regular"})],
                 ]
        form = window.create(pride.gui.widgets.form.Form, fields=fields,
                             target_object=self)
        self._form = form

    def write_to(self, data):
        self._current_line += data
        try:
            self.lines[-1] += data
        except IndexError:
            self.lines.append(data)
        self.update_text_field()

    def handle_return(self):
        self.input_history.append(self._current_line)
        self._current_line = ''
        self.lines.append('')
        self.synchronize_scroll_bars()
        if not self.vertical_slider.hidden: # auto scroll to end; necessary to prevent weird newline behavior
            self.y_scroll_value = max(0, len(self.lines) - self.line_count)
            self.vertical_slider.update_position_from_value()

    def handle_backspace(self):
        try:
            old_line = self.lines[-1]
        except IndexError:
            pass
        else:
            if old_line:
                self.lines[-1] = old_line[:-1]
            else:
                del self.lines[-1]
        self.synchronize_scroll_bars()

    def update_text_field(self):
        self.text_field = '\n'.join(self.lines[self.y_scroll_value:self.y_scroll_value + self.line_count])
        self._form.synchronize_fields()

    def handle_area_change(self, old_area):
        super(Scrollable_Text_Window, self).handle_area_change(old_area)
        font_size = self.sdl_window.renderer.font_manager.wrapped_object.size
        self.line_count = int(ceil(self._form.rows[0].h / 17.5))
        self.synchronize_scroll_bars()

    def handle_y_scroll(self, old_value, new_value):
        super(Scrollable_Text_Window, self).handle_y_scroll(old_value, new_value)
        self.update_text_field()

    def synchronize_scroll_bars(self):
        slider = self.vertical_slider
        if slider is not None:
            slider.maximum = max(0, len(self.lines) - self.line_count)
            slider.update_position_from_value()
            slider.pack()
            self.update_text_field()



class Data(pride.components.base.Base):
    """ Use: set as the target_object of a Tabbed_Form
        Attributes named in `tab_names` will have tabs generated.
        `fields` can be used to control appearance.
        *should have _either_ tab_names or fields set*
        Iterables such as tuples/lists will be turned into Tabbed_Forms
        row_kwargs can be used to set attributes on rows in the form
        - row kwargs is a dictionary mapping row numbers to dictionaries """
    tab_names = tuple()
    inherited_attributes = {"tab_names" : tuple}
    field_type = "pride.gui.widgets.form.Form"


class Tabbed_Form(pride.gui.widgets.tabs.Tabbed_Window):
    """ Creates one tab per item in target_object.tab_names. """

    defaults = {"target_object" : None, "include_new_tab_button" : False,
                "default_form_type" : "pride.gui.widgets.form.Form",
                "tabbed_form_type" : "pride.gui.widgets.formext.Tabbed_Form"}
    required_attributes = ("target_object", )

    def create_subcomponents(self):
        tab_targets = self.tab_targets = []
        for name in self.target_object.tab_names:

            def callable(self=self, name=name):
                values = getattr(self.target_object, name)
                fields = copy.deepcopy(getattr(values, "fields", None))

                try:
                    row_kwargs = values.row_kwargs
                except AttributeError:
                    row_kwargs = dict()

                try:
                    form_type = values.form_type
                except AttributeError:
                    form_type = self.default_form_type

                kwargs = {"target_object" : values, "row_kwargs" : row_kwargs}
                if fields is not None:
                    kwargs["fields"] = fields

                if getattr(values, "tab_names", False):
                    if fields is None:
                        fields = kwargs["fields"] = []
                    fields.append([field_info(name,
                                              field_type=self.tabbed_form_type,
                                             target_object=values)])
                form = self.main_window.create(form_type, **kwargs)
                values.form_reference = form.reference
                return form
            callable.tab_text = name
            tab_targets.append(callable)
        super(Tabbed_Form, self).create_subcomponents()


def test_Tabbed_Form():
    import pride.gui
    import pride.gui.main

    class Test_Data(Data):

        tab_names = ("tab1", "tab2", "tab3")

    class Tab1_Contents(Data):

        defaults = {"test_bool" : True, "test_str" : "string", "test_int" : 0}
        fields = [[field_info(key) for key in sorted(defaults.keys())]]
        row_kwargs = {0 : {"h_range" : (0, .1)}}


    class Tab2_Contents(Data):

        defaults = {"subtab1" : Data(attribute=1, fields=[[field_info("attribute")]]),
                    "subtab2" : Data(attribute=2, fields=[[field_info("attribute")]])
                    }
        tab_names = ("subtab1", "subtab2")


    class Tab3_Contents(Data):

        defaults = {"subtab1" : Data(attribute=3, fields=[[field_info("attribute")]]),
                    "subtab2" : Data(attribute=4, fields=[[field_info("attribute")]]),
                    "test_attribute" : "tabs and a form"}
        tab_names = ("subtab1", "subtab2")
        fields = [[field_info("test_attribute")]]


    data = Test_Data(tab1=Tab1_Contents(), tab2=Tab2_Contents(),
                     tab3=Tab3_Contents())
    window = pride.objects[pride.gui.enable()]
    forms = lambda **kwargs: Tabbed_Form(target_object=data, **kwargs)
    window.create(pride.gui.main.Gui, startup_programs=(forms, ),
                  user=pride.objects["/User"])


def test_Scrollable_Text_Window():
    import pride.gui, pride.gui.main
    window = pride.objects[pride.gui.enable()]
    window.create(pride.gui.main.Gui,
                  startup_programs=(Scrollable_Text_Window, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Tabbed_Form()
    #test_Scrollable_Text_Window()
