import pride.gui
import pride.gui.color
import pride.components.base

import sdl2

MAX_W, MAX_H = pride.gui.SCREEN_SIZE

def _default_colors():
    return {"background" : pride.gui.color.Color(180, 180, 180, 200),
            "shadow" : pride.gui.color.Color(0, 0, 0, 255),
            "shadow_thickness" : 5,
            "text_background" : pride.gui.color.Color(0, 0, 85, 255),
            "text" : pride.gui.color.Color(45, 45, 45, 255),
            "glow" : pride.gui.color.Color(255, 255, 255, 235),
            "glow_thickness" : 0,
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

        if self.text:
            assert self.wrap_text
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", area, self.text, width=self.w if self.wrap_text else None,
                    bg_color=self.text_background_color, color=self.text_color,
                    center_text=self.center_text, hide_excess_text=self.hide_excess_text)


class Perspective_Theme(Theme):

    theme_colors = Theme.theme_colors.copy()
    for profile in theme_colors.values():
        profile["vanishing_point"] = (-MAX_W, MAX_H / 2)

    defaults = {"animating" : False, "vanishing_point_backup" : None,
                "frame_count" : 13, "frame_number" : 0}

    frame_cache = dict((key, dict()) for key in theme_colors.keys())

    def draw_frames(self):
        self.enable_animation()

    def enable_animation(self):
        #raise NotImplementedError()
        # too slow, caching doesn't work properly. didn't want to spend more time
        if self.vanishing_point_backup is None:
            self.vanishing_point_backup = self.vanishing_point
        if not self.animating:
            pride.objects[self.sdl_window].schedule_postdraw_operation(self.animate)
            self.animating = True
            self.frame_number = 0
            self.vanishing_point = self.vanishing_point_backup
            self.wrapped_object.texture_invalid = True

    def animate(self):
        x, y = self.vanishing_point
        x += (self.frame_number + 1) ** 4#abs(x)
        if self.frame_number == self.frame_count - 1 or not self.frame_count:
            self.animating = False
            self.vanishing_point = tuple()
        else:
            pride.objects[self.sdl_window].schedule_postdraw_operation(self.animate)
            self.vanishing_point = (x, y)
            self.frame_number += 1

        self.wrapped_object.texture_invalid = True

    def delete(self):
        if self.animating:
            pride.objects[self.sdl_window].postdraw_queue.remove(self.animate)
        super(Perspective_Theme, self).delete()

    def draw_texture(self):
        assert not self.hidden
    #    assert self.frame_number <= self.frame_count - 1, (self.frame_number, self.frame_count)
    #    print("Frame number {}".format(self.frame_number))
        x, y, w, h = area = self.area
        size = (w, h)
        profile = self.theme_profile
        try:
            texture, ready = self.frame_cache[profile][size][self.frame_number]
        except KeyError:
            _new_texture = pride.objects[self.sdl_window].create_texture
            _cache = [(_new_texture(size, blendmode=sdl2.SDL_BLENDMODE_ADD), False) for
                      count in range(self.frame_count)]
            if profile in self.frame_cache:
                self.frame_cache[profile][size] = _cache
            else:
                self.frame_cache[profile] = {size : _cache}
            texture, ready = _cache[self.frame_number]

        if ready and self.animating:
            #print("Using cached texture for {}/{} {} {}".format(self.frame_number, self.frame_count - 1, size, profile))
            self.draw("copy", texture.texture, dstrect=area)
            if self.text:
                assert self.wrap_text
                assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
                self.draw("text", area, self.text, width=self.w if self.wrap_text else None,
                        bg_color=self.text_background_color, color=self.text_color,
                        center_text=self.center_text, hide_excess_text=self.hide_excess_text)
            return
        self.draw("fill", area, color=self.background_color)
        #print("Drawing texture for {}/{} {} {}".format(self.frame_number, self.frame_count - 1, size, profile))
        shadow_thickness = self.shadow_thickness
        vanishing_point = self.vanishing_point
    #    assert not vanishing_point
        if shadow_thickness:
            r, g, b, a = self.shadow_color
            if vanishing_point and a:
                for thickness in range(shadow_thickness):
                    self.draw("rect_perspective", (x + thickness, y + thickness,
                                    w - (2 * thickness), h - (2 * thickness)),
                            vanishing_point,
                            color=(r, g, b, a / (thickness + 1)))
            elif a:
                for thickness in range(shadow_thickness):
                    self.draw("rect", (x + thickness, y + thickness,
                                    w - (2 * thickness), h - (2 * thickness)),
                            color=(r, g, b, a / (thickness + 1)))

        glow_thickness = self.glow_thickness
        if glow_thickness:
            r, g, b, a = self.glow_color
            fade_scalar = a / glow_thickness
            assert fade_scalar > 0
            if vanishing_point and a:
                for thickness in range(glow_thickness):
                    self.draw("rect_perspective", (x - thickness, y - thickness,
                                    w + (2 * thickness), h + (2 * thickness)),
                            vanishing_point,
                            color=(r, g, b, a - (thickness * fade_scalar)))
            elif a:
                for thickness in range(glow_thickness):
                    self.draw("rect", (x - thickness, y - thickness,
                                    w + (2 * thickness), h + (2 * thickness)),
                            color=(r, g, b, a - (thickness * fade_scalar)))

        pride.objects[self.sdl_window].renderer.draw(texture.texture,
                                                     self._draw_operations)
        ##del self._draw_operations[:]
        ##self.draw("copy", texture.texture, srcrect=(0, 0) + self.size, dstrect=area)
        self.frame_cache[profile][size][self.frame_number] = (texture, True)

        if self.text:
            assert self.wrap_text
            assert isinstance(self.text, str), (type(self.text), self.text, self.parent)
            self.draw("text", area, self.text, width=self.w if self.wrap_text else None,
                    bg_color=self.text_background_color, color=self.text_color,
                    center_text=self.center_text, hide_excess_text=self.hide_excess_text)


class Animated_Theme(Perspective_Theme):

    defaults = {"frame_number" : 0, "frame_count" : 1, "frames" : None}
    theme_colors = Perspective_Theme.theme_colors.copy()

    def draw_texture(self):
        frame_number = self.frame_number
        area = self.area
        #self.wrapped_object.alert("Copying frame")
        #texture = pride.objects[self.sdl_window].create_texture(self.size)
        #super(Animated_Theme, self).draw_texture()
        #pride.objects[self.sdl_window].renderer.draw(texture.texture, self._draw_operations)
        #self.draw("copy", texture, area, area)
        self.wrapped_object.alert("drawing at {}".format(self.area))
        self.draw("copy", self.frames[frame_number], area, area)
        if frame_number + 1 < self.frame_count:
            self.frame_number = frame_number + 1
            pride.objects[self.sdl_window].schedule_postdraw_operation(self._next_frame)

    def _next_frame(self):
        self.wrapped_object.texture_invalid = True

    def draw_frames(self):
        self.wrapped_object.alert("caching at {}".format(self.area))
        texture = pride.objects[self.sdl_window].create_texture(self.size)
        super(Animated_Theme, self).draw_texture()
        pride.objects[self.sdl_window].renderer.draw(texture.texture, self._draw_operations)
        self.frames = [texture]
        return
        size = self.size
        backup = self.vanishing_point
        frames = self.frames = []
        window = pride.objects[self.sdl_window]
        create_texture = window.create_texture
        fetch_instructions = super(Animated_Theme, self).draw_texture
        draw_to_texture = window.renderer.draw
        operations = self._draw_operations
        #for frame_number in range(self.frame_count - 1):
        #    texture = create_texture(size)
        #    fetch_instructions()
        #    draw_to_texture(texture.texture, operations)
        #    frames.append(texture)
        self.vanishing_point = backup
        texture = create_texture(size)
        fetch_instructions()
        draw_to_texture(texture.texture, operations)
        frames.append(texture)

    def start_animation(self):
        pride.objects[self.sdl_window].schedule_postdraw_operation(self._enable_animation)

    def _enable_animation(self):
        self.frame_number = 0
        self.texture_invalid = True


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
