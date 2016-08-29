import pride.networkssl
        
if __name__ == "__main__":
    certificate = pride.networkssl.Self_Signed_Certificate(parse_args=True)    
    pride.Instruction("/Python", "exit").execute()