from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        self.file = open('output.c', 'w')
        self.file.write('#include <stdio.h>\n#include <setjmp.h>\n\nint main(){\n')

    def generate_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[0].place + " = "
        p[0].code += p[1].get_value() + " " + p[2] + " " + p[3].get_value()
        code = '\tdouble ' + temp + ';\n\t' + p[0].code + ';\n'
        self.file.write(code)

    def end(self):
        self.file.write('}')
        self.file.close()