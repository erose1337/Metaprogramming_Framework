import importlib
import os
import sys
import inspect
import mpre.utilities as utilities
import mpre._compile
import mpre.fileio
import mpre.importers

startup_modules = ["mpre." + module_name for module_name 
                   in ("defaults", "metaclass", "base", "network", 
                       "_metapython", "shell_launcher")]
required_modules = ["sys", "os", "types", "pickle", "importlib"]
embed_objects = [utilities, mpre.importers]
LAUNCHER_FILENAME = "exelauncher.py"

def build_launcher(from_modules):
    with open(LAUNCHER_FILENAME, 'w+') as launcher:
        imports = r''
        for module in required_modules:
            imports += "import {}\n".format(module)
        launcher.write(imports)
        
        embedded_string = r''
        for embedded_object in embed_objects:
            embedded_string += "{}\n\n".format(inspect.getsource(embedded_object))
        launcher.write(embedded_string)
        
        add_module = r"Encrypted_String_Importer.add_module('{}', {}_source)" + "\n\n"
        for module_name in from_modules:
            _module_name = module_name.replace('.', '_')
            importlib.import_module(module_name)
            source = inspect.getsource(sys.modules[module_name])
            encrypted_file = mpre.fileio.Encrypted_File(module_name, file_system="virtual", 
                                                        persistent=True)
            encrypted_file = encrypted_file.update() # make it attach source so it can be rebuilt
            encrypted_file.write(source)
            launcher.write("{}_source = r'''{}'''\n\n".format(_module_name, 
                                                              encrypted_file.save()))
            launcher.write(add_module.format(module_name, _module_name))
        launcher.write("sys.meta_path = [Encrypted_String_Importer()]\n\n")
        launcher.write("if __name__ == '__main__':\n")
        launcher.write("    import mpre._metapython\n")
        launcher.write("    metapython = mpre._metapython.Metapython(parse_args=True)\n")
        launcher.write("    metapython.start_machine()")
        launcher.flush()
        mpre._compile.py_to_compiled([LAUNCHER_FILENAME], 'exe')
        
if __name__ == "__main__":
    build_launcher(startup_modules)
    #os.remove(LAUNCHER_FILENAME)