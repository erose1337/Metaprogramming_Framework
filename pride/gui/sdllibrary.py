import itertools
import operator
import os
import sys
import string
import ctypes
import collections
import traceback

import pride
import pride.components.base as base
import pride.components.scheduler as scheduler
import pride.functions.utilities as utilities
import pride.gui
resolve_string = utilities.resolve_string
Instruction = pride.Instruction

import sdl2
import sdl2.ext
import sdl2.sdlttf
sdl2.ext.init()
sdl2.sdlttf.TTF_Init()
font_module = sdl2.sdlttf

def instruction_generator(instructions):
    always_on_top = []
    for layer in instructions.itervalues():
        for window_object in layer:
            if window_object.always_on_top:
                always_on_top.append(window_object)
            else:
                for operation in window_object._draw_operations:
                    yield operation
    for window_object in always_on_top:
        for operation in window_object._draw_operations:
            yield operation
    #for layer in instructions.itervalues():
    #    for window_object in (item for item in layer if item.scroll_instructions):
    #        for operation in window_object.scroll_instructions:
    #            yield operation

class SDL_Component(base.Proxy): pass


class SDL_Window(SDL_Component):

    defaults = {"size" : pride.gui.SCREEN_SIZE, "showing" : True,
                'position' : (0, 0), 'x' : 0, 'y' : 0, 'z' : 0,
                'w' : pride.gui.SCREEN_SIZE[0], 'h' : pride.gui.SCREEN_SIZE[1],
                "area" : (0, 0) + pride.gui.SCREEN_SIZE, "priority" : .04,
                "name" : "/Python", "texture_access_flag" : sdl2.SDL_TEXTUREACCESS_TARGET,
                "renderer_flags" : sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_TARGETTEXTURE,
                "software_renderer_flags" : sdl2.SDL_RENDERER_SOFTWARE | sdl2.SDL_RENDERER_TARGETTEXTURE,
                "window_flags" : None}#sdl2.SDL_WINDOW_BORDERLESS | sdl2.SDL_WINDOW_RESIZABLE}

    mutable_defaults = {"redraw_objects" : list, "predraw_queue" : list,
                        "postdraw_queue" : list,
                        "drawing_instructions" : collections.OrderedDict}

    predefaults = {"running" : False, "_ignore_invalidation" : None}

    def _get_size(self):
        return (self.w, self.h)
    def _set_size(self, size):
        self.w, self.h = size
    size = property(_get_size, _set_size)

    def _get_position(self):
        return self.x, self.y
    def _set_position(self, value):
        self.x, self.y = value
    position = property(_get_position, _set_position)

    def _get_area(self):
        return (self.x, self.y, self.w, self.h)
    def _set_area(self, rect):
        self.x, self.y, self.w, self.h = rect
    area = property(_get_area, _set_area)

    def _get_gui_children(self):
        return (child for child in self.children if hasattr(child, "pack"))
    gui_children = property(_get_gui_children)

    def __init__(self, **kwargs):
        super(SDL_Window, self).__init__(**kwargs)
        self.run_instruction = Instruction(self.reference, "run")
        self.sdl_window = self.reference

        window = sdl2.ext.Window(self.name, size=self.size, flags=self.window_flags)

        self.wraps(window)
        self.window_handler = self.create(Window_Handler)

        self.renderer = self.create(Renderer, self, predefaults=self.renderer_flags)
        self.user_input = self.create(SDL_User_Input)
        self.organizer = self.create("pride.gui.gui.Organizer")
        #self.texture_atlas = self.create("pride.gui.gui.Texture_Atlas", sdl_window=self.reference)
        self.drawing_instructions[0] = []

        if self.showing:
            self.show()

        self._texture = self.create_texture(self.renderer.max_size, self.texture_access_flag)

        objects["/Finalizer"].add_callback((self.reference, "delete"), 0)

    def create_texture(self, size, access=sdl2.SDL_TEXTUREACCESS_TARGET):
        _create_texture = self.renderer.sprite_factory.create_texture_sprite
        return _create_texture(self.renderer.wrapped_object, size, access=access)

    def invalidate_object(self, instance):
       # if instance is self._ignore_invalidation:
       #     return
        self._schedule_run()
        self.redraw_objects.append(instance)

    def _schedule_run(self):
        if not self.running:
            self.running = True
            self.run_instruction.execute(priority=self.priority)

    def create(self, *args, **kwargs):
        kwargs.setdefault("sdl_window", self.reference)
        instance = super(SDL_Window, self).create(*args, **kwargs)
        try:
            instance.pack()
        except AttributeError:
            pass
        return instance

    def remove_window_object(self, window_object):
        try:
            self.user_input._remove_from_coordinates(window_object.reference)
        except ValueError:
            pass
        try:
            self.user_input.always_on_top.remove(window_object)
        except ValueError:
            pass
        if self.user_input.under_mouse == window_object.reference:
            self.user_input.under_mouse = None
        try:
            self.redraw_objects.remove(window_object)
        except ValueError:
            pass
        try:
            self.drawing_instructions[window_object.z].remove(window_object)
        except (KeyError, ValueError):
            pass

    def run(self):
        self.organizer.pack_items()
        if self.predraw_queue:
            queue = self.predraw_queue[:]
            del self.predraw_queue[:]
            for callable in queue:
                callable()
        self.update_drawing_instructions()
        self.draw(instruction_generator(self.drawing_instructions))
        self.running = False
        if self.postdraw_queue:
            queue = self.postdraw_queue[:]
            del self.postdraw_queue[:]
            for callable in queue:
                callable()

    def update_drawing_instructions(self):
        instructions = self.drawing_instructions
        for window_object in self.redraw_objects:
            assert not window_object.deleted, window_object.reference
            old_z = self.user_input._update_coordinates(window_object,
                                                        window_object.reference,
                                                        window_object.area,
                                                        window_object.z)

            #draw_position = texture_atlas.add_to_atlas(window_object)
            #backup_position = window_object.position
            #self._ignore_invalidation = window_object
            #window_object.position = draw_position
        #    window_object.alert("Drawing")
            window_object._draw_texture()

            #window_object.position = backup_position
            #self._ignore_invalidation = None

            #instructions.extend(draw_operations)

            #copy_instruction = ("copy_subsection", draw_position + window_object.size, window_object.area)
            try:
                instructions[old_z].remove(window_object)
            except (KeyError, ValueError):
                pass
            z = window_object.z
            assert window_object not in instructions.get(z, [])
            #try:
            #    instructions[z].remove(window_object)
            #except (KeyError, ValueError):
            #    pass
            try:
                instructions[z].append(window_object)
            except KeyError:
                instructions[z] = [window_object]
        del self.redraw_objects[:]

    def draw(self, instructions):
        renderer = self.renderer
        draw_procedures = renderer.instructions
        texture = self._texture.texture
        renderer.set_render_target(texture)
        renderer.clear()
        for operation, args, kwargs in instructions:
            #if operation == "text" and not args[0]:
                #if not args[0]:
            #    continue
            draw_procedures[operation](*args, **kwargs)

        renderer.set_render_target(None)
        area = (0, 0, self.size[0], self.size[1])
        renderer.copy(texture, area, area)
        renderer.present()

    def schedule_predraw_operation(self, callable):
        self.predraw_queue.append(callable)

    def schedule_postdraw_operation(self, callable):
        self.postdraw_queue.append(callable)

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

    def delete(self):
        # delete window objects before sdl components
        for child in self.children:
            if hasattr(child, "pack"):
                child.delete()
        del self.predraw_queue[:]
        super(SDL_Window, self).delete()
        objects["/Finalizer"].remove_callback((self.reference, "delete"), 0)
        pride.Instruction.purge(self.reference)


class Window_Context(SDL_Window):

    defaults = {"showing" : False}

    def run(self):
        self.update_drawing_instructions()
        return list(instruction_generator(self.drawing_instructions))

    def invalidate_object(self, item):
        self.redraw_objects.append(item)


class Window_Handler(pride.components.base.Base):

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
                             sdl2.SDL_WINDOWEVENT_TAKE_FOCUS : self.handle_take_focus,
                             sdl2.SDL_WINDOWEVENT_CLOSE : self.handle_close}

    def handle_event(self, event):
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
            self.parent.user_input.active_item.held = False
        except AttributeError:
            pass

    def handle_focus_gained(self, event):
        self.parent.user_input._ignore_click = True

    def handle_focus_lost(self, event):
        try:
            self.parent.user_input.active_item.held = False
        except AttributeError:
            pass

    def handle_take_focus(self, event):
        pass

    def handle_close(self, event):
        pass


class SDL_User_Input(scheduler.Process):

    defaults = {"event_verbosity" : 0, "_ignore_click" : False, "active_item" : None,
                "under_mouse" : None}
    mutable_defaults = {"_layer_tracker" : collections.OrderedDict,
                        "always_on_top" : list}

    verbosity = {"handle_text_input" : "vvv"}

    def _get_active_item(self):
        return self._active_item
    def _set_active_item(self, value):
        self._active_item = value

    def __init__(self, **kwargs):
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

        self.setup_event_handler()

    def setup_event_handler(self):
        unhandled = self.handle_unhandled_event
        self.handlers = {"sdl2.SDL_DOLLARGESTURE" : unhandled,
                         "sdl2.SDL_DROPFILE" : unhandled,
                         "sdl2.SDL_FINGERMOTION" : unhandled,
                         "sdl2.SDL_FINGERDOWN" : unhandled,
                         "sdl2.SDL_FINGERUP" : unhandled,
                         "sdl2.SDL_FINGERMOTION" :unhandled,
                         "sdl2.SDL_KEYDOWN" : self.handle_keydown,
                         "sdl2.SDL_KEYUP" : self.handle_keyup,
                         "sdl2.SDL_JOYAXISMOTION" : unhandled,
                         "sdl2.SDL_JOYBALLMOTION" : unhandled,
                         "sdl2.SDL_JOYHATMOTION" : unhandled,
                         "sdl2.SDL_JOYBUTTONDOWN" : unhandled,
                         "sdl2.SDL_JOYBUTTONUP" : unhandled,
                         "sdl2.SDL_MOUSEMOTION" : self.handle_mousemotion,
                         "sdl2.SDL_MOUSEBUTTONDOWN" : self.handle_mousebuttondown,
                         "sdl2.SDL_MOUSEBUTTONUP" : self.handle_mousebuttonup,
                         "sdl2.SDL_MOUSEWHEEL" : self.handle_mousewheel,
                         "sdl2.SDL_MULTIGESTURE" : unhandled,
                         "sdl2.SDL_QUIT" : self.handle_quit,
                         "sdl2.SDL_SYSWMEVENT" : unhandled,
                         "sdl2.SDL_TEXTEDITING" : unhandled,
                         "sdl2.SDL_TEXTINPUT" : self.handle_textinput,
                         "sdl2.SDL_USEREVENT" : unhandled,
                         "sdl2.SDL_WINDOWEVENT" : self.parent.window_handler.handle_event}
        self.event_names = dict((resolve_string(key), key) for key, value in self.handlers.items())
        self.handlers = dict((resolve_string(key), value) for key, value in self.handlers.items())

    def run(self):
        handlers = self.handlers
        for event in sdl2.ext.get_events():
            try:
                handler = handlers[event.type]
            except KeyError:
                self.alert("Unhandled event: {}".format(self.event_names.get(event.type, event.type)), level=0)
            else:
                try:
                    handler(event)
                except Exception as error:
                    self.alert("Exception handling {};\n{}".format(self.event_names.get(event.type, event.type),
                                                                   traceback.format_exc()),
                                level=0)

    def _update_coordinates(self, item, reference, area, z):
        old_z = pride.objects[reference]._old_z
        try:
            self._layer_tracker[old_z].remove(reference)
        except (KeyError, ValueError):
            pass
        assert reference not in self._layer_tracker.get(z, []), (z, reference)
        try:
            self._layer_tracker[z].append(reference)
        except KeyError:
            self._layer_tracker[z] = [reference]
        pride.objects[reference]._old_z = z
        return old_z

    def _remove_from_coordinates(self, item):
        self._layer_tracker[pride.objects[item]._old_z].remove(item)
        assert pride.objects[item] not in self._layer_tracker.get(pride.objects[item].z, [])
        if self.active_item == item:
            self.active_item = None

    def handle_textinput(self, event):
        text = event.edit.text
        cursor = event.edit.start
        selection_length = event.edit.length
        self.alert("Handling textinput {} {} {}".format(text, cursor, selection_length),
                   level=self.verbosity["handle_text_input"])
        if self.active_item:
            instance = pride.objects[self.active_item]
            instance.text_entry(text)

    def handle_unhandled_event(self, event):
        self.alert("{0} passed unhandled".format(event.type), 'vv')

    def handle_quit(self, event):
        self.parent.delete()
        if "/User/Shell" not in pride.objects:
            raise SystemExit()

    def handle_mousebuttondown(self, event):
        mouse = event.button
        mouse_position = (mouse.x, mouse.y)
        self.alert("mouse button down at {}".format(mouse_position), level='v')

        active_item = self.under_mouse#self._get_object_under_mouse(mouse_position)
        objects = pride.objects

        # deselect old active item
        old_active_item = self.active_item
        if old_active_item and objects[old_active_item]._selected: # item can deselect itself
            try:
                objects[old_active_item].deselect(mouse, active_item)
            except KeyError:
                if old_active_item in objects:
                    raise

        # select new active item
        self.active_item = active_item
        try:
            objects[active_item].select(mouse)
        except KeyError:
            if active_item in objects:
                raise

        if active_item:
            if self._ignore_click:
                self._ignore_click = False
            else:
                try:
                    objects[active_item].press(mouse)
                except KeyError:
                    if active_item in objects:
                        raise
                    else:
                        self.alert("Active item has been deleted {}".format(active_item, ), level=0)
                        self.active_item = None

    def _get_object_under_mouse(self, mouse_position):
        # find the top-most item such that the mouse position is within its area
        objects = pride.objects
        active_item = None
        for item in self.always_on_top:
            if pride.gui.point_in_area(objects[item].area, mouse_position):
                active_item = item
                break
        else:
            for layer_number, layer in reversed(self._layer_tracker.items()):
                for item in layer:
                    assert item in objects
                    if pride.gui.point_in_area(objects[item].area, mouse_position):
                        active_item = item
                        break
                if active_item:
                    break
        return active_item

    def handle_mousebuttonup(self, event):
        active_item = self.active_item
        if active_item:
            instance = pride.objects[active_item]
            if instance.held:
                area = instance.area
                mouse = event.button
                if pride.gui.point_in_area(area, (mouse.x, mouse.y)):
                    instance.release(mouse)

    def handle_mousewheel(self, event):
        if self.active_item:
            wheel = event.wheel
            pride.objects[self.active_item].mousewheel(wheel.x, wheel.y)

    def handle_mousemotion(self, event):
        if self.active_item:
            motion = event.motion
            pride.objects[self.active_item].mousemotion(motion.xrel, motion.yrel)
        #else:
        motion = event.motion
        position = (motion.x, motion.y)
        if not self.under_mouse:
            self.under_mouse = under_mouse = self._get_object_under_mouse(position)
            try:
                pride.objects[under_mouse].on_hover()
            except KeyError:
                if under_mouse is not None:
                    raise
        else:

            under_mouse = pride.objects[self.under_mouse]
            if under_mouse.children:
                new_under_mouse = self._get_object_under_mouse(position)
                if under_mouse.reference != new_under_mouse:
                    under_mouse.hover_ends()
                    self.under_mouse = new_under_mouse
                    pride.objects[new_under_mouse].on_hover()
            else:
                if not pride.gui.point_in_area(under_mouse.area, position):
                    under_mouse.held = False 
                    new_under_mouse = self._get_object_under_mouse(position)
                    under_mouse.hover_ends()
                    self.under_mouse = new_under_mouse
                    pride.objects[new_under_mouse].on_hover()
        #    pride.objects[self.under_mouse].mousemotion(position.xrel, position.yrel)
            #if not pride.gui.point_in_area(under_mouse.area, position):
            #    under_mouse.hover_ends()
            #    self.under_mouse = under_mouse = self._get_object_under_mouse(position)
            #    pride.objects[under_mouse].on_hover()
        #    else:
        #        print("Mouse still within {}".format(under_mouse))

    def handle_keydown(self, event):
        try:
            instance = pride.objects[self.active_item]
        except KeyError:
            if self.active_item is not None:
                self.alert("No instance of '{}' to handle keystrokes".format(self.active_item), level='v')
            else:
                self.alert("Active item is None; unable to handle keystrokes", level='v')
            return

        key_value = event.key.keysym.sym
        modifier = event.key.keysym.mod

      #  if key_value < 256 or key_value > 0: # in ascii range

        try:
            key = chr(key_value)
        except ValueError:
            return # key was a modifier key
        else:
            if key == "\r":
                key = "\n"
            key_press = [key, None]

            if modifier in self.uppercase_modifiers:
                try:
                    key = self.uppercase[key]
                except KeyError:
                    pass
            elif modifier:
                key_press[1] = modifier

            if ord(key) < 32 or key_press[1] is not None:
                reference, method = self.get_hotkey(instance, tuple(key_press))
                if reference is not None:
                    getattr(pride.objects[reference], method)()

    def get_hotkey(self, instance, key_press):
        if key_press in instance.hotkeys:
            callback_info = (instance.reference, instance.hotkeys[key_press])
        else:
            try:
                callback_info = self.get_hotkey(instance.parent, key_press)
            except AttributeError:
                callback_info = (None, None)
        return callback_info

    def handle_keyup(self, event):
        pass

    def save(self):
        with pride.functions.contextmanagers.backup(self, "handlers", "_layer_tracker"):
            self.handlers = None
            self._layer_tracker = self._layer_tracker.items()
            attributes = super(SDL_User_Input, self).save()
        return attributes

    def on_load(self, attributes):
        super(SDL_User_Input, self).on_load(attributes)
        self.setup_event_handler()


class Renderer(SDL_Component):

    defaults = {"flags" : sdl2.SDL_RENDERER_ACCELERATED,
                "blendmode_flag" : sdl2.SDL_BLENDMODE_BLEND, # SDL_BLENDMODE_ADD for slider puzzles?
                "logical_size" : (800, 600)}

    def __init__(self, window, **kwargs):
        super(Renderer, self).__init__(**kwargs)

        self.wraps(sdl2.ext.Renderer(window, flags=self.flags))

        self.blendmode = self.blendmode_flag

        self.sprite_factory = self.create(Sprite_Factory)
        self.font_manager = self.create(Font_Manager)
        self.instructions = dict((name, getattr(self, "draw_" + name)) for
                                  name in ("point", "line", "rect", "rect_width", "text"))
        self.instructions["fill"] = self.fill
        self.instructions["copy"] = self.copy
        self.instructions["copy_subsection"] = self.render_copy
        #self.instructions["copyex"] = self.copyex
        self.clear()

        info = self.get_renderer_info()
        self.max_size = (info.max_texture_width, info.max_texture_height)

    def render_copy(self, source_area, destination_area):
        self.copy(self.parent._texture.texture, source_area, destination_area)

    def draw_text(self, area, text, **kwargs):
        x, y, w, h = area
        assert w
        #kwargs.setdefault("width", w)
        ellipses = ''
        _text = text
        assert "width" in kwargs
        hide_excess = False#kwargs.get("hide_excess_text", False) # needs to be re-done
        while True:
            texture = self.sprite_factory.from_text(text + ellipses,
                                                    fontmanager=self.font_manager,
                                                    **kwargs)
            _w, _h = texture.size
            if kwargs.get("center_text", False) and _w <= (w + 40): # +40? seems to fix scaled text snapping between centered/not
                    destination = ((x + (w / 2)) - (_w / 2),
                                   (y + (h / 2)) - (_h / 2),
                                   _w - 2, _h)
            else:
                destination = (x + 2, y + 2, _w - 2, _h)

            if hide_excess:
                if destination[2] <= w - 12:
                    break
                else:
                #    print "Shrinking...", destination, area
                    text = text[:-3]
                    ellipses = "..."
                    if not text:
                        text = _text
                        break
            else:
                break
        self.copy(texture, dstrect=destination)

    def get_text_size(self, area, text, **kwargs):
        x, y, w, h = area
        kwargs.setdefault("w", w)
        texture = self.sprite_factory.from_text(text,
                                                fontmanager=self.font_manager,
                                                **kwargs)
        return texture.size

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

    def draw(self, texture, draw_instructions, background=None, clear=True):
        self.set_render_target(texture)
        if clear:
            self.clear()
        if background:
            self.copy(background)

        instructions = self.instructions
        for shape, args, kwargs in draw_instructions:
            instructions[shape](*args, **kwargs)
        self.set_render_target(None)
        return texture

    def get_renderer_info(self):
        info = sdl2.SDL_RendererInfo()
        sdl2.SDL_GetRendererInfo(self.renderer, info)
        return info


class Sprite_Factory(SDL_Component):

    def __init__(self, **kwargs):
        super(Sprite_Factory, self).__init__(**kwargs)
        self.wraps(sdl2.ext.SpriteFactory(renderer=self.parent))

    def save(self):
        sprite_factory = self.wrapped_object
        self.wraps(None)
        attributes = super(Sprite_Factory, self).save()
        self.wraps(sprite_factory)
        print "\n\n\nReturning: ", attributes
        return attributes


class Font_Manager(SDL_Component):

    defaults = {"font_path" : os.path.join(pride.gui.PACKAGE_LOCATION,
                                           "resources", "fonts", "Aero.ttf"),
                "default_font_size" : 14, "default_color" : (150, 150, 255),
                "default_background" : (0, 0, 0)}

    def __init__(self, **kwargs):
        _defaults = self.defaults
        options = {"font_path" : _defaults["font_path"],
                   "size" : _defaults["default_font_size"],
                   "color" : _defaults["default_color"],
                   "bg_color" : _defaults["default_background"]}
        kwargs["wrapped_object"] = sdl2.ext.FontManager(**options)
        super(Font_Manager, self).__init__(**kwargs)

    def save(self):
        raise NotImplementedError()
        with pride.functions.contextmanagers.backup(self, "_bgcolor", "_textcolor", "_default_font", "fonts"):
            color = self._bgcolor
            self._bgcolor = (color.r, color.g, color.b, color.a)

            text_color = self._textcolor
            self._textcolor = (color.r, color.g, color.b, color.a)

            self.fonts = {}

            default_font = self._default_font
            self._default_font = self.defaults["font_path"]
            attributes = super(Font_Manager, self).save()
        return attributes

    def on_load(self, attributes):
        color = attributes["_bgcolor"]
        attributes["_bgcolor"] = sdl2.ext.Color(*color)

        text_color = attributes["_textcolor"]
        attributes["_textcolor"] = sdl2.ext.Color(*text_color)
        raise NotImplementedError()
        #options = {"font_path" : attributes["font_path"],
        #           "size" : attributes["default_font_size"],
        #           "color" : attributes["default_color"],
        #           "bg_color" : attributes["default_background"]}
        #attributes["wrapped_object"] = sdl2.ext.FontManager(**options)

        super(Font_Manager, self).on_load(attributes)
