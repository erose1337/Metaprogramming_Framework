import pride.gui.gui

import sdl2.ext

class Image_Theme(pride.gui.gui.Theme):

    def draw_texture(self):
        area = self.area
        self.draw("fill", area, color=self.background_color)
        self.draw("copy", self.image_texture, dstrect=self.area)


class Image(pride.gui.gui.Window_Object):

    defaults = {"filename" : '', "_enforce_flag" : "SDL",
                "theme_type" : Image_Theme, "color" : (0, 0, 0, 255)}

    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
        image_surface = sdl2.ext.load_image(self.filename, enforce=self._enforce_flag)
        image_texture = self.sdl_window.renderer.sprite_factory.from_surface(image_surface)
        sdl2.SDL_SetTextureAlphaMod(image_texture.texture, self.color[-1])
        self.image_texture = image_texture
