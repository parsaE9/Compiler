class SymbolTableObjects:
    def __init__(self, name, entity_type, var_type='', return_type='none', size=-1, scope='', place=''):
        self.name = name
        self.entity_type = entity_type
        self.var_type = var_type
        self.size = size
        self.address = -1
        self.return_type = return_type
        self.place = place
        self.scope = scope