import os
import platform

def install_pysdl2():
    command = "pip install PySDL2" if platform.system() == "Windows" else "sudo pip install PySDL2"
    print(command)
    os.system(command)

try:
    import sdl2.ext
except ImportError:
    from pride.components.shell import get_permission
    print("pySDL2 not installed")
    permission = get_permission("Install pySDL2 now?: ")
    if permission:
        install_pysdl2()
        del get_permission
    else:
        print("Unable to load gui package")
        raise
else:
    Color = sdl2.ext.Color

if "__file__" not in globals():
    __file__ = os.getcwd()
PACKAGE_LOCATION = os.path.dirname(os.path.abspath(__file__))

SCREEN_SIZE = (800, 600)
MAX_LAYER = int('1' * 64, 2)
R = 0
G = 115
B = 10

def point_in_area(area, position):
    x, y, w, h = area
    point_x, point_y = position
    if point_x >= x and point_x <= x + w:
        if point_y >= y and point_y <= y + h:
            return True

def enable(**kwargs):
    import pride
    #import pride.components.blackbox
    if "/Python/SDL_Window" not in pride.objects:
        window = pride.objects["/Python"].create("pride.gui.sdllibrary.SDL_Window",
                                                 **kwargs).reference
        #service = pride.objects["/Python"].create(pride.components.blackbox.Black_Box_Service)
        #client = pride.components.blackbox.Black_Box_Client(sdl_window=window, mouse_support=True)
        return window
    else:
        return "/Python/SDL_Window"

def lerp(x, y, t):
    return x * (1.0 - t) + y * t
