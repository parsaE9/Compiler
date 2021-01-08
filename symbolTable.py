from symbolTableObjects import SymbolTableObjects

class SymbolTable:
    def __init__(self):
        self.object_list = []
        self.stack = []
        self.current_scope = ''
        self.current_address = 0
        self.current_type = ''

    # TODO param arr[] left

    def add_variable(self, name):
        new_obj = SymbolTableObjects(name, 'variable', scope=self.current_scope)
        self.object_list.append(new_obj)
        self.stack.append(new_obj)

    def add_array(self, name, length):
        for i in range(0, length):
            self.add_variable(name + '[' + str(i) + ']')

    def already_defined(self, name):
        for var in self.object_list:
            if name == var.name:
                # TODO check when scope changes
                return True
        return False

    def add_param_var(self, name):
        size = self.get_type_size(self.current_type)
        new_obj = SymbolTableObjects(name, 'variable', var_type=self.current_type, size=size)
        if len(self.object_list) == 0:
            new_obj.address = 0
            self.current_address = size
        else:
            head_obj = self.object_list[len(self.object_list) - 1]
            address = head_obj.size + head_obj.address
            new_obj.address = address
            self.current_address += size
        self.object_list.append(new_obj)
        self.stack.append(new_obj)

    def set_var_type(self, type_):
        increment = self.get_type_size(type_)
        # for function param, in this case stack is empty
        if len(self.stack) == 0:
            self.current_type = type_
            return
        for var in self.stack:
            var.var_type = type_
            var.size = increment
            if self.current_address == 0:
                var.address = 0
                self.current_address = increment
            else:
                var.address = self.current_address
                self.current_address += increment
        self.stack.clear()

    def end(self):
        for var in self.object_list:
            if var.scope == '':
                var.scope = 'main'

    def get_type_size(self, type_):
        size = 0
        if type_ == 'Int':
            size = 4
        elif type_ == 'Float':
            size = 8
        elif type_ == 'Boolean':
            size = 1
        return size

    def print_symbolTable(self):
        template = "{0:20}|{1:12}|{2:12}|{3:12}|{4:12}|{5:12}|{6:12}|{7:12}"
        print("----------------------------------------------------------------------------------------------------")
        print(template.format("name", "entity type", "var type", "size", "address", "return type", "scope", "place"))
        print("----------------------------------------------------------------------------------------------------")
        for var in self.object_list:
            print(template.format(var.name, var.entity_type, var.var_type, str(var.size), str(var.address),
                                  var.return_type, var.scope, var.place))

    def new_scope_begin(self):
        self.current_scope = 'new_scope'
        for param in self.stack:
            param.scope = self.current_scope
        self.stack.clear()

    def new_scope_end(self, scope_name):
        for var in self.object_list:
            if var.scope == 'new_scope':
                var.scope = scope_name
        self.current_scope = ''

    def add_place(self, name, place):
        for var in self.object_list:
            if var.name == name:
                var.place = place

    def find_place(self, name):
        for var in self.object_list:
            if var.name == name:
                return var.place