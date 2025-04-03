import ply.lex as lex
import ply.yacc as yacc

# Monjaraz Briseño Luis Fernando
# Compiladores
# HANDS-ON 3.3: Validador de Expresiones Complejas 

# Tokens: Se usan NUMBER para valores numéricos y los operadores aritméticos y lógicos.
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'AND', 'OR', 'NOT'
)

# Regla para NUMBER
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_TIMES(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_AND(t):
    r'AND'
    return t

def t_OR(t):
    r'OR'
    return t

def t_NOT(t):
    r'NOT'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# Precedencia: se asigna prioridad para operadores lógicos y aritméticos.
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Gramática
# <expr> ::= <expr> OR <expr> | <expr> AND <expr> | <arith>
def p_expr_or(p):
    'expr : expr OR expr'
    p[0] = ('OR', p[1], p[3])

def p_expr_and(p):
    'expr : expr AND expr'
    p[0] = ('AND', p[1], p[3])

def p_expr_not(p):
    'expr : NOT expr'
    p[0] = ('NOT', p[2])

def p_expr_arith(p):
    'expr : arith'
    p[0] = p[1]

# <arith> ::= <arith> + <term> | <arith> - <term> | <term>
def p_arith_plus(p):
    'arith : arith PLUS term'
    p[0] = ('+', p[1], p[3])
    
def p_arith_minus(p):
    'arith : arith MINUS term'
    p[0] = ('-', p[1], p[3])
    
def p_arith_term(p):
    'arith : term'
    p[0] = p[1]

# <term> ::= <term> * <factor> | <term> / <factor> | <factor>
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = ('*', p[1], p[3])
    
def p_term_divide(p):
    'term : term DIVIDE factor'
    if p[3] == 0:
        print("Error: División por cero")
        p[0] = None
    else:
        p[0] = ('/', p[1], p[3])
    
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

# <factor> ::= ( <expr> ) | NUMBER
def p_factor_expr(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]
    
def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()

# Prueba del analizador sintáctico
if __name__ == '__main__':
    while True:
        try:
            s = input('Ingrese una expresión compleja: ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        if result is None:
            print("Salida: Expresión inválida")
        else:
            print("Salida: Expresión válida")
