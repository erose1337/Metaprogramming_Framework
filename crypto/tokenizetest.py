import tokenize

FILENAME = "tokenizetest.py"

with open(FILENAME, 'r') as _file:
    token_info = tokenize.generate_tokens(_file.readline)
    
    for info in token_info:
        print info