class Color(object):

    colors = ('r', 'g', 'b', 'a')


    def _on_set(self, coordinate, value):
        lower_bound, upper_bound = getattr(self,
                                           coordinate + "_range", (value, value))
        setattr(self, '_' + coordinate, max(lower_bound, min(value, upper_bound)))

    def _get_r(self):
        return self._r
    def _set_r(self, value):
        self._on_set('r', value)
    r = property(_get_r, _set_r)

    def _get_g(self):
        return self._g
    def _set_g(self, value):
        self._on_set('g', value)
    g = property(_get_g, _set_g)

    def _get_b(self):
        return self._b
    def _set_b(self, value):
        self._on_set('b', value)
    b = property(_get_b, _set_b)

    def _get_a(self):
        return self._a
    def _set_a(self, value):
        self._on_set('a', value)
    a = property(_get_a, _set_a)

    def _get_color(self):
        return (self.r, self.g, self.b, self.a)
    def _set_color(self, colors):
        self.r = colors[0]
        self.g = colors[1]
        self.b = colors[2]
        try:
            self.a = colors[3]
        except IndexError:
            self.a = 255
    color = property(_get_color, _set_color)

    def _get_r_range(self):
        return self._r_range
    def _set_r_range(self, value):
        self._r_range = value
        self.r = self._r
    r_range = property(_get_r_range, _set_r_range)

    def _get_g_range(self):
        return self._g_range
    def _set_g_range(self, value):
        self._g_range = value
        self.g = self._g
    g_range = property(_get_g_range, _set_g_range)

    def _get_b_range(self):
        return self._b_range
    def _set_b_range(self, value):
        self._b_range = value
        self.b = self._b
    b_range = property(_get_b_range, _set_b_range)

    def _get_a_range(self):
        return self._a_range
    def _set_a_range(self, value):
        self._a_range = value
        self.a = self._a
    a_range = property(_get_a_range, _set_a_range)

    def __init__(self, r=0, g=0, b=0, a=0,
                 r_range=(0, 255), g_range=(0, 255), b_range=(0, 255), a_range=(0, 255)):
        super(Color, self).__init__()
        self._r = self._g = self._b = self._a = 0
        self._r_range = self._g_range = self._b_range = self._a_range = (0, 255)
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.r_range = r_range
        self.g_range = g_range
        self.b_range = b_range
        self.a_range = a_range

    def __iter__(self):
        return iter((self.r, self.g, self.b, self.a))

    def __getitem__(self, index):
        return (self.r, self.g, self.b, self.a)[index]
