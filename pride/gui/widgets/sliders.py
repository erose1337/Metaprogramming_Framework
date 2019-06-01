import pride.gui.gui

class _Slider_Dragger(pride.gui.gui.Button):

    defaults = {"target" : tuple(), "bounds" : tuple(), "on_adjustment" : None}
    required_attributes = ("target", "bounds", "on_adjustment")

    def set_initial_position(self):
        _object, name = self.target
        try:
            value = getattr(_object, name)
        except AttributeError as error:
            try:
                value = _object[name]
            except KeyError:
                raise error
        # value = (left_edge - left_intersection) * increment
        # value / increment = left_edge - left_intersection
        # (value / increment) + left_intersection = left_edge
        indicator_w = self.w
        parent = self.parent
        p3 = parent.parent.parent
        left_end = p3.left_end
        right_end = p3.right_end
        left_intersection = left_end.x + left_end.w
        right_intersection = right_end.x

        _min, _max = self.bounds
        length = right_intersection - left_intersection
        increment = (_max - _min) / max(1, float(length - indicator_w))

        left_edge = (value / increment) + left_intersection
        self.x = int(left_edge)

        self.on_adjustment()
        p3.parent.set_value_indicator(value)

    def mousemotion(self, x, y, x_change, y_change):
        if self.held:
            self_x = x#self.x + x_change

            indicator_w = self.w
            parent = self.parent
            p3 = parent.parent.parent
            left_end = p3.left_end
            right_end = p3.right_end
            left_intersection = left_end.x + left_end.w
            right_intersection = right_end.x

            left_edge = self_x
            if left_edge <= left_intersection:
                left_edge = left_intersection

            right_edge = left_edge + indicator_w
            if right_edge >= right_intersection:
                right_edge = right_intersection
                left_edge = right_edge - indicator_w
            self.x = left_edge

            _min, _max = self.bounds
            length = right_intersection - left_intersection
            increment = (_max - _min) / float(length - indicator_w)
            value = int((left_edge - left_intersection) * increment)

            _object, name = self.target
            if isinstance(_object, dict):
                _object[name] = value
            else:
                setattr(_object, name, value)

            self.on_adjustment()
            p3.parent.set_value_indicator(value)

    def delete(self):
        self.on_adjustment = None
        super(_Slider_Dragger, self).delete()


class _Slider_Bar(pride.gui.gui.Container):

    defaults = {"target" : tuple(), "bounds" : tuple(), "on_adjustment" : None}
    required_attributes = ("target", "bounds", "on_adjustment")
    autoreferences = ("dragger", )

    def _on_set(self, coordinate, value):
        super(_Slider_Bar, self)._on_set(coordinate, value)
        if coordinate == 'w' and self.dragger is not None:
            window = self.sdl_window
            window.schedule_predraw_operation(self.dragger.set_initial_position)

    def __init__(self, **kwargs):
        super(_Slider_Bar, self).__init__(**kwargs)
        self.dragger = self.create(_Slider_Dragger, target=self.target,
                                   bounds=self.bounds, w_range=(0, 20),
                                   on_adjustment=self.on_adjustment)


class Slider_Bar(pride.gui.gui.Container):

    defaults = {"pack_mode" : "top", "label" : '', "initial_value" : '',
                "target" : None, "bounds" : tuple(), "on_adjustment" : None}
    autoreferences = ("left_end", "right_end")

    def __init__(self, **kwargs):
        super(Slider_Bar, self).__init__(**kwargs)
        self.left_end = self.create("pride.gui.gui.Container", text=self.label,
                                    pack_mode="left", scale_to_text=False,
                                    w_range=(0, .05))
        middle = self.create("pride.gui.gui.Container", pack_mode="left")
        self.parent._slider_bar = middle.create(_Slider_Bar, pack_mode="bottom",
                                                target=self.target,
                                                bounds=self.bounds,
                                                on_adjustment=self.on_adjustment)
        self.right_end = self.create("pride.gui.gui.Container", text=str(self.initial_value),
                                     pack_mode="left", scale_to_text=False,
                                     w_range=(0, .05))


class Slider_Widget(pride.gui.gui.Container):

    defaults = {"label" : '', "bounds" : (0, 255), "target" : tuple(),
                "on_adjustment" : None}
    mutable_defaults = {"level" : dict}
    required_attributes = ("target", "on_adjustment")
    autoreferences = ("slider_bar", "_slider_bar")

    def __init__(self, **kwargs):
        super(Slider_Widget, self).__init__(**kwargs)
        _object, _attribute = self.target
        try:
            value = getattr(_object, _attribute)
        except AttributeError:
            value = _object[_attribute]

        label = self.label.replace('_', ' ')
        self.slider_bar = self.create(Slider_Bar, pack_mode="top", label=label,
                                      target=self.target, bounds=self.bounds,
                                      on_adjustment=self.on_adjustment,
                                      initial_value=value)

    def readjust_sliders(self):
        self._slider_bar.dragger.set_initial_position()

    def set_value_indicator(self, value):
        self.slider_bar.right_end.text = str(value)

    def set_label(self, value):
        self.slider_bar.left_end.text = value

    def set_level(self, level):
        self._slider_bar.dragger.set_position(self.level[level])
