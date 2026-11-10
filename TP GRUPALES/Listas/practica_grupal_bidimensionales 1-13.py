# LISTAS BIDIMENSIONALES
# =============================================================

def crear_matriz(filas, columnas):
    matriz = []
    contador = 1

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)

    return matriz


# Ejercicio 1: Crear una matriz de numeros
# =============================================================
def ejercicio_1():
    matriz = crear_matriz(3, 4)
    for fila in matriz:
        print(fila)


# Ejercicio 2: Suma de todos los elementos
# =============================================================
def ejercicio_2():
    lista_bidimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    total = 0

    for fila in lista_bidimensional:
        for numero in fila:
            total += numero

    print(f"El total de la lista es de {total}")


# Ejercicio 3: Suma de cada fila
# =============================================================
def ejercicio_3():
    lista_bidimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for fila in lista_bidimensional:
        suma_fila = 0
        for numero in fila:
            suma_fila += numero
        print(f"El valor de la fila {fila} es {suma_fila}")


# Ejercicio 4: Matriz transpuesta
# =============================================================
def ejercicio_4():
    lista_bidimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpuesta = []

    for columna in range(len(lista_bidimensional[0])):
        nueva_fila = []
        for fila in range(len(lista_bidimensional)):
            nueva_fila.append(lista_bidimensional[fila][columna])
        transpuesta.append(nueva_fila)

    print("Matriz original:")
    for fila in lista_bidimensional:
        print(fila)

    print("\nMatriz transpuesta:")
    for fila in transpuesta:
        print(fila)


# Ejercicio 5: Encontrar el elemento mayor
# =============================================================
def ejercicio_5():
    lista_bidimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lista_mayor = [numero for fila in lista_bidimensional for numero in fila]
    print(f"El valor más grande de la lista es {max(lista_mayor)}")


# Ejercicio 6: Multiplicar una matriz por un escalar
# =============================================================
def ejercicio_6():
    lista_bidimensional = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    escalar = int(input("Ingrese un valor para escalar la lista: "))
    lista_multiplicada = []

    for fila in lista_bidimensional:
        nueva_fila = []
        for numero in fila:
            nueva_fila.append(numero * escalar)
        lista_multiplicada.append(nueva_fila)

    print("Lista original:")
    for fila in lista_bidimensional:
        print(fila)

    print("\nLista escalada:")
    for fila in lista_multiplicada:
        print(fila)


# Ejercicio 7: Diagonal de una matriz cuadrada
# =============================================================
def ejercicio_7():
    matriz_principal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonal = []

    for i in range(len(matriz_principal)):
        diagonal.append(matriz_principal[i][i])

    print(f"Diagonal principal: {diagonal}")


# Ejercicio 8: Matriz identidad
# =============================================================
def ejercicio_8():
    n = 3
    matriz_identidad = []

    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matriz_identidad.append(fila)

    print("Matriz identidad:")
    for fila in matriz_identidad:
        print(fila)


# Ejercicio 9: Matriz identidad inversa
# =============================================================
def ejercicio_9():
    n = 3
    matriz_identidad_inversa = []

    for horizontal in range(n):
        fila = []
        for columna in range(n):
            if columna + horizontal == n - 1:
                fila.append(1)
            else:
                fila.append(0)
        matriz_identidad_inversa.append(fila)

    print("Matriz identidad inversa:")
    for fila in matriz_identidad_inversa:
        print(fila)


# Ejercicio 10: Verificar matriz simétrica
# =============================================================
def ejercicio_10():
    matriz_simetrica = [[1, 2, 3], [2, 5, 6], [3, 6, 9]]
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


# Ejercicio 11: Rotar una matriz 90 grados
# =============================================================
def ejercicio_11():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = len(matriz)
    nueva = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            nueva[j][n - 1 - i] = matriz[i][j]

    print("Matriz rotada 90 grados:")
    for fila in nueva:
        print(fila)


# Ejercicio 12: Analizador y filtrado de calificaciones
# =============================================================
def ejercicio_12():
    notas = "45, 88, -5, 92, 30, 110, 75, 60, 15"
    aprobados = []
    reprobados = []
    notas_validas = []
    lista_notas = notas.split(", ")

    for nota in lista_notas:
        nota_num = int(nota)
        if nota_num < 0 or nota_num > 100:
            continue

        notas_validas.append(nota_num)
        if nota_num >= 60:
            aprobados.append(nota_num)
        else:
            reprobados.append(nota_num)

    promedio = sum(notas_validas) / len(notas_validas)
    ultimos_aprobados = aprobados[-2:]

    print("Últimos 2 aprobados registrados:", ultimos_aprobados)
    print("El promedio es", promedio)
    print("Aprobados:", aprobados)
    print("Reprobados:", reprobados)


# Ejercicio 13: Gestor interactivo de proyectos
# =============================================================
def ejercicio_13():
    tareas = []
    opcion = 0

    while opcion != 4:
        try:
            opcion = int(input("""---GESTOR INTERACTIVO---
1. Agregar tarea
2. Eliminar tarea
3. Ver resumen
4. Salir
"""))
        except ValueError:
            print("Opción no válida.")
            continue

        if opcion == 1:
            tarea = input("Ingrese el nombre de su tarea: ")
            if tarea in tareas:
                print("Esta tarea ya está registrada.")
            else:
                tareas.append(tarea)

        elif opcion == 2:
            nombre_tarea = input("Ingrese la tarea a eliminar: ")
            if nombre_tarea in tareas:
                tareas.remove(nombre_tarea)
            else:
                print("Esa tarea no está registrada.")

        elif opcion == 3:
            primeras_3_tareas = ", ".join(tareas[:3])
            print(f"""El total de tareas que se han registrado son: {len(tareas)}
Las primeras 3 tareas son: {primeras_3_tareas}""")

        elif opcion == 4:
            break

        else:
            print("Opción no válida.")


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
