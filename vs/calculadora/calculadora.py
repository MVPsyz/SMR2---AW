numeros = [10, 20, 30, 40, 50]

# Paso 1 y 2: Sumar y contar
suma_total = sum(nomeros) #Aquí está el cambio, de "numeros" a "nomeros".
cantidad_numeros = len(numeros) #Primer error, numeros no es una variable definida, debería ser "nomeros", por lo tanto "cantidad_numeros", noserá nada.

# Paso 3: Dividir
if cantidad_numeros > 0:  # Cada vez que aparezca "cantidad numeros" no se podr´a llevar a cabo la operación deseada.
    promedio = suma_total / cantidad_numeros
    print(f"La lista de números es: {numeros}") #Segundo error, numeros no es una variable definida, debería ser "nomeros".
    print(f"La suma total es: {suma_total}")
    print(f"La cantidad de números es: {cantidad_numeros}")
    print(f"El promedio es: {promedio}")
else:
    print("La lista está vacía, no se puede calcular el promedio.")