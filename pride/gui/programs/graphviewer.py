import pride.gui.gui
import pride.gui.themes


class Node(pride.gui.gui.Button):

    defaults = {"location" : 'z', "display_name" : ''}


class Graph_Visualizer_Theme(pride.gui.themes.Minimal_Theme):

    wrapped_object_name = "graph"

    def draw_texture(self):
        raise NotImplementedError()
        graph = self.graph
        area = graph.area
        self.draw("fill", area, color=self.background_color)

        w, h = 80, 80
        draw_node = super(Graph_Visualizer_Theme, self).draw_texture
        for node in graph.nodes:
            self.x, self.y, self.w, self.h = node.x, node.y, w, h
            self.text = node.display_name
            draw_node()



class Graph_Visualizer(pride.gui.gui.Window):

    defaults = {"location" : "top", #"theme_type" : Graph_Visualizer_Theme,
                "node_info" : tuple(), "node_type" : Node}
    mutable_defaults = {"nodes" : list}

    def __init__(self, **kwargs):
        super(Graph_Visualizer, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        node_type = self.node_type
        for kwargs in self.node_info:
            self.create(node_type, **kwargs)

    def add(self, instance):
        super(Graph_Visualizer, self).add(instance)
        if isinstance(instance, Node):
            self.nodes.append(instance)

    def remove(self, instance):
        super(Graph_Visualizer, self).remove(instance)
        if isinstance(instance, Node):
            self.nodes.remove(instance)


def test_Graph_Visualizer():
    import pride.gui
    from random import randint
    window = pride.objects[pride.gui.enable()]
    node_info = [{'x' : randint(80, window.w - 80), 'w' : 80,
                  'y' : randint(80, window.h - 80), 'h' : 80,
                  "text" : str(i)} for i in range(32)]
    programs = (lambda **kwargs: Graph_Visualizer(node_info=node_info, **kwargs), )
    window.create("pride.gui.main.Gui", user=pride.objects["/User"],
                  startup_programs=programs)

if __name__ == "__main__":
    test_Graph_Visualizer()
