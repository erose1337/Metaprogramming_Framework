#bit trace
#to do: extend to 3d
import os
import collections

import pride.gui.gui

class Bit_Trace(pride.gui.gui.Window):

    defaults = {"x_position" : None, "y_position" : None, "point_size" : 4, "max_points" : 128}
    mutable_defaults = {"points" : list}
    required_attributes = ("bits", )
    post_initializer = "trace"
    predefaults = {"_bits" : (None, None)}

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
        x_position = self.trace_bits(x_bits, self.w)
        y_position = self.trace_bits(y_bits, self.h)
        self.points.append((x_position, y_position))

    def trace_bits(self, bits, space_size):
        position = space_size / 2
        adjustment = position
        for bit in bits:
            adjustment = adjustment / 2
            if bit:
                position += adjustment
            else:
                position -= adjustment
        assert position >= 0
        return position

    def draw_texture(self):
        size = self.point_size
        color = self.color
        x, y = self.points[0]
        self.draw("rect", (x - size, y - size, size, size), color=color)
        last_point = (x, y)
        for x, y in self.points[1:]:
            self.draw("rect", (x - size, y - size, size, size), color=color)
            self.draw("line", last_point + (x, y), color=color)
            last_point = (x, y)
        if self.points > self.max_points:
            self.points[:] = self.points[-self.max_points:]


class Animated_Bit_Trace(Bit_Trace):

    defaults = {"dimension" : 2, "priority" : .025}
    predefaults = {"_bits" : ((0, 0), (0, 0))}
    post_initializer = "begin_trace"

    def begin_trace(self):
        self.bits = [self.random_bits(2), self.random_bits(2)]
        self.trace_instruction = pride.Instruction(self.reference, "begin_trace") # so it can be unscheduled upon deletion
        self.trace_instruction.execute(priority=self.priority)

    @classmethod
    def random_bits(self, amount):
        in_bytes = (amount / 8) or 1
        random_bytes = os.urandom(in_bytes)
        bits = [int(item) for item in ''.join(format(ord(byte), 'b').zfill(8) for byte in random_bytes)[:amount]]
        return bits

    def delete(self):
        self.trace_instruction.unschedule()
        super(Animated_Bit_Trace, self).delete()
