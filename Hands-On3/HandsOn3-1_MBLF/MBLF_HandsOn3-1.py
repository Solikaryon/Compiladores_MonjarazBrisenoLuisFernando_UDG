import ply.lex as lex
import ply.yacc as yacc

# HANDS-ON 3.1: Validador de Expresiones Aritméticas (Básico)
# Monjaraz Briseño Luis Fernando
# Compiladores

tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'
)

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLUS(t): r'\+'; return t

def t_MINUS(t): r'-'; return t

def t_TIMES(t): r'\*'; return t

def t_DIVIDE(t): r'/'; return t

def t_LPAREN(t): r'\('; return t

def t_RPAREN(t): r'\)'; return t

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression_plus(p): 'expression : expression PLUS term'; p[0] = p[1] + p[3]
def p_expression_minus(p): 'expression : expression MINUS term'; p[0] = p[1] - p[3]
def p_term_times(p): 'term : term TIMES factor'; p[0] = p[1] * p[3]
def p_term_divide(p): 'term : term DIVIDE factor'; p[0] = p[1] / p[3] if p[3] != 0 else print("Error: División por cero")
def p_expression_term(p): 'expression : term'; p[0] = p[1]
def p_term_factor(p): 'term : factor'; p[0] = p[1]
def p_factor_num(p): 'factor : NUMBER'; p[0] = p[1]
def p_factor_expr(p): 'factor : LPAREN expression RPAREN'; p[0] = p[2]
def p_error(p): print("Error de sintaxis") 

parser = yacc.yacc()

# Prueba del analizador sintáctico
if __name__ == "__main__":
    while True:
        try:
            s = input('Ingrese una expresión aritmética: ')
        except EOFError:
            print("Salida: Expresión vacía")
            break
        if not s:
            continue
        if parser.parse(s) is None:
            print("Salida: Expresión inválida")
        else:
            print("Salida: Expresión válida")
            print("Resultado:", parser.parse(s))
