# --- Implementación de Bucles para Resolver Problemas Repetitivos ---

# Documentación oficial sobre bucles:
# for: https://docs.python.org/3/tutorial/controlflow.html#for-statements
# while: https://docs.python.org/3/tutorial/controlflow.html#while-statements
# break, continue, else con bucles: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

print("--- Bucles (Loops) para Resolver Problemas Repetitivos ---")

# 1. Bucle 'for' con 'range()'
#    Ideal para iterar un número conocido de veces. 'range(inicio, fin, paso)' genera una secuencia de números.
print("\n1. Bucle 'for' con 'range()':")
for i in range(5):  # Itera 5 veces (0, 1, 2, 3, 4)
    print(f"Iteración número: {i + 1}")

print("\nBucle 'for' con 'range(inicio, fin)':")
for numero in range(1, 6): # Itera del 1 al 5 (el 6 es exclusivo)
    print(f"Contando: {numero}")

# 2. Bucle 'for' para iterar sobre una colección (lista, tupla, cadena, conjunto, diccionario)
#    Permite procesar cada elemento de una colección directamente.
print("\n2. Bucle 'for' sobre una lista:")
frutas = ["manzana", "platano", "cereza", 9, "precio"]
asignaturassegundo = ["Matemáticas", "Física", "Química"]
precio = [7,8,,]
for fruta in frutas:
    print(f"Me gusta comer {fruta}.")

print("\nBucle 'for' sobre una cadena (string):")
palabra = "Python"
for letra in palabra:
    print(f"Letra: {letra}")

print("\nBucle 'for' sobre un diccionario (iterando claves):")
persona = {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Barcelona'}
for clave in persona:
    print(f"Clave: {clave}") # Por defecto, itera sobre las claves

print("\nBucle 'for' sobre un diccionario (iterando valores):")
for valor in persona.values():
    print(f"Valor: {valor}")

print("\nBucle 'for' sobre un diccionario (iterando pares clave-valor):")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# 3. Bucle 'while'
#    Ejecuta un bloque de código mientras una condición sea True. Requiere una variable de control.
print("\n3. Bucle 'while':")
contador = 0
while contador < 3:
    print(f"Bucle while - Contador: {contador}")
    contador += 1 # Es crucial actualizar la variable de control para evitar un bucle infinito

# 4. Uso de 'break' en bucles
#    Termina el bucle inmediatamente, saliendo de él.
print("\n4. Uso de 'break':")
for num in range(1, 10):
    if num == 5:
        print("Se encontró el 5, rompiendo el bucle.")
        break
    print(f"Número actual: {num}")

# 5. Uso de 'continue' en bucles
#    Salta la iteración actual y pasa a la siguiente iteración del bucle.
print("\n5. Uso de 'continue':")
for i in range(1, 6):
    if i % 2 == 0: # Si 'i' es par
        print(f"Saltando número par: {i}")
        continue
    print(f"Número impar procesado: {i}")

# 6. Bucle 'for' con 'else'
#    El bloque 'else' se ejecuta si el bucle 'for' completa todas sus iteraciones sin ser interrumpido por un 'break'.
print("\n6. Bucle 'for' con 'else':")
elementos_busqueda = [10, 20, 30, 40]
valor_a_encontrar = 50 # Este valor no está en la lista

for elemento in elementos_busqueda:
    if elemento == valor_a_encontrar:
        print(f"¡{valor_a_encontrar} encontrado en la lista!")
        break
else: # Se ejecuta si el 'break' nunca fue activado (es decir, el elemento no se encontró)
    print(f"{valor_a_encontrar} no se encontró en la lista después de revisar todos los elementos.")

# 7. Bucle 'while' con 'else'
#    Similar al 'for', el 'else' se ejecuta si la condición del 'while' se vuelve False (el bucle termina normalmente)
#    y no hubo un 'break' dentro del bucle.
print("\n7. Bucle 'while' con 'else':")
intentos = 0
contrasena_correcta = "secreto"
contrasena_ingresada = "123" # No coincide

while intentos < 3:
    if contrasena_ingresada == contrasena_correcta:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
        intentos += 1
        contrasena_ingresada = "otra" # Simula otro intento
else:
    print("Has agotado tus intentos. Acceso denegado.")


# --- Uso de Operadores Lógicos y Relacionales para Controlar el Flujo del Programa ---

# Documentación oficial de operadores relacionales (comparación):
# https://docs.python.org/3/reference/expressions.html#comparisons
# Documentación oficial de operadores lógicos:
# https://docs.python.org/3/reference/expressions.html#boolean-operations

print("\n--- Operadores Lógicos y Relacionales en Control de Flujo ---")

# Variables para demostración
saldo = 1200
limite_credito = 1000
es_cliente_vip = True
edad_cliente = 22
monto_compra = 300

# 1. Operadores Relacionales (Comparación): ==, !=, <, >, <=, >=
#    Se usan para comparar dos valores y devuelven True o False.
print("\n1. Operadores Relacionales:")
if saldo >= monto_compra: # Mayor o igual que
    print(f"Saldo actual: {saldo}. Compra de {monto_compra} permitida.")
else:
    print(f"Saldo insuficiente para una compra de {monto_compra}.")

if edad_cliente != 18: # Diferente de
    print("El cliente no tiene exactamente 18 años.")

# 2. Operador Lógico 'and'
#    Devuelve True si AMBAS condiciones son True.
print("\n2. Operador Lógico 'and':")
if saldo > monto_compra and es_cliente_vip:
    print("Compra procesada con prioridad: saldo suficiente y cliente VIP.")
else:
    print("La compra requiere más saldo o el cliente no es VIP para prioridad.")

# 3. Operador Lógico 'or'
#    Devuelve True si AL MENOS UNA de las condiciones es True.
print("\n3. Operador Lógico 'or':")
if saldo > limite_credito or es_cliente_vip:
    print("Se puede ofrecer un descuento: buen saldo o cliente VIP.")
else:
    print("No califica para un descuento especial en este momento.")

# 4. Operador Lógico 'not'
#    Invierte el valor booleano de una condición (True se vuelve False, y False se vuelve True).
print("\n4. Operador Lógico 'not':")
producto_en_stock = False
if not producto_en_stock:
    print("El producto no está disponible. Enviando notificación de falta de stock.")

# 5. Combinación de operadores lógicos y relacionales en bucles y condicionales
#    Permite crear condiciones muy específicas para controlar el flujo.
print("\n5. Combinación en bucles/condicionales:")
intentos_restantes = 3
usuario_bloqueado = False

while intentos_restantes > 0 and not usuario_bloqueado: # Bucle continúa si quedan intentos Y el usuario no está bloqueado
    print(f"Quedan {intentos_restantes} intentos.")
    clave_ingresada = input("Introduce la clave (pista: 'master'): ")

    if clave_ingresada == "master" and intentos_restantes > 0: # Condición compuesta con 'and'
        print("Acceso concedido.")
        break
    elif clave_ingresada != "master" and intentos_restantes > 1: # Condición compuesta con 'and' y operador relacional
        print("Clave incorrecta. Inténtalo de nuevo.")
        intentos_restantes -= 1
    else: # Último intento incorrecto
        print("Clave incorrecta. Has agotado tus intentos.")
        usuario_bloqueado = True
        intentos_restantes -= 1
else:
    if usuario_bloqueado:
        print("Cuenta bloqueada por demasiados intentos fallidos.")
    else:
        print("Programa terminado (por alguna otra razón si no hubo break).")

# 6. Condición con 'in' / 'not in' (ya visto, pero relevante para flujo)
#    Se usa para verificar la pertenencia de un elemento en una secuencia o colección.
print("\n6. Condición con 'in' y 'not in':")
colores_validos = ["red", "green", "blue"]
color_elegido = "yellow"

if color_elegido in colores_validos:
    print(f"El color '{color_elegido}' es válido.")
else:
    print(f"El color '{color_elegido}' no es válido. Elige entre {', '.join(colores_validos)}.")

# --- Fin del código de bucles y operadores ---
