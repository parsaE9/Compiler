from ply import yacc
from lexer import Lexer


class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        # self.tempCount = 0
        # self.codeGenerator = CodeGenerator()
        pass

    def p_program(self, p):
        """program : declist MAIN LRB RRB block"""
        print("program : declist MAIN LRB RRB block")

    def p_program_simple(self, p):
        """program : MAIN LRB RRB block"""
        print("program : MAIN LRB RRB block")

    def p_declist_dec(self, p):
        """declist : dec"""
        print("declist : dec")

    def p_declist_declist(self, p):
        """declist : declist dec"""
        print("declist : declist dec")

    # TODO : commenting this reduces 2 conflicts but doesn't parse p_program without declist any more so i added p_program_simple rule
    # def p_declist_lambda(self, p):
    #     """declist : """
    #     print("declist : ")

    def p_dec_vardec(self, p):
        """dec : vardec"""
        print("dec : vardec")

    def p_dec_funcdec(self, p):
        """dec : funcdec"""
        print("dec : funcdec")

    def p_type_integer(self, p):
        """type : INTEGER"""
        print("type : INTEGER")

    def p_type_float(self, p):
        """type : FLOAT"""
        print("type : FLOAT")

    def p_type_boolean(self, p):
        """type : BOOLEAN"""
        print("type : BOOLEAN")

    def p_iddec_id(self, p):
        """iddec : ID"""
        print("iddec : ID")

    def p_iddec_id_array(self, p):
        """iddec : ID LSB exp RSB"""
        print("iddec : ID LSB exp RSB")

    def p_iddec_id_assign(self, p):
        """iddec : ID ASSIGN exp"""
        print("iddec : ID ASSIGN exp")

    # def p_iddec_array_assign(self, p):
    #     "iddec : ID ASSIGN ID LSB exp RSB"
    #     print("iddec : ID ASSIGN ID LSB exp RSB")

    def p_idlist_iddec(self, p):
        """idlist : iddec"""
        print("idlist : iddec")

    def p_idlist_idlist(self, p):
        """idlist : idlist COMMA iddec"""
        print("idlist : idlist COMMA iddec")

    def p_vardec_idlist(self, p):
        """vardec : idlist COLON type SEMICOLON"""
        print("vardec : idlist COLON type SEMICOLON")

    def p_funcdec_type_block(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB COLON type block"""
        print("funcdec : FUNCTION ID LRB paramdecs RRB COLON type block")

    def p_funcdec_block(self, p):
        """funcdec : FUNCTION ID LRB paramdecs RRB block"""
        print("funcdec : FUNCTION ID LRB paramdecs RRB block")

    def p_paramdecs_paramdecslist(self, p):
        """paramdecs : paramdecslist"""
        print("paramdecs : paramdecslist")

    def p_paramdecs_lambda(self, p):
        """paramdecs : """
        print("paramdecs : ")

    def p_paramdecslist_paramdec(self, p):
        """paramdecslist : paramdec"""
        print("paramdecslist : paramdec")

    def p_paramdecslist_paramdecslist(self, p):
        """paramdecslist : paramdecslist COMMA paramdec"""
        print("paramdecslist : paramdecslist COMMA paramdec")

    def p_paramdec_id(self, p):
        """paramdec : ID COLON type"""
        print("paramdec : ID COLON type")

    def p_paramdec_id_array(self, p):
        """paramdec : ID LSB RSB COLON type"""
        print("paramdec : ID LSB RSB COLON type")

    def p_block_stmtlist(self, p):
        """block : LCB stmtlist RCB"""
        print("block : LCB stmtlist RCB")

    def p_stmtlist_stmt(self, p):
        """stmtlist : stmt"""
        print("stmtlist : stmt")

    def p_stmtlist_stmtlist(self, p):
        """stmtlist : stmtlist stmt"""
        print("stmtlist : stmtlist")

    # TODO : commenting this grammar reduces 30 conflicts and doesn't produce errors but i'm not sure if it parses correctly
    # def p_stmtlist_lambda(self, p):
    #     """stmtlist : """
    #     print("stmtlist : ")

    #
    # def p_varlist_varlist(self, p):
    #     "varlist : varlist vardec"
    #     print("varlist : varlist vardec")

    def p_lvalue_id_array(self, p):
        """lvalue : ID LSB exp RSB"""
        print("lvalue : ID LSB exp RSB")

    def p_lvalue_id(self, p):
        """lvalue : ID"""
        print("lvalue : ID")

    def p_case_where(self, p):
        """case : WHERE exp COLON stmtlist"""
        print("case : WHERE exp COLON stmtlist")

    def p_cases_case(self, p):
        """cases : case"""
        print("cases : case")

    def p_cases_cases(self, p):
        """cases : cases case"""
        print("cases : cases case")

    # TODO : commenting this reduces 1 conflict, but im not sure...
    # def p_cases_lambda(self, p):
    #     """cases : """
    #     print("cases : ")

    def p_stmt_return(self, p):
        """stmt : RETURN exp SEMICOLON"""
        print("stmt : RETURN exp SEMICOLON")

    def p_stmt_exp(self, p):
        """stmt : exp SEMICOLON"""
        print("stmt : exp SEMICOLON")

    def p_stmt_block(self, p):
        """stmt : block"""
        print("stmt : block")

    def p_stmt_vardec(self, p):
        """stmt : vardec"""
        print("stmt : vardec")

    def p_stmt_while(self, p):
        """stmt : WHILE LRB exp RRB stmt"""
        print("stmt : WHILE LRB exp RRB stmt")

    def p_stmt_on(self, p):
        """stmt : ON LRB exp RRB LCB cases RCB SEMICOLON"""
        print("stmt : ON LRB exp RRB LCB cases RCB SEMICOLON")

    def p_stmt_for_exp(self, p):
        """stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt"""
        print("stmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt")

    def p_stmt_for_id(self, p):
        """stmt : FOR LRB ID IN ID RRB stmt"""
        print("stmt : FOR LRB ID IN ID RRB stmt")

    def p_stmt_print(self, p):
        """stmt : PRINT LRB ID RRB SEMICOLON"""
        print("stmt : PRINT LRB ID RRB SEMICOLON")

    def p_stmt_elseIfList(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist"""
        print("stmt : IF LRB exp RRB stmt elseiflist")

    def p_stmt_else(self, p):
        """stmt : IF LRB exp RRB stmt elseiflist ELSE stmt"""
        print("stmt : IF LRB exp RRB stmt elseiflist ELSE stmt")

    # TODO : commenting this reduces 1 conflict but im not sure if it's correct
    # def p_elseIfList_elseIf(self, p):
    #     """elseiflist : ELSEIF LRB exp RRB stmt"""
    #     print("elseiflist : ELSEIF LRB exp RRB stmt")

    def p_elseIfList_elseIfList(self, p):
        """elseiflist : elseiflist ELSEIF LRB exp RRB stmt"""
        print("elseiflist : elseiflist ELSEIF LRB exp RRB stmt")

    def p_elseIfList_lambda(self, p):
        """elseiflist : """
        print("elseiflist : ")

    def p_exp_lvalue_assign(self, p):
        """exp : lvalue ASSIGN exp"""
        print("exp : lvalue ASSIGN exp")

    # TODO this was added by me
    # with this we can parse expressions like a = b[i]; or a = 3 + c[i];
    def p_exp_id_assign(self, p):
        """exp : ID ASSIGN exp"""
        print("exp : ID ASSIGN exp")

    def p_exp_lvalue(self, p):
        """exp : lvalue"""
        print("exp : lvalue")

    def p_exp_id_explist(self, p):
        """exp : ID LRB explist RRB"""
        print("exp : ID LRB explist RRB")

    def p_exp_parenthesis_exp(self, p):
        """exp : LRB exp RRB"""
        print("exp : LRB exp RRB")

    def p_exp_id(self, p):
        """exp : ID LRB RRB"""
        print("exp : ID LRB RRB")

    def p_exp_SUB_exp(self, p):
        """exp : SUB exp"""
        print("exp : SUB exp")

    def p_exp_not_exp(self, p):
        """exp : NOT exp"""
        print("exp : NOT exp")

    def p_exp_or(self, p):
        """exp : exp OR exp"""
        print("exp : OR")

    def p_exp_and(self, p):
        """exp : exp AND exp"""
        print("exp : AND")

    def p_exp_sum(self, p):
        "exp : exp SUM exp"
        print("exp : exp SUM exp")
        # self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        print("exp : exp SUB exp")
        # self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        print("exp : exp MUL exp")
        # self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        print("exp : exp DIV exp")
        # self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mod(self, p):
        """exp : exp MOD exp"""
        print("exp : exp MOD exp")

    def p_exp_gt_exp(self, p):
        """exp : exp GT exp"""
        print("exp : exp GT exp")

    def p_exp_lt_exp(self, p):
        """exp : exp LT exp"""
        print("exp : exp LT exp")

    def p_exp_ne_exp(self, p):
        """exp : exp NE exp"""
        print("exp : exp NE exp")

    def p_exp_eq_exp(self, p):
        """exp : exp EQ exp"""
        print("exp : exp EQ exp")

    def p_exp_ge_exp(self, p):
        """exp : exp GE exp"""
        print("exp : exp GE exp")

    def p_exp_le_exp(self, p):
        """exp : exp LE exp"""
        print("exp : exp LE exp")

    def p_exp_int(self, p):
        """exp : INTEGERNUMBER"""
        print("exp : INTEGERNUMBER")

    def p_exp_float(self, p):
        """exp : FLOATNUMBER"""
        print("exp : FLOATNUMBER")

    def p_exp_true(self, p):
        """exp : TRUE"""
        print("exp : TRUE")

    def p_exp_false(self, p):
        """exp : FALSE"""
        print("exp : FALSE")

    def p_explist_exp(self, p):
        """explist : exp"""
        print("explist : exp")

    def p_explist_explist(self, p):
        """explist : explist COMMA exp"""
        print("explist : explist COMMA exp")

    # def p_exp_integerNumber(self, p):
    #     "exp : INTEGERNUMBER"
    #     print("exp : INTEGERNUMBER")
    #     # p[0] = NonTerminal()
    #     # p[0].value = p[1]

    precedence = (
        ('right', 'ASSIGN'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'LT', 'GT', 'NE', 'EQ', 'LE', 'GE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('left', 'NOT'),
    )

    # TODO : ASSIGN precedence reduces 40 conflicts but im not sure if it parses correctly
    # TODO : if we add ('left', 'LRB', 'RRB') to precedences, else grammar can't be parsed, we may handle else in another way

    def new_temp(self):
        # temp = "T" + str(self.tempCount)
        # self.tempCount += 1
        # return temp
        pass

    def p_error(self, p):
        # print(p.value)
        print(p)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
