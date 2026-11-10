# Ejercicio 1: Suma de elementos
# =============================================================
def ejercicio_1():
    lista = pedir_lista()
    print("Lista ingresada:", lista)
    print("La suma de los elementos es:", sum(lista))


# Ejercicio 2: Encontrar el mayor y el menor
# =============================================================
def ejercicio_2():
    lista = pedir_lista()
    print(f"Valor maximo: {max(lista)}")
    print(f"Valor minimo: {min(lista)}")


# Ejercicio 3: Invertir una lista
# =============================================================
def ejercicio_3():
    lista = pedir_lista()
    lista.reverse()
    print("Lista invertida:", lista)


# Ejercicio 4: Contar pares e impares
# =============================================================
def ejercicio_4():
    lista = pedir_lista()
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Hay un total de {pares} números pares")
    print(f"Hay un total de {impares} números impares")


# Ejercicio 5: Multiplicar cada elemento por un valor
# =============================================================
def ejercicio_5():
    lista = pedir_lista()
    valor = int(input("Ingrese un valor por el cual quiere multiplicar cada elemento: "))
    for i in range(len(lista)):
        lista[i] = lista[i] * valor
    print("Lista multiplicada:", lista)


# Ejercicio 6: Eliminar duplicados
# =============================================================
def ejercicio_6():
    lista = pedir_lista()
    sin_duplicados = []

    for numero in lista:
        if numero not in sin_duplicados:
            sin_duplicados.append(numero)

    print("Lista sin duplicados:", sin_duplicados)


# Ejercicio 7: Promedio de una lista
# =============================================================
def ejercicio_7():
    lista = pedir_lista()
    if not lista:
        print("No se ingresaron elementos, no hay promedio.")
        return
    promedio = sum(lista) / len(lista)
    print("El promedio es:", promedio)


# Ejercicio 8: Encontrar elementos repetidos
# =============================================================
def ejercicio_8():
    lista_numeros = [1, 2, 3, 4, 2, 7, 3, 8, 1, 9, 4, 4]
    repetidos = []

    for elemento in lista_numeros:
        if elemento not in repetidos and lista_numeros.count(elemento) > 1:
            repetidos.append(elemento)

    print("Elementos repetidos:", repetidos)

    for elemento in repetidos:
        print(f"{elemento} aparece {lista_numeros.count(elemento)} veces")


# Ejercicio 9: Lista de números primos
# =============================================================
def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True


def ejercicio_9():
    datos = input("Ingrese una lista de numeros separados por comas: ")
    lista = [int(x.strip()) for x in datos.split(",")]
    primos = [numero for numero in lista if es_primo(numero)]

    print(f"Lista original: {lista}")
    print(f"Numeros primos: {primos}")


# Ejercicio 10: Eliminar un elemento por su indice
# =============================================================
def ejercicio_10():
    datos = input("Ingrese una lista de numeros separados por comas: ")
    lista = [int(x.strip()) for x in datos.split(",")]

    indice = int(input(f"Ingrese el indice a eliminar (0 a {len(lista) - 1}): "))

    if 0 <= indice < len(lista):
        lista.pop(indice)
        print(f"Lista despues de eliminar el indice {indice}: {lista}")
    else:
        print("Indice fuera de rango.")


# Ejercicio 11: Contar ocurrencias de un elemento
# =============================================================
def ejercicio_11():
    datos = input("Ingrese una lista de numeros separados por comas: ")
    lista = [int(x.strip()) for x in datos.split(",")]

    numero = int(input("Ingrese el numero a buscar: "))
    ocurrencias = lista.count(numero)

    print(f"El numero {numero} aparece {ocurrencias} veces en la lista.")


# Ejercicio 12: Sumar listas elemento por elemento
# =============================================================
def ejercicio_12():
    datos1 = input("Ingrese la primera lista de numeros separados por comas: ")
    lista1 = [int(x.strip()) for x in datos1.split(",")]

    datos2 = input("Ingrese la segunda lista de numeros separados por comas: ")
    lista2 = [int(x.strip()) for x in datos2.split(",")]

    if len(lista1) != len(lista2):
        print("Error: las listas deben tener la misma longitud.")
        return

    suma = [a + b for a, b in zip(lista1, lista2)]
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Suma elemento por elemento: {suma}")


# Ejercicio 13: NumPy para trabajar con matrices y arrays
# =============================================================
def ejercicio_13():
    try:
        import numpy as np
    except ImportError:
        print("Para ejecutar este ejercicio se necesita instalar NumPy: pip install numpy")
        return

    array = np.array([1, 2, 3, 4, 5])
    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print("Array 1D:", array)
    print("Matriz 2D:\n", matriz)
    print("Array + 10:", array + 10)
    print("Array * 2:", array * 2)
    print("Suma de la matriz:", matriz.sum())
    print("Maximo de la matriz:", matriz.max())
    print("Minimo de la matriz:", matriz.min())
    print("Promedio de la matriz:", matriz.mean())
    print("Matriz transpuesta:\n", matriz.T)
    identidad = np.eye(3)
    print("Producto matriz x identidad:\n", matriz.dot(identidad))
    print("Forma de la matriz:", matriz.shape)


# =============================================================
def pedir_lista():
    cantidad = int(input("Ingrese la cantidad de elementos que quiere añadir: "))
    lista = []

    for i in range(cantidad):
        numero = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(numero)

    return lista


# =============================================================
# Menu principal para probar cada ejercicio
# =============================================================
if __name__ == "__main__":
    print("Ejercicios disponibles: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13")
    opcion = input("Que ejercicio queres ejecutar?: ").strip()

    print(f"\n--- Ejecutando Ejercicio {opcion} ---")

    if opcion == "1":
        ejercicio_1()
    elif opcion == "2":
        ejercicio_2()
    elif opcion == "3":
        ejercicio_3()
    elif opcion == "4":
        ejercicio_4()
    elif opcion == "5":
        ejercicio_5()
    elif opcion == "6":
        ejercicio_6()
    elif opcion == "7":
        ejercicio_7()
    elif opcion == "8":
        ejercicio_8()
    elif opcion == "9":
        ejercicio_9()
    elif opcion == "10":
        ejercicio_10()
    elif opcion == "11":
        ejercicio_11()
    elif opcion == "12":
        ejercicio_12()
    elif opcion == "13":
        ejercicio_13()
    else:
        print("Opcion no valida.")