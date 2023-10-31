import sys
import ply.yacc as yacc
import lexFile

tokens = lexFile.tokens
lexer = lexFile.lexer

start = 'program'


def p_program(p):
    '''program : statements'''
    p[0] = p[1]


def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_assignment(p):
    '''assignment : ID EQUALS expression
                  | ID EQUALS DOLLAR LPAREN arithmetic_expression RPAREN'''
    if len(p) == 4:
        p[0] = ('assignment', p[1], p[3])
    else:
        p[0] = ('assignment', p[1], p[5])


def p_expression(p):
    '''
    expression : NUMBER
               | STRING
               | MINUS expression
               | ID
               | LPAREN expression RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_statement(p):
    '''statement : while_statement
                 | if_statement
                 | for_statement
                 | command
                 | assignment
                 | comment
	               | arithmetic_expression
                 | insertion
                 | pipe_command'''
    p[0] = p[1]

def p_command(p):
    '''command : ID
               | command ID
               | command NUMBER
               | command STRING
               | command MINUS ID
               | command MINUS MINUS ID
    '''
    if len(p) == 2:
        p[0] = ('command', p[1])
    elif p[2] == '-' and len(p) == 4:
        if len(p[3]) == 1:
            p[0] = ('command', p[1], p[2] + p[3])
        else:
            raise SyntaxError("Single character expected after a single '-'")
    elif p[2] == '-' and len(p) == 3:
        if len(p[3]) == 1:
            p[0] = ('command', p[1], p[2] + p[3])
        else:
            raise SyntaxError("Single character expected after a single '-'")
    else:
        p[0] = ('command', p[1], p[2])


def p_comment(p):
    '''comment : HASHTAG ID'''
    p[0] = ('comment', p[2])

def p_insertion(p):
    '''insertion : command ID INSERTION ID
		             | command STRING INSERTION ID'''
    p[0] = ('insertion', p[2], p[3])

def p_pipe_command(p):
    '''pipe_command : command PIPE command'''
    p[0] = ('pipe', p[1], p[3])

def p_while_statement(p):
    '''while_statement : WHILE condition DO statements DONE'''
    p[0] = ('while', p[2], p[4])

def p_condition(p):
    '''condition : LEFT_BRACKET expression RIGHT_BRACKET'''
    p[0] = ('condition', p[2])


def p_arithmetic_expression(p):
	'''arithmetic_expression : NUMBER
                           | DOLLAR ID
	                         | LPAREN arithmetic_expression RPAREN
	                         | arithmetic_expression PLUS arithmetic_expression
		                       | arithmetic_expression MINUS arithmetic_expression
		                       | arithmetic_expression TIMES arithmetic_expression
                           | arithmetic_expression DIVIDE arithmetic_expression
	'''
	if len(p) == 2:
		p[0] = ('arithmetic_expression', p[1])
	elif len(p) == 4:
		p[0] = ('arithmetic_expression', p[2], p[1], p[3])


def p_for_statement(p):
    '''for_statement : FOR ID IN command DO statements DONE'''
    p[0] = ('for', p[2], p[4], p[6])


def p_if_statement(p):
    '''if_statement : IF condition THEN statements ELSE statements FI'''
    p[0] = ('if', p[2], p[4], p[6])


def p_error(p):
	if p:
		print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token {p.type} - {p.value}")
	else:
		print("Syntax error: Unexpected end of input")
	sys.exit(1)

parser = yacc.yacc()

if __name__ == '__main__':
    input_text = '''asustctl --char 6'''
    try:
        result = parser.parse(input_text, lexer=lexer)
        print("Success")
    except SyntaxError as e:
        print(e)
