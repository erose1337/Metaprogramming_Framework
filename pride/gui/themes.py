import pride.gui
import pride.gui.color
import pride.components.base

MAX_W, MAX_H = pride.gui.SCREEN_SIZE

def _default_colors():
    return {"background" : pride.gui.color.Color(180, 180, 180, 200),
            "shadow" : pride.gui.color.Color(0, 0, 0, 255),
            "shadow_thickness" : 5,
            "text_background" : pride.gui.color.Color(0, 0, 85, 255),
            "text" : pride.gui.color.Color(45, 45, 45, 255),
            "glow" : pride.gui.color.Color(255, 255, 255, 235),
            "glow_thickness" : 0, "vanishing_point" : (MAX_W * 10, MAX_H / 2),
            "color" : pride.gui.color.Color(110, 110, 110, 255)} # to do: remove unused "color" key


class Theme(pride.components.base.Wrapper):

    defaults = {"dont_save" : True}
    theme_profiles = ("default", "interactive", "hover", "placeholder",
                      "indicator", "inert", "borderless")
    theme_colors = dict((profile, _default_colors()) for profile in theme_profiles)
    assert theme_colors["default"]["text_background"].b == 85, str(theme_colors["default"]["text_background"])
    theme_colors["interactive"]["background"] = pride.gui.color.Color(225, 225, 225, 200)
    theme_colors["hover"]["background"] = pride.gui.color.Color(245, 245, 220)
    theme_colors["placeholder"]["background"] = pride.gui.color.Color(0, 0, 0, 255)
    theme_colors["indicator"]["background"] = pride.gui.color.Color(85, 85, 185, 235)
    theme_colors["inert"]["background"] = pride.gui.color.Color(85, 85, 185, 75)
    theme_colors["borderless"]["shadow_thickness"] = 0
    _theme_users = [] # may need metaclass to make a new _theme_users for subclasses

    def draw_texture(self):
        raise NotImplementedError

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

    theme_colors = Theme.theme_colors.copy()

    def __init__(self, **kwargs):
        super(Minimal_Theme, self).__init__(**kwargs)
        self.instruction.execute(priority=.038)

    def increment_perspectivex(self):
        self.perspective_x += self.delta_x
        self.delta_x = int(self.delta_x * 2)
        self.instruction.execute(priority=.025)
        self.wrapped_object.texture_invalid = True

    def delete(self):
        self.instruction.unschedule()
        super(Minimal_Theme, self).delete()

    def draw_texture(self):
        assert not self.hidden
        #if self._cached:
        #    self.draw("copy", self.texture, self.area, self.area)
        #else:
        x, y, w, h = area = self.area
        self.draw("fill", area, color=self.background_color)
        shadow_thickness = self.shadow_thickness
        if shadow_thickness:
            r, g, b, a = self.shadow_color
            for thickness in range(shadow_thickness):
                self.draw("rect", (x + thickness, y + thickness,
                                   w - (2 * thickness), h - (2 * thickness)),
                        color=(r, g, b, a / (thickness + 1)))

        glow_thickness = self.glow_thickness
        if glow_thickness:
            r, g, b, a = self.glow_color
            fade_scalar = a / glow_thickness
            assert fade_scalar > 0
            for thickness in range(glow_thickness):
                self.draw("rect", (x - thickness, y - thickness,
                                   w + (2 * thickness), h + (2 * thickness)),
                        color=(r, g, b, a - (thickness * fade_scalar)))
        #elif shadow_thickness:


        if self.text:
            assert self.wrap_text
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", area, self.text, width=self.w if self.wrap_text else None,
                    bg_color=self.text_background_color, color=self.text_color,
                    center_text=self.center_text, hide_excess_text=self.hide_excess_text)
        #renderer = pride.objects[self.sdl_window].renderer
        #renderer.draw(self.texture.texture, self._draw_operations)
        #self._cached= True

class Perspective_Theme(Theme):

    theme_colors = Theme.theme_colors.copy()

    def draw_texture(self):
        assert not self.hidden
        #if self._cached:
        #    self.draw("copy", self.texture, self.area, self.area)
        #else:
        x, y, w, h = area = self.area
        self.draw("fill", area, color=self.background_color)
        shadow_thickness = self.shadow_thickness
        vanishing_point = self.vanishing_point
        if shadow_thickness:
            r, g, b, a = self.shadow_color
            if vanishing_point:
                for thickness in range(shadow_thickness):
                    self.draw("rect_perspective", (x + thickness, y + thickness,
                                    w - (2 * thickness), h - (2 * thickness)),
                              vanishing_point,
                              color=(r, g, b, a / (thickness + 1)))
            else:
                for thickness in range(shadow_thickness):
                    self.draw("rect", (x + thickness, y + thickness,
                                       w - (2 * thickness), h - (2 * thickness)),
                              color=(r, g, b, a / (thickness + 1)))

        glow_thickness = self.glow_thickness
        if glow_thickness:
            r, g, b, a = self.glow_color
            fade_scalar = a / glow_thickness
            assert fade_scalar > 0
            if self.vanishing_point:
                for thickness in range(glow_thickness):
                    self.draw("rect_perspective", (x - thickness, y - thickness,
                                    w + (2 * thickness), h + (2 * thickness)),
                            vanishing_point,
                            color=(r, g, b, a - (thickness * fade_scalar)))
            else:
                for thickness in range(shadow_thickness):
                    self.draw("rect", (x + thickness, y + thickness,
                                    w - (2 * thickness), h - (2 * thickness)),
                              color=(r, g, b, a / (thickness + 1)))
        #elif shadow_thickness:


        if self.text:
            assert self.wrap_text
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", area, self.text, width=self.w if self.wrap_text else None,
                    bg_color=self.text_background_color, color=self.text_color,
                    center_text=self.center_text, hide_excess_text=self.hide_excess_text)
        #renderer = pride.objects[self.sdl_window].renderer
        #renderer.draw(self.texture.texture, self._draw_operations)
        #self._cached= True


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
            self.draw("text", self.area, self.text, width=self.w if self.wrap_text else None,
                      bg_color=self.text_background_color, color=self.text_color,
                      center_text=self.center_text)


class Copy_Theme(Theme):

    def draw_texture(self):
        texture = self.texture
        self.draw("copy", texture, (0, 0) + self.size, self.area)
