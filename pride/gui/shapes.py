import pride.components.base

import sdl2.ext # for Color

class Shape(pride.components.base.Base):

    coordinates = ('x', 'y', 'w', 'h', 'z')

    def __init__(self, **kwargs):
        for coordinate in self.coordinates:
            setattr(self, "_" + coordinate, 0)
        super(Shape, self).__init__(**kwargs)

    def _on_set(self, coordinate, value):
        setattr(self, "_" + coordinate, value)

    def _get_x(self):
        return self._x
    def _set_x(self, value):
        self._on_set('x', value)
    x = property(_get_x, _set_x)

    def _get_y(self):
        return self._y
    def _set_y(self, value):
        self._on_set('y', value)
    y = property(_get_y, _set_y)

    def _get_w(self):
        return self._w
    def _set_w(self, value):
        self._on_set('w', value)
    w = property(_get_w, _set_w)

    def _get_h(self):
        return self._h
    def _set_h(self, value):
        self._on_set('h', value)
    h = property(_get_h, _set_h)

    def _get_z(self):
        return self._z
    def _set_z(self, value):
        self._on_set('z', value)
    z = property(_get_z, _set_z)

    def _get_position(self):
        return (self.x, self.y)
    def _set_position(self, position):
        self.x, self.y = position
    position = property(_get_position, _set_position)

    def _get_size(self):
        return (self.w, self.h)
    def _set_size(self, size):
        self.w, self.h = size
    size = property(_get_size, _set_size)

    def _get_area(self):
        return (self.x, self.y, self.w, self.h)
    def _set_area(self, rect):
        self.x, self.y, self.w, self.h = rect
    area = property(_get_area, _set_area)


class Bounded_Shape(Shape):

    def _get_w_range(self):
        return self._w_range
    def _set_w_range(self, value):
        screen_w, screen_h = self.sdl_window.size
        if isinstance(value[0], float):
            lower = value[0]
            if lower < 0.0 or lower > 1.0:
                raise ValueError("float w_range must be between 0.0 and 1.0; got {}".format(lower))
            value = (int(lower * screen_w), value[1])
        if isinstance(value[1], float):
            upper = value[1]
            if upper < 0.0 or upper > 1.0:
                raise ValueError("float h_range must be between 0.0 and 1.0; got {}".format(upper))
            value = (value[0], int(upper * screen_w))
        self._w_range = value
    w_range = property(_get_w_range, _set_w_range)

    def _get_h_range(self):
        return self._h_range
    def _set_h_range(self, value):
        screen_w, screen_h = self.sdl_window.size
        if isinstance(value[0], float):
            value = (int(value[0] * screen_h), value[1])
        if isinstance(value[1], float):
            value = (value[0], int(value[1] * screen_h))
        self._h_range = value
    h_range = property(_get_h_range, _set_h_range)

    def __init__(self, **kwargs):
        assert not isinstance(kwargs["sdl_window"], str), kwargs
        max_width, max_height = kwargs["sdl_window"].size
        self._w_range, self._h_range = (0, max_width), (0, max_height)
        super(Bounded_Shape, self).__init__(**kwargs)

    def _on_set(self, coordinate, value):
        lower_bound, upper_bound = getattr(self,
                                           coordinate + "_range", (value, value))
        super(Bounded_Shape, self)._on_set(coordinate,
                                           max(lower_bound, min(value, upper_bound)))
