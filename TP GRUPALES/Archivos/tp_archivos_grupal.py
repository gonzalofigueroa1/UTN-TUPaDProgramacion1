# %%


def leer_alumnos():
    alumnos_dicc = {}
    archivo_crear = open("alumnos.txt", "a")
    archivo_crear.close() # para que no tire error si no existe
    with open("alumnos.txt", "r") as archivo:
        for linea in archivo:
            if not linea.strip():
                continue
            nombre, apellido, legajo, nota= linea.strip().split(";")
            alumnos_dicc[legajo]={"Nombre": nombre, "Apellido": apellido, "Nota": float(nota)}
    return alumnos_dicc



alumnos_dicc = leer_alumnos()  # carga los alumnos ya guardados en alumnos.txt
def agregar_alumno(alumnos_dicc):
    legajo= input("INGRESE EL LEGAJO DE 5 DIGITOS")
    while not legajo.isdigit() or len(legajo)!= 5:
        print("Error el legajo debe ser de 5 digitos")
        legajo= input("INGRESE EL LEGAJO DE 5 DIGITOS")

    if legajo in alumnos_dicc:
        print(f"El legajo {legajo} ya existe en el archivo alumnos.txt, no se permite su escritura")
        return
    nombre=input("INGRESE EL NOMBRE")
    while not nombre.isalpha():
        print("Error, ingrese el nombre sin numeros ni espacios")
        nombre= input("INGRESE EL NOMBRE")
    apellido= input("INGRESE EL APELLIDO")
    while not apellido.isalpha():
            print("Error, ingrese el apellido sin numeros ni espacios")
            apellido= input("INGRESE EL APELLIDO")

    nota= input("INGRESE UNA NOTA ENTRE 1-10")
    while not nota.replace(".", "", 1).isdigit() or float(nota) < 1 or float(nota) > 10:
        print("Error: Ingresó una nota inválida")
        nota = input("INGRESE UNA NOTA ENTRE 1-10: ")

        while not nota.replace(".", "", 1).isdigit():
            print("Error: Debe ingresar un valor numérico")
            nota = input("INGRESE UNA NOTA ENTRE 1-10: ")

    nota = float(nota)

    with open("alumnos.txt", "a") as archivo:
        archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
        alumnos_dicc[legajo]={"Nombre": nombre, "Apellido": apellido, "Nota": float(nota)}


def guardar_aprobados(alumnos_dicc):

    with open("aprobados.txt", "w") as archivo:
        hay_aprobados= False
        for legajo,datos in alumnos_dicc.items():
            if datos["Nota"]>=6:
                hay_aprobados= True
                nombre= datos["Nombre"]
                apellido= datos["Apellido"]
                nota= datos["Nota"]
                archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
                print(f"Legajo: {legajo} | Nombre: {nombre} {apellido} | Nota: {nota}")
                
        if hay_aprobados== False:
            print("No hay alumnos aprobados registrados.")



opcion = ""
while opcion != "4":
    print("1. Ver alumno")
    print("2. Agregar alumno")
    print("3. Generar y mostrar archivo de aprobados")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "2":
        agregar_alumno(alumnos_dicc)
    elif opcion == "3":
        guardar_aprobados(alumnos_dicc)
    elif opcion == "1":
            for legajo, datos in alumnos_dicc.items():
                print(f"Legajo: {legajo} | Nombre: {datos['Nombre']} {datos['Apellido']} | Nota: {datos['Nota']}")
    elif opcion == "4":
        print("Saliendo...")
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 4.")



# %%



