
KEYWORDS = {'integer', 'function', 'bool', 'real', 'if', 'endif', 
            'else', 'ret', 'put', 'get', 'while', 'true', 'false'}
SEPARATORS = {'(', ')', '{', '}', ',', ';', '#'}
OPERATORS = {'=', '==', '!=', '>', '<', '<=', '>=', '+', '-', '*', '/'}
DELIMITERS = {' ', '\n', '(', ')', '{', '}', ',', ';', '#'}

# DFA representation for identifiers returns true if is an identifier
def isID(input):
    # transition states 
    transition = {
        "letter": {
            "A": "B",
            "B": "C",
            "C": "C",
            "D": "C",
            "E": "E" # sink state to account for empty state
        },
        "digit": {
            "A": "E",
            "B": "D",
            "C": "D",
            "D": "D",
            "E": "E" # sink state to account for empty state
        }
    }
    
    # declartion of the DFAs definitions
    accepting = ["B", "C"]
    starting_state = "A"
    legal_letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    legal_digits = set("0123456789")
    current = starting_state
    
    # goes through the input string and follows the transition table
    for ch in input:
        # if input = l
        if ch in legal_letters:
            current = transition["letter"][current]
        # if input = d
        elif ch in legal_digits:
            current = transition["digit"][current]
        else:
        # neither letter or digit
            return False
    if current in accepting:
        return True
    else:
        return False

# DFA representation for integers returns true if an integer
def isInt(input):
    transition = {
        "A": "B",
        "B": "B"
    }
    
    legal_digits = set("0123456789")
    accepting = "B"
    # setting current to starting state
    current = 'A'
    for ch in input:
        if ch in legal_digits:
            current = transition[current]
        else: 
            return False
    if current == accepting:
        return True
    else: 
        return False

# dfa representation for real numbers ex: 123.321 returns true if input is a real number 
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
    legal_digits = set("0123456789")
    accepting = 'D'
    # setting current to starting state
    current = 'A'
    for ch in input:
        if ch in legal_digits:
            current = transition['digit'][current]
        elif ch == '.':
            current = transition['dot'][current]
        else:
            return False
    if current == accepting:
        return True
    else:
        return False

# classifies a given lexeme into a predefined token
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
        token = "INVALID TOKEN"
    return token, lexeme



testFiles = ["testCase1.txt", "testCase2.txt", "testCase3.txt"]
outputFiles = ["output1.txt", "output2.txt", "output3.txt" ]
for i in range(3):
    with open(testFiles[i], 'a') as f:
        f.write(' ')
# reads through all of the test files and outputs them into their respective output files
for i in range(3):
    with open(testFiles[i], 'r') as f, open(outputFiles[i], 'w') as out:
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


