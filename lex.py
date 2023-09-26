
KEYWORDS = {'integer', 'function', 'bool', 'real', 'if', 'endif', 
            'else', 'ret', 'put', 'get', 'while', 'true', 'false'}
SEPARATORS = {'(', ')', '{', '}', ',', ';'}
OPERATORS = {'=', '==', '!=', '>', '<', '<=', '>=', '+', '-', '*', '/'}
DELIMITERS = {' ', '\n', '(', ')', '{', '}', ',', ';'}

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
    # THIS COULD HAVE BEEN DONE ON ONE LINE BUT I THINK THE PROFESSOR WANTS US TO USE THE DFA
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
        result = f"KEYWORD: {lexeme}"
    elif lexeme in OPERATORS:
        result = f"OPERATOR: {lexeme}"
    elif lexeme in SEPARATORS:
        result = f"SEPARATOR: {lexeme}"
    elif isReal(lexeme):
        result = f"REAL: {lexeme}"
    elif isID(lexeme):
        result = f"IDENTIFIER: {lexeme}"
    elif isInt(lexeme):
        result = f"INTEGER: {lexeme}"
    else:
        result = False
    return result


# main loop
with open('testCase1.txt', 'r') as f:
    ch = f.read(1)
    while ch:
        buffer = ''
        while ch not in DELIMITERS:
            buffer += ch
            ch = f.read(1)
        # need to account for separators and <= and >= 
        if ch in SEPARATORS:
            print(lexer(buffer))
            print(lexer(ch))
            ch = f.read(1)
        else:
            print(lexer(buffer))
            ch = f.read(1)
    


