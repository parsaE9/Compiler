from lexer import Lexer
from Parser import Parser

lexer = Lexer().build()
file = open('parser contents//test.txt')
text_input = file.read()
file.close()
lexer.input(text_input)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
#     print(tok.type, tok.value)
parser = Parser()
parser.build().parse(text_input, lexer, False)
