import getpass

import zxcvbn

def password_selection(prompt):
    while True:
        password = getpass.getpass(prompt)
        password_stats = zxcvbn.password_strength(password)
        output = (password_stats["crack_time"], password_stats["crack_time_display"],
                  password_stats["entropy"], password_stats["score"])
        print("Time to crack: {} ({}); Entropy: {}; Score: {}/4;".format(*output))          
        if raw_input("Really use the supplied password?: y/n ")[0].lower() == 'y':
            return password       
                        
def test_password_selection():
    password = password_selection("Please create a password: ")
    
if __name__ == "__main__":
    test_password_selection()
    