from ply import lex


class Lexer:

    # reserved keywords, we do like this to make compilation faster
    reserved = {
        'if': 'IF',
        'else': 'ELSE',
        'elseif': 'ELSEIF',
        'then': 'THEN',
        'while': 'WHILE',
        'print': 'PRINT',
        'fun': 'FUNCTION',
        'return': 'RETURN',
        'main': 'MAIN',
        'on': 'ON',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
        'in': 'IN',
        'Error': 'ERROR',
    }

    tokens = [
        'LRB', 'RRB', 'LCB', 'RCB', 'LSB', 'RSB',
        'INTEGER', 'FLOAT', 'ID',
        'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'ASSIGN',
        'LT', 'GT', 'GE', 'LE', 'EQ', 'NE',
        'SEMICOLON', 'COLON', 'COMMA',
    ] + list(reserved.values())

    # COLONS
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','
    # BRACKETS
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LSB = r'\['
    t_RSB = r'\]'

    # OPERATOR
    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = r'\%'
    t_GT = r'\>'
    t_LT = r'\<'
    t_GE = r'\>='
    t_LE = r'\<='
    t_EQ = r'\=='
    t_NE = r'\!='

    def t_ERROR(self, t):
        r'(\d+\.\d+\.\d*)|([0-9]+[a-zA-Z_]+)|([A-Z][a-zA-z0-9_]*)|([\+\-\*\/\%][ \+\-\*\/\%]+)'
        return t

    def t_FLOAT(self, t):
        r'\d+\.\d+'
        if len(t.value.split('.')[0]) < 10 and len(t.value.split('.')[1]) < 10:
            t.value = float(t.value)
            return t
        t.type = "ERROR"
        return t

    def t_INTEGER(self, t):
        r'\d+'
        # r'[+|-]?(\d+)'
        # print(t, t.value, len(t.value))
        if len(t.value) < 10:
            t.value = int(t.value)
            return t
        t.type = "ERROR"
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words
        # Look up symbol table information and return a tuple
        # t.value = (t.value, symbol_lookup(t.value))
        return t

    # def t_KEYWORD(self, t):
    #     r'[a-zA-Z][a-zA-Z_0-9]*'
    #     t.type = self.reserved.get(t.value, 'KEYWORD')  # Check for reserved words
    #     # Look up symbol table information and return a tuple
    #     # t.value = (t.value, symbol_lookup(t.value))
    #     return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    # to discard a token, such as comment, simply define a token rule that returns no value
    def t_COMMENT(self, t):
        r'\#.*'
        pass
        # No return value. Token discarded

    # alternative solution
    # t_ignore_LEADINGZERO = r'0+'

    def t_error(self, t):
        # raise Exception('Error at', t.value)
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
