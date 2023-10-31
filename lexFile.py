import ply.lex as lex

tokens = (
		'STRING',
		'EQUALS',
    'DOLLAR',
    'SPACE',  # New token for spaces
    'PIPE',
    'HASHTAG',
    'INSERTION',
    'ID',
    'IF',
    'THEN',
    'ELIF',
    'ELSE',
    'FI',
    'TIME',
    'FOR',
    'IN',
    'UNTIL',
    'WHILE',
    'DO',
    'DONE',
    'CASE',
    'ESAC',
    'COPROC',
    'SELECT',
    'FUNCTION',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'CLEFT_BRACKET',
    'CRIGHT_BRACKET',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'EXCLAMATION_MARK',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'elif': 'ELIF',
    'else': 'ELSE',
    'fi': 'FI',
    'time': 'TIME',
    'for': 'FOR',
    'in': 'IN',
    'until': 'UNTIL',
    'while': 'WHILE',
    'do': 'DO',
    'done': 'DONE',
    'case': 'CASE',
    'esac': 'ESAC',
    'coproc': 'COPROC',
    'select': 'SELECT',
    'function': 'FUNCTION',
    '{': 'LEFT_BRACE',
    '}': 'RIGHT_BRACE',
    '[[': 'CLEFT_BRACKET',
    ']]': 'CRIGHT_BRACKET',
    '[': 'LEFT_BRACKET',
    ']': 'RIGHT_BRACKET',
    '!': 'EXCLAMATION_MARK',
}

t_EQUALS = r'='
t_HASHTAG = r'\#'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IF = r'if'
t_THEN = r'then'
t_ELIF = r'elif'
t_ELSE = r'else'
t_FI = r'fi'
t_TIME = r'time'
t_FOR = r'for'
t_IN = r'in'
t_UNTIL = r'until'
t_WHILE = r'while'
t_DO = r'do'
t_DONE = r'done'
t_CASE = r'case'
t_ESAC = r'esac'
t_COPROC = r'coproc'
t_SELECT = r'select'
t_FUNCTION = r'function'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_CLEFT_BRACKET = r'\[\['
t_CRIGHT_BRACKET = r'\]\]'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_EXCLAMATION_MARK = r'!'
t_PIPE = r'\|'
t_DOLLAR = r'\$'
t_INSERTION = r'\>\>'

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove the double quotes
    return t


# Define the SPACE token to match spaces and tabs
def t_SPACE(t):
    r'[ \t]+'
    return t

# Define the ID token, including '.' and '_' as part of identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_\.]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define the NUMBER token to match integers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Skip over spaces and tabs
t_ignore = ' \t'

# Handle newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for unrecognized characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

