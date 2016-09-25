import pride.components.networkssl
        
if __name__ == "__main__":
    certificate = pride.components.networkssl.Self_Signed_Certificate(parse_args=True)    
    pride.Instruction("/Python", "exit").execute()