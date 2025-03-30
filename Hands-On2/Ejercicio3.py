import ply.lex as lex

# Definición de tokens
tokens = (
    'INT',       # Palabra clave 'int'
    'RETURN',    # Palabra clave 'return'
    'ID',        # Identificadores
    'NUMBER',    # Números enteros
    'STRING',    # Cadenas de texto
    'OPERATOR',  # Operadores (+, -, *, /)
    'DELIMITER', # Delimitadores (;, {}, ())
    'EQUALS',    # Operador de asignación '='
)

# Expresiones regulares para tokens simples
t_INT = r'int'
t_RETURN = r'return'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER = r'\d+'
t_STRING = r'"[^"]*"'
t_OPERATOR = r'[\+\-*/]'  # Corregido: guion escapado correctamente
t_DELIMITER = r'[;\{\}\(\)]'  # Corregido: caracteres escapados correctamente
t_EQUALS = r'='

# Ignorar espacios, tabulaciones y saltos de línea
t_ignore = ' \t\n'

# Expresión regular para comentarios de una línea
def t_COMMENT(t):
    r'//.*'
    pass  # Ignorar comentarios

# Expresión regular para comentarios de múltiples líneas
def t_MULTILINE_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    pass  # Ignorar comentarios

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Contadores
counters = {
    'INT': 0,
    'RETURN': 0,
    'ID': 0,
    'NUMBER': 0,
    'STRING': 0,
    'OPERATOR': 0,
    'DELIMITER': 0,
    'EQUALS': 0,
}

# Prueba del analizador léxico
data = """
int main() {
    int x = 42;
    return x + 1;
}
"""

# Alimentar el analizador con la entrada
lexer.input(data)

# Contar tokens
for token in lexer:
    if token.type in counters:
        counters[token.type] += 1

# Imprimir resultados
print("Conteo de tokens:")
for token_type, count in counters.items():
    print(f"{token_type}: {count}")