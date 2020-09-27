import pride.gui.link
import pride.gui.form
from pride.components import Component
from pride.gui.form import field_info, row_info, layout
page = pride.gui.link.page

class Theme_Form(pride.gui.form.Form):

    subcomponents = {"form" :
                    Component("pride.gui.programs.themecustomizer.Theme_Form")}

    def get_parent_theme_editor(self):
        parent = self.parent
        while not hasattr(parent, "target_theme"):
            parent = parent.parent
        return parent

    def handle_value_changed(self, field, old, new):
        self.get_parent_theme_editor().target_theme.update_theme_users()

    def save_theme(self):
        self.get_parent_theme_editor().save_theme()

    def load_theme(self):
        self.get_parent_theme_editor().load_theme()


def generate_theme_editor_layout(theme):
    names = sorted(theme.theme_colors.keys())
    links = []
    for theme_profile in names:
        _theme_profile = theme.theme_colors[theme_profile]
        _links = []
        for color_profile in sorted(_theme_profile.keys()):
            _object = _theme_profile[color_profile]
            if isinstance(_object, int):
                _layout = layout(row_info(0,
                                      field_info(color_profile, minimum=0)),
                                 target_object=_theme_profile)
            else:
                _layout = \
                    layout(row_info(0,
                                field_info('a', minimum=0, maximum=255)),
                           row_info(1,
                                field_info('r', minimum=0, maximum=255)),
                           row_info(2,
                                field_info('g', minimum=0, maximum=255)),
                           row_info(3,
                                field_info('b', minimum=0, maximum=255)),
                            target_object=_object)
                interface = getattr(_object, "interface",
                                    (tuple(), tuple()))
                additional = tuple()
                for name in "rgba":
                    if name not in interface:
                        additional += (name, )
                _object.interface = (interface[0],
                                     interface[1] + additional)
            _links.append(page(color_profile, _layout))
        links.append(page(theme_profile,
                          layout(links=_links,
                            tab_bar_kwargs={"include_new_tab_button" : False})))
    return layout(links=links)

def generate_options_layout():
    return layout(
            row_info(0, field_info("save_theme", button_text="Save Theme",
                                   entry_kwargs={"scale_to_text" : False}),
                        field_info("load_theme", button_text="Load Theme",
                                   entry_kwargs={"scale_to_text" : False}),
                     h_range=(0, .1)),
                  tab_bar_kwargs={"include_new_tab_button" : False})


class Theme_Editor(pride.gui.link.Linked_Form):

    defaults = {"target_theme" : None}
    subcomponents = {"form" :
                    Component("pride.gui.programs.themecustomizer.Theme_Form"),
                     "tab_bar" : Component(include_new_tab_button=False),
                     "file_saver" :
                         Component("pride.gui.programs.fileexplorer.File_Saver",
                                   location="top", autodelete=True),
                     "file_selector" :
                     Component("pride.gui.programs.fileexplorer.File_Selector")}
    autoreferences = ("file_saver", "file_selector")

    def create_subcomponents(self):
        if self.target_theme is None:
            self.target_theme = self.theme
        theme = self.target_theme
        theme_editor_layout = generate_theme_editor_layout(theme)
        options_layout = generate_options_layout()
        self.layout = layout(links=(page("editor", theme_editor_layout),
                                    page("options", options_layout)))
        super(Theme_Editor, self).create_subcomponents()

    def save_theme(self):
        if self.file_saver is None:
            # have to use this window to make the result look "right"
            window = self.main_window.children[0].form.main_window
            file_saver = window.create(self.file_saver_type,
                                       data=self.theme.serialize(),
                                       **self.file_saver_kwargs)
            self.file_saver = file_saver
        else:
            self.file_saver.delete()

    def load_theme(self):
        if self.file_selector is None:
            # have to use this window to make the result look "right"
            window = self.main_window.children[0].form.main_window
            file_selector = window.create(self.file_selector_type,
                                          callback=self._load_theme,
                                          **self.file_selector_kwargs)
            self.file_selector = file_selector
        else:
            self.file_selector.delete()

    def _load_theme(self, filename):
        with open(filename, 'r') as _file:
            _bytes = _file.read()
        theme_colors = self.theme.deserialize(_bytes)
        self.theme.update_theme_colors(theme_colors)


def test_Theme_Editor():
    import pride.gui.main
    pride.gui.main.run_programs([Theme_Editor])

if __name__ == "__main__":
    test_Theme_Editor()
