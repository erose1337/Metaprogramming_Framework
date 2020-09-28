""" pride.gui.sdllibrary contains the components that are responsible for:

    - Creating/managing OS-level windows
    - Drawing to those windows
    - Capturing user input in those windows

The api is designed to work with the `Window_Object`s provided by `pride.gui.gui`.
`SDL_Component`s are a `Proxy` for pysdl2 components, which are wrappers around SDL2 components.
They extend the behavior of the underlying objects and adapt them for use with the rest of the system.
"""

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
timestamp = utilities.timestamp

import sdl2
import sdl2.ext
import sdl2.sdlttf
import sdl2.sdlgfx
sdl2.ext.init()
sdl2.sdlttf.TTF_Init()
font_module = sdl2.sdlttf

COPY_BLENDMODE = sdl2.SDL_BLENDMODE_ADD
DRAW_BLENDMODE = sdl2.SDL_BLENDMODE_NONE
TEXT_BLENDMODE = sdl2.SDL_BLENDMODE_BLEND

def condense_instructions(layer):
    raise NotImplementedError()
    for operation_infos in zip(*(item._draw_operations for item in layer)):
        if len(operation_infos) == 1:
            # only one operation; unable to batch
            #print operation_infos
            print("Yielding1 {}".format(len(operation_infos[0])))
            yield operation_infos[0]
            raise StopIteration()
        print operation_infos[0][0]
        rects = []
        fills = []
        other = []
        for op in operation_infos:
            if op[0] == "rect":
                rects.append(op)
            elif op[0] == "fill":
                fills.append(op)
            else:
                other.append(op)
        if operation_infos[0][0] in ("rect", "fill"):
            distinct = []
            areas = []
            extra = []
            for op_info in operation_infos:
                if op_info[0] not in ("rect", "fill"):
                    extra.append(op_info)
                    continue
                if op_info[2] not in distinct:
                    distinct.append(op_info[2])
                    areas.append([op_info[1][0]])
                else:
                    areas[distinct.index(op_info[2])].append(op_info[1][0])

            #for i, kwargs in enumerate(distinct):
            #    yield op_info[0], areas[i], kwargs
            new_instructions = tuple((op_info[0], (areas[i], ), kwargs) for i, kwargs
                                     in enumerate(distinct)) #+ tuple(extra)
            for item in new_instructions:
                a, b, c = item
                print("Yielding2 {} {}".format(len(item), item))
                yield item#a, b, c
            #yield new_instructions
        else:
            for op in operation_infos:
                assert len(op) == 3, op
                print("Yielding3 {} {}".format(len(item), item))
                yield op
            #print operation_infos
            #raw_input()

class SDL_Component(base.Proxy): pass


class SDL_Window(SDL_Component):

    defaults = {"showing" : True,
                'x' : 0, 'y' : 0, 'z' : 0, 'w' : 1024, 'h' : 768,#pride.gui.SCREEN_SIZE[0], 'h' : pride.gui.SCREEN_SIZE[1],
                "priority" : .038, "name" : "/Program",
                "tip_bar_type" : "pride.gui.gui.Container", "tip_bar_h_range" : (0, .05),
                "tip_bar_location" : "bottom",
                "texture_access_flag" : sdl2.SDL_TEXTUREACCESS_TARGET,
                "renderer_flags" : sdl2.SDL_RENDERER_ACCELERATED | sdl2.SDL_RENDERER_TARGETTEXTURE,
                "window_flags" : None}#sdl2.SDL_WINDOW_BORDERLESS | sdl2.SDL_WINDOW_RESIZABLE}

    mutable_defaults = {"redraw_objects" : list,
                        "layer_cache" : list, "dirty_layers" : set,
                        "predraw_queue" : list, "postdraw_scheduled" : dict,
                        "drawing_instructions" : collections.OrderedDict}

    predefaults = {"running" : False, "_ignore_invalidation" : None,
                   "_in_pack_queue" : False} # smoothes Organizer optimization out

    autoreferences = ("tip_bar", )

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

        self.sdl_window = self # children may attempt to access the sdl_window attribute of their parent
        window = sdl2.ext.Window(self.name, position=self.position,
                                 size=self.size, flags=self.window_flags)
        self.position = (0, 0) # position is used above to set initial window position; it is zero'd here because it would confuse the Organizer otherwise
        self.wraps(window)
        self.window_handler = self.create(Window_Handler)

        self.renderer = self.create(Renderer, self, predefaults=self.renderer_flags)
        self.user_input = self.create(SDL_User_Input)
        self.organizer = self.create("pride.gui.gui.Organizer")
        #self.texture_atlas = self.create("pride.gui.gui.Texture_Atlas", sdl_window=self.reference)
        self.drawing_instructions[0] = []

        self.tip_bar = self.create(self.tip_bar_type, location=self.tip_bar_location,
                                   h_range=self.tip_bar_h_range, center_text=False,
                                   tip_bar_text="Tip Bar: Provides details, hints, and status information")
        if self.showing:
            self.show()

        # for drawing always_on_top separately
        self.top_texture = self.create_texture(self.renderer.max_size,
                                               self.texture_access_flag)

        objects["/Finalizer"].add_callback((self.reference, "delete"), 0)
        self.run_instruction.execute(priority=self.priority)

    def create_texture(self, size, access=sdl2.SDL_TEXTUREACCESS_TARGET,
                       blendmode=COPY_BLENDMODE):
        _create_texture = self.renderer.sprite_factory.create_texture_sprite
        texture = _create_texture(self.renderer.wrapped_object, size, access=access)
        sdl2.SDL_SetTextureBlendMode(texture.texture, blendmode)
        return texture

    def cache_operations(self, size, draw_operations):
        texture = self.create_texture(size)
        self.renderer.draw(texture.texture, draw_operations)
        return texture

    def invalidate_object(self, instance):
        assert not instance.deleted
        self._schedule_run()
        self.redraw_objects.append(instance)

    def _schedule_run(self):
        if not self.running:
            self.running = True

    def create(self, *args, **kwargs):
        kwargs.setdefault("sdl_window", self)
        instance = super(SDL_Window, self).create(*args, **kwargs)
        try:
            instance.pack()
        except AttributeError:
            pass
        return instance

    def remove_window_object(self, window_object):
        try:
            del self.postdraw_scheduled[window_object]
        except KeyError:
            pass
        try:
            self.user_input._remove_from_coordinates(window_object.reference)
        except ValueError:
            pass
        try:
            self.user_input.always_on_top.remove(window_object)
        except ValueError:
            pass
        if self.user_input.under_mouse == window_object:
            self.user_input.under_mouse = None
        try:
            self.redraw_objects.remove(window_object)
        except ValueError:
            pass
        window_object.texture_invalid = False # texture_invalid reflects whether or not window_object is in redraw_objects
        try:
            self.drawing_instructions[window_object.z].remove(window_object)
        except (KeyError, ValueError):
            pass
        if not self.redraw_objects:
            self.running = True # trigger run to wipe out the screen

    def run(self):
        #frame_start = timestamp()
        self.run_instruction.execute(priority=self.priority)
        assert not any(caller.deleted for caller in self.postdraw_scheduled.keys())
        self.user_input.run()

        if self.predraw_queue:
            queue = self.predraw_queue
            self.predraw_queue = []
            for callable in queue:
                callable()

        organizer = self.organizer
        if organizer.pack_queue or organizer.window_queue:
            organizer.pack_items()

        #before = timestamp()
        if self.redraw_objects:
            self.update_drawing_instructions() # tends to take more time than the draw+present loop
        #after = timestamp()
        #print("Time taken to reorganize draw instructions: {0:.5f}".format(after - before))
        assert not self.redraw_objects

        #before = timestamp()
        if self.running:
            self.draw(self.drawing_instructions) # tends to take less time than re-arranging draw instructions
            assert not self.redraw_objects
        self.running = False
        #after = timestamp()
        #print("Time taken to redraw and present:           {0:.5f}".format(after - before))

        #if self.take_screenshot:


        if self.postdraw_scheduled:
            assert not any(caller.deleted for caller in self.postdraw_scheduled.keys())
            queue = itertools.chain(*self.postdraw_scheduled.values())
            self.postdraw_scheduled = dict()
            for callable in queue:
                callable()
        #frame_end = timestamp()
        #print("Allocated {0:.5f}; Used: {1:.5f}; Spare: {2:.5f}".format(self.priority, frame_end - frame_start, self.priority - (frame_end - frame_start)))

    def update_drawing_instructions(self):
        instructions = self.drawing_instructions
        layer_cache = self.layer_cache
        dirty_layers = self.dirty_layers
        _size = self.size
        needs_sorting = False
        #print("Redoing {} different drawing instructions".format(len(self.redraw_objects)))
        for window_object in self.redraw_objects:
            assert not window_object.deleted, window_object.reference
            assert not window_object.hidden, window_object
            old_z = self.user_input._update_coordinates(window_object,
                                                        window_object.reference,
                                                        window_object.area,
                                                        window_object.z)
            window_object._redraw()

            z = window_object.z
            dirty_layers.add(old_z)
            dirty_layers.add(z)
            if (z != old_z or old_z not in instructions or
                window_object not in instructions[old_z]):
                try:
                    instructions[old_z].remove(window_object)
                except KeyError:
                    instructions[old_z] = []
                    layer_texture = self.create_texture(_size)
                    layer_cache.append((old_z, layer_texture))
                    #assert layer_texture is sorted(layer_cache)[old_z][1]
                    needs_sorting = True
                except ValueError:
                    pass
                assert window_object not in instructions.get(z, [])

                try:
                    instructions[z].append(window_object)
                except KeyError:
                    instructions[z] = [window_object]
                    layer_texture = self.create_texture(_size)
                    layer_cache.append((z, layer_texture))
                    # assert layer_texture is sorted(layer_cache)[z][1]
                    needs_sorting = True
        del self.redraw_objects[:]
        if needs_sorting:
            layer_cache = sorted(layer_cache)

    def draw(self, instructions):
        area = (0, 0) + self.size
        renderer = self.renderer
        draw_procedures = renderer.instructions
        layer_cache = self.layer_cache
        dirty_layers = self.dirty_layers
        renderer.set_render_target(None)
        renderer.clear()

        # redraw dirty layers onto cache
        # copy layers to screen
        for layer_number, layer_texture in layer_cache:
            layer = instructions[layer_number]
            if not layer:
                continue
            layer_texture = layer_texture.texture
            if layer_number in dirty_layers:
                renderer.set_render_target(layer_texture)
                renderer.clear()
                #print("Performing {} instructions for layer {}".format(sum(len(item._draw_operations) for item in layer), layer_number))
                for item in layer:
                    #if item.always_on_top:
                    #    continue
                    for operation, args, kwargs in item._draw_operations:
                        draw_procedures[operation](*args, **kwargs)
                renderer.set_render_target(None)
            renderer.copy(layer_texture, area, area)
        self.dirty_layers.clear()

        top_items = self.user_input.always_on_top
        if top_items:
            dirty = False
            top_texture = self.top_texture.texture
            renderer.set_render_target(top_texture)
            renderer.clear()
            for item in self.user_input.always_on_top:
                if item.texture_invalid:
                    dirty = True
                    for operation, args, kwargs in item._draw_operations:
                        draw_procedures[operation](*args, **kwargs)
            if dirty:
                renderer.set_render_target(None)
                renderer.copy(top_texture, area, area)
        renderer.present()

    def schedule_postdraw_operation(self, callable, caller):
        assert not caller.deleted
        try:
            self.postdraw_scheduled[caller].append(callable)
        except KeyError:
            self.postdraw_scheduled[caller] = [callable]

    def unschedule_postdraw_operation(self, callable, caller):
        self.postdraw_scheduled[caller].remove(callable)

    def schedule_predraw_operation(self, callable):
        self.predraw_queue.append(callable)

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
        self.run_instruction.unschedule()
        super(SDL_Window, self).delete()
        objects["/Finalizer"].remove_callback((self.reference, "delete"), 0)
        pride.Instruction.purge(self.reference)

    def set_tip_bar_text(self, text, immediately=False):
        self.tip_bar.text = text
        if immediately:
            self.run_instruction.unschedule()
            self.run()

    def clear_tip_bar_text(self):
        if not self.tip_bar.deleted:
            self.tip_bar.text = ''


class Window_Context(SDL_Window):

    defaults = {"showing" : False}

    def run(self):
        raise NotImplementedError()


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
        pass

    def handle_focus_lost(self, event):
        try:
            self.parent.user_input.active_item.held = False
        except AttributeError:
            pass

    def handle_take_focus(self, event):
        pass

    def handle_close(self, event):
        pass


class SDL_User_Input(pride.components.base.Base):

    defaults = {"event_verbosity" : 0, "_ignore_click" : False}
    mutable_defaults = {"_layer_tracker" : collections.OrderedDict,
                        "always_on_top" : list}
    autoreferences = ("active_item", "under_mouse")
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
        old_z = item._old_z
        try:
            self._layer_tracker[old_z].remove(reference)
        except (KeyError, ValueError):
            pass
        #assert reference not in self._layer_tracker.get(z, []), (z, reference)
        try:
            self._layer_tracker[z].append(reference)
        except KeyError:
            self._layer_tracker[z] = [reference]
        pride.objects[reference]._old_z = z
        return old_z

    def _remove_from_coordinates(self, item):
        self._layer_tracker[pride.objects[item]._old_z].remove(item)
        if self.active_item == item:
            self.active_item = None

    def handle_textinput(self, event):
        text = event.edit.text
        cursor = event.edit.start
        selection_length = event.edit.length
        self.alert("Handling textinput {} {} {}".format(text, cursor, selection_length),
                   level=self.verbosity["handle_text_input"])
        if self.active_item:
            instance = self.active_item
            instance.text_entry(text)

    def handle_unhandled_event(self, event):
        self.alert("{0} passed unhandled".format(event.type), 'vv')

    def handle_quit(self, event):
        self.parent.delete()
        if "/User/Shell" not in pride.objects:
            raise SystemExit()

    def handle_mousebuttondown(self, event):
        mouse = event.button
        self.alert("mouse button down at {}".format((mouse.x, mouse.y)), level='v')
        active_item = self.under_mouse
        self.select_active_item(active_item)
        if active_item:
            if self._ignore_click:
                self._ignore_click = False
            else:
                try:
                    active_item.press(mouse)
                except KeyError:
                    if active_item in objects:
                        raise
                    else:
                        #self.alert("Active item has been deleted {}".format(active_item, ),
                        #           level=self.verbosity["active_item_deleted"])
                        self.active_item = None

    def select_active_item(self, active_item):
        objects = pride.objects

        # deselect old active item
        old_active_item = self.active_item
        if old_active_item and old_active_item._selected: # item can deselect itself
            old_active_item.deselect(active_item)

        # select new active item
        self.active_item = active_item
        if active_item:
            active_item.select()

    #def _check_children(self, active_item, mouse_position):
    #    # have to check if it clicked on the children of the always_on_top item
    #    for child in active_item.children:
    #        if child.clickable and pride.gui.point_in_area(active_item.area, mouse_position):
    #            active_item = child
    #            active_item = self._check_children(active_item, mouse_position) # recursion until no descendants left to check
    #            break
    #    return active_item

    def _get_object_under_mouse(self, mouse_position):
        # find the top-most item such that the mouse position is within its area
        objects = pride.objects
        active_item = None
        for item in self.always_on_top:
            if item.clickable and pride.gui.point_in_area(item.area, mouse_position):
                active_item = item
                #active_item = self._check_children(active_item)
                break
        else:
            for layer_number, layer in reversed(self._layer_tracker.items()):
                for item in layer:
                    #assert item in objects
                    #assert not pride.objects[item].hidden
                    item = objects[item]
                    if item.clickable and pride.gui.point_in_area(item.area, mouse_position):
                        active_item = item
                        break
                if active_item:
                    break
        return active_item

    def handle_mousebuttonup(self, event):
        active_item = self.active_item
        if active_item:
            instance = active_item
            if instance.held:
                area = instance.area
                mouse = event.button
                if pride.gui.point_in_area(area, (mouse.x, mouse.y)):
                    instance.release(mouse)
            instance.held = False

    def handle_mousewheel(self, event):
        if self.active_item:
            wheel = event.wheel
            self.active_item.mousewheel(wheel.x, wheel.y)

    def handle_mousemotion(self, event):
        motion = event.motion
        mouse_x, mouse_y = position = (motion.x, motion.y)
        if self.active_item:
            motion = event.motion
            self.active_item.mousemotion(mouse_x, mouse_y,
                                         motion.xrel, motion.yrel, event.button)
        if not self.under_mouse:
            self.under_mouse = under_mouse = self._get_object_under_mouse(position)
            if under_mouse is not None:
                under_mouse.on_hover()
        else:
            under_mouse = self.under_mouse
            if under_mouse.children:
                new_under_mouse = self._get_object_under_mouse(position)
                if under_mouse != new_under_mouse:
                    under_mouse.hover_ends()
                    self.under_mouse = new_under_mouse
                    if new_under_mouse is not None:
                        new_under_mouse.on_hover()
            else:
                if not pride.gui.point_in_area(under_mouse.area, position):
                    new_under_mouse = self._get_object_under_mouse(position)
                    under_mouse.hover_ends()
                    self.under_mouse = new_under_mouse
                    if new_under_mouse is not None:
                        new_under_mouse.on_hover()
                elif self.always_on_top:
                    for item in self.always_on_top:
                        if item is under_mouse:
                            break
                        if item.clickable and pride.gui.point_in_area(item.area, position):
                            new_under_mouse = item
                            under_mouse.hover_ends()
                            self.under_mouse = new_under_mouse
                            if new_under_mouse is not None:
                                new_under_mouse.on_hover()
                            break

    def handle_keydown(self, event):
        if self.active_item is None:
            self.alert("Active item is None; unable to handle keystrokes", level='v')
            return
        instance = self.active_item
        key_value = event.key.keysym.sym
        modifier = event.key.keysym.mod
        #  if key_value < 256 or key_value > 0: # in ascii range
        try:
            key = chr(key_value)
        except ValueError:
            if not modifier:
                modifier = None
            reference, method = self.get_hotkey(instance, (key_value, modifier))
            if reference is not None:
                getattr(pride.objects[reference], method)()
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
            #if ord(key) < 32 or ord(key) == 127 or key_press[1] is not None: # delete is 127

            reference, method = self.get_hotkey(instance, tuple(key_press))
            if reference is not None and method is not None:
                getattr(pride.objects[reference], method)()

    def get_hotkey(self, instance, key_press):
        if key_press in instance.hotkeys:
            callback_info = (instance.reference, instance.hotkeys[key_press])
            if callback_info[1] is None:
                try:
                    callback_info = self.get_hotkey(instance.parent, key_press)
                except AttributeError:
                    callback_info = (None, None)
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
                "blendmode_flag" : DRAW_BLENDMODE, "logical_size" : (800, 600)}
    mutable_defaults = {"_get_text_size_memo" : dict}

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
        self.instructions["rect_perspective"] = self.draw_rect_perspective
        self.instructions["line_perspective"] = self.draw_line_perspective
        self.instructions["rounded_rect"] = self.draw_rounded_rect
        self.instructions["render_copy"] = self.render_copy
        self.instructions["set_blendmode"] = self.set_blendmode
        self.clear()

        info = self.get_renderer_info()
        self.max_size = (info.max_texture_width, info.max_texture_height)

    def screencapture(self, filename):
        format = sdl2.SDL_PIXELFORMAT_ARGB8888
        surface = sdl2.SDL_CreateRGBSurfaceWithFormat(0, 800, 600, 32, format)
        sdl2.SDL_RenderReadPixels(self.wrapped_object.renderer, None, format,
                                  surface.pixels, surface.pitch);
        sdl2.SDL_SaveBMP(surface, filename);
        sdl2.SDL_FreeSurface(surface);

    def render_copy(self, source_area=None, destination_area=None, angle=0,
                    center=None, flip=sdl2.SDL_FLIP_NONE):
        self.copy(self.get_render_target(), source_area, destination_area,
                  angle, center, flip)

    def set_blendmode(self, blendmode):
        error = sdl2.SDL_SetRenderDrawBlendMode(self.wrapped_object.renderer,
                                                blendmode)
        if error:
            message = "SDL_SetRenderDrawBlendMode failed with code {}"
            raise Sdl2Error(message.format(error))

    def draw_rounded_rect(self, rect, radius=22, **kwargs):
        #raise NotImplementedError("rounded_rect not yet supported")
        x, y, w, h = rect
        #print self.wrapped_object.renderer
        r, g, b, a = kwargs["color"]
        renderer = self.wrapped_object.renderer
        draw_mode = sdl2.SDL_BlendMode()
        assert not sdl2.SDL_GetRenderDrawBlendMode(self.wrapped_object.renderer, draw_mode)
        sdl2.sdlgfx.roundedRectangleRGBA(self.wrapped_object.renderer, x, y, x + w, y + h, radius, r, g, b, 255)
        #sdl2.sdlgfx.rectangleRGBA(self.wrapped_object.renderer, x, y, x + w, y + h, *kwargs["color"])
        #self.draw_rect(rect, **kwargs)
        assert not sdl2.SDL_SetRenderDrawBlendMode(renderer, DRAW_BLENDMODE)

    def draw_line_perspective(self, point, length, vanishing_point, **kwargs):
        x, y = point
        vx, vy = vanishing_point
        a = y - vy
        b = x - vx
        try:
            slope = a / float(b)
        except ZeroDivisionError:
            end_y = y
        else:
            end_y = y + int(slope * length)
        end_x = x + length
        self.draw_line((x, y, end_x, end_y), **kwargs)

    def draw_rect_perspective(self, rect, vanishing_point, **kwargs):
        # draw line from upper left corner of rect to vanishing point of length w
        x, y, w, h = rect
        points = [x, y]
        vx, vy = vanishing_point
        #top_left = (x, y)
        a = y - vy
        b = x - vx
        try:
            slope = a / float(b)
        except ZeroDivisionError:
            top_right_y = y
        else:
            top_right_y = y + int(slope * w)
        top_right_x = x + w

        #bottom_left = (x, y + h)
        _y = y + h
        a = _y - vy
        try:
            slope = a / float(b)
        except ZeroDivisionError:
            bottom_right_y = _y
        else:
            bottom_right_y = _y + int(slope * w)
        bottom_right_x = x + w

        self.draw_line((x, y, top_right_x, top_right_y,
                        bottom_right_x, bottom_right_y,
                        x, y + h, x, y),
                       **kwargs)

    def draw_text(self, area, text, **kwargs):
        x, y, w, h = area
        assert w, (area, text, kwargs)
        assert "width" in kwargs
        texture = self.sprite_factory.from_text(text,
                                                fontmanager=self.font_manager,
                                                **kwargs)
        _w, _h = texture.size
        if kwargs.get("center_text", False):# and _w <= (w + 40): # +40? seems to fix scaled text snapping between centered/not
            destination = [(x + (w / 2)) - (_w / 2),
                           (y + (h / 2)) - (_h / 2),
                           _w - 2, _h]
        else:
            destination = (x + 2, y + 2, _w - 2, _h)

        sdl2.SDL_SetTextureBlendMode(texture.texture, TEXT_BLENDMODE)
        self.copy(texture, dstrect=destination)

    def get_text_size(self, area, text, **kwargs):
        try:
            return self._get_text_size_memo[(area, text)]
        except KeyError:
            x, y, w, h = area
            kwargs.setdefault("w", w)
            texture = self.sprite_factory.from_text(text,
                                                    fontmanager=self.font_manager,
                                                    **kwargs)
            size = texture.size
            self._get_text_size_memo[(area, text)] = size
            return size

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

    def get_render_target(self):
        return sdl2.SDL_GetRenderTarget(self.renderer)

    def draw(self, texture, draw_instructions, background=None, clear=True,
             blendmode=DRAW_BLENDMODE):
        blendmode_backup = self.blendmode
        target_backup = self.get_render_target()
        self.blendmode = blendmode
        self.set_render_target(texture)

        if clear:
            self.clear()
        if background:
            self.copy(background)
        instructions = self.instructions
        for shape, args, kwargs in draw_instructions:
            instructions[shape](*args, **kwargs)

        self.set_render_target(target_backup)
        self.blendmode = blendmode_backup
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
    mutable_defaults = {"font_listing" : list}

    def __init__(self, **kwargs):
        _defaults = self.defaults
        options = {"font_path" : _defaults["font_path"],
                   "size" : _defaults["default_font_size"],
                   "color" : _defaults["default_color"],
                   "bg_color" : _defaults["default_background"]}
        kwargs["wrapped_object"] = sdl2.ext.FontManager(**options)
        super(Font_Manager, self).__init__(**kwargs)
        self.load_fonts()

    def load_fonts(self):
        fonts_dir = os.path.join(pride.gui.PACKAGE_LOCATION, "resources", "fonts")
        listing = self.font_listing
        for file in (item for item in os.listdir(fonts_dir)):
            _file, extension = os.path.splitext(file)
            if extension != ".ttf":
                continue
            listing.append(os.path.split(_file)[-1])
            font_file = os.path.join(fonts_dir, file)
            # take care to distinguish between self.add (from Base) and FontManager.add (from SDL2)
            self.wrapped_object.add(font_file)

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
