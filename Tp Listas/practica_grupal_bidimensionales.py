#Ejercicio 1: Suma de Elementos 
# Escribe un programa que permita al usuario ingresar una lista de números y calcule la suma de todos los elementos en la lista.
lista_numeros = input("Ingrese números para agregar a su lista, separados por comas: ").split(",")
lista_numeros = [int(x) for x in lista_numeros]
suma = sum(lista_numeros)
print(f"Su lista dio como suma total: {suma}")

#Ejercicio 2: Suma de Todos los Elementos
#  Escribe un programa que calcule la suma de todos los elementos en una lista bidimensional. 
lista_bidimensional = [[1,2,3],[4,5,6],[7,8,9]]
suma_bidimensional = 0
for fila in lista_bidimensional:
    for numero in fila:
        suma_bidimensional += numero
print(f"El total de la lista es de {suma_bidimensional}")

#Ejercicio 3: Suma de Cada Fila 
# Modifica el programa anterior para que imprima la suma de cada fila de la lista bidimensional.
for fila in lista_bidimensional:
    suma_bidimensional = 0
    for numero in fila:
        suma_bidimensional += numero
    print(f"El valor de la fila {fila} es {suma_bidimensional}")

#Ejercicio 4: Matriz Transpuesta 
# Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una matriz intercambia sus filas por columnas. 
print("Matriz original")
for fila in lista_bidimensional:
    print(fila)

print("Matriz transpuesta")
matriz = []
for columna in range(len(lista_bidimensional[0])):
    nueva_fila = []
    for fila in range(len(lista_bidimensional)):
        nueva_fila.append(lista_bidimensional[fila][columna])
    matriz.append(nueva_fila)
    print(nueva_fila)

# Ejercicio 5: Encontrar el Elemento Mayor
#  Escribe un programa que encuentre el valor más grande en una lista bidimensional.
lista_mayor = [numero for fila in lista_bidimensional for numero in fila]
mayor = max(lista_mayor)
print(f"El valor más grande de la lista es {mayor}")

#Ejercicio 6: Multiplicar una Matriz por un Escalar 
# Escribe un programa que multiplique cada elemento de una lista bidimensional por un valor escalar dado por el usuario.
escalado = int(input("Ingrese un valor para escalar la lista: "))
print("Lista original")
for fila in lista_bidimensional:
    print(fila)

print()
print("lista escalada")
lista_multiplicada = []
for fila in lista_bidimensional:
    nueva_fila = []
    for numero in fila:
        nueva_fila.append(numero * escalado)
    lista_multiplicada.append(nueva_fila)
    print(nueva_fila)
#Ejercicio 7: Diagonal de una Matriz Cuadrada 
# Escribe un programa que extraiga los elementos de la diagonal principal de una matriz cuadrada.
matriz_principal = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
diagonal = []
for i in range(len(matriz_principal)):
    diagonal.append(matriz_principal[i][i])

print(f"Diagonal principal: {diagonal}")

#Ejercicio 8: Matriz Identidad 
# Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto son 0.
n = 3
matriz_identidad = []
print("matriz identidad")
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad.append(fila)
    print(fila)

#Ejercicio 9: Matriz Identidad Inversa 
# Crea un programa que genere una matriz identidad inversa de tamaño n. 
# Una matriz identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa principal son 1 y el resto son 0.
n = 3
matriz_identidad_inversa = []
print("matriz identidad")
for horizontal in range(n):
    fila = []
    for columna in range(n):
        if columna + horizontal == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad_inversa.append(fila)
    print(fila)

#Ejercicio 10: Verificar Matriz Simétrica 
# Una matriz es simétrica si es igual a su transpuesta.
#  Escribe un programa que verifique si una matriz es simétrica.
matriz_simetrica = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]
matriz_transpuesta = []
for horizontal in range(len(matriz_simetrica[0])):
    fila = []
    for columna in range(len(matriz_simetrica)):
        fila.append(matriz_simetrica[columna][horizontal])
    matriz_transpuesta.append(fila)

if matriz_simetrica == matriz_transpuesta:
    print("Es una matriz simétrica")
else:
    print("No es una matriz simétrica")

#Ejercicio 11: Rotar una Matriz 90 Grados 
#Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido de las agujas del reloj.
matriz_normal = [
    [1,2,3]
    [4,5,6]
    [7,8,9]
]
matriz_rotada = []