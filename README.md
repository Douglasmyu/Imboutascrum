## To Do

- [x] create dicts for other identifiers: keywords(subset of id), delimiters/separators, operators
- [x] implement isdigit() (do we have to use our fsm or can we just use .isnumeric())
- [x] implement isID() //takes string and returns true if it passes as an id
- [x] implement isreal()
- [x] implement lexer() function - takes in buffer/lexeme and returns token + lexem
- [ ] create the main loop - reads through input file char by char from input.txt - adds chars into 'buffer' until hitting a separator/delimiter (also account for cases like >=) - once you hit a separator, call lexer function that returns token + lexeme - write token + lexeme into output file - clear buffer to start recognizing next token

## Questions:

- clarify the process for turning nfsms -> dfas -> code
  (how do we handle empty/epsilon values) => i just used a "sink" value
- do we really have to implement integer dfa using the fsm or can we just use .isnumeric()
- in what format and where do we output the data

## other things to do

- double check nfsms and resulting dfas
- double check list of keywords, separators, operators
- create test cases (at least 3)
- turn .py file into an .exe file
- write documentation
