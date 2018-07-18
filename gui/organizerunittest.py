import pride.gui.gui

class Noisy_Container(pride.gui.gui.Container):
    
    def left_click(self, mouse):
        self.alert("Clicked inside {}".format(self.area))
        
        
class Organizer_Unit_Test(pride.gui.gui.Window):
    
    defaults = {"container_type" : Noisy_Container}
    
    def __init__(self, **kwargs):
        super(Organizer_Unit_Test, self).__init__(**kwargs)
        
        container = self.container_type
                
        top = self.create(container, pack_mode="top")
        left = self.create(container, pack_mode="left")
        right = self.create(container, pack_mode="right")
        bottom = self.create(container, pack_mode="bottom")
        main = self.create(container, pack_mode="main")
        
        top_level = (top, left, right, bottom, main)
        destinations = ("top", "left", "right", "bottom", "main")
        for place in top_level:            
            for destination in destinations:           
                next_place = place.create(container, pack_mode=destination)
                
                for destination2 in destinations:
                    final_layer = next_place.create(container, pack_mode=destination2)
                final_layer.create("pride.gui.grid.Grid", grid_size=(4, 4), 
                                   square_colors=((55, 55, 55, 255), (225, 225, 225, 255)))
        