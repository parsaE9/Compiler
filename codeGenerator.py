from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        self.file = open('output.c', 'w')
        self.file.write('#include <stdio.h>\n#include <setjmp.h>\n\nint main(){\n')
        self.nonTerminals_list = []

    def generate_arithmetic_code(self, p, temp, place1='', place3=''):
        p[0] = NonTerminal()
        p[0].place = temp
        p[0].code = p[0].place + " = "
        op1_place = place1
        op3_place = place3
        if place1 == '':
            op1_place = p[1].get_value()
        if place3 == '':
            op3_place = p[3].get_value()
        p[0].code += op1_place + " " + p[2] + " " + op3_place
        code = '\tint ' + temp + ';\n\t' + p[0].code + ';\n'
        self.file.write(code)

    def assign(self, p, temp, exp_place=''):
        print("---------------")
        print(p[0])
        print(p[1])
        print(p[2])
        print(p[3])
        print("---------------")
        p[0] = NonTerminal()
        self.nonTerminals_list.append(p[0])
        p[0].place = temp
        op1_place = exp_place
        if exp_place == '':
            op1_place = p[3].get_value()
        p[0].code = p[0].place + ' = ' + op1_place
        code = '\tint ' + temp + ';\n\t' + p[0].code + ';\n'
        self.file.write(code)

    def print(self, ID):
        self.file.write('\tprintf("%d", ' + ID + ');\n')

    def end(self):
        self.file.write('\treturn 0;\n}')
        self.file.close()
