print("Monjaraz Briseño Luis Fernando")
print("----------------------------------------------")
print("Autómata 1: Validación de cadenas alfabéticas.")

def validate_alpha(s):
    return s.isalpha()

# Original
input_str = "HelloWorld"
if validate_alpha(input_str):
    print("Cadena válida.")
else:
    print("Cadena inválida.")

# Varias cadenas alfabéticas 5 válidas y 5 inválidas.
input_str = ["HelloWorld", "Hello", "World", "HelloWorld123", "Hello123", "123HelloWorld", "Hello World", "Hello123World", "Hello123World!", "Hello123World@"]
for s in input_str:
    if validate_alpha(s):
        print(s, "- Cadena válida.")
    else:
        print(s, "- Cadena inválida.")

print("----------------------------------------------")
print("Autómata 2: Validación de números reales.")
def validate_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# Original
input_str = "-123.456"
if validate_real(input_str):
    print("Número válido.")
else:
    print("Número inválido.")

# Varias cadenas numéricas 6 válidas y 4 inválidas.
input_str = ["-123.456", "123.456", "123", "-123", "123.", ".123", "123.456.789", "123.456.789", "123,456", "123,456,789"]
for s in input_str:
    if validate_real(s):
        print(s, "- Número válido.")
    else:
        print(s, "- Número inválido.")

print("----------------------------------------------")
print("Autómata 3: Validación de sentencias selectivas (if-else).")

def validate_if_else(s):
    return "if" in s and "else" in s

# Original
input_str = "if x > 0: pass else: pass"
if validate_if_else(input_str):
    print("Sentencia válida.")
else:
    print("Sentencia inválida.")

# Varias sentencias selectivas 5 válidas y 5 inválidas.
input_str = [
    "if x > 0: pass else: pass",  
    "if (x > 0) { } else { }",    
    "if x > 0: print(x) else: print('No')",  
    "if x > 0: pass elif x == 0: pass else: pass",  
    "if x > 0: pass else: pass",  
    "if x > 0: pass",             
    "else: pass",                 
    "if x > 0: pass elif x == 0: pass",  
    "if x > 0: pass else if x == 0: pass",  
    "print('Hello')"              
]

for s in input_str:
    if validate_if_else(s):
        print(s, "- Sentencia válida.")
    else:
        print(s, "- Sentencia inválida.")

print("----------------------------------------------")
