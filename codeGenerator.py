from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        self.file = open('output.c', 'w')
        self.file.write('#include <stdio.h>\n#include <setjmp.h>\n\nint main(){\n')
        self.stac = []

    def generate_arithmetic_code(self, p, temp):
        p[0] = NonTerminal()
        # p[0].place = temp
        # p[0].code = p[0].place + " = "
        # p[0].code += p[1].get_value() + " " + p[2] + " " + p[3].get_value()
        # code = '\tdouble ' + temp + ';\n\t' + p[0].code + ';\n'
        # self.stac.append(p[0])
        # self.file.write(code)

    def assign(self, p, temp):
        pass
        # print(p[1])
        # print(p[2])
        # print(p[3])
        # # x = input('$$$$$$$$$$$$$$$$$$')
        # p[0] = NonTerminal()
        # p[0].place = temp
        # p[0].code = p[0].place + ' = ' + p[3].get_value()
        # code = '\tdouble ' + temp + ';\n\t' + p[0].code + ';\n'
        # self.stac.append(p[0])
        # self.file.write(code)

    def assign2(self, p, temp):
        pass
        # print(p[0])
        # print(p[1])
        # p[0] = NonTerminal()
        # p[0].place = temp
        # p[0].code = p[0].place + ' = ' + p[3].get_value()
        # code = '\tdouble ' + temp + ';\n\t' + p[0].code + ';\n'
        # self.file.write(code)

    def end(self):
        self.file.write('}')
        self.file.close()