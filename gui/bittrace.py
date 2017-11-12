#bit trace
import pride.gui.gui

class Bit_Trace(pride.gui.gui.Window):
    
    defaults = {"bits" : tuple(), "y_pos" : None, "point_size" : 4}
    required_attributes = ("bits", )
    post_initializer = "trace_bits"
        
    def _get_bits(self):
        return self._bits
    def _set_bits(self, value):
        self._bits = value
        self.trace_bits()
        self.texture_invalid = True        
    bits = property(_get_bits, _set_bits)
    
    def trace_bits(self):
        bits = self.bits
        y_pos = self.h / 2
        adjustment = y_pos
        for bit in bits:
            adjustment = adjustment / 2
            if bit:
                y_pos += adjustment
            else:
                y_pos -= adjustment
        self.y_pos = y_pos
        assert y_pos >= 0        
        
    def draw_texture(self):        
        x = self.w / 2
        y = self.y_pos
        size = self.point_size
        print "Drawing: ", x - size, y - size, size, size
        self.draw("rect", (x - size, y - size, size, size), color=self.color)
        #self.draw("point", (self.w / 2, self.y_pos), color=self.color)        
        #self.draw("line", (0, self.y_pos, self.w, self.y_pos), color=self.color)
        
        