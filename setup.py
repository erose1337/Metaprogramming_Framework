from setuptools import setup

#with open(".\\pride\\readme.md", 'r') as _file:
#    long_description = _file.read()
    
# create list of all the pride\gui\resources files
import os
import os.path

def find_resource_files(directory):
    is_file = os.path.isfile      
    join = os.path.join
    folder_list = [directory]
    output = []
    for current_folder in folder_list:        
        file_list = os.listdir(current_folder)    
        folder_files = []
        entry = (current_folder, folder_files)
        print("Searching through {}".format(current_folder))
        for item in file_list:
            item = join(current_folder, item)            
            if is_file(item):                
                folder_files.append(item)
                print("Added {}".format(folder_files[-1]))
            else:
                print("Queuing folder {}".format(item))
                folder_list.append(item)
        if folder_files:
            output.append(entry)
    return output
        
options = {"name" : "pride",
           "version" : "7.1.0a",
           "description" : "Python runtime and integrated development environment",
           "long_description" : '',
           "url" : "https://github.com/erose1337/pride",
           "download_url" : "https://github.com/erose1337/pride/archive/master.zip",
           "author" : "Ella Rose",
           "author_email" : "python_pride@protonmail.com",
           "packages" : ["pride", "pride.audio", "pride.gui", "pride.programs",
                         "pride.components", "pride.functions"],
           #"scripts" : ["main.py"],
           "data_files" : [("pride\\gui", ["pride\\gui\\libfreetype-6.dll", "pride\\gui\\SDL2.dll", "pride\\gui\\SDL2_ttf.dll",
                                           "pride\\gui\\sdlgfx.dll", "pride\\gui\\zlib1.dll", "pride\\gui\\sdlgfx.lib"])] +
                          find_resource_files(os.path.join("pride", "gui", "resources")),
           #"include_package_data" : True,
           "classifiers" : ["Development Status :: 4 - Alpha", 
                            "Intended Audience :: Developers",
                            "Intended Audience :: End Users/Desktop",
                            "Operating System :: Microsoft :: Windows",
                            "Operating System :: POSIX :: Linux",
                            "Programming Language :: Python :: 2.7",
                            "Topic :: Desktop Environment", "Topic :: Documentation",
                            "Topic :: Games/Entertainment", "Topic :: Multimedia :: Sound/Audio",
                            "Topic :: Software Development :: Libraries :: Application Frameworks",
                            "Topic :: Software Development :: Libraries :: Python Modules",
                            "Topic :: Software Development :: User Interfaces",
                            "Topic :: Software Development :: Widget Sets",
                            "Topic :: System :: Distributed Computing",
                            "Topic :: System :: Shells", 
                            "Topic :: Text Editors :: Integrated Development Environments (IDE)"]
                            }
if __name__ == "__main__":
    setup(**options)
    