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