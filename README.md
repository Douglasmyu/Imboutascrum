## To Do

- [] create dicts for other identifiers: keywords(subset of id), delimiters/separators, operators
- [] implement isdigit() (do we have to use our fsm or can we just use .isnumeric())
- [x] implement isID() //takes string and returns true if it passes as an id
- [] implement isreal()
- [] implement lexer() function
  - reads through each character
  - creates a 'buffer' and adds characters to it until you hit a delimiter
  - once you hit a delimiter:
    - check if buffer forms a token
    - if it does, print token and lexeme (maybe into textfile?) (put tokens and lexemes in dict?)
    - clear buffer and continue parsing text
