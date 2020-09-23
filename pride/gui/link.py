# layouts include a `links` attribute
# create a tab for each link
import pride.gui.tabs
from pride.components import Component
from pride.gui.tabs import tab_info, lazy_loaded

def page(page_id, page_layout):
    return (page_id, page_layout)

class Linked_Form(pride.gui.tabs.Tabbed_Window):

    subcomponents = {"form" : Component("pride.gui.form2.Remote_Form")}
    autoreferences = ("form", )

    def create_subcomponents(self):
        _layout = self.layout
        form_type = self.form_type
        tabs = []
        for page_id, page_layout in _layout[-1].get("links", tuple()):
            target = lazy_loaded(Linked_Form, layout=page_layout,
                                 form_type=form_type)
            tabs.append(tab_info(target, text=page_id,
                                 entry_kwargs={"scale_to_text" : False}))
        self.tab_bar_kwargs["tab_info"] = tabs
        super(Linked_Form, self).create_subcomponents()
        if not tabs:
            self.tab_bar.hide()
        if _layout[0]:
            self.alert("Creating form")
            self.form = self.main_window.create(form_type, layout=_layout)

def test_Linked_Form():
    import pride.gui.main
    import pride.gui.form
    field_info = pride.gui.form.field_info
    row_info = pride.gui.form.row_info
    layout = pride.gui.form.layout

    _layout = layout(row_info(0,
                              field_info("formvar0"), field_info("formvar1")),
                     row_info(1, field_info("formvar2")),
                     formvar0=0, formvar1=1, formvar2="string",
                     links=(page("files", layout(row_info(0, field_info("var0")),
                                                 var0=0)),
                            page("media", layout(row_info(0, field_info("var1")),
                                                 var1="test"))))


    class test_Linked_Form(Linked_Form):

        defaults = {"layout" : _layout}

    pride.gui.main.run_programs([test_Linked_Form])



if __name__ == "__main__":
    test_Linked_Form()
