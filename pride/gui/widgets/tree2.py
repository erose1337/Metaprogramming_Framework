import os
import time

import pride.gui.gui
import pride.gui.form
from pride.gui.form import field_info, row_info, layout
from pride.functions.utilities import slide


class Node_Viewer(pride.gui.form.Form):

    pass


class Tree_Viewer(pride.gui.form.Scrollable_Window):

    defaults = {"current_node" : '', "max_count" : 8,
                "initial_node" : "Tree Viewer",
                "node_label" : "current node", "viewer_type" : Node_Viewer}
    autoreferences = ("navbar", "bottom", "viewer")
    mutable_defaults = {"history" : list}

    def __init__(self, **kwargs):
        super(Tree_Viewer, self).__init__(**kwargs)
        self.create_subcomponents()
        self.view_node()

    def create_subcomponents(self):
        window = self.main_window
        _layout = \
            layout(row_info(0,
                            field_info("handle_back", button_text='<',
                                       scale_to_text=True),
                            field_info("handle_up", button_text="/\\",
                                       scale_to_text=True),
                            field_info("current_node",
                                       display_name=self.node_label),
                            #field_info("view_node", button_text="view",
                            #           scale_to_text=True)
                            field_info("delete", button_text='x',
                                       scale_to_text=True)))

        #fields += self.generate_nodes()
        self.navbar = window.create(pride.gui.form.Form,
                                    location="top", target_object=self,
                                    h_range=(0, .1), layout=_layout)
        self.viewer_area = window.create("pride.gui.gui.Container",
                                         location="top")

    def generate_nodes(self):
        """ Returns a list of field_infos """
        return []

    # "view" button does not use identifier and uses self.current_node
    def view_node(self, identifier=None):
        if identifier is None:
            identifier = self.current_node
        if self.history and identifier == self.history[-1]:
            return
        children = self.lookup(identifier)
        if children is None:
            return
        _layout = layout(*self.children_to_fields(children))
        if self.viewer is not None:
            self.viewer.delete()
        viewer_type = self.viewer_type
        self.viewer = self.viewer_area.create(viewer_type, target_object=self,
                                              layout=_layout, max_rows=6,
                                              row_h_range=(0, .15))

        if self.history: # need to check for contents before testing [-1] in case history is empty
            if self.history[-1] != identifier:
                self.history.append(identifier)
        else:
            self.history.append(identifier)
        self.current_node = identifier
        self.navbar.synchronize_fields()

    def handle_back(self):
        if self.history:
            assert self.history[-1] == self.current_node, (self.history, self.current_node)
        try:
            prior = self.history[-2]
        except IndexError:
            return
        else:
            del self.history[-2:]
            self.view_node(prior)

    def handle_up(self):
        raise NotImplementedError()

    def children_to_fields(self, children):
        return [row_info(i,
                        [self.new_entry(child) for child in chunk]) for
                 i, chunk in enumerate(slide(children, self.max_count))]

    @staticmethod
    def new_entry(child):
        return field_info("view_node", button_text=getattr(child, "text",
                                                           str(child)),
                          args=(child, ), scale_to_text=False)

    def lookup(self, identifier):
        return []


def test_Tree_Viewer():
    import pride.gui
    window = pride.objects[pride.gui.enable()]
    window.create("pride.gui.main.Gui", startup_programs=(Tree_Viewer, ),
                  user=pride.objects["/User"])


if __name__ == "__main__":
    test_Tree_Viewer()
