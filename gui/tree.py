import random

import pride.gui.gui

class Tree(pride.gui.gui.Window):
    
    defaults = {"point_color" : (255, 255, 255, 255), "line_color" : (255, 255, 255, 255)}
    mutable_defaults = {"points" : list, "lines" : list}
    
    def draw_texture(self):
        for x, y in enumerate(self.points):
            self.draw("point", (x, y), color=self.point_color)
            
        for x1, y1, x2, y2 in self.lines:
            self.draw("line", (x1, y1, x2, y2), color=self.line_color)
        
        
class Number_Tree(Tree):
    
    defaults = {"edge_padding" : 30}
    required_attributes = ("factors", )
    flags = {"_factors" : None}
    
    def _get_factors(self):
        return self._factors
    def _set_factors(self, value):
        self._factors = value
        self.texture_invalid = True
        self.derive_lines()
    factors = property(_get_factors, _set_factors)      
        
    def __init__(self, *args, **kwargs):
        super(Number_Tree, self).__init__(*args, **kwargs)
        self.derive_lines()
        
    def derive_lines(self):        
        if not self.factors:
            raise ValueError("Factors not supplied")
        del self.lines[:]
        edge_padding = self.edge_padding
        y_increment = (self.h - edge_padding) / len(self.factors)
        y_coord = self.h
        available_width = self.w - edge_padding     
        x_points = [available_width / 2]
        for depth, factor in enumerate(self.factors):            
            next_y_coord = y_coord - y_increment            
            space_per_point = available_width / factor            
            for x_coord in x_points:                
                next_x_coord = edge_padding + (space_per_point / 2) - (depth * 10)
                new_points = []
                for edge in range(factor):                                               
                    line = (x_coord, y_coord, next_x_coord, next_y_coord)
                    self.lines.append(line)                                   
                    new_points.append(next_x_coord)
                    next_x_coord += space_per_point
            x_points[:] = new_points
            y_coord -= y_increment
            
            
class Animated_Tree(Number_Tree):
    
    defaults = {"update_tree_priority" : .005}
    
    def __init__(self, *args, **kwargs):
        super(Animated_Tree, self).__init__(*args, **kwargs)
        self.update_tree_instruction = pride.Instruction(self.reference, "update_tree")
        self.update_tree_instruction.execute(priority=self.update_tree_priority)
        
    def update_tree(self):
        modulus = len(self.factors)
        index1 = random.randint(0, modulus - 1)
        index2 = (index1 + 1) % modulus
        
        factors = self.factors
        item1, item2 = factors[index1], factors[index2]
        if random.randint(0, 10) > 8:
            _item1 = (item1 + item2) % max(factors)
            if _item1 < 2:
                item1 = item1
            else:
                item1 = _item1
        factors[index1], factors[index2] = item2, item1
        self.update_tree_instruction.execute(priority=self.update_tree_priority)        
        self.factors = factors # to trigger Texture Invalid
                