class _Slider_Dragger(pride.gui.gui.Button):

    defaults = {"target" : tuple(), "bounds" : tuple(), "on_adjustment" : None,
                "_slider_label" : ''}
    required_attributes = ("target", "bounds", "on_adjustment", "_slider_label")

    def set_initial_position(self):
        parent = self.parent
        px, py, pw, ph = parent.area
        _object, name = self.target
        _min, _max = self.bounds
        try:
            value = getattr(_object, name)
        except AttributeError as error:
            try:
                value = _object[name]
            except KeyError:
                raise error
        scalar = (value + _min) / float(_max)
        x = int(scalar * (pw - self.w)) + self.w
        self.x = max(min(pride.objects[parent.parent.right_end].x - self.w,
                         x),
                     pride.objects[parent.parent.left_end].w)
        self.on_adjustment()
        pride.objects[self._slider_label].set_label_value(value)

    def mousemotion(self, x_change, y_change):
        if self.held:
            parent = self.parent
            px, py, pw, ph = parent.area
            self_w = self.w
            left_end_w = pride.objects[parent.parent.left_end].w
            self.x = max(min(pride.objects[parent.parent.right_end].x - self_w,
                             self.x + x_change),
                         left_end_w)
            _object, name = self.target
            _min, _max = self.bounds
            scalar = max(min((self.x - self_w) / float(pw - self_w), 1.0), 0)
            value = int((_max * scalar) - _min)
            if isinstance(_object, dict):
                _object[name] = value
            else:
                setattr(_object, name, value)

            self.on_adjustment()
            pride.objects[self._slider_label].set_label_value(value)

    def delete(self):
        self.on_adjustment = None
        super(_Slider_Dragger, self).delete()


class _Slider_Bar(pride.gui.gui.Container):

    defaults = {"target" : tuple(), "bounds" : tuple(), "on_adjustment" : None,
                "_slider_label" : ''}
    predefaults = {"dragger" : None}
    required_attributes = ("target", "bounds", "on_adjustment", "_slider_label")

    def _on_set(self, coordinate, value):
        super(_Slider_Bar, self)._on_set(coordinate, value)
        if coordinate == 'w' and self.dragger is not None:
            window = pride.objects[self.sdl_window]
            dragger = pride.objects[self.dragger]
            window.schedule_predraw_operation(dragger.set_initial_position)

    def __init__(self, **kwargs):
        super(_Slider_Bar, self).__init__(**kwargs)
        self.dragger = self.create(_Slider_Dragger, target=self.target, bounds=self.bounds,
                                   w_range=(0, 20), on_adjustment=self.on_adjustment,
                                   _slider_label=self._slider_label).reference

    def delete(self):
        self.dragger = None
        super(_Slider_Bar, self).delete()


class Slider_Label(pride.gui.gui.Container):

    defaults = {"label" : ''}
    required_attributes = ("label", )

    def set_label_value(self, value):
        self.text = "{} ({})".format(self.label, value)


class Slider_Widget(pride.gui.gui.Container):

    defaults = {"label" : '', "bounds" : (0, 255), "target" : tuple(),
                "on_adjustment" : None, "label" : ''}
    required_attributes = ("target", "on_adjustment")

    def __init__(self, **kwargs):
        super(Slider_Widget, self).__init__(**kwargs)
        label = self.label.replace('_', ' ')
        self.slider_bar = slider_bar = self.create("pride.gui.gui.Container", pack_mode="top")
        slider_bar.left_end = slider_bar.create("pride.gui.gui.Container", text=self.label,
                                                pack_mode="left", scale_to_text=True,
                                                theme_type="pride.gui.gui.Text_Only_Theme").reference
        self._slider_bar = slider_bar.create(_Slider_Bar, pack_mode="main", target=self.target,
                                             bounds=self.bounds, on_adjustment=self.on_adjustment,
                                             _slider_label=slider_label).reference
        slider_bar.right_end = slider_bar.create("pride.gui.gui.Container",
                                                 text=str(getattr(self.target, self.label)),
                                                 pack_mode="right", scale_to_text=True,
                                                 theme_type="pride.gui.gui.Text_Only_Theme").reference

    def readjust_sliders(self):
        pride.objects[pride.objects[self._slider_bar].dragger].set_initial_position()


def test():
