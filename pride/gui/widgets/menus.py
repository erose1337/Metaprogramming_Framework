# Menu
# ====
#   [Menu name]
#    option1
#    option2
#    option3
#
# A container of options
# Options perform some action when selected


# Recursive Menu
# ==============
#
#   [back][up][Menu name, current_place]
#            rect   rect
#            rect   rect
#
# Each rect displays an option from a menu e.g.:
#
#     play   load
#     create options
#
# Selecting an option:
#     - hides currently displayed choices
#     - appends the selected option onto the current_place
#     - Either:
#         - The selected option opens a new menu
#         - The selected option performs some function
from math import sqrt, ceil

import pride.gui.gui
from pride.functions.utilities import slide

class Option_Button(pride.gui.gui.Button):

    def __init__(self, **kwargs):
        super(Option_Button, self).__init__(**kwargs)
        self.indicator = self.create("pride.gui.widgetlibrary.Status_Indicator").reference

    def left_click(self, mouse):
        self.parent_application.select_option(self, self.text)


class Recursive_Menu(pride.gui.gui.Application):

    defaults = {"row_type" : "pride.gui.gui.Container", "row_pack_mode" : "top",
                "tree" : None, "initial_options" : tuple(), "menu_name" : '',
                "option_type" : Option_Button, "startup_components" : tuple(),
                "current_button" : ''}
    mutable_defaults = {"rows" : list}

    def __init__(self, **kwargs):
        super(Recursive_Menu, self).__init__(**kwargs)
        top_bar = self.create("pride.gui.gui.Container", h_range=(0, .10), pack_mode="top")
        top_bar.create("pride.gui.widgetlibrary.Method_Button", target=self.reference,
                       method="handle_back", text='<', scale_to_text=True, pack_mode="left")
        self._name = top_bar.create("pride.gui.gui.Container", text=self.menu_name,
                                    pack_mode="left").reference
        self.create_menu(self.initial_options)

    def create_menu(self, options):
        if self.rows:
            for row in self.rows:
                pride.objects[row].delete()
#        if options not in self.tree:
#            assert options == self.menu_name, (options, self.menu_name)
#            return self.create_menu(self.initial_options)

        row_type = self.row_type
        row_pack_mode = self.row_pack_mode
        option_type = self.option_type
        length = int(ceil(sqrt(len(options))))
        rows = self.rows = []
        window = self.application_window
        for options in slide(options, length):
            row = window.create(row_type, pack_mode=row_pack_mode)
            self.rows.append(row.reference)
            for option_name in options:
                row.create(option_type, text=option_name, pack_mode="left")

    def select_option(self, button, option_name):
        try:
            pride.objects[pride.objects[self.current_button].indicator].disable_indicator()
        except KeyError:
            if self.current_button in pride.objects:
                raise
        self.current_button = button.reference
        pride.objects[button.indicator].enable_indicator()
        result = self.tree[option_name]
        try:
            result(option_name)
        except TypeError:
            if hasattr(result, "__call__"):
                raise
            pride.objects[self._name].text += '/' + option_name
            self.create_menu(result)
        else:
            return True

    def handle_back(self):
        _name = pride.objects[self._name]
        _history = _name.text.rsplit('/', 1)
        try:
            history, current_item = _history
        except ValueError:
            return

        try:
            history, prior_item = history.rsplit('/', 1)
        except ValueError:
            # go back to root menu
            _name.text = history
            options = self.initial_options
        else:
            # go back to prior
            _name.text = history + '/' + prior_item
            options = self.tree[prior_item]
        self.create_menu(options)

def test():
    import pride.gui
    window = pride.objects[pride.gui.enable()]
    def printf(output):
        print(output)

    tree = {'1' : ['5', '9', "13", "17", "19"], '2' : ['6', "10", "14"],
            '5' : ['9', "13"], '6' : ["10", "14"],
            '9' : printf, '10' : printf, '13' : printf, '14' : printf,
            '17' : ['2', '5', '6'], '19' : ['6', '10', '14']}
    menu = lambda **kwargs: Recursive_Menu(tree=tree, initial_options=('1', '2'),
                                           menu_name="Test Menu", **kwargs)
    gui = window.create("pride.gui.main.Gui", user=pride.objects["/User"],
                        startup_programs=(menu, ))

if __name__ == "__main__":
    test()
