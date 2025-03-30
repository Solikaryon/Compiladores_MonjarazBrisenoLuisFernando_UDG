import ply.lex as lex
import ply.yacc as yacc

# Monjaraz Briseño Luis Fernando
# Compiladores
# HANDS-ON 3.2: Validador de Expresiones Lógicas 

# Definición de tokens
tokens = ('BOOLEAN', 'AND', 'OR', 'NOT', 'LPAREN', 'RPAREN')

def t_BOOLEAN(t):
    r'[01]'
    t.value = int(t.value)
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

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Gramática según la definición BNF
def p_expr_and(p):
    'expr : expr AND term'
    p[0] = p[1] and p[3]

def p_expr_or(p):
    'expr : expr OR term'
    p[0] = p[1] or p[3]

def p_expr_term(p):
    'expr : term'
    p[0] = p[1]

def p_term_not(p):
    'term : NOT factor'
    p[0] = not p[2]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expr RPAREN'
    p[0] = p[2]

def p_factor_boolean(p):
    'factor : BOOLEAN'
    p[0] = bool(p[1])

def p_error(p):
    print("Error de sintaxis")
    
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        try:
            s = input("Ingrese una expresión lógica: ")
        except EOFError:
            continue
        if not s:
            continue
        result = parser.parse(s)
        # Si result es None, hubo error; si no, la expresión fue válida.
        if result is None:
            print("Salida: Expresión inválida")
        else:
            print("Salida: Expresión válida")
