import copy
import ast
import pprint

import pride.gui
import pride.gui.color
import pride.components.base
from pride.components import deep_update

import sdl2

MAX_W, MAX_H = pride.gui.SCREEN_SIZE

lerp = pride.gui.lerp

def _default_colors(_color=pride.gui.color.Color):
    return {"background" : _color(18, 18, 18, 200),
            "glow" : _color(255, 255, 255, 235),
            "glow_thickness" : 0,
            "shadow" : _color(0, 0, 0, 255),
            "shadow_thickness" : 5,
            "text" : _color(45, 45, 45, 255),
            "text_background" : _color(0, 0, 85, 255)}

class Theme(pride.components.base.Wrapper):

    defaults = {"dont_save" : True}
    theme_profiles = ("default", "interactive", "hover", "placeholder",
                      "indicator", "inert", "borderless", "alert")
    theme_colors = dict((profile, _default_colors()) for profile in theme_profiles)
    assert theme_colors["default"]["text_background"].b == 85, str(theme_colors["default"]["text_background"])
    theme_colors["interactive"]["background"] = pride.gui.color.Color(225, 225, 225, 200)
    theme_colors["hover"]["background"] = pride.gui.color.Color(245, 245, 220)
    theme_colors["placeholder"]["background"] = pride.gui.color.Color(0, 0, 0, 255)
    theme_colors["indicator"]["background"] = pride.gui.color.Color(85, 85, 185, 235)
    theme_colors["inert"]["background"] = pride.gui.color.Color(85, 85, 185, 75)
    theme_colors["borderless"]["shadow_thickness"] = 0
    theme_colors["blank"] = dict((key, pride.gui.color.Color(0, 0, 0, 0)) for key in _default_colors().keys())
    theme_colors["blank"].update({"glow_thickness" : 0, "shadow_thickness" : 0})
    theme_profiles += ("blank", )

    _theme_users = [] # may need metaclass to make a new _theme_users for subclasses

    def serialize(self):
        theme_colors = self.theme_colors
        output = dict()
        for profile_name, profile in theme_colors.items():
            _output = output[profile_name] = dict()
            for key, value in profile.items():
                try:
                    value = value.r, value.g, value.b, value.a
                except AttributeError:
                    _output[key] = value
                else:
                    _output[key] = value
        return pprint.pformat(output)

    @staticmethod
    def deserialize(serialized_theme_colors):
        output = ast.literal_eval(serialized_theme_colors)
        for profile_name, profile in output.items():
            for key, value in profile.items():
                try:
                    r, g, b, a = value
                except TypeError:
                    pass
                else:
                    profile[key] = pride.gui.color.Color(r, g, b, a)
        return output

    def update_theme_colors(self, theme_colors):
        # what if keys have been removed/deprecated from the code since theme_colors was serialized?
        # what if theme_colors contains keys for profiles that do not exist? yet (or anymore)?
        deep_update(self.theme_colors, theme_colors)

    def wraps(self, _object):
        super(Theme, self).wraps(_object)
        self._theme_users.append(_object)

    def delete(self):
        self._theme_users.remove(self.wrapped_object)
        self.wrapped_object = None
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

    theme_colors = copy.deepcopy(Theme.theme_colors)
    _cache = dict() # for conspiring with gui.Animated_Object. update_theme_users should flush the cache
    _replacement_string = '*' * 10
    draw_instructions = ("fill", "shadow", "glow")

    @classmethod
    def update_theme_users(cls):
        cls._cache.clear()
        super(Minimal_Theme, cls).update_theme_users()

    def text_instruction(self, renderer):
        text = self.text
        if text or self.draw_cursor:
            assert self.wrap_text
            assert isinstance(text, str), (type(text), text, self.parent)
            # note that it is the responsibility of the theme to control whether or not passwords are displayed
            if text and self.wrapped_object.confidential:
                text = self._replacement_string
            if self.draw_cursor:
                offset = getattr(self, "_cursor_offset", 0)
                if offset:
                    text = text[:-offset] + self.cursor_symbol + text[-offset:]
                else:
                    text += self.cursor_symbol
            if getattr(self, "_formext_fix", False):
                # conspires with gui.widgets.formext.Scrollable_Text_Window
                # fixes a bug that causes a jittering effect
                # bug is caused by the width of the texture produced when rendering the text
                # if the text consists of only one line (contains no `\n`), then it will have a width determined by the text length
                # if the text has newlines, then the texture will have the maximum width
                # when text rendering is upgraded to use an atlas, this fix should no longer be necessary
                text += "\n\n"

            # use self.x, self.y, self.w, self.h explicitly because:
            # - animation sets these values and not self.area
            # - attribute assignemnt on wrappers does not "write through" to the wrapped object
            w = self.w
            area = (self.x, self.y, w, self.h)
            renderer.draw_text(area, text,
                               width=w if self.wrap_text else None,
                               bg_color=self.text_background_color,
                               alias=self.font, color=self.text_color,
                               center_text=self.center_text)

    def fill_instruction(self, renderer):
        offset = self.glow_thickness
        renderer.fill((offset, offset, self.w, self.h),
                      color=self.background_color)

    def shadow_instruction(self, renderer):
        shadow_thickness = self.shadow_thickness
        w, h = self.w, self.h
        if shadow_thickness:
            r, g, b, a = self.shadow_color
            offset = self.glow_thickness
            for thickness in range(shadow_thickness):
                _offset = offset + thickness
                renderer.draw_rect((_offset, _offset,
                                    w - (2 * thickness), h - (2 * thickness)),
                                   color=(r, g, b, a / (thickness + 1)))

    def glow_instruction(self, renderer):
        glow_thickness = self.glow_thickness
        w, h = self.w, self.h
        if glow_thickness:
            r, g, b, a = self.glow_color
            if not a:
                return
            fade_scalar = a / glow_thickness
            assert fade_scalar > 0, (a, glow_thickness, fade_scalar)
            for thickness in range(glow_thickness):
                offset = glow_thickness - thickness
                renderer.draw_rect((offset, offset,
                                    w + (2 * thickness), h + (2 * thickness)),
                                 color=(r, g, b, a - (thickness * fade_scalar)))


class Animated_Theme(Minimal_Theme):

    defaults = {"_animating_movement" : False, "frame_count" : 7,
                "_old_area" : None, "_end_area" : None}

    def start_area_animation(self, old_area):
        assert old_area != self.area
        self._animating_movement = True
        self.frame_number = 0
        self._old_area = old_area
        self._end_area = self.area
        self.animate_area()

    def end_area_animation(self):
        self._animating_movement = False
        self._old_area = self._end_area = None
        del self.x, self.y, self.w, self.h # removes lerp'd values from Wrapper; future attribute accesses will go through to wrapped object
        self.wrapped_object.handle_transition_animation_end()

    def animate_area(self):
        if self._animating_movement:
            assert self.frame_number <= self.frame_count, (self.frame_number,
                                                           self.frame_count)
            midpoint = float(self.frame_number) / self.frame_count
            old_area = self._old_area
            end_area = self._end_area
            assert old_area is not None
            assert end_area is not None
            assert 0.0 <= midpoint <= 1.0, (midpoint, self.frame_number,
                                            self.frame_count)
            (self.x, self.y,
             self.w, self.h) = [int(round(lerp(old_value, end_value, midpoint))) for
                                old_value, end_value in zip(old_area, end_area)]
            self.frame_number += 1
            if (self.frame_number > self.frame_count or
                (self.x, self.y, self.w, self.h) == self.wrapped_object.area):
                assert (self.x, self.y, self.w, self.h) == self.wrapped_object.area
                self.end_area_animation()
            else: # end_area_animation can delete this self; delete clears the postdraw queue
                self.sdl_window.schedule_postdraw_operation(self._invalidate_self, self.wrapped_object)

    def _invalidate_self(self):
        self.sdl_window.invalidate_object(self)
        self.animate_area()
