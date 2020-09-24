import os
import time

import pride.gui.gui
import pride.gui.form
from pride.functions.utilities import slide
from pride.gui.form import field_info, row_info, layout


class Node_Viewer(pride.gui.form.Form):

    pass


# change current_node theme profile to alert if it does not exist

class Tree_Viewer(pride.gui.gui.Application):

    defaults = {"current_node" : '', "max_count" : 8, "node_label" : "current node"}
    autoreferences = ("top", "bottom", "viewer")
    mutable_defaults = {"history" : list}

    def __init__(self, **kwargs):
        super(Tree_Viewer, self).__init__(**kwargs)
        self.create_subcomponents()
        self.view_node()

    def create_subcomponents(self):
        window = self.application_window
        _layout = layout(
                    row_info(0,
                        field_info("handle_back", button_text='<',
                                   scale_to_text=True),
                        field_info("handle_up", button_text="/\\",
                                   scale_to_text=True),
                        field_info("current_node",
                                   display_name=self.node_label),
                        field_info("view_node", button_text="view",
                                   scale_to_text=True),
                        field_info("delete", button_text='x',
                                   scale_to_text=True)))
        self.top = window.create(pride.gui.form.Form, location="top",
                                 target_object=self, h_range=(0, .1),
                                 layout=_layout)
        self.bottom = window.create("pride.gui.gui.Container", location="top")

    def view_node(self, identifier=None): # "view" button does not use identifier and uses self.current_node
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
        self.viewer = self.bottom.create(Node_Viewer, target_object=self,
                                         layout=_layout, row_h_range=(0, .15),
                                         max_rows=10)
        if self.history: # need to check for contents before testing [-1] in case history is empty
            if self.history[-1] != identifier:
                self.history.append(identifier)
        else:
            self.history.append(identifier)
        self.current_node = identifier
        self.top.synchronize_fields()

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
        return [row_info(i, self.new_entry(child)) for
                i, child in enumerate(children)]

    @staticmethod
    def new_entry(child):
        return field_info("view_node",
                          button_text=getattr(child, "text", str(child)),
                          args=(child, ),
                          entry_kwargs={"scale_to_text" : False})

    def lookup(self, identifier):
        """ lookup should return a sequence of items that are children of the current node """
        raise NotImplementedError()
