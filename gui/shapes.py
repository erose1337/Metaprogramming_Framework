import pride.components.base

import sdl2.ext # for Color

class Shape(pride.components.base.Base):
    
    flags = {"transparency_enabled" : True}
    coordinates = ('x', 'y', 'w', 'h', 'z')  
    colors = ('r', 'g', 'b', 'a')         
       
    def __init__(self, **kwargs):
        self._color = sdl2.ext.Color(0, 0, 0, 0)
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
            
    def _get_r(self):
        return self._r
    def _set_r(self, value):
        self._on_set('r', value)
        self._color.r = value
        #r, g, b, a = self.color
        #self._color = sdl2.ext.Color(value, g, b, a)
    r = property(_get_r, _set_r)
    
    def _get_g(self):
        return self._g
    def _set_g(self, value):
        self._on_set('g', value)
        self._color.g = value
        #r, g, b, a = self.color
        #self._color = sdl2.ext.Color(r, value, b, a)
    g = property(_get_g, _set_g)
    
    def _get_b(self):
        return self._b
    def _set_b(self, value):
        self._on_set('b', value)
        self._color.b = value
        #r, g, b, a = self.color        
        #self._color = sdl2.ext.Color(r, g, value, a)
    b = property(_get_b, _set_b)
     
    def _get_a(self):
        return self._a if self.transparency_enabled else 255
    def _set_a(self, value):
        self._on_set('a', value)
        self._color.a = value
        #r, g, b, a = self.color
        #self._color = sdl2.ext.Color(r, g, b, value)
    a = property(_get_a, _set_a)
    
    def _get_color(self):
        return (self._color.r, self._color.g, self._color.b, self._color.a)
    def _set_color(self, colors):
        color = self._color
        self._r = color.r = colors[0]
        self._g = color.g = colors[1]
        self._b = color.b = colors[2]
        try:
            self._a = color.a = colors[3]
        except IndexError:
            self._a = color.a = 255
        #self._color = sdl2.ext.Color(self.r, self.g, self.b, self.a)        
    color = property(_get_color, _set_color)  
    
            
class Bounded_Shape(Shape):                   
    
    def _get_w_range(self):
        return self._w_range
    def _set_w_range(self, value):
        self._w_range = value
        self.w = self._w
    w_range = property(_get_w_range, _set_w_range)
    
    def _get_h_range(self):
        return self._h_range
    def _set_h_range(self, value):
        self._h_range = value
        self.h = self._h
    h_range = property(_get_h_range, _set_h_range)
    
    def __init__(self, **kwargs):
        max_width, max_height = pride.gui.SCREEN_SIZE
        self._w_range, self._h_range = (0, max_width), (0, max_height)
  #      self._x_range, self._y_range = (0, max_width), (0, max_height)
        super(Bounded_Shape, self).__init__(**kwargs)
        for color in self.colors:
            setattr(self, color + "_range", (0, 255))
            
    def _on_set(self, coordinate, value):
        lower_bound, upper_bound = getattr(self, 
                                           coordinate + "_range", (value, value))
        super(Bounded_Shape, self)._on_set(coordinate, 
                                           max(lower_bound, min(value, upper_bound)))
                                           