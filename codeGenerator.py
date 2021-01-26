from nonTerminal import NonTerminal


class CodeGenerator:

    def __init__(self):
        self.lineCounter = 4
        self.file = open('output.c', 'w')
        self.file.write('#include <stdio.h>\n#include <setjmp.h>\n\nint main(){\n')

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
        self.lineCounter += 2
        self.add_nonTerminal_operation(p[0].place, op1_place, op3_place, p[2])

    def boolean_expression(self, p, temp, place1='', place3=''):
        p[0] = NonTerminal()
        p[0].place = temp
        op1_place = place1
        op3_place = place3
        if place1 == '':
            op1_place = p[1].get_value()
        if place3 == '':
            op3_place = p[3].get_value()
        self.add_nonTerminal_operation(p[0].place, op1_place, op3_place, p[2])
        # p[0].true = ''
        # p[0].false = ''
        # p[0].code = "\tif (" + p[1].get_value() + " " + p[2] + " " + p[3].get_value() + ") goto " + p[0].true + "\n"
        # p[0].code += "\tgoto " + p[0].false + '\n'
        # self.file.write(code)
        # self.lineCounter += 2

    def assign(self, p, temp, exp_place=''):
        print("%%%%%%")
        # print(p[0])
        # print(p[1])
        print(p[2])
        print(p[3])
        print("%%%%%%")
        p[0] = NonTerminal()
        p[0].place = temp
        op1_place = exp_place
        if exp_place == '':
            val = p[3].get_value()
            if val.startswith('B'):
                val = self.get_bool_result()
            op1_place = val
        p[0].code = p[0].place + ' = ' + str(op1_place)
        print(p[0].code)
        code = '\tint ' + temp + ';\n\t' + p[0].code + ';\n'
        self.file.write(code)
        self.lineCounter += 2
        print("#### ", op1_place)
        self.add_nonTerminal_assign(p[0].place, op1_place)
        self.delete_bool_vars()

    def not_assign(self, p, temp, exp_place=''):
        print("%%%%%%")
        # print(p[1])
        print(p[2])
        print("%%%%%%")
        p[0] = NonTerminal()
        p[0].place = temp
        op1_place = exp_place
        if exp_place == '':
            val = p[2].get_value()
            if val.startswith('B'):
                val = self.get_bool_result()
            op1_place = val
        p[0].code = p[0].place + ' = -' + str(op1_place)
        print(p[0].code)
        code = '\tint ' + temp + ';\n\t' + p[0].code + ';\n'
        self.file.write(code)
        self.lineCounter += 2
        print("#### ", op1_place)
        self.add_nonTerminal_assign_not(p[0].place, op1_place)
        self.delete_bool_vars()

    def print(self, ID):
        self.file.write('\tprintf("%d", ' + ID + ');\n')

    def end(self):
        self.file.write('\treturn 0;\n}')
        self.file.close()

    def add_nonTerminal_assign(self, name, value1):
        try:
            print("$$$$$$$")
            print(value1)
            print("$$$$$$$")
            NonTerminal.nonTerminals_list[name] = int(value1)
        except ValueError:
            value = NonTerminal.nonTerminals_list[value1]
            NonTerminal.nonTerminals_list[name] = value

    def add_nonTerminal_assign_not(self, name, value1):
        try:
            print("$$$$$$$")
            print(value1)
            print("$$$$$$$")
            NonTerminal.nonTerminals_list[name] = -1 * int(value1)
        except ValueError:
            value = NonTerminal.nonTerminals_list[value1]
            NonTerminal.nonTerminals_list[name] = -1 * value

    def add_nonTerminal_operation(self, name, value1, value2, operation):
        print(operation)
        print(type(operation))
        try:
            NonTerminal.nonTerminals_list[name] = self.do_operation(int(value1), int(value2), operation)
        except ValueError:
            try:
                value = NonTerminal.nonTerminals_list[value1]
                NonTerminal.nonTerminals_list[name] = self.do_operation(value, int(value2), operation)
            except:
                try:
                    value = NonTerminal.nonTerminals_list[value2]
                    NonTerminal.nonTerminals_list[name] = self.do_operation(int(value1), value, operation)

                except:
                    value_1 = NonTerminal.nonTerminals_list[value1]
                    value_2 = NonTerminal.nonTerminals_list[value2]
                    NonTerminal.nonTerminals_list[name] = self.do_operation(value_1, value_2, operation)

    def do_operation(self, value1, value2, operation):
        if operation == '+':
            return value1 + value2
        elif operation == '-':
            return value1 - value2
        elif operation == '*':
            return value1 * value2
        elif operation == '/':
            return int(value1 / value2)
        elif operation == '%':
            return value1 % value2
        elif operation == '>':
            if value1 > value2:
                return 1
            else:
                return 0
        elif operation == '<':
            if value1 < value2:
                return 1
            else:
                return 0
        elif operation == '>=':
            if value1 >= value2:
                return 1
            else:
                return 0
        elif operation == '>=':
            if value1 > value2:
                return 1
            else:
                return 0
        elif operation == '<=':
            if value1 <= value2:
                return 1
            else:
                return 0
        elif operation == '==':
            if value1 == value2:
                return 1
            else:
                return 0
        elif operation == '!=':
            if value1 > value2:
                return 1
            else:
                return 0

    def get_bool_result(self):
        for key, value in NonTerminal.nonTerminals_list.items():
            if key.startswith('B') and value == 0:
                return 0
        return 1

    def delete_bool_vars(self):
        list_ = []
        for key, value in NonTerminal.nonTerminals_list.items():
            if key.startswith('B'):
                list_.append(key)
        for item in list_:
            NonTerminal.nonTerminals_list.pop(item)
