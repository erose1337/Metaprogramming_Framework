""" pride.site_config - site configuration module.

    Site specific defaults, mutable_defaults, flags, and verbosity may be set
    here. Entries take the form of the full name of the object, meaning the
    name of the class, the module the class resides in, and any packages the
    module resides in. Because the '.' symbol denotes attribute access, names
    must have the '.' symbol replaced with '_'. For example:
        
        pride_user_User_defaults = {'username' : 'localhost'}
        
    The above line effectively does the following at runtime, before the class
    is constructed:
    
        pride.components.user.User.defaults["username"] = "localhost"
        
    This feature is facilitated by the Base metaclass and will work for all
    objects that inherit from Base.
    
    Note that these are the class defaults, meaning that all instances will
    use these values when instantiated (unless the attributes were specified
    explicitly).
    
    For more information on Base objects and default attributes, please see the
    documentation for pride.components.base.Base 
    
    Temporary customization
    ---------
    The site_config file can be modified temporarily for a single execution via
    command line argument. Simply enter the --site_config flag followed by the
    desired entries, like so:
        
        python -m pride.main --site_config pride_user_User_defaults['username']='Ella'
        
    This will use a different default username for a single execution of the program.
    
    Multiple changes can be made with multiple statements, separated via semicolons:
        
        python -m pride.main --site_config pride_user_User_verbosity['password_verified']=0;pride_user_User_defaults['username']='Ella'            
    """   
# site_config 
# defaults specified here will override defaults defined in the source code
import os

def ensure_folder_exists(pathname):
    path_progress = r''    
    for directory in os.path.split(pathname):
        path_progress = os.path.join(path_progress, directory)
        if not os.path.exists(path_progress) or not os.path.isdir(path_progress):
            os.mkdir(path_progress) 
            
PRIDE_DIRECTORY = os.path.split(os.path.abspath(__file__))[0]
AUDIO_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "audio")

DATA_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "data")  
DATABASE_DIRECTORY = os.path.join(DATA_DIRECTORY, "database")
LOG_DIRECTORY = os.path.join(DATA_DIRECTORY, "log")

ensure_folder_exists(DATA_DIRECTORY)
ensure_folder_exists(DATABASE_DIRECTORY)
ensure_folder_exists(LOG_DIRECTORY)  

FUNCTIONS_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "functions")
GUI_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "gui")
OBJECTLIBRARY_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "components")
PROGRAMS_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "programs")

SITE_CONFIG_FILE = __file__ if __file__[-1] != 'c' else __file__[:-1]
del os

import sys
def write_to(entry, **values):    
    site_config_module = sys.modules[__name__]
    if hasattr(site_config_module, entry):
        file_data = "\n{}.update({})\n"
    else:        
        file_data = "\n{} = {}\n"
    file_data = file_data.format(entry, str(values))    
    with open(SITE_CONFIG_FILE, 'a') as _file:
        _file.write(file_data)
        _file.flush()
        
pride_components_interpreter_Shell_defaults = {"startup_definitions" : \
r"""import pride.components.base
import pride

from pride.functions.utilities import documentation, usage

def open_firefox():
    try:
        import selenium.webdriver
    except ImportError:
        pass
    else:
        return selenium.webdriver.Firefox()
        
def create(instance_type, *args, **kwargs):
    return objects["/Python"].create(instance_type, *args, **kwargs)

def delete(reference):
    objects[reference].delete()     

def logout(program="/User/Shell"):
    objects[program].logout()
    
#import pride.audio
#pride.audio.enable()
import pride.gui
window = pride.gui.enable()

#trace = objects[window].create("pride.gui.bittrace.Animated_Bit_Trace")
#import animated
#slider = objects[window].create(animated.Slider_Puzzle)


#w = objects[window].create("pride.gui.gui.Window")
#def new(pack_mode, w=w):
#    _object = w.create("pride.gui.gui.Container", pack_mode=pack_mode)   
#    w.pack()    
#    return _object
#    
#def organizer_test(pieces=("top", "bottom", "main", "left", "left", "right"), w=w):
#    components = [new(piece) for piece in pieces]
#    w.pack()
#    return components
#top, bottom, main, left1, left2, right = organizer_test()

#import pride.components.sdts
#
#client1 = pride.components.sdts.Secure_Data_Transfer_Client(username="Ella6")
#client2 = pride.components.sdts.Secure_Data_Transfer_Client(username="Ella7")
#client1.connect("Ella7", client2.public_key)
 
#_map = objects["/Python/SDL_Window"].create("map.Map")
#test = objects["/Python/SDL_Window"].create("pride.gui.organizerunittest.Organizer_Unit_Test")
#game = objects["/Python/SDL_Window"].create("game2.gui.battlescreen.Battle_Screen.unit_test")
calendar = objects["/Python/SDL_Window"].create("pride.gui.calendar.Calendar", month="August")

"""}

pride_components_rpc_Rpc_Server_defaults = {'keyfile': 'c:\\users\\_\\pythonbs\\pride\\data\\ssl_server.key', 'certfile': 'c:\\users\\_\\pythonbs\\pride\\data\\ssl_server.crt'}
