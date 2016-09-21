import pride.functions.utilities
import pride.objectlibrary.base

class Documentation_Creator(pride.objectlibrary.base.Base):
        
    defaults = {"object_name" : '', "parse_args" : True}

    def __init__(self, **kwargs):
        super(Documentation_Creator, self).__init__(**kwargs)        
        self.create("pride.objectlibrary.package.Documentation", resolve_string(self.object_name))
    
if __name__ == "__main__":  
    documentation_creator = Documentation_Creator()
    # and done!