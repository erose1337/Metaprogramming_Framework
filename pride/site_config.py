""" pride.site_config - site configuration module.

    Site specific defaults, mutable_defaults, predefaults, and verbosity may be set
    here. Entries go in the config dictionary, and should take the form of the full
    name of the object, meaning the name of the class, the module the class resides
    in, and any packages the module resides in:

        config["pride.components.user.User.defaults"].update({'username' : 'localhost'})

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

        python -m pride.main --site_config pride.user.User.defaults = {\'username\':\'Ella\'}

    This will use a different default username for a single execution of the program.

    Multiple changes can be made with multiple statements, separated via semicolons:

        python -m pride.main --site_config pride.user.User.verbosity = {\'password_verified\':0};pride.user.User.defaults = {\'username\':\'Ella\'}

    Alternative configurations
    ------
    It is possible to run multiple instances of pride with different site_config values.
    Simply create a shell script that runs:

        python -m pride.main --site_config ...(config entries here)...
    """
# site_config
# defaults specified here will override defaults defined in the source code
import os
import ast
import ConfigParser
import base64

def ensure_folder_exists(pathname):
    path_progress = r''
    for directory in os.path.split(pathname):
        path_progress = os.path.join(path_progress, directory)
        if not os.path.exists(path_progress) or not os.path.isdir(path_progress):
            os.mkdir(path_progress)
        assert os.path.exists(path_progress)
        assert os.path.isdir(path_progress)

PRIDE_DIRECTORY = os.path.split(os.path.abspath(__file__))[0]
AUDIO_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "audio")

DATA_DIRECTORY = os.path.join(os.path.expanduser('~'), "pride")
DATABASE_DIRECTORY = os.path.join(DATA_DIRECTORY, "database")
LOG_DIRECTORY = os.path.join(DATA_DIRECTORY, "log")

ensure_folder_exists(DATA_DIRECTORY)
ensure_folder_exists(DATABASE_DIRECTORY)
ensure_folder_exists(LOG_DIRECTORY)

FUNCTIONS_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "functions")
GUI_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "gui")
OBJECTLIBRARY_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "components")
PROGRAMS_DIRECTORY = os.path.join(PRIDE_DIRECTORY, "programs")

CONFIGURATION_FILE = os.path.join(DATA_DIRECTORY, "default.ini")#__file__ if __file__[-1] != 'c' else __file__[:-1]

class Config_File(object):

    def __init__(self, filename):
        self._config = ConfigParser.ConfigParser()
        self.setup_file(filename)

    def setup_file(self, filename):
        self.filename = filename
        entries = self.mapping = dict()
        _config = self._config
        _config.read(filename)
        for section in _config.sections():
            entry_dict = entries[section] = dict()
            for option, value in _config.items(section):
                value = ast.literal_eval(value)
                if isinstance(value, str):
                    value = base64.standard_b64decode(value)
                entry_dict[option] = value

    def write_to(self, entry, **values):
        for key, value in values.items():
            self[entry, key] = value

    def __contains__(self, key):
        return self._config.has_section(key)

    def __getitem__(self, key):
        length = len(key)
        if length > 2 or length == 1:
                return self.mapping[key]
        else:
            return self.mapping[key[0]][key[1]]

    def __setitem__(self, key, value):
        _config = self._config
        key0, key1 = key
        try:
            self.mapping[key0][key1] = value
        except KeyError:
            if key0 not in self.mapping:
                _config.add_section(key0)
                self.mapping[key0] = {key1 : value}
            else:
                raise
        _config.set(key0, key1, "'{}'".format(base64.standard_b64encode(value)))
        with open(self.filename, 'r+') as _file:
            _config.write(_file)

config = Config_File(CONFIGURATION_FILE)
write_to = config.write_to
config["pride.components.interpreter.Shell.defaults", "startup_definitions"] = \
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
    objects[program].logout()"""
