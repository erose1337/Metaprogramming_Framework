# pride.objectlibrary.shell_launcher - default module for launching the python shell 
import pride.objectlibrary.user

def launch_shell(user=None):       
    user = pride.objectlibrary.user.User(parse_args=True) if user is None else user
    
    user.create("pride.objectlibrary.interpreter.Shell", username=user.username, parse_args=True)
    
    try:
        command_line = user.objects["Command_Line"][0]
    except KeyError:
        command_line = user.create("pride.objectlibrary.shell.Command_Line")
    python_shell = command_line.create("pride.objectlibrary.shell.Python_Shell")
    command_line.set_default_program(python_shell.name, (python_shell.reference, "handle_input"), set_backup=True)
    
if __name__ == "__main__":   
    launch_shell()