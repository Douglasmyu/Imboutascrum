
KEYWORDS = {'integer', 'function', 'bool', 'real', 'if', 'endif', 
            'else', 'ret', 'put', 'get', 'while', 'true', 'false'}
SEPARATORS = {'(', ')', '{', '}', ',', ';', '#'}
OPERATORS = {'=', '==', '!=', '>', '<', '<=', '>=', '+', '-', '*', '/'}
DELIMITERS = {' ', '\n', '(', ')', '{', '}', ',', ';', '#'}

# takes in a string and returns true or false if string is an indentifier  
def isID(input):
    # basically the final dfa shoved into a dict
    transition = {
        "letter": {
            "A": "B",
            "B": "C",
            "C": "C",
            "D": "C",
            "E": "E" # sink state to account for empty
        },
        "digit": {
            "A": "E",
            "B": "D",
            "C": "D",
            "D": "D",
            "E": "E" # sink state to account for empty
        }
    }
    
    accepting = ["B", "C"]
    starting_state = "A"
    current = starting_state
    
    # loops through input string and follows dfa table
    for ch in input:
        # if input = l
        if ch.isalpha():
            current = transition["letter"][current]
        # if input = d
        elif ch.isnumeric():
            current = transition["digit"][current]
        else:
        # neither letter or digit
            return "False"
    if current in accepting:
        return True
    else:
        return False

# takes in input string and returns if is an int
def isInt(input):
    transition = {
        "A": "B",
        "B": "B"
    }
    legal_inputs = ['0','1','2','3','4','5','6','7','8','9']
    accepting = "B"
    # setting current to starting state
    current = 'A'
    for ch in input:
        if ch in legal_inputs:
            current = transition[current]
        else: 
            return False
    if current == accepting:
        return True
    else: 
        return False

# takes in input string and returns true if follows real number re    
def isReal(input):
    transition = {
        "digit": {
            'A': 'B',
            'B': 'B',
            'C': 'D',
            'D': 'D',
            'E': 'E' # represents empty state
        },
        "dot": {
            'A': 'E',
            'B': 'C',
            'C': 'E',
            'D': 'E',
            'E': 'E' # sink state
        }
    }
    accepting = 'D'
    # setting current to starting state
    current = 'A'
    for ch in input:
        if ch.isnumeric():
            current = transition['digit'][current]
        elif ch == '.':
            current = transition['dot'][current]
        else:
            return False
    if current == accepting:
        return True
    else:
        return False

# takes buffer as input and returns token and lexeme 
def lexer(lexeme):
    if lexeme in KEYWORDS:
        token = "KEYWORDS"
    elif lexeme in OPERATORS:
        token = "OPERATOR"
    elif lexeme in SEPARATORS:
        token = "SEPARATOR"
    elif isReal(lexeme):
        token = "REAL"
    elif isID(lexeme):
        token = "IDENTIFIER"
    elif isInt(lexeme):
        token = "INTEGER"
    else:
        # if token is unreadable return false
        token = False
    return token, lexeme

with open('testCase3.txt', 'a') as f:
    f.write(' ')

# main code
with open('testCase3.txt', 'r') as f, open('output.txt', 'w') as out:
    
    # string formatting and title creation
    string_format = "{:<15} {}"
    underline = '-' * 22
    print(string_format.format("TOKEN", "LEXEME"))
    print(underline)
    out.write(string_format.format("TOKEN", "LEXEME") + '\n')
    out.write(underline + '\n')
    isComment = False
    # read in initial char
    ch = f.read(1)

    # while there is a char to read
    while ch:
        # initialize empty buffer
        buffer = ''
        
        # handling comments
        if ch == '[':
            nextCh = f.read(1)
            if nextCh == '*':
                isComment = True
            else:
                buffer += ch
                ch = nextCh 
                continue
        elif isComment and ch == '*':
            nextCh = f.read(1)
            if nextCh == ']':
                isComment = False
                ch = f.read(1)
                continue
        if isComment:
            ch = f.read(1)
            continue
            
        # read in ch until hitting delim
        while ch not in DELIMITERS:
            buffer += ch
            ch = f.read(1)
        # if there is something in buffer call lexer for token and print
        if buffer:
            token = lexer(buffer)[0]
            lexeme = lexer(buffer)[1]
            if token:
                out.write(string_format.format(token, lexeme) + '\n')
                print(string_format.format(token, lexeme))
        # if current char is a separator print separator
        if ch in SEPARATORS:
            token = lexer(ch)[0]
            if token:
                out.write(string_format.format(token, ch) + '\n')
                print(string_format.format(token, ch))
                
        ch = f.read(1)

