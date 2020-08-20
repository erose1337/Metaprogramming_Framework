import pride
import pride.gui.widgetlibrary    
        
class Prompt(pride.gui.widgetlibrary.Text_Box):
    
    defaults = {"location" : "main", "prompt" : "\n>>> ", "program" : '',
                "end_of_field" : len("\n>>> "), "text" : '', "scroll_bars_enabled" : True}                  
 
    required_attributes = ("program", )
    
    def __init__(self, **kwargs):
        super(Prompt, self).__init__(**kwargs)
        self.text = self.text + "\n>>> "
        self.end_of_field = len(self.text)            
    
    def handle_return(self):
        output = pride.objects[self.program].handle_input(self.text[self.end_of_field:]) # slice off excess i.e. the prompt            
        self.text += (output or self.prompt) + "\n"
        self.end_of_field = len(self.text)
        
# input interface -> interpreter connection -> interpret input -> output and prompt
# pride.components.shell.Program_Shell -> pride.components.interpreter.Shell -> /Program/Interpreter -> .../Program_Shell/Prompt   
     
class Program_Shell(pride.gui.gui.Application):
               
    defaults = {"username" : '', "startup_definitions" : '',
                "ip" : "localhost", "port" : 40022,
                "target_service" : "/Program/Interpreter"}
                
    def __init__(self, **kwargs):
        super(Program_Shell, self).__init__(**kwargs)
        shell_connection = self.create("pride.components.interpreter.Shell", username=self.username, 
                                       startup_definitions=self.startup_definitions,
                                       ip=self.ip, port=self.port, target_service=self.target_service,
                                       stdout=self)
        shell_interface = self.create("pride.components.shell.Program_Shell", shell=shell_connection.reference)        
        self.prompt = self.create("pride.gui.shell.Prompt", program=shell_interface.reference)
        
        self._children.remove(shell_connection) # don't try to pack/draw
        self._children.remove(shell_interface) 
        
    def write(self, data):
        self.prompt.text_entry(data)
        