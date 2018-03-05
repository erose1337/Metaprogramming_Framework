from math import floor, sqrt, ceil

import pride
import pride.components.base as base
import pride.gui
import pride.gui.shapes
Instruction = pride.Instruction
#objects = pride.objects

import sdl2
import sdl2.ext
SDL_Rect = sdl2.SDL_Rect

R, G, B, A = 0, 80, 255, 30

MAX_W, MAX_H = pride.gui.SCREEN_SIZE
_OPPOSING_SIDE = {"left" : "right", "right" : "left", "top" : "bottom", "bottom" : "top"}

def create_texture(size, access=sdl2.SDL_TEXTUREACCESS_TARGET,
                   factory="/Python/SDL_Window/Renderer/SpriteFactory",
                   renderer="/Python/SDL_Window/Renderer"):
    return objects[factory].create_texture_sprite(objects[renderer].wrapped_object,
                                                  size, access=access)
    
class Organizer(base.Base):
    
    mutable_defaults = {"pack_modes" : dict, "_pack_modes" : dict, "_pack_index" : dict}

    def get_pack_mode(self, instance):
        return self.pack_modes[instance]
     
    def set_pack_mode(self, instance, value): 
        if value is None:
            try:
                del self._pack_modes[instance]
            except KeyError: 
                pass
            old_pack_mode = self.pack_modes.pop(instance)
            del self._pack_index[instance]  
            
            _instance = pride.objects[instance]
            parent = _instance.parent_name
            if parent in self._pack_modes:
            #    print "removing : ", _instance, self._pack_modes[parent][old_value]
                self._pack_modes[parent][old_pack_mode].remove(instance)
            return
        parent = pride.objects[instance].parent.reference
        old_pack_mode = self.pack_modes.get(instance, '')
        if old_pack_mode:
            self._pack_modes[parent][old_pack_mode].remove(instance)

        self.pack_modes[instance] = value
        try:
            self._pack_modes[parent][value].append(instance)
        except KeyError:
            if parent not in self._pack_modes:
                self._pack_modes[parent] = dict((key, []) for key in ("top", "bottom", "left", "right", "main"))
                self._pack_modes[parent][value] = [instance]
            else:
                self._pack_modes[parent][value] = [instance]
        self._pack_index[instance] = self._pack_modes[parent][value].index(instance)
    
    def add_pack_method(self, name, callback):
        setattr(self, name, "pack_{}".format(name), callback)
        
    def pack_item(self, item):
   #     self.alert("packing: {}, {} {} {}", 
   #               [item, item.area, item.z, item.pack_mode],
   #                level=self.verbosity["packing"])
        reference = item.reference
        pack_mode = self.pack_modes[reference]
        pack = getattr(self, "pack_{0}".format(pack_mode))
        parent = item.parent
        old_size = item.size
        pack(parent, item, self._pack_index[reference], 
             len(self._pack_modes[parent.reference][pack_mode]))
        item.alert("Packed into: {} {}".format(item.area, item.z), 
                   level=item.verbosity["packed"])
    
    def pack_main(self, parent, item, count, length):
        item.z = parent.z + 1
        pack_modes = self._pack_modes[parent.reference]
        sides = [[objects[name] for name in pack_modes[side]] for side in ("top", "bottom", "left", "right")]
        top, bottom, left, right = sides
        top_count, bottom_count, left_count, right_count = (len(side) for side in sides)
        parent_x, parent_y, parent_w, parent_h = parent.area

        width_spacing = parent_w / (left_count + length + right_count)
        height_spacing = parent_h / (top_count + length + bottom_count)
                
        width_of = self._width_of
        height_of = self._height_of
        height_of_top = height_of(top, height_spacing)        
        height_of_bottom = height_of(bottom, height_spacing)
        width_of_right = width_of(right, width_spacing)
        width_of_left = width_of(left, width_spacing)
        
        item.x = parent_x + width_of_left
        item.y = parent_y + height_of_top                             
        item.w = parent_w - (width_of_left + width_of_right)
        item.h = parent_h - (height_of_bottom + height_of_top)
        
    def pack_left(self, parent, item, count, length):
        item.z = parent.z + 1
        pack_modes = self._pack_modes[parent.reference]
        sides = [[objects[name] for name in pack_modes[side]] for side in ("top", "bottom", "left", "right", "main")]
        top, bottom, left, right, main = sides
        top_count, bottom_count, left_count, right_count, main_count = (len(side) for side in sides)
        item_x, item_y, item_w, item_h = parent_x, parent_y, parent_w, parent_h = parent.area

        width_spacing = parent_w / (left_count + int(any((top_count, main_count, bottom_count))) + right_count)
        height_spacing = parent_h / ((top_count + bottom_count) or 1)
                
        width_of = self._width_of
        height_of = self._height_of
        height_of_top = height_of(top, height_spacing)        
        height_of_bottom = height_of(bottom, height_spacing)
        width_of_right = width_of(right, width_spacing)
        width_of_left = width_of(left[:count], width_spacing)
        width_of_main = width_of(main, width_spacing)
        
        item.y = parent.y #+ height_of_top 
        item.x = item_x + width_of_left                                    
        item.w = width_spacing#parent_w - (width_of_right + width_of_main + width_of_left)
        item.h = parent_h# - height_of_bottom
        #print parent_h, height_of_bottom, height_of_top, height_spacing, top_count, bottom_count
        
    def _height_of(self, side, sizing):
        return sum(min(sizing, item.h_range[1]) for item in side)
        
    def _width_of(self, side, sizing):
        return sum(min(sizing, item.w_range[1]) for item in side)
        
    def pack_top(self, parent, item, count, length):
        item.z = parent.z + 1
             
        _items = self._pack_modes[parent.reference]
        main_items = _items["main"]
        bottom_items = _items["bottom"]
        top_items = _items["top"]     
        left_items = _items["left"]
        right_items = _items["right"]
        height_of = self._height_of        
        width_of = self._width_of
        
        vertical_sizing = parent.h / (len(top_items) + len(main_items) + len(bottom_items))
        height_of_top = height_of((objects[name] for name in top_items[:count]), vertical_sizing)
        height_of_main = height_of((objects[name] for name in main_items), vertical_sizing)
        height_of_bottom = height_of((objects[name] for name in bottom_items), vertical_sizing)
        
        horizontal_sizing = parent.w / (len(left_items) + 1 + len(right_items)) # + 1 for the top
        width_of_left = width_of((objects[name] for name in left_items), horizontal_sizing)
        width_of_right = width_of((objects[name] for name in right_items), horizontal_sizing)
                
        item.y = parent.y + height_of_top
        item.x = parent.x + width_of_left  
       # print parent.x, width_of_left, len(left_items), horizontal_sizing
        item.w = parent.w - (width_of_left + width_of_right)
       # print parent.w, width_of_left, width_of_right, len(left_items), len(right_items)
        item.h = (parent.h - sum((height_of_main, height_of_bottom))) / len(top_items)
        #print item.h, parent.h, height_of_top, height_of_main, height_of_bottom, vertical_sizing, len(top_items), len(main_items), len(bottom_items)
        
        if count == length - 1 and not main_items:  
            height_of_top = height_of((objects[name] for name in top_items[:-1]), vertical_sizing)            
            available_space = parent.h - (height_of_top + height_of_bottom)            
            item.h = available_space                       
            
    def pack_grid(self, parent, item, count, length):
        grid_size = sqrt(length)

        if grid_size != floor(grid_size):
            grid_size = floor(grid_size) + 1
        position = (int(floor((count / grid_size))), int(count % grid_size))

        item.z = parent.z + 1        
        
        pack_modes = self._pack_modes[parent.reference]
        right_objects = [pride.objects[reference] for reference in pack_modes["right"]]
        left_objects = [pride.objects[reference] for reference in pack_modes["left"]]
        main_objects = [pride.objects[reference] for reference in pack_modes["main"]]
        horizontal_spacing = parent.w / ((len(left_objects) + len(right_objects) + len(main_objects)) or 1)
        occupied_left_area =  sum((item.w or min(item.w_range[1], horizontal_spacing) for item in left_objects))
        occupied_right_area = sum((item.w or min(item.w_range[1], horizontal_spacing) for item in right_objects))
        
        top_objects = [pride.objects[reference] for reference in pack_modes["top"]]
        bottom_objects = [pride.objects[reference] for reference in pack_modes["bottom"]]
        vertical_spacing = parent.h / ((len(top_objects) + len(bottom_objects) + len(main_objects)) or 1)
        occupied_top_area = sum((item.h or min(item.h_range[1], vertical_spacing) for item in top_objects))
        occupied_bottom_area = sum((item.h or min(item.h_range[1], vertical_spacing) for item in bottom_objects))
        
        available_width = parent.w - occupied_left_area - occupied_right_area
        available_height = parent.h - occupied_top_area - occupied_bottom_area
        item.size = int(available_width / grid_size), int(available_height / grid_size)
        item.x = (item.w * position[1]) + parent.x + occupied_left_area
        item.y = (item.h * position[0]) + parent.y + occupied_top_area
        
    def pack_z(self, parent, item, count, length):
        item.z = parent.z + 1

    def pack_bottom(self, parent, item, count, length):
        item.z = parent.z + 1       
                        
        pack_modes = self._pack_modes[parent.reference]
        height_of = self._height_of            
        width_of = self._width_of
        
        left_objects = [objects[name] for name in pack_modes["left"]]
        right_objects = [objects[name] for name in pack_modes["right"]]
        bottom_objects = [objects[name] for name in pack_modes["bottom"]]
        top_objects = [objects[name] for name in pack_modes["top"]]
        main_objects = pack_modes["main"]
        
        # stretch to fit
        sizing = parent.h / (len(bottom_objects) + len(main_objects) + len(top_objects))
        height_of_bottom = height_of(bottom_objects[:count + 1], sizing)
        height_of_top = height_of(top_objects, sizing)
        
        w_sizing = parent.w / (len(left_objects) + int(any(bottom_objects)) + len(right_objects))
        width_of_left = width_of(left_objects, w_sizing)
        width_of_right = width_of(right_objects, w_sizing)
                
        item.y = (parent.y + parent.h) - height_of_bottom
        item.x = parent.x + width_of_left
        item.w = parent.w - (width_of_left + width_of_right)
        item.h = sizing    
        
        if not pack_modes["main"] and count == length - 1:
            height_of_top = height_of(top_objects, sizing)                
            item.y = parent.y + height_of_top
            item.h = (parent.h - (height_of_top + height_of(bottom_objects[:count], sizing)))
                         
    def pack_right(self, parent, item, count, length):  
        item.z = parent.z + 1
        pack_modes = self._pack_modes[parent.reference]
        sides = [[objects[name] for name in pack_modes[side]] for side in ("top", "bottom", "left", "right", "main")]
        top, bottom, left, right, main = sides
        top_count, bottom_count, left_count, right_count, main_count = (len(side) for side in sides)
        parent_x, parent_y, parent_w, parent_h = parent.area

        width_spacing = parent_w / (left_count + int(any((top_count, main_count, bottom_count))) + right_count)
        height_spacing = parent_h / ((top_count + bottom_count) or 1)
                
        width_of = self._width_of
        height_of = self._height_of
        height_of_top = height_of(top, height_spacing)        
        height_of_bottom = height_of(bottom, height_spacing)
        width_of_right = width_of(right, width_spacing)
        width_of_left = width_of(left, width_spacing)
        width_of_main = width_of(main[:1], width_spacing)
        
        item.y = parent_y #+ height_of_top 
        item.w = parent_w - (width_of(right[:count], width_spacing) + max((width_of(top[:1], width_spacing), width_of_main, width_of(bottom[:1], width_spacing))) + width_of_left)
        item.x = (parent_x + parent_w) - (item.w + width_of(right[:count], width_spacing))
        item.h = parent_h# - height_of_bottom        
                
    def pack_drop_down_menu(self, parent, item, count, length): 
        SCREEN_SIZE = pride.gui.SCREEN_SIZE
        item.area = (parent.x, parent.y + parent.h,
                     SCREEN_SIZE[0] / 5, min(120, SCREEN_SIZE[1] / length))
        item.z = parent.z + 1
        
    def pack_popup_menu(self, parent, item, count, length):        
        item.z = max(pride.objects[item.sdl_window + "/SDL_User_Input"]._coordinate_tracker.keys())
        w, h = pride.gui.SCREEN_SIZE
        item.position = (w / 4, h / 4)                         
        
        
class Theme(pride.base.Wrapper):
    
    def draw_texture(self):
        raise NotImplementedError
        
        
class Minimal_Theme(Theme):
            
    def draw_texture(self):
        area = self.area
        self.draw("fill", area, color=self.background_color)
        self.draw("rect_width", area, color=self.color, width=self.outline_width)        
        if self.text:
            width = self.w if self.wrap_text else None
        #    assert width is not None, (self, width, self.w, self.wrap_text, self.text)
            assert isinstance(self.text, str), (type(self.text), self.text, self)
            self.draw("text", area, self.text, width=self.w if self.wrap_text else None,
                      bg_color=self.background_color, color=self.text_color)

                             
class Organized_Object(pride.gui.shapes.Bounded_Shape):
    
    defaults = {'x' : 0, 'y' : 0, "size" : (0, 0), "pack_mode" : ''}

    flags = {"sdl_window" : ''}
    
    mutable_defaults = {"_children" : list}
    verbosity = {"packed" : "packed"}       
    
    def _get_pack_mode(self):      
        return self._pack_mode
    def _set_pack_mode(self, value):
        self._pack_mode = value
        objects[(self.sdl_window  or self.parent.sdl_window) + "/Organizer"].set_pack_mode(self.reference, value)
    pack_mode = property(_get_pack_mode, _set_pack_mode)
    
    def pack(self):
        organizer = objects[self.sdl_window + "/Organizer"]
        organizer.pack_item(self)        
        for item in self.children:             
            item.pack()
            
    def delete(self):
        self.pack_mode = None # clear Organizer cache      
        super(Organized_Object, self).delete()
        
        
class Window_Object(Organized_Object):
    """ to do: write documentation!
    
        FAQ: I get the following message when exiting, why?:
            Exception TypeError: "'NoneType' object is not callable" in <bound method Window.__del__ of <sdl2.ext.window.Window object at 0xXXXXXXX> ignore
            Except AttributeError: "'NoneType' object has no attribute 'SDL_DestroyTexture'" in ignored  
        A: Your window object still exists somewhere and needs to be deleted properly. Make sure there are no scheduled instructions and/or attributes using your object"""
    defaults = {"outline_width" : 1,
                "background_color" : (0, 0, 0, 0), #(25, 125, 225, 125),
                "color" : (15, 165, 25, 255), "text_color" : (15, 165, 25, 255),
                "held" : False, "allow_text_edit" : False, "wrap_text" : True,
                "_ignore_click" : False, "hidden" : False, "movable" : False, 
                "text" : '', "scroll_bars_enabled" : False, 
                "_scroll_bar_h" : None, "_scroll_bar_w" : None,
                "theme_type" : "pride.gui.gui.Minimal_Theme"}    
        
    flags = {"scale_to_text" : False, "_texture_invalid" : False,
             "_texture_window_x" : 0, "_texture_window_y" : 0,
             "_text" : '', "_pack_mode" : '', "_sdl_window" : ''}
    
    mutable_defaults = {"_draw_operations" : list, "_children" : list}
    verbosity = {"press" : "vv", "release" : "vv", "packed" : "packed"} 
    
    hotkeys = {("\b", None) : "handle_backspace", ("\n", None) : "handle_return"}
    
    def _get_texture_invalid(self):
        return self._texture_invalid
    def _set_texture_invalid(self, value):
        if not self._texture_invalid and value:
          #  assert self.sdl_window
            objects[self.sdl_window].invalidate_object(self)         
        self._texture_invalid = value
    texture_invalid = property(_get_texture_invalid, _set_texture_invalid)
    
    def _on_set(self, coordinate, value):
        if not self.texture_invalid and coordinate in ('z', 'x', 'y', 'w', 'h', 'r', 'g', 'b', 'a'):
            self.texture_invalid = True           
        super(Window_Object, self)._on_set(coordinate, value)
                                                                 
    def _get_text(self):
        return self._text
    def _set_text(self, value):
        self._text = value
        if value and self.scale_to_text:
            assert self.sdl_window
            w, h = objects[self.sdl_window].renderer.get_text_size(self.area, value)
            w += 2
            self.w_range = (0, w)
            self.w = w            
        self.texture_invalid = True
    text = property(_get_text, _set_text)
    
    def _get_bg_color(self):
        return self._background_color
    def _set_bg_color(self, color):
        self.texture_invalid = True
        self._background_color = color if self.transparency_enabled else color[:3] + (255, )#sdl2.ext.Color(*color)
    background_color = property(_get_bg_color, _set_bg_color)
    
    def _get_color(self):
        return super(Window_Object, self)._get_color()
    def _set_color(self, colors):
        super(Window_Object, self)._set_color(colors)
        self.texture_invalid = True        
    color = property(_get_color, _set_color)
    
    def _get_text_color(self):
        return self._text_color
    def _set_text_color(self, colors):
        self._text_color = colors#sdl2.ext.Color(*colors)
        self.texture_invalid = True
    text_color = property(_get_text_color, _set_text_color)
    
    def _get_texture_window_x(self):
        return self._texture_window_x
    def _set_texture_window_x(self, value):
        self._texture_window_x = value
        self.texture_invalid = True
    texture_window_x = property(_get_texture_window_x, _set_texture_window_x)
    
    def _get_texture_window_y(self):
        return self._texture_window_y
    def _set_texture_window_y(self, value):
        self._texture_window_y = value
        self.texture_invalid = True
    texture_window_y = property(_get_texture_window_y, _set_texture_window_y)
        
    def _get_parent_application(self):
        result = None
        instance = self
        while not result:
            if isinstance(instance, Application):
                result = instance
            else:
                try:
                    instance = instance.parent
                except AttributeError:
                    raise ValueError("Unable to find parent application of {}".format(self))
        return result
    parent_application = property(_get_parent_application)
        
    def _get_children(self):
        return self._children
    def _set_children(self, value):
        self._children = value
    children = property(_get_children, _set_children)
    
    def _get_sdl_window(self):        
        return (self._sdl_window or getattr(self.parent, "sdl_window", self.parent_name))
    def _set_sdl_window(self, value):
        self._sdl_window = value
    sdl_window = property(_get_sdl_window, _set_sdl_window)
    
    def __init__(self, **kwargs):               
        super(Window_Object, self).__init__(**kwargs)       
        self.texture_window_x = self.texture_window_y = 0        
        self.texture_invalid = True
        
        self.theme = self.create(self.theme_type, wrapped_object=self)
        self._children.remove(self.theme)
        pride.objects[self.sdl_window + "/SDL_User_Input"]._update_coordinates(self.reference, self.area, self.z)
        
    def create(self, *args, **kwargs):
        kwargs.setdefault('z', self.z + 1)
        kwargs.setdefault("sdl_window", self.sdl_window)
        return super(Window_Object, self).create(*args, **kwargs)
        
    def add(self, _object):
        self._children.append(_object)
        super(Window_Object, self).add(_object)
        
    def remove(self, _object):
        try:
            self._children.remove(_object)
        except ValueError:
            if _object is not self.theme:                
                raise
        super(Window_Object, self).remove(_object)
        
    def press(self, mouse):
        self.alert("Pressing", level=self.verbosity["press"])
        self.held = True
        for instance in self.children:
            instance.held = True        

    def release(self, mouse):
        self.alert("Releasing", level=self.verbosity["release"])
        self.held = False
        if self._ignore_click:
            self._ignore_click = False
        elif mouse.button == 1:
            self.left_click(mouse)
        elif mouse.button == 3:
            self.right_click(mouse)
        else:
            self.alert("Button {} not yet implemented".format(mouse.button), level=0)
                    
    def left_click(self, mouse):
        pass
        
    def right_click(self, mouse):
        pass

    def mousewheel(self, x_amount, y_amount):
        pass

    def mousemotion(self, x_change, y_change, top_level=True):
        if self.movable and self.held:
            self._ignore_click = True
            #self.alert("Mousemotion {} {}".format(x_change, y_change), level=0)
            _x, _y = self.position       
            self.x += x_change
            self.y += y_change
            
            if top_level:
                mouse_position = objects[self.sdl_window].get_mouse_position()   
                parent = self.parent
                if not pride.gui.point_in_area(parent.area, mouse_position):
                    if self in parent.children:
                    #    self.parent.alert("Removing {}; {} not in {}", [self, objects["SDL_Window"].get_mouse_position(), self.parent.area], level=0)
                        parent.remove(self)                    
                        parent.pack({"position" : parent.position})
                        self.z -= 1
                elif self not in parent.children: 
                 #   self.parent.alert("Adding {}", [self], level=0)
                    parent.add(self)
                    parent.pack({"position" : parent.position})
                    #self.held = False                    
            x_difference = self.x - _x
            y_difference = self.y - _y
            for instance in self.children:
                instance.held = True
                instance.mousemotion(x_difference, y_difference, top_level=False)
                instance.held = False
            
    def toggle_hidden(self):
        if not self.hidden:
            sdl_user_input = pride.objects[self.sdl_window + "/SDL_User_Input"]
            sdl_user_input._update_coordinates(self.reference,
                                               self.area, -1)            
        self.hidden = not self.hidden
       
    def draw(self, figure, *args, **kwargs):
        """ Draws the specified figure on self. figure can be any shape supported
            by the renderer, namely: "rect", "line", "point", "text", and "rect_width".
            The first argument(s) will include the destination of the shape in the
            form appropriate for the figure specified (i.e. an area for a rect, a
            pair of points for a point). For a full list of arguments for a 
            particular figure, see the appropriate draw method of the renderer. """
        # draw operations are enqueued and processed in batches by the Renderer
        self._draw_operations.append((figure, args, kwargs))
                                                               
    def _draw_texture(self):    
        if self.hidden:
            return []
                
        del self._draw_operations[:]
        self.draw_texture()        
        instructions = self._draw_operations[:]        

        if self._texture_window_x or self._texture_window_y:
            x, y, w, h = self.area
            source_rect = (x + self.texture_window_x,
                           y + self.texture_window_y, w, h)  
            
            if x + w > MAX_W:
                w = MAX_W - x
            if y + h > MAX_H:
                h = MAX_H - y
            destination = (x, y, w, h)        
          #  assert destination == self.area
            instructions.append(("copy", (objects[self.sdl_window]._texture.texture, source_rect, destination), {}))
                                          
        self.texture_invalid = False        
        
    def draw_texture(self):
        self.theme.draw_texture()
        
    def pack(self):        
        super(Window_Object, self).pack()
        try:
            pack_modes = objects[self.sdl_window + "/Organizer"]._pack_modes[self.reference]
        except KeyError:
            pass
        else:
            total_height = sum((objects[name].h for name in pack_modes["top"] + pack_modes["bottom"]))
            total_width = sum((objects[name].w for name in pack_modes["right"] + pack_modes["left"]))
         #   if total_height > self.h:
         #       if total_width > self.w:
         #           self.texture_size = (total_width, total_height)
         #       else:
         #           self.texture_size = (self.texture_size[0], total_height)
         #       self.texture = create_texture(self.texture_size)
         #       self.alert("Resized texture to: {}".format(self.texture_size), level=0)
         #   elif total_width > self.w:
         #       self.texture_size = (total_width, self.texture_size[1])
                
            if self.scroll_bars_enabled:
                excess_height = total_height > self.h
                excess_width = total_width > self.w
                if not self._scroll_bar_h:
                    if excess_height:
                        bar = self.create("pride.gui.widgetlibrary.Scroll_Bar", pack_mode="right",
                                        target=(self.reference, "texture_window_y"))
                        self._scroll_bar_h = bar.reference
                        bar.pack()
                elif not excess_height:
                    objects[self._scroll_bar_h].delete()
                    self._scroll_bar_h = None
                    
                if not self._scroll_bar_w:
                    if excess_width:
                        bar = self.create("pride.gui.widgetlibrary.Scroll_Bar",
                                        pack_mode="bottom", target=(self.reference,
                                                                    "texture_window_x"))
                        self._scroll_bar_w = bar.reference
                        bar.pack()
                elif not excess_width:
                    objects[self._scroll_bar_w].delete()
                    self._scroll_bar_w = None
                
    def delete(self):                
        pride.objects[self.sdl_window].remove_window_object(self)                        
        self.theme.delete()
        super(Window_Object, self).delete()                
                
    def deselect(self, mouse, next_active_object):
        pass
        
    def select(self, mouse):
        pass    
    
    def text_entry(self, text):        
        if self.allow_text_edit:
            self.text += text        
        
    def handle_return(self):
        pass
        
    def handle_backspace(self):
        if self.allow_text_edit:
            self.text = self.text[:-1]
        
class Window(Window_Object):

    defaults = {"pack_mode" : "main", "size" : pride.gui.SCREEN_SIZE}

    
class Container(Window_Object):

    defaults = {"pack_mode" : "top"}


class Button(Window_Object):

    defaults = {"shape" : "rect", "pack_mode" : "top"}


class Application(Window):
    
    defaults = {"startup_components" : ("pride.gui.widgetlibrary.Task_Bar", ),
                "application_window_type" : "pride.gui.gui.Window"}
    flags = {"transparency_enabled" : False}
        
    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        self.application_window = self.create(self.application_window_type)       
        
    def draw_texture(self):
        assert not self.deleted
        super(Application, self).draw_texture()
        self.application_window.texture_invalid = True
        
        
class Placeholder(Organized_Object):

    defaults = {"pack_mode" : "left"}
    
    
class Texture_Atlas(Organized_Object):
    
    defaults = {"size" : (4096, 4096), "screen_size" : pride.gui.SCREEN_SIZE, "subsections" : tuple(),
                "placeholder_type" : Placeholder, "pack_mode" : "main"}
    
   # flags = {"sdl_window" : ''}
    
    def __init__(self, *args, **kwargs):
        super(Texture_Atlas, self).__init__(*args, **kwargs)        
        # top-left: screen;      top-right: vertical placeholders
        #         bottom-top: square placeholders
        #         bottom-bottom: horizontal placeholders
        placeholder_type = self.placeholder_type
        sdl_window = self.sdl_window
        
        top = self.create(placeholder_type, pack_mode="top", sdl_window=sdl_window)
        bottom = self.create(placeholder_type, pack_mode="top", sdl_window=sdl_window)
        
        screen_w, screen_h = self.screen_size
                
        top_left = top.create(placeholder_type, h_range=(screen_h, screen_h), pack_mode="left", sdl_window=sdl_window)
        top_right = top.create(placeholder_type, pack_mode="left", sdl_window=sdl_window)
        bottom_top = bottom.create(placeholder_type, pack_mode="top", sdl_window=sdl_window)
        bottom_bottom = bottom.create(placeholder_type, pack_mode="bottom", sdl_window=sdl_window)
        self.subsections = (top_left, top_right, bottom_top, bottom_bottom)
        
        top.pack()
        
    def add_to_atlas(self, window_object):        
        subsection, pack_mode = self.determine_subsection(window_object)
        placeholder = subsection.create(self.placeholder_type, pack_mode=pack_mode, sdl_window=self.sdl_window)
        window_object._texture_atlas_reference = placeholder.reference
        placeholder.pack()
        return placeholder.position
        
    def remove_from_atlas(self, window_object):        
        pride.objects[window_object._texture_atlas_reference].delete()
        del window_object._texture_atlas_reference
        
    def determine_subsection(self, window_object):
        # determine approximate "square-ness" of (w, h)
        #   - if w / h > 2:
        #       item is horizontal
        #   - if h / w > 2:
        #       item is vertical
        #   - else item fits well enough in a square
        # also returns which way to pack the item into the according subsection
        w, h = window_object.size       
        if h and w / h > 2:
            return self.subsections[3], "top" # horizontal -> bottom: bottom
        elif w and h / w > 2:
            return self.subsections[1], "left" # vertical -> top: right
        else:
            return self.subsections[2], "left" # square -> bottom: top             
                        