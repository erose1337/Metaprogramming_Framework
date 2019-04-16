import operator
from math import floor, sqrt

import pride
import pride.functions.utilities
import pride.components.base as base
import pride.gui
import pride.gui.shapes
import pride.gui.color
import pride.gui.sdllibrary
Instruction = pride.Instruction

import sdl2
import sdl2.ext
SDL_Rect = sdl2.SDL_Rect

MAX_W, MAX_H = pride.gui.SCREEN_SIZE

def _default_colors():
    return {"background" : pride.gui.color.Color(180, 180, 180, 200),
            "shadow" : pride.gui.color.Color(0, 0, 0, 255),
            "shadow_thickness" : 5, "shadow_fade_scalar" : 2,
            "text_background" : pride.gui.color.Color(0, 0, 0, 255),
            "text" : pride.gui.color.Color(45, 45, 45, 255),
            "color" : pride.gui.color.Color(110, 110, 110, 255)} # to do: remove unused "color" key

def create_texture(size, access=sdl2.SDL_TEXTUREACCESS_TARGET,
                   factory="/Python/SDL_Window/Renderer/SpriteFactory",
                   renderer="/Python/SDL_Window/Renderer"):
    return objects[factory].create_texture_sprite(objects[renderer].wrapped_object,
                                                  size, access=access)

class Organizer(base.Base):

    mutable_defaults = {"pack_queue" : list, "window_queue" : list}

    def schedule_pack(self, item):
        if isinstance(item, pride.gui.sdllibrary.SDL_Window):
            if item not in self.window_queue:
                self.window_queue.append(item)
        elif item not in self.pack_queue:
            self.pack_queue.append(item)

    def unschedule_pack(self, item):
        try:
            if item.__class__.__name__ == "SDL_Window":
                self.window_queue.remove(item)
            else:
                self.pack_queue.remove(item)
        except ValueError:
            return

    def pack_items(self):
        if self.window_queue:
            #self.alert("Packing Window")
            window_queue = self.window_queue[:]
            del self.window_queue[:]
            for sdl_window in window_queue:
                self.pack_children(sdl_window, list(sdl_window.gui_children))
        if self.pack_queue:
            #self.alert("Packing items")
            pack_queue = sorted(self.pack_queue, key=operator.attrgetter('z'))
            del self.pack_queue[:]
            for item in pack_queue:
                self.pack_children(item, list(item.children))
                item._pack_scheduled2 = item._pack_scheduled = False

    def pack_children(self, parent, children):
    #    parent.alert("Packing children {}".format(children))
        if not children:
            return

        _lists = {"top" : [], "main" : [], "bottom" : [], "left" : [], "right" : []}
        for child in children:
            if child.hidden:
                child.area = (0, 0, 0, 0)
            else:
                try:
                    _lists[child.pack_mode].append(child)
                except KeyError:
                    raise NotImplementedError("Unsupported pack mode '{}'".format(child.pack_mode))
        top, main, bottom, left, right = (_lists[item] for item in ("top", "main", "bottom", "left", "right"))
        assert len(main) in (0, 1), main
        area = parent.area
        z = parent.z + 1

        if top or main or bottom:
            self.pack_verticals(area, z, top, main, bottom)
            top_height = sum(child.h for child in top)
            bottom_height = sum(child.h for child in bottom)
        else:
            top_height = bottom_height = 0

        if left or main or right:
            self.pack_horizontals(area, z, left, main, right,
                                  top_height, bottom_height)

        for child in children:
        #    self.unschedule_pack(child)
            assert child not in self.pack_queue
            assert not child._pack_scheduled
            child._pack_scheduled2 = False
            #child._pack_scheduled = False
            self.pack_children(child, list(child.children))

    def pack_horizontals(self, area, z, left, main, right, top_height, bottom_height):
        x, y, w, h = area
        left_main_right = left + main + right
        left_main_right_len = len(left_main_right)
        available_space = w
        _spacing = available_space / left_main_right_len
        small_items = [child for child in left_main_right if child.w_range[1] < _spacing]
        if small_items:
            while True: # extra space caused by small items can make spacing larger and make items that were not small become small
                spacing = _spacing + sum(_spacing - item.w_range[1] for item in small_items) / ((len(left_main_right) - len(small_items)) or 1)

                extra = w - ((spacing * len([child for child in left_main_right if child not in small_items])) +
                            sum(child.w_range[1] for child in small_items))

                new_small_items = [child for child in left_main_right if child.w_range[1] < spacing and
                                child not in small_items]
                if new_small_items:
                    small_items += new_small_items
                else:
                    break
        else:
            spacing = _spacing
            extra = w - (spacing * left_main_right_len)
        assert extra >= 0, extra

        offset = 0
        for child in left:
            child.y = y + top_height
            child.h = h - (top_height + bottom_height)
            child.x = x + offset
            child.w = spacing
            if extra and child not in small_items:
                child.w += extra
                extra = 0
            child.z = z
            offset += child.w

        if main:
            main_item = main[0]
            main_item.x = x + offset
            main_item.w = spacing
            if extra and main_item not in small_items:
                main_item.w += extra
                extra = 0
            offset += main_item.w

        offset = 0
        for child in right:
            child.y = y + top_height
            child.h = h - (top_height + bottom_height)
            child.w = spacing
            if extra and child not in small_items:
                child.w += extra
                extra = 0
            offset += child.w
            child.x = x + w - offset
            child.z = z

    def pack_verticals(self, area, z, top, main, bottom):
        x, y, w, h = area
        top_main_bottom = top + main + bottom
        top_main_bottom_len = len(top_main_bottom)
        available_space = h

        _spacing = available_space / (top_main_bottom_len or 1)
        small_items = [child for child in top_main_bottom if child.h_range[1] < _spacing]
        if small_items:
            while True:
                spacing = _spacing + sum(_spacing - item.h_range[1] for item in small_items) / ((top_main_bottom_len - len(small_items)) or 1)
                extra = h - ((spacing * len([child for child in top_main_bottom if child not in small_items])) +
                            sum(child.h_range[1] for child in small_items))
                new_small_items = [child for child in top_main_bottom if child.h_range[1] < spacing and
                                   child not in small_items]
                if new_small_items:
                    small_items += new_small_items
                else:
                    break
        else:
            spacing = _spacing
            extra = h - (spacing * top_main_bottom_len)
        assert extra >= 0, extra

        offset = 0
        for child in top:
            child.x = x
            child.w = w
            child.y = y + offset
            child.h = spacing
            if extra and child not in small_items:
                child.h += extra
                extra = 0
            child.z = z
            offset += child.h # h_range can constrain, so use child.h instead of spacing
        top_height = offset

        if main:
            main_item = main[0]
            main_item.y = y + offset
            main_item.h = spacing
            if extra and main_item not in small_items:
                main_item.h += extra
                extra = 0
            main_item.z = z
            offset += main_item.h

        offset = 0
        for child in bottom:
            child.x = x
            child.w = w
            child.h = spacing
            if extra and child not in small_items:
                child.h += extra
                extra = 0
            offset += child.h
            child.y = y + h - offset
            child.z = z


class Theme(pride.base.Wrapper):

    defaults = {"dont_save" : True}
    theme_profiles = ("default", "interactive")
    theme_colors = dict((profile, _default_colors()) for profile in theme_profiles)
    theme_colors["interactive"]["background"] = pride.gui.color.Color(225, 225, 225, 200)
    _theme_users = []

    def draw_texture(self):
        raise NotImplementedError

    def wraps(self, _object):
        super(Theme, self).wraps(_object)
        self._theme_users.append(_object)

    def delete(self):
        self._theme_users.remove(self.wrapped_object)
        super(Theme, self).delete()

    @classmethod
    def update_theme_users(cls):
        for instance in cls._theme_users:
            instance.texture_invalid = True

    def __getstate__(self):
        state = super(Theme, self).__getstate__()
        del state["wrapped_object"]
        return state


class Minimal_Theme(Theme):

    theme_colors = Theme.theme_colors.copy()

    def draw_texture(self):
        assert not self.hidden
        x, y, w, h = area = self.area

        self.draw("fill", area, color=self.background_color)
        shadow_thickness = self.shadow_thickness
        if shadow_thickness:
            r, g, b, a = self.shadow_color
            scalar = self.shadow_fade_scalar
            for thickness in range(shadow_thickness):
                self.draw("rect", (x + thickness, y + thickness,
                                   w - (scalar * thickness), h - (scalar * thickness)),
                        color=(r, g, b, a / (thickness + 1)))
        if self.text:
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", area, self.text, w=self.w if self.wrap_text else None,
                      bg_color=self.text_background_color, color=self.text_color,
                      center_text=self.center_text, hide_excess_text=self.hide_excess_text)


class Blank_Theme(Theme):

    def draw_texture(self):
        self.draw("fill", self.area, color=(0, 0, 0))


class Spacer_Theme(Theme):

    def draw_texture(self):
        return


class Text_Only_Theme(Theme):

    def draw_texture(self):
        if self.text:
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", self.area, self.text, w=self.w if self.wrap_text else None,
                      bg_color=self.text_background_color, color=self.text_color,
                      center_text=self.center_text)


class Organized_Object(pride.gui.shapes.Bounded_Shape):

    defaults = {'x' : 0, 'y' : 0, "size" : (0, 0), "pack_mode" : '',
                "_pack_scheduled" : False}

    predefaults = {"sdl_window" : '', "_pack_scheduled2" : False}

    mutable_defaults = {"_children" : list}
    verbosity = {"packed" : "packed"}

    def pack(self):
        if not self._pack_scheduled2:
            parent = self.parent
            pack_scheduled = False
            while parent.reference != self.sdl_window:
                if parent._pack_scheduled:
                    pack_scheduled = True
                else:
                    parent = parent.parent
            if not pack_scheduled:
                objects[self.sdl_window + "/Organizer"].schedule_pack(parent)
                parent._pack_scheduled = True
                self._pack_scheduled2 = True


class Window_Object(Organized_Object):
    """ to do: write documentation!

        FAQ: I get the following message when exiting, why?:
            Exception TypeError: "'NoneType' object is not callable" in <bound method Window.__del__ of <sdl2.ext.window.Window object at 0xXXXXXXX> ignore
            Except AttributeError: "'NoneType' object has no attribute 'SDL_DestroyTexture'" in ignored
        A: Your window object still exists somewhere and needs to be deleted properly. Make sure there are no scheduled instructions and/or attributes using your object"""
    defaults = {"outline_width" : 1, "center_text" : True,
                "held" : False, "allow_text_edit" : False, "wrap_text" : True,
                "_ignore_click" : False, "hidden" : False, "movable" : False,
                "text" : '', "scroll_bars_enabled" : False,
                "_scroll_bar_h" : None, "_scroll_bar_w" : None,
                "theme_type" : "pride.gui.gui.Minimal_Theme",
                "_selected" : False, "hide_excess_text" : True}

    predefaults = {"_scale_to_text" : False, "_texture_invalid" : False,
                   "_texture_window_x" : 0, "_texture_window_y" : 0,
                   "_text" : '', "_pack_mode" : '', "_sdl_window" : '',
                   "queue_scroll_operation" : False, "_backup_w_range" : tuple(),
                   "_old_z" : 0, "_parent_hidden" : False, "_hidden" : False,
                   "_always_on_top" : False, "use_custom_colors" : False,
                   "theme_profile" : "default", "_status" : None}

    mutable_defaults = {"_draw_operations" : list, "_children" : list,
                        "scroll_instructions" : list, "colors" : dict}
    verbosity = {"press" : "vv", "release" : "vv"}

    hotkeys = {("\b", None) : "handle_backspace", ("\n", None) : "handle_return"}

    def _get_always_on_top(self):
        return self._always_on_top
    def _set_always_on_top(self, value):
        self._always_on_top = value
        if value:
            pride.objects[self.sdl_window].user_input.always_on_top.append(self.reference)
        else:
            try:
                pride.objects[self.sdl_window].user_input.always_on_top.remove(self.reference)
            except ValueError:
                pass
    always_on_top = property(_get_always_on_top, _set_always_on_top)

    def _get_texture_invalid(self):
        return self._texture_invalid
    def _set_texture_invalid(self, value):
        if not self._texture_invalid and value and not self.deleted:
          #  assert self.sdl_window
            objects[self.sdl_window].invalidate_object(self)
        self._texture_invalid = value
    texture_invalid = property(_get_texture_invalid, _set_texture_invalid)

    def _on_set(self, coordinate, value):
        if not self.texture_invalid:# and coordinate in ('z', 'x', 'y', 'w', 'h', 'r', 'g', 'b', 'a'):
            self.texture_invalid = True
        #if self.scale_to_text and coordinate == 'w' and self.w_range[1] > value:
        #    self._backup_text = self.text
        super(Window_Object, self)._on_set(coordinate, value)

    def _get_text(self):
        return self._text
    def _set_text(self, value):
        self._text = value
        if value and self.scale_to_text:
            assert self.sdl_window
            w, h = objects[self.sdl_window].renderer.get_text_size(self.area, value)
            w += 11
        #    print("Scaling to text {} ({}) ({})".format(value, w, self.texture_invalid))
            if not self._backup_w_range:
                self._backup_w_range = self.w_range
            self.w_range = (0, w)
            #self.w = w
        elif self._backup_w_range and self._backup_w_range != self.w_range:
            self.w_range = self._backup_w_range
        self.texture_invalid = True
    text = property(_get_text, _set_text)

    def _get_scale_to_text(self):
        return self._scale_to_text
    def _set_scale_to_text(self, value):
        self._scale_to_text = value
        # If text and scale_to_text are set as kwargs, there is no priority to set scale_to_text first
        # if text is set first, then _set_text wouldn't scale w properly
        self.text = self.text # triggers _set_text descriptor;
    scale_to_text = property(_get_scale_to_text, _set_scale_to_text)


    for color_key in ("background", "text", "text_background", "shadow",
                      "shadow_thickness", "shadow_fade_scalar"):
        def _getter(self, color_key=color_key):
            profile = self.theme_profile
            if profile in self.colors and color_key in self.colors[profile]:
                return self.colors[profile][color_key]
            return self.theme.theme_colors[profile][color_key]
        def _setter(self, value, color_key=color_key):
            try:
                self.colors[self.theme_profile][color_key] = value
            except KeyError:
                self.colors[self.theme_profile] = {color_key : value}
            self.texture_invalid = True
        if color_key not in ("shadow_thickness", "shadow_fade_scalar"):
            vars()["{}_color".format(color_key)] = property(_getter, _setter)
        else:
            vars()[color_key] = property(_getter, _setter)


    def _get_color(self):
        return self.colors["color"]
    def _set_color(self, colors):
        self.colors["color"] = colors
        self.texture_invalid = True
    color = property(_get_color, _set_color)

    def _get_hidden(self):
        return self._hidden or self._parent_hidden
    def _set_hidden(self, value):
        self._hidden = value
    hidden = property(_get_hidden, _set_hidden)

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
        #self.colors = self.theme_type.theme_colors.copy()#DEFAULT_COLORS.copy()
        super(Window_Object, self).__init__(**kwargs)
        self.texture_invalid = True

        self.theme = self.create(self.theme_type, wrapped_object=self)
        self._children.remove(self.theme)
        pride.objects[self.sdl_window + "/SDL_User_Input"]._update_coordinates(self, self.reference, self.area, self.z)
        self.pack()

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

    def hide(self, parent_call=False):
        #assert not self.hidden
        try: # not sure if this is the right way to deal with this happening, but it appears to work
            pride.objects[self.sdl_window + "/SDL_User_Input"]._remove_from_coordinates(self.reference)
        except ValueError:
            pass
        self.texture_invalid = True
        if parent_call:
            self._parent_hidden = True
        else:
            self.hidden = True
        for child in self.children:
            child.hide(True)

    def show(self, parent_call=False):
        #assert self.hidden
        if parent_call:
            self._parent_hidden = False
        else:
            self.hidden = False
        if not self.hidden:
            pride.objects[self.sdl_window + "/SDL_User_Input"]._update_coordinates(self, self.reference, self.area, self.z)
            self.texture_invalid = True
            for child in self.children:
                child.show(True)

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
            self._draw_operations = []
            self.texture_invalid = False
            return

        del self._draw_operations[:]
        self.draw_texture()
        #instructions = self._draw_operations[:]
        self.texture_invalid = False

    def draw_texture(self):
        self.theme.draw_texture()

    def pack(self):
        super(Window_Object, self).pack()
        pride.objects[self.sdl_window]._schedule_run()

    def delete(self):
        assert not self.deleted, self
        pride.objects[self.sdl_window].remove_window_object(self)
        self.theme.delete()
        if self.parent.reference != self.sdl_window:
            #self.parent.pack()
            self.pack()
        super(Window_Object, self).delete()

    def deselect(self, mouse, next_active_object):
        self._selected = False

    def select(self, mouse):
        self._selected = True

    def text_entry(self, text):
        if self.allow_text_edit:
            self.text += text

    def handle_return(self):
        pass

    def handle_backspace(self):
        if self.allow_text_edit:
            self.text = self.text[:-1]

    def __getstate__(self):
        state = super(Window_Object, self).__getstate__()
        state["theme"] = self.theme.save()
        del state["_draw_operations"]
        del state["_children"]
        print self, "getstate"
        import pprint
        pprint.pprint(self.objects)

        return state

    def on_load(self, state):
        super(Window_Object, self).on_load(state)
        self.theme = pride.functions.utilities.resolve_string(self.theme_type).load(self.theme)
        self.theme.wraps(self)
        self._draw_operations = []
        self._children = list(super(Window_Object, self).children)
        print self, "on load"
        import pprint
        pprint.pprint(self.objects)
        self._children.remove(self.theme)

    def show_status(self, text, fade_out=True, **kwargs):
        if self._status is not None:
            assert False
        _kwargs = {"h_range" : (0, .10), "pack_mode" : "bottom"}
        _kwargs.update(kwargs)
        if fade_out:
            self._status = self.create("pride.gui.widgetlibrary.Popup_Notification", text=text, **_kwargs).reference
        else:
            self._status = self.create("pride.gui.gui.Container", text=text, **_kwargs).reference
        pride.objects[self.sdl_window].run()

    def hide_status(self):
        pride.objects[self._status].delete()
        self._status = None


class Window(Window_Object):

    defaults = {"pack_mode" : "main"}#, "size" : pride.gui.SCREEN_SIZE}


class Container(Window_Object):

    defaults = {"pack_mode" : "top"}


class Button(Window_Object):

    defaults = {"pack_mode" : "top"}
    predefaults = {"theme_profile" : "interactive"}


class Application(Window):

    defaults = {"startup_components" : ("pride.gui.widgetlibrary.Task_Bar", ),
                "application_window_type" : "pride.gui.gui.Window"}
    predefaults = {"transparency_enabled" : False}

    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        window = self.application_window = self.create(self.application_window_type)

    def draw_texture(self):
        assert not self.deleted
        super(Application, self).draw_texture()
        self.application_window.texture_invalid = True

    def __getstate__(self):
        state = super(Application, self).__getstate__()
        del state["application_window"]
        return state

    def on_load(self, state):
        super(Application, self).on_load(state)
        self.application_window = self.objects["Window"][0] # brittle, needs to be done properly


class Placeholder(Organized_Object):

    defaults = {"pack_mode" : "left"}


class Texture_Atlas(Organized_Object):

    defaults = {"size" : (4096, 4096), "screen_size" : pride.gui.SCREEN_SIZE, "subsections" : tuple(),
                "placeholder_type" : Placeholder, "pack_mode" : "main"}

   # predefaults = {"sdl_window" : ''}

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
