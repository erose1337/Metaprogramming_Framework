import os
import sys
import string
import ctypes
import collections
import StringIO

import mpre
import mpre.base as base
import mpre.vmlibrary as vmlibrary
import mpre.utilities as utilities
import mpre.gui
Instruction = mpre.Instruction
objects = mpre.objects

import sdl2
import sdl2.ext
import sdl2.sdlttf
sdl2.ext.init()
sdl2.sdlttf.TTF_Init()
font_module = sdl2.sdlttf

class SDL_Component(base.Proxy):

    defaults = base.Proxy.defaults.copy()
    

class SDL_Window(SDL_Component):

    defaults = SDL_Component.defaults.copy()
    defaults.update({"size" : mpre.gui.SCREEN_SIZE,
                     "showing" : True,
                     'position' : (0, 0),
                     'x' : 0,
                     'y' : 0,
                     'z' : 0,
                     'w' : mpre.gui.SCREEN_SIZE[0],
                     'h' : mpre.gui.SCREEN_SIZE[1],
                     "area" : (0, 0) + mpre.gui.SCREEN_SIZE,
                     "name" : "Metapython",
                     "renderer_flags" : sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_TARGETTEXTURE,
                     "window_flags" : None, #sdl2.SDL_WINDOW_BORDERLESS, # | sdl2.SDL_WINDOW_RESIZABLE 
                     "priority" : .04})
    
    def _get_size(self):
        return (self.w, self.h)
    def _set_size(self, size):
        self.w, self.h = size
    size = property(_get_size, _set_size)
    
    def __init__(self, **kwargs):
        self.max_layer, self.invalid_layer = 1, 0
        self.children = []
        self.layers = collections.OrderedDict((x, (None, [])) for 
                                               x in xrange(100))
        self.latency = utilities.Latency(name="framerate")
        self.running = False
        
        super(SDL_Window, self).__init__(**kwargs)
        window = sdl2.ext.Window(self.name, size=self.size, 
                                 flags=self.window_flags)
        self.wraps(window)
        self.create(Window_Handler)
        
        self.renderer = self.create(Renderer, self, flags=self.renderer_flags)
        self.user_input = self.create(SDL_User_Input)
        self.run_instruction = Instruction(self.instance_name, "run")
               
        if self.showing:
            self.show()  

    def invalidate_layer(self, layer):
        self.invalid_layer = min(self.invalid_layer, layer)
        if not self.running:
            self.running = True
            self.run_instruction.execute(priority=self.priority)
    
    def remove_from_layer(self, instance, z):
        self.layers[z][1].remove(instance)
        
    def set_layer(self, instance, value):
        z = instance.z
        try:
            self.layers[z][1].remove(instance)
        except ValueError:
            pass
        self.layers[value][1].append(instance)    
        self.max_layer = max(value, self.max_layer)
                
    def create(self, *args, **kwargs):
        instance = super(SDL_Window, self).create(*args, **kwargs)
        if hasattr(instance, 'pack'):
            instance.pack()
        return instance
        
    def run(self):
        renderer = self.renderer
        draw_instructions = renderer.instructions
        renderer.set_render_target(None)
        renderer.clear()
                
        user_input = objects["SDL_User_Input"]
        layers = self.layers
        screen_width, screen_height = self.size
      #  print
        for layer_number in xrange(self.invalid_layer, self.max_layer + 1):
        #    self.alert("Drawing layer: {}", [layer_number], level=0)
            layer_info = layers[layer_number]
            
            layer_texture, layer_components = layer_info
            if layer_texture is None:
                layer_texture = mpre.gui.gui.create_texture(self.size)
                layers[layer_number] = (layer_texture, layer_components)
            renderer.set_render_target(layer_texture.texture)
            renderer.clear()
            
            if layer_number:
                # copy previous layer as background
                renderer.copy(layers[layer_number - 1][0])
        
            for instance in layer_components:
                srcrect = x, y, w, h = instance.area
                user_input._update_coordinates(instance.instance_name, srcrect, instance.z)
                
      #          x += instance.texture_window_x
      #          y += instance.texture_window_y
                if x + w > screen_width:
                    w = screen_width - x
                if y + h > screen_height:
                    h = screen_height - y               
                area = (x, y, w, h)
               # srcrect = (x + instance.texture_window_x, y + instance.texture_window_y,
               #            w, h)
                if instance.texture_invalid:
                 #   self.alert("Redrawing {} texture", [instance], level=0)
                    _texture = instance.texture.texture
                    instance.draw_texture()
                    renderer.set_render_target(_texture)
                    for operation, args, kwargs in instance._draw_operations:
                        if operation == "text":
                            if not args[0]:
                                continue
                        draw_instructions[operation](*args, **kwargs)
                        
                    instance._draw_operations = []
                    renderer.set_render_target(layer_texture.texture)
                    instance.texture_invalid = False
               # self.alert("Copying {} texture to {}", [instance, area], level=0)
                renderer.copy(instance.texture.texture, 
                              srcrect=(x + instance.texture_window_x, 
                                       y + instance.texture_window_y, w, h), dstrect=area)
                
        self.invalid_layer = self.max_layer
        renderer.set_render_target(None)
        renderer.copy(layer_texture)
        renderer.present()
        self.running = False
        
    def get_mouse_state(self):
        mouse = sdl2.mouse
        x = ctypes.c_long(0)
        y = ctypes.c_long(0)
        buttons = mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))

        states = (mouse.SDL_BUTTON_LMASK, mouse.SDL_BUTTON_RMASK, mouse.SDL_BUTTON_MMASK,
                  mouse.SDL_BUTTON_X1MASK, mouse.SDL_BUTTON_X2MASK)
        return ((x.value, y.value), map(lambda mask: buttons & mask, states))

    def get_mouse_position(self):
        return self.get_mouse_state()[0]

    def pack(self, modifiers=None):
        pass
            
            
class Window_Handler(mpre.base.Base):
    
    def __init__(self, **kwargs):
        super(Window_Handler, self).__init__(**kwargs)
        self.event_switch = {sdl2.SDL_WINDOWEVENT_SHOWN : self.handle_shown,
                             sdl2.SDL_WINDOWEVENT_HIDDEN : self.handle_hidden,
                             sdl2.SDL_WINDOWEVENT_EXPOSED : self.handle_exposed,
                             sdl2.SDL_WINDOWEVENT_MOVED :  self.handle_moved,
                             sdl2.SDL_WINDOWEVENT_RESIZED : self.handle_resized,
                             sdl2.SDL_WINDOWEVENT_SIZE_CHANGED : self.handle_size_changed,
                             sdl2.SDL_WINDOWEVENT_MINIMIZED : self.handle_minimized,
                             sdl2.SDL_WINDOWEVENT_MAXIMIZED : self.handle_maximized,
                             sdl2.SDL_WINDOWEVENT_RESTORED : self.handle_restored,
                             sdl2.SDL_WINDOWEVENT_ENTER : self.handle_enter,
                             sdl2.SDL_WINDOWEVENT_LEAVE : self.handle_leave,
                             sdl2.SDL_WINDOWEVENT_FOCUS_GAINED : self.handle_focus_gained,
                             sdl2.SDL_WINDOWEVENT_FOCUS_LOST : self.handle_focus_lost,
                             sdl2.SDL_WINDOWEVENT_CLOSE : self.handle_close}
    
    def handle_event(self, event):
     #   self.alert("Handling {}", [self.event_switch[event.window.event]], level=0)
        self.event_switch[event.window.event](event)
        
    def handle_shown(self, event):
        pass
        
    def handle_hidden(self, event):
        pass
        
    def handle_exposed(self, event):
        pass
        
    def handle_moved(self, event):
        pass
        
    def handle_resized(self, event):
        pass
        
    def handle_size_changed(self, event):
        pass
        
    def handle_minimized(self, event):
        pass
        
    def handle_maximized(self, event):
        pass
        
    def handle_restored(self, event):
        pass
        
    def handle_enter(self, event):
        pass
        
    def handle_leave(self, event):
        try:
            objects["SDL_User_Input"].active_item.held = False
        except AttributeError:
            pass
        
    def handle_focus_gained(self, event):
        objects["SDL_User_Input"]._ignore_click = True
        
    def handle_focus_lost(self, event):
        try:
            objects["SDL_User_Input"].active_item.held = False
        except AttributeError:
            pass
                
    def handle_close(self, event):
        pass
        
        
class SDL_User_Input(vmlibrary.Process):

    defaults = vmlibrary.Process.defaults.copy()
    defaults.update({"event_verbosity" : 0,
                     "_ignore_click" : False,
                     "active_item" : None})
    
    def _get_active_item(self):
        return self._active_item
    def _set_active_item(self, value):
        self._active_item = value
        
    def __init__(self, **kwargs):
        self.coordinate_tracker = {}
        self._coordinate_tracker = collections.OrderedDict()
        self.popups = []
        self._stringio = StringIO.StringIO()
        super(SDL_User_Input, self).__init__(**kwargs)
        self.uppercase_modifiers = (sdl2.KMOD_SHIFT, sdl2.KMOD_CAPS,
                                    sdl2.KMOD_LSHIFT, sdl2.KMOD_RSHIFT)
        uppercase = self.uppercase = {'1' : '!',
                                      '2' : '@',
                                      '3' : '#',
                                      '4' : '$',
                                      '5' : '%',
                                      '6' : '^',
                                      '7' : '&',
                                      '8' : '*',
                                      '9' : '(',
                                      '0' : ')',
                                      ";" : ':',
                                      '\'' : '"',
                                      '[' : ']',
                                      ',' : '<',
                                      '.' : '>',
                                      '/' : "?",
                                      '-' : "_",
                                      '=' : "+",
                                      '\\' : "|",
                                      '`' : "~"}
        letters = string.ascii_letters
        for index, character in enumerate(letters[:26]):
            uppercase[character] = letters[index+26]

        # for not yet implemented features
        unhandled = self.handle_unhandled_event

        self.handlers = {sdl2.SDL_DOLLARGESTURE : unhandled,
                         sdl2.SDL_DROPFILE : unhandled,
                         sdl2.SDL_FINGERMOTION : unhandled,
                         sdl2.SDL_FINGERDOWN : unhandled,
                         sdl2.SDL_FINGERUP : unhandled,
                         sdl2.SDL_FINGERMOTION :unhandled,
                         sdl2.SDL_KEYDOWN : self.handle_keydown,
                         sdl2.SDL_KEYUP : self.handle_keyup,
                         sdl2.SDL_JOYAXISMOTION : unhandled,
                         sdl2.SDL_JOYBALLMOTION : unhandled,
                         sdl2.SDL_JOYHATMOTION : unhandled,
                         sdl2.SDL_JOYBUTTONDOWN : unhandled,
                         sdl2.SDL_JOYBUTTONUP : unhandled,
                         sdl2.SDL_MOUSEMOTION : self.handle_mousemotion,
                         sdl2.SDL_MOUSEBUTTONDOWN : self.handle_mousebuttondown,
                         sdl2.SDL_MOUSEBUTTONUP : self.handle_mousebuttonup,
                         sdl2.SDL_MOUSEWHEEL : self.handle_mousewheel,
                         sdl2.SDL_MULTIGESTURE : unhandled,
                         sdl2.SDL_QUIT : self.handle_quit,
                         sdl2.SDL_SYSWMEVENT : unhandled,
                         sdl2.SDL_TEXTEDITING : unhandled,
                         sdl2.SDL_TEXTINPUT : self.handle_textinput,
                         sdl2.SDL_USEREVENT : unhandled,
                         sdl2.SDL_WINDOWEVENT : objects["Window_Handler"].handle_event}

    def run(self):
        handlers = self.handlers
        for event in sdl2.ext.get_events():
            try:
                handlers[event.type](event)
            except KeyError:
                self.alert("Unhandled event: {}".format(event.type))

    def _update_coordinates(self, item, area, z):
        try:
            _, old_z = self.coordinate_tracker[item]
        except KeyError:
            try:
                self._coordinate_tracker[z].append(item)
            except KeyError:
                self._coordinate_tracker[z] = [item]
        else:            
            self._coordinate_tracker[old_z].remove(item)
            self._coordinate_tracker[z].append(item)
        self.coordinate_tracker[item] = (area, z)
        
    def _remove_from_coordinates(self, item):
        _, old_z = self.coordinate_tracker[item]
        self._coordinate_tracker[old_z].remove(item)
        del self.coordinate_tracker[item]
        if self.active_item == item:
            self.active_item = None
    
    def handle_textinput(self, event):
        text = event.edit.text
        cursor = event.edit.start
        selection_length = event.edit.length
        self.alert("Handling textinput {} {} {}",
                   (text, cursor, selection_length), level='vv')
        if self.active_item:
            instance = objects[self.active_item]
            print "Instance allows text edit: ", instance.allow_text_edit
            if instance.allow_text_edit:
                instance.text += text
        
    def handle_unhandled_event(self, event):        
        self.alert("{0} passed unhandled", [event.type], 'vv')

    def handle_quit(self, event):
        sys.exit()
        
    def handle_mousebuttondown(self, event):        
        mouse = event.button
        mouse_position = (mouse.x, mouse.y)
        self.alert("mouse button down at {}", [mouse_position], level='v')        
        active_item = None
        max_z = 0
        coordinates = self.coordinate_tracker
        for layer_number, layer in reversed(self._coordinate_tracker.items()):
            for item in layer:
                area, z = coordinates[item]
                if mpre.gui.point_in_area(area, mouse_position):
                    active_item = item
                    break
            if active_item:
                break

        self.active_item = active_item
        if active_item:
            if self._ignore_click:
                self._ignore_click = False
            else:
                mpre.objects[active_item].press(mouse)
            
    def handle_mousebuttonup(self, event):
        active_item = self.active_item
        if active_item:            
            instance = mpre.objects[active_item]
            if instance.held:
                area, z = self.coordinate_tracker[active_item]
                mouse = event.button
                if mpre.gui.point_in_area(area, (mouse.x, mouse.y)):
                    instance.release(mouse)
       
    def handle_mousewheel(self, event):
        if self.active_item:
            wheel = event.wheel
            mpre.objects[self.active_item].mousewheel(wheel.x, wheel.y)

    def handle_mousemotion(self, event):        
        if self.active_item:
            motion = event.motion
            mpre.objects[self.active_item].mousemotion(motion.xrel, motion.yrel)

    def handle_keydown(self, event):
        pass
    #    try:
    #        instance = mpre.objects[self.active_item]
    #    except KeyError:
    #        self.alert("No instance '{}' to handle keystrokes".format(self.active_item), level='v')
    #        return
    #    try:
    #        key = chr(event.key.keysym.sym)
    #    except ValueError:
    #        return # key was a modifier key
    #    else:
    #        if key == "\r":
    #            key = "\n"
    #        modifier = event.key.keysym.mod
    #        if modifier in self.uppercase_modifiers:
    #            try:
    #                key = self.uppercase[key]
    #            except KeyError:
    #                pass            
    #        elif modifier:
    #            hotkey = self.get_hotkey(instance, (key, modifier))
    #            if hotkey:
    #                hotkey.execute()
    #            
    #        elif instance.allow_text_edit:                
    #            if ord(key) == 8: # backspace
    #                instance.text = instance.text[:-1]
    #            else:
    #                instance.text += key
    #                                
    #            #print "Changed {}.text to {}".format(self.active_item, self.active_item.text)
                
    def get_hotkey(self, instance, key_press):
        try:
            hotkey = instance.hotkeys.get(key_press)
            if not hotkey:
                hotkey = self.get_hotkey(instance.parent, key_press)
        except AttributeError:
            hotkey = None
        return hotkey

    def handle_keyup(self, event):
        pass


class Renderer(SDL_Component):

    defaults = SDL_Component.defaults.copy()
    defaults.update({"flags" : sdl2.SDL_RENDERER_ACCELERATED,
                     "blendmode_flag" : sdl2.SDL_BLENDMODE_BLEND})
                
    def __init__(self, window, **kwargs):      
        super(Renderer, self).__init__(**kwargs)
        self.wraps(sdl2.ext.Renderer(window, flags=self.flags))
        self.blendmode = self.blendmode_flag
        
        self.sprite_factory = self.create(Sprite_Factory, renderer=self)
        self.font_manager = self.create(Font_Manager)
        self.instructions = dict((name, getattr(self, "draw_" + name)) for 
                                  name in ("point", "line", "rect", "rect_width", "text"))
        self.instructions["fill"] = self.fill
        self.clear()
        
    def draw_text(self, area, text, **kwargs):
        x, y, w, h = area
        kwargs.setdefault("width", w)
        texture = self.sprite_factory.from_text(text, fontmanager=self.font_manager, 
                                                **kwargs)        
        _w, _h = texture.size
        self.copy(texture, dstrect=(x + 2, y + 2, 
                                    (_w if _w < w else w) - 2,
                                    _h))
        
    def draw_rect_width(self, area, **kwargs):
        width = kwargs.pop("width")
        x, y, w, h = area        
        
        for rect_size in xrange(1, width + 1):
            new_x = x + rect_size
            new_y = y + rect_size
            new_w = w - rect_size
            new_h = h - rect_size
            self.draw_rect((new_x, new_y, new_w, new_h), **kwargs)

    def merge_layers(self, textures):
        self.clear()
        for texture in textures:
            self.copy(texture)
        return self.sprite_factory.from_surface(self.rendertarget.get_surface())
    
    def set_render_target(self, texture):            
        code = sdl2.SDL_SetRenderTarget(self.wrapped_object.renderer, texture)
        if code < 0:
            raise ValueError("error code {}. Could not set render target of renderer {} to texture {}".format(code, self.wrapped_object.renderer, texture))
            
    def draw(self, texture, draw_instructions, background=None):
        self.set_render_target(texture)
        self.clear()
        if background:
            self.copy(background)               

        instructions = self.instructions
        for shape, args, kwargs in draw_instructions:
            instructions[shape](*args, **kwargs)     
        self.set_render_target(None)
        return texture
        
        
class Sprite_Factory(SDL_Component):

    defaults = SDL_Component.defaults.copy()

    def __init__(self, **kwargs):
        kwargs["wrapped_object"] = sdl2.ext.SpriteFactory(renderer=kwargs["renderer"])
        super(Sprite_Factory, self).__init__(**kwargs)


class Font_Manager(SDL_Component):

    defaults = SDL_Component.defaults.copy()
    defaults.update({"font_path" : os.path.join(mpre.gui.PACKAGE_LOCATION,
                                                "resources", "fonts", 
                                                "Aero.ttf"),
                     "default_font_size" : 14,
                     "default_color" : (150, 150, 255),
                     "default_background" : (0, 0, 0)})

    def __init__(self, **kwargs):
        _defaults = self.defaults
        options = {"font_path" : _defaults["font_path"],
                   "size" : _defaults["default_font_size"],
                   "color" : _defaults["default_color"],
                   "bg_color" : _defaults["default_background"]}
        kwargs["wrapped_object"] = sdl2.ext.FontManager(**options)
        super(Font_Manager, self).__init__(**kwargs)