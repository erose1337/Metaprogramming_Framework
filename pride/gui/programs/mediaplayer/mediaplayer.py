import pride.gui.link
from pride.components import Component
from pride.gui.form import (field_info, row_info, layout, load_resources,
                            read_file, generate_manifest)
page = pride.gui.link.page

class Media_Player(pride.gui.link.Linked_Form):

    defaults = {"filename" : ''}
    parser_args = ("filename", )
    parser_modifiers = {"filename" : {"types" : ("positional", )}}
    subcomponents = {"tab_bar" : Component(include_new_tab_button=False)}

    def create_subcomponents(self):
        filename = self.filename
        alias = os.path.split(filename)[-1]
        manifest, manifest_data = load_resources((alias, filename))
        control_page = \
            page("controls",
                 layout(
                    row_info(0,
                         field_info("filename",
                                    field_type="pride.gui.fields.Media_Field")),
                        manifest=manifest, filename=alias))

        self.layout = control_page[1]#layout(links=(control_page, ))
        super(Media_Player, self).create_subcomponents()

def main():
    import pride.gui.main
    callable = lambda **kwargs: Media_Player(parse_args=True, **kwargs)
    pride.gui.main.run_programs([callable])

if __name__ == "__main__":
    main()
