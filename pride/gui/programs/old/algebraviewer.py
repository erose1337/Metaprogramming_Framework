import random

import pride.gui.widgets.form

class Vector(object):

    def __init__(self, x=0, y=0, z=0, t=0):
        self.x = x; self.y = y; self.z = z; self.t = t


class Matrix(object):

    def __init__(self, vectors=(Vector(), Vector(), Vector(), Vector())):
        self.vectors = vectors

    def __getitem__(self, key):
        try:
            return self.vectors[key]
        except IndexError:
            raise KeyError("{} not in range".format(key))

    def __setitem(self, key, value):
        self.vectors[key] = value

    def __delitem__(self, key):
        del self.vectors[key]


class Algebra_Test(pride.gui.widgets.form.Scrollable_Window):

    defaults = {"coords" : "xyzt", "_state_counter" : 0}
    mutable_defaults = {"vector" : Vector, "matrix" : Matrix}
    autoreferences = ("matrix_form", "vector_form", "spacer")

    def __init__(self, **kwargs):
        super(Algebra_Test, self).__init__(**kwargs)
        self.create("pride.gui.widgets.form.Form", h_range=(0, .05),
                    fields=[[("visualize_apply", {"button_text" : "Apply"}),
                             ("shuffle_vector", {"button_text" : "Shuffle vector"})]],
                    pack_mode="top", target_object=self)

        fields = [[(coord, {"editable" : False, "auto_create_id" : False,
                            "target_object" : row}) for coord in self.coords]
                   for row in self.matrix.vectors]
        m = self.main_window.create(pride.gui.widgets.form.Form, fields=fields,
                                    form_name="Matrix", max_rows=5)
        self.matrix_form = m

        vector_fields = [[(coord, {"editable" : False, "pack_mode" : "top",
                                   "orientation" : "stacked"}) for coord in self.coords]]
        v = self.create(pride.gui.widgets.form.Form, pack_mode="right",
                        w_range=(0, .25), fields=vector_fields, form_name="Vector",
                        target_object=self.vector, max_rows=5)
        self.vector_form = v
        self.spacer = self.create("pride.gui.gui.Container", pack_mode="right")

    def visualize_apply(self):
        vector_form = self.vector_form
        vector_form.pack_mode = "top"
        vector_form.w_range = (0, .5)
        vector_form.h_range = (0, .2)
        for field in self.vector_form.fields_list:
            field.pack_mode = "left"
        self.vector_form.pack()
        pride.Instruction(self.reference, "visualize_dot_product").execute(priority=3)

    def shuffle_vector(self):
        random.shuffle(self.vector_form.rows[0].children)
        self.vector_form.rows[0].pack()

    def visualize_dot_product(self):
        # interleave the vector into the row
        state_counter = self._state_counter
        #row = self.matrix_form.rows[state_counter].children
        #row[:] = zip(row, self.vector_form.rows[0].children)
        #self.matrix_form.pack()


def test_Algebra_Test():
    import pride.gui
    window = pride.objects[pride.gui.enable(x=50, y=50)]
    window.create("pride.gui.main.Gui", startup_programs=(Algebra_Test, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Algebra_Test()
