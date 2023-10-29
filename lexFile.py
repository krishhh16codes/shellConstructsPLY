import ply.lex as lex
tokens = (
	'VARIABLE',
  'NUMBER',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
)


reserved =
{
	'if'	
	'then'	
  'elif'	
  'else'	
  'fi'	
  'time' 
  'for'
  'in'	
  'until'	
  'while'	
  'do'	
  'done' 
  'case'	
  'esac'	
  'coproc'	
  'select'	
  'function' 
  '{'	
  '}'	
  '['
  '['
  ']'
  ']'
  '!'

}


t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'



def t_WORD(t):
	r"\b\w+\b"
	return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)


def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t


t_ignore  = ' \t'



lexer = lex.lex()






