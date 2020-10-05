""" pride.gui.gui - Contains the root `Window_Object`.
`Window_Object`s represent a rectangular area on the screen.
`Window_Object`s provide hooks for user input within (or related to) that area."""

import operator

import pride
import pride.functions.utilities
import pride.components.base as base
import pride.gui
import pride.gui.shapes
import pride.gui.sdllibrary
Instruction = pride.Instruction

import sdl2

lerp = pride.gui.lerp

def create_texture(size, access=sdl2.SDL_TEXTUREACCESS_TARGET,
                   factory="/Program/SDL_Window/Renderer/SpriteFactory",
                   renderer="/Program/SDL_Window/Renderer"):
    return objects[factory].create_texture_sprite(objects[renderer].wrapped_object,
                                                  size, access=access)

class Organizer(base.Base):
    """ The `Organizer` component is responsible for determining the size and placement of `Window_Object`s, based on their relative positions and constraints (e.g. screen size).
        Each `Window_Object` specifies its relative location within its parent object.
            - Each `Window_Object` declares whether it should be on the left, right, top, bottom, or main (middle) area.

        Note: Using both horizontal (top/bottom) and vertical (left/right) pack modes will break *unless* a main item is present.
        If a main item is not present, then the organizer would have to decide whether to scale the height of the vertical item according to either the top/bottom arbitrarily
        Quoting the zen of python:

            > In the face of ambiguity, refuse the temptation to guess.

        If mixing horizontal and vertical pack modes is necessary, include a `main` object."""
    mutable_defaults = {"pack_queue" : list, "window_queue" : list}

    def schedule_pack(self, item):
        if isinstance(item, pride.gui.sdllibrary.SDL_Window):
            if item not in self.window_queue:
                self.window_queue.append(item)
        else:
            assert item not in self.pack_queue
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
            window_queue = self.window_queue
            self.window_queue = []
            for sdl_window in window_queue:
                self.pack_children(sdl_window, list(sdl_window.gui_children))
                sdl_window._in_pack_queue = False
        if self.pack_queue:
            #self.alert("Packing {} top-level items".format(len(self.pack_queue)))
            pack_queue = sorted(self.pack_queue, key=operator.attrgetter('z'))
            del self.pack_queue[:]
            for item in pack_queue:
                self.pack_children(item, list(item.children))
                item._in_pack_queue = item._pack_requested = False

    def pack_children(self, parent, children):
        if not children:
            return
        area = parent.area
        z = parent.z + 1

        _lists = {"top" : [], "main" : [], "bottom" : [], "left" : [],
                  "right" : []}
        old_area = dict()
        for child in children:
            location = child.location
            if location is None or child.hidden:
                continue
            if location == 'z':
                old_area[child] = child.area
                child.z = z
                continue
            if location == "fill":
                old_area[child] = child.area
                child.z = z
                child.area = area
                continue
            else:
                try:
                    _lists[location].append(child)
                except KeyError:
                    raise NotImplementedError("Unsupported pack mode '{}' on {}".format(location, child))
                old_area[child] = child.area

        top, main, bottom, left, right = (_lists[item] for item in ("top", "main", "bottom", "left", "right"))
        if len(main) not in (0, 1):
            message = "More than 1 object declared as 'main' ({})"
            raise ValueError(message.format([str(item) for item in main]))

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
            if child.hidden or child._parent_hidden:
                continue
            _old_area = old_area[child]
            area = child.area
            if parent._in_pack_queue or area != _old_area:
                self.pack_children(child, list(child.children))
                child._pack_requested = False
                if area != _old_area:
                    child.handle_area_change(_old_area)

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
                new_small_items = [child for child in left_main_right if child.w_range[1] < spacing and
                                child not in small_items]
                if new_small_items:
                    small_items += new_small_items
                else:
                    extra = w - ((spacing * len([child for child in left_main_right if child not in small_items])) +
                                sum(child.w_range[1] for child in small_items))
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
                new_small_items = [child for child in top_main_bottom if child.h_range[1] < spacing and
                                   child not in small_items]
                if new_small_items:
                    small_items += new_small_items
                else:
                    extra = h - ((spacing * len([child for child in top_main_bottom if child not in small_items])) +
                                sum(child.h_range[1] for child in small_items))
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


class Organized_Object(pride.gui.shapes.Bounded_Shape):
    """ A `Bounded_Shape` that can be organized into place via the `pack` method.
        `Organized_Object`s have a `location` attribute that determines the placement of the object within its parent."""

    defaults = {"location" : '',
                "_pack_requested" : False, "_in_pack_queue" : False}
    allowed_values = {"location" : ("left", "right", "top", "bottom", "main",
                                     'z', "fill", None)}
    mutable_defaults = {"_children" : list}
    verbosity = {"packed" : "packed"}
    interface = (tuple(), ("location", ))

    def pack(self):
        """ usage: window_object.pack()

        Ensures that `self` has its area updated before the next frame is presented"""
        parent = self.parent
        if not parent._in_pack_queue:
            parent._in_pack_queue = self._pack_requested = True
            self.sdl_window.organizer.schedule_pack(parent)
        #if not self._pack_scheduled2:
        #    parent = self.parent
        #    pack_scheduled = False
        #    while parent.reference != self.sdl_window:
        #        if parent._pack_scheduled:
        #            pack_scheduled = True
        #            break
        #        else:
        #            parent = parent.parent
        #    if not pack_scheduled and not parent.deleted:
        #        parent = self.parent
        #        if not parent.deleted:
        #            #print
        #            #print objects[self.sdl_window.organizer.reference] # somehow causes KeyError
        #            #print
        #            self.sdl_window.organizer.schedule_pack(parent)
        #            parent._pack_scheduled = True
        #            self._pack_scheduled2 = True


class _Window_Object(Organized_Object):
    """ to do: write documentation!

        FAQ: I get the following message when exiting, why?:
            Exception TypeError: "'NoneType' object is not callable" in <bound method Window.__del__ of <sdl2.ext.window.Window object at 0xXXXXXXX> ignore
            Except AttributeError: "'NoneType' object has no attribute 'SDL_DestroyTexture'" in ignored
        A: Your window object still exists somewhere and needs to be deleted properly. Make sure there are no scheduled instructions and/or attributes using your object"""
    defaults = {"center_text" : True, "hoverable" : False,
                "held" : False, "allow_text_edit" : False, "wrap_text" : True,
                "_ignore_click" : False, "hidden" : False,
                "text" : '', "_hover_backup_theme_profile" : '',
                "hovering" : False,
                "_selected" : False, "confidential" : False,
                "tip_bar_text" : '', "font" : "Aero",
                "theme_type" : "pride.gui.themes.Minimal_Theme",
                "theme_profile" : "default", "clickable" : True,
                "draw_edge" : True, "transition_state" : None}
    # transition_state is needed by SDL_Window even if this class doesn't use it
    predefaults = {"_scale_to_text" : False, "_texture_invalid" : False,
                   "_texture_window_x" : 0, "_texture_window_y" : 0,
                   "_text" : '', "draw_cursor" : False,
                   "queue_scroll_operation" : False, "_backup_w_range" : tuple(),
                   "_old_z" : 0, "_parent_hidden" : False, "_hidden" : False,
                   "use_custom_colors" : False,
                   "_status" : None, "_tip_set" : False,
                   "_theme_profile" : "default"}

    mutable_defaults = {"_children" : list,
                        "scroll_instructions" : list, "colors" : dict}
    verbosity = {"press" : "vv", "release" : "vv"}
    hotkeys = dict()
    inherited_attributes = {"hotkeys" : dict}
    autoreferences = ("_sdl_window", )
    interface = (tuple(), ("center_text", "hoverable", "wrap_text",
                           "theme_profile", "text",
                           "scale_to_text"))
    allowed_values = {"theme_type" : ("pride.gui.themes.Theme",
                                      "pride.gui.themes.Minimal_Theme",
                                      "pride.gui.themes.Animated_Theme")}

    def _get_texture_invalid(self):
        return self._texture_invalid
    def _set_texture_invalid(self, value):
        assert not self.deleted
        if value and not self.hidden and not self._texture_invalid:
            self.sdl_window.invalidate_object(self)
        self._redraw_needed = self._texture_invalid = value
    texture_invalid = property(_get_texture_invalid, _set_texture_invalid)

    def _on_set(self, coordinate, value):
        if not self.texture_invalid:
            self.texture_invalid = True
        super(_Window_Object, self)._on_set(coordinate, value)
        if coordinate == 'z':
            self.sdl_window.user_input._update_coordinates(self)

    def _get_text(self):
        return self._text
    def _set_text(self, value):
        self._text = value
        if self.scale_to_text:
            if value:
                w, h = self.sdl_window.renderer.get_text_size(self.area, value)
                w += 20
            else:
                w = 20
            if not self._backup_w_range:
                self._backup_w_range = self.w_range
            self.w_range = (0, w)
        elif self._backup_w_range and self._backup_w_range != self.w_range:
            self.w_range = self._backup_w_range
            self._backup_w_range = tuple()
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
                      "shadow_thickness", "glow", "glow_thickness",
                      "vanishing_point"):
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
        def _deleter(self, color_key=color_key):
            del self.colors[self.theme_profile][color_key]

        if color_key not in ("shadow_thickness", "glow_thickness", "vanishing_point"):
            vars()["{}_color".format(color_key)] = property(_getter, _setter, _deleter)
        else:
            vars()[color_key] = property(_getter, _setter, _deleter)

    def _get_theme_profile(self):
        return self._theme_profile
    def _set_theme_profile(self, value):
        self._theme_profile = value
        self.texture_invalid = True
    theme_profile = property(_get_theme_profile, _set_theme_profile)

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

    def _get_children(self):
        return self._children
    def _set_children(self, value):
        self._children = value
    children = property(_get_children, _set_children)

    def _get_sdl_window(self):
        return (self._sdl_window or getattr(self.parent, "sdl_window", self.parent_name))
    def _set_sdl_window(self, value):
        assert not isinstance(value, str)
        self._sdl_window = value
    sdl_window = property(_get_sdl_window, _set_sdl_window)

    def __init__(self, **kwargs):
        super(_Window_Object, self).__init__(**kwargs)
        self.texture_invalid = True

        self.theme = self.create(self.theme_type, wrapped_object=self)

        self._children.remove(self.theme)
        window = self.sdl_window
        window.user_input._update_coordinates(self)
        #self.texture = window.create_texture(window.size)
        self.pack()

    def create(self, *args, **kwargs):
        kwargs.setdefault('z', self.z + 1)
        kwargs.setdefault("sdl_window", self.sdl_window)
        return super(_Window_Object, self).create(*args, **kwargs)

    def add(self, _object):
        self._children.append(_object)
        super(_Window_Object, self).add(_object)

    def remove(self, _object):
        try:
            self._children.remove(_object)
        except ValueError:
            if _object is not self.theme:
                self.alert("Failed to remove {} from _children".format(_object))
                raise
        super(_Window_Object, self).remove(_object)

    def press(self, mouse):
        self.alert("Pressing", level=self.verbosity["press"])
        self.held = True
        for instance in self.children:
            instance.held = True

    def release(self, mouse):
        self.alert("Releasing", self.verbosity["release"])
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

    def mousemotion(self, x, y, x_change, y_change, mouse):
        pass

    def on_hover(self):
        #self.alert("Mouse hovering")
        if self.hoverable and not self.hovering:
            self._hover_backup_theme_profile = self.theme_profile
            self.theme_profile = "hover"
            self.hovering = True

        if self.tip_bar_text:
            self.sdl_window.set_tip_bar_text(self.tip_bar_text)
            self._tip_set = True

    def hover_ends(self):
        if self.hovering:
            assert self.hoverable
            if self.theme_profile == "hover":
                self.theme_profile = self._hover_backup_theme_profile
                self._hover_backup_theme_profile = ''
            self.hovering = False

        if self._tip_set:
            self._clear_tip_bar_text()

    def _clear_tip_bar_text(self):
        if self._tip_set:
            self.sdl_window.clear_tip_bar_text()
            self._tip_set = False

    def hide(self, parent_call=False):
        if self.hidden:
            return
        self.sdl_window.remove_window_object(self)
        if parent_call:
            self._parent_hidden = True
        else:
            self.hidden = True
        self.hover_ends()
        for child in self.children:
            child.hide(True)

    def show(self, parent_call=False):
        if not self.hidden:
            return
        if parent_call:
            self._parent_hidden = False
        else:
            self.hidden = False
        if not self.hidden:
            assert not self.deleted
            window = self.sdl_window
            window.user_input._update_coordinates(self)
            if self.texture_invalid:
                window.invalidate_object(self) # need to re-invalidate after _update_coordinates
            else:
                self.texture_invalid = True
            for child in self.children:
                child.show(True)

    def pack(self):
        super(_Window_Object, self).pack()
        self.sdl_window._schedule_run()

    def delete(self):
        assert not self.deleted, self
        self._clear_tip_bar_text()
        self.theme.delete()
        self.theme = None
        if self.parent.reference != self.sdl_window:
            self.pack()
        self.sdl_window.remove_window_object(self)
        super(_Window_Object, self).delete()

    def deselect(self, next_active_object):
        self._selected = False

    def select(self):
        self._selected = True

    def text_entry(self, text):
        if self.allow_text_edit:
            self.text += text

    def __getstate__(self):
        state = super(_Window_Object, self).__getstate__()
        state["theme"] = self.theme.save()
        del state["_children"]
        print self, "getstate"
        import pprint
        pprint.pprint(self.objects)

        return state

    def on_load(self, state):
        super(_Window_Object, self).on_load(state)
        theme_type = self.theme_type
        self.theme = pride.functions.utilities.resolve_string(theme_type).load(self.theme)
        self.theme.wraps(self)
        self._children = list(super(_Window_Object, self).children)
        print self, "on load"
        import pprint
        pprint.pprint(self.objects)
        self._children.remove(self.theme)

    def show_status(self, text, immediately=False):
        self.sdl_window.set_tip_bar_text(text, immediately)

    def clear_status(self):
        self.sdl_window.clear_tip_bar_text()

    def handle_area_change(self, old_area):
        assert old_area != self.area


class Animated_Object(_Window_Object):

    defaults = {"frame_count" : 5, "_backup_theme_profile" : None,
                "animation_enabled" : True, "click_animation_enabled" : True,
                "click_radius" : 2,
                "theme_type" : "pride.gui.themes.Animated_Theme"}
    predefaults = {"animating" : False, "_old_theme" : None,
                   "_colors_backup" : None, "_start_animation_enabled" : False,
                   "transition_state" : 0}

    def _get_theme_profile(self):
        return super(Animated_Object, self)._get_theme_profile()
    def _set_theme_profile(self, value):
        if self.animating:
            self.end_color_animation()
        if value != self.theme_profile:
            self._old_theme = self.theme_profile
        super(Animated_Object, self)._set_theme_profile(value)
        if (self.animation_enabled and
            self._old_theme is not None and
            self._old_theme != self.theme_profile):
            self.start_color_animation()
    theme_profile = property(_get_theme_profile, _set_theme_profile)

    def __init__(self, **kwargs):
        super(Animated_Object, self).__init__(**kwargs)
        self._start_animation_enabled = True

    def press(self, mouse):
        super(Animated_Object, self).press(mouse)
        if self.click_animation_enabled:
            x, y = mouse.x, mouse.y
            radius = self.click_radius
            rect = self.create("pride.gui.gui._Mouse_Click")
            rect.area = (x - radius, y - radius, radius, radius)

    def hide(self, parent_call=False):
        try:
            self.theme.end_area_animation()
        except AttributeError:
            if hasattr(self, "theme"):
                raise
            # Slider_Field.maximum hides the slider if maximum is set to 0
            # theme may have not been created when maximum is assigned
        super(Animated_Object, self).hide(parent_call)

    def show(self, parent_call=False):
        super(Animated_Object, self).show(parent_call)
        backup = self._backup_theme_profile or self.theme_profile
        assert backup is not None
        self.theme_profile = "blank" # forces fade-in from blank color
        self.theme_profile = backup
        self._backup_theme_profile = None

    def start_color_animation(self):
        if not self._start_animation_enabled: # dont animate when setting initial theme_profile
            return
        assert self.theme_profile != self._old_theme
        self.animating = True
        self.texture_invalid = True
        self.transition_state = 0
        self.animate_color()

    def end_color_animation(self):
        self.animating = False
        self.colors.clear()
        self._old_theme = None
        self.transition_state = 0
        try:
            self.sdl_window.unschedule_postdraw_operation(self.animate_color,
                                                          self)
        except KeyError:
            pass

    def handle_transition_animation_end(self):
        # this is used by the Animated_Theme end animation
        # NOT the color animation performed by this class
        pass

    def animate_color(self):
        animating = self.animating
        state_counter = self.transition_state
        if animating:
            if state_counter > self.frame_count:
                self.end_color_animation()
            else:
                assert self.theme_profile != self._old_theme, (self.theme_profile, self._old_theme, state_counter, self.frame_count)
                assert state_counter <= self.frame_count, (state_counter, self.frame_count)
                self.next_frame()
                self.transition_state += 1
                assert not self.deleted
                self.sdl_window.schedule_postdraw_operation(self.animate_color, self)

    def next_frame(self):
        end_profile = self.theme_profile
        old_profile = self._old_theme
        unit = 1.0 / self.frame_count
        scalar = self.transition_state
        set_theme = super(Animated_Object, self)._set_theme_profile
        theme = self.theme
        _theme_colors = theme.theme_colors
        _cache = theme._cache # conspires with Minimal_Theme class to keep the cache fresh when theme colors are edited
        for key in theme.theme_colors[end_profile].keys():
            if key not in ("shadow_thickness", "glow_thickness"):
                key += "_color"
            try:
                new_value = _cache[(scalar, old_profile, end_profile, key)]
            except KeyError:
                if key not in ("shadow_thickness", "glow_thickness"):
                    end_value = _theme_colors[end_profile][key[:-6]]#getattr(self, key)
                else:
                    end_value = _theme_colors[end_profile][key]
                set_theme(old_profile)
                old_value = getattr(self, key)
                set_theme(end_profile)
                if old_value != end_value:
                    new_value = lerp(old_value, end_value, scalar * unit)
                else:
                    new_value = end_value
                if key in ("shadow_thickness", "glow_thickness"):
                    new_value = int(round(new_value))
                _cache[(scalar, old_profile, end_profile, key)] = new_value
            setattr(self, key, new_value)

    def handle_area_change(self, old_area):
        assert self.area != old_area
        if self.animation_enabled:
            self.theme.start_area_animation(old_area)


class _Mouse_Click(Animated_Object):

    defaults = {"clickable" : False, "location" : "fill"}

    def handle_transition_animation_end(self):
        self.sdl_window.schedule_postdraw_operation(self.delete, self)

Window_Object = Animated_Object # can upgrade everything in-place by changing this


class Window(Window_Object):

    defaults = {"location" : "top"}


class Container(Window_Object):

    defaults = {"location" : "top"}


class Button(Window_Object):

    defaults = {"location" : "top", "theme_profile" : "interactive",
                "hoverable" : True}


class Placeholder(Container):

    defaults = {"location" : "left", "theme_profile" : "placeholder"}
