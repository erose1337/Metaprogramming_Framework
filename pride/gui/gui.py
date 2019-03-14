import operator
from math import floor, sqrt

import pride
import pride.components.base as base
import pride.gui
import pride.gui.shapes
import pride.gui.sdllibrary
Instruction = pride.Instruction

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
        for sdl_window in self.window_queue:
            self.pack_children(sdl_window, list(sdl_window.gui_children))
        for item in sorted(self.pack_queue, key=operator.attrgetter('z')):
            self.pack_children(item, list(item.children))
        del self.window_queue[:]
        del self.pack_queue[:]

    def pack_children(self, parent, children):
        parent.alert("Packing")
        area = parent.area
        z = parent.z

        top = [child for child in children if child.pack_mode == "top"]
        main = [child for child in children if child.pack_mode == "main"]
        bottom = [child for child in children if child.pack_mode == "bottom"]

        top_main_bottom = top + main + bottom
        if top_main_bottom:
            self.pack_verticals(area, z, top_main_bottom, top, main, bottom)
            top_height = sum(child.h for child in top)
            bottom_height = sum(child.h for child in bottom)
        else:
            top_height = bottom_height = 0

        left = [child for child in children if child.pack_mode == "left"]
        right = [child for child in children if child.pack_mode == "right"]
        left_main_right = left + main + right
        if left_main_right:
            self.pack_horizontals(area, z, left_main_right, left, main, right,
                                  top_height, bottom_height)

        for child in children:
            self.unschedule_pack(child)
            self.pack_children(child, list(child.children))

    def pack_horizontals(self, area, z, left_main_right, left, main, right, top_height, bottom_height):
        x, y, w, h = area
        left_main_right_len = len(left_main_right)
        available_space = w
        spacing = available_space / left_main_right_len
        small_items = [child for child in left_main_right if child.w_range[1] < spacing]
        if small_items:
            spacing += sum(spacing - item.w_range[1] for item in small_items)
            spacing /= (len(left_main_right) - len(small_items)) or 1
            extra = w - ((spacing * len([child for child in left_main_right if child not in small_items])) +
                        sum(child.w_range[1] for child in small_items))
        else:
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
            child.w += spacing
            if extra and child not in small_items:
                child.w += extra
                extra = 0
            offset += child.w
            child.x = x + w - offset
            child.z = z

    def pack_verticals(self, area, z, top_main_bottom, top, main, bottom):
        x, y, w, h = area
        top_main_bottom_len = len(top_main_bottom)
        available_space = h
        spacing = available_space / (top_main_bottom_len or 1)
        small_items = [child for child in top_main_bottom if child.h_range[1] < spacing]
        if small_items:
            spacing += sum(spacing - item.h_range[1] for item in small_items)
            spacing /= (top_main_bottom_len - len(small_items)) or 1
            extra = h - ((spacing * len([child for child in top_main_bottom if child not in small_items])) +
                        sum(child.h_range[1] for child in small_items))
        else:
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

    def draw_texture(self):
        raise NotImplementedError


class Minimal_Theme(Theme):

    def draw_texture(self):
        area = self.area
        self.draw("fill", area, color=self.background_color)
        self.draw("rect_width", area, color=self.color, width=self.outline_width)
        if self.text:
            assert isinstance(self.text, str), (type(self.text), self.text, self)
            self.draw("text", area, self.text, w=self.w if self.wrap_text else None,
                      bg_color=self.text_background_color, color=self.text_color,
                      center_text=self.center_text)


class Organized_Object(pride.gui.shapes.Bounded_Shape):

    defaults = {'x' : 0, 'y' : 0, "size" : (0, 0), "pack_mode" : ''}

    predefaults = {"sdl_window" : ''}

    mutable_defaults = {"_children" : list}
    verbosity = {"packed" : "packed"}

    def pack(self):
        organizer = objects[self.sdl_window + "/Organizer"]
        organizer.schedule_pack(self.parent)


class Window_Object(Organized_Object):
    """ to do: write documentation!

        FAQ: I get the following message when exiting, why?:
            Exception TypeError: "'NoneType' object is not callable" in <bound method Window.__del__ of <sdl2.ext.window.Window object at 0xXXXXXXX> ignore
            Except AttributeError: "'NoneType' object has no attribute 'SDL_DestroyTexture'" in ignored
        A: Your window object still exists somewhere and needs to be deleted properly. Make sure there are no scheduled instructions and/or attributes using your object"""
    defaults = {"outline_width" : 1, "center_text" : True,
                "background_color" : (0, 0, 0, 0), "text_background_color" : (0, 0, 0, 255),
                "color" : (15, 165, 25, 255), "text_color" : (15, 165, 25, 255),
                "held" : False, "allow_text_edit" : False, "wrap_text" : True,
                "_ignore_click" : False, "hidden" : False, "movable" : False,
                "text" : '', "scroll_bars_enabled" : False,
                "_scroll_bar_h" : None, "_scroll_bar_w" : None,
                "theme_type" : "pride.gui.gui.Minimal_Theme",
                "_selected" : False}

    predefaults = {"scale_to_text" : False, "_texture_invalid" : False,
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
        self.texture_invalid = True
        #try:
        #    pack_modes = objects[self.sdl_window + "/Organizer"]._pack_modes[self.reference]
        #except KeyError:
        #    pass
        #else:
        #    total_height = sum((objects[name].h for name in pack_modes["top"] + pack_modes["bottom"]))
        #    total_width = sum((objects[name].w for name in pack_modes["right"] + pack_modes["left"]))
        # #   if total_height > self.h:
        # #       if total_width > self.w:
        # #           self.texture_size = (total_width, total_height)
        # #       else:
        # #           self.texture_size = (self.texture_size[0], total_height)
        # #       self.texture = create_texture(self.texture_size)
        # #       self.alert("Resized texture to: {}".format(self.texture_size), level=0)
        # #   elif total_width > self.w:
        # #       self.texture_size = (total_width, self.texture_size[1])

        #    if self.scroll_bars_enabled:
        #        excess_height = total_height > self.h
        #        excess_width = total_width > self.w
        #        if not self._scroll_bar_h:
        #            if excess_height:
        #                bar = self.create("pride.gui.widgetlibrary.Scroll_Bar", pack_mode="right",
        #                                target=(self.reference, "texture_window_y"))
        #                self._scroll_bar_h = bar.reference
        #                bar.pack()
        #        elif not excess_height:
        #            objects[self._scroll_bar_h].delete()
        #            self._scroll_bar_h = None

        #        if not self._scroll_bar_w:
        #            if excess_width:
        #                bar = self.create("pride.gui.widgetlibrary.Scroll_Bar",
        #                                pack_mode="bottom", target=(self.reference,
        #                                                            "texture_window_x"))
        #                self._scroll_bar_w = bar.reference
        #                bar.pack()
        #        elif not excess_width:
        #            objects[self._scroll_bar_w].delete()
        #            self._scroll_bar_w = None

    def delete(self):
        pride.objects[self.sdl_window].remove_window_object(self)
        self.theme.delete()
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


class Window(Window_Object):

    defaults = {"pack_mode" : "main", "size" : pride.gui.SCREEN_SIZE}


class Container(Window_Object):

    defaults = {"pack_mode" : "top"}


class Button(Window_Object):

    defaults = {"shape" : "rect", "pack_mode" : "top"}


class Application(Window):

    defaults = {"startup_components" : ("pride.gui.widgetlibrary.Task_Bar", ),
                "application_window_type" : "pride.gui.gui.Window"}
    predefaults = {"transparency_enabled" : False}

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
