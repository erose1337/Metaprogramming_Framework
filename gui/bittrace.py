#bit trace
import pride.gui.gui

class Bit_Trace(pride.gui.gui.Window):
    
    defaults = {"x_position" : None, "y_position" : None, "point_size" : 4}
    required_attributes = ("bits", )
    post_initializer = "trace"
    flags = {"_bits" : (None, None)}
    
    def _get_bits(self):
        return self._bits
    def _set_bits(self, value):
        assert value != (None, None)
        self._bits = value        
        self.trace()
        self.texture_invalid = True        
    bits = property(_get_bits, _set_bits)
        
    def trace(self):
        x_bits, y_bits = self.bits
        self.trace_bits(x_bits, self.w, "x_position")
        self.trace_bits(y_bits, self.h, "y_position")                    
        
    def trace_bits(self, bits, space_size, attribute):        
        position = space_size / 2
        adjustment = position
        for bit in bits:
            adjustment = adjustment / 2
            if bit:
                position += adjustment
            else:
                position -= adjustment
        assert position >= 0        
        setattr(self, attribute, position)
                
    def draw_texture(self):        
        x = self.x_position
        y = self.y_position
        size = self.point_size        
        self.draw("rect", (x - size, y - size, size, size), color=self.color)
        #self.draw("point", (self.w / 2, self.y_position), color=self.color)        
        #self.draw("line", (0, self.y_position, self.w, self.y_position), color=self.color)
        
        