#1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

#Añadir las siguientes frutas con sus respectivos precios:

precios_frutas["Naranja"] =1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print(precios_frutas.keys())

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
lista_contactos = {}
for contactos in range(5):
    contacto = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número del contacto: ")
    lista_contactos[contacto] = numero
pedido = input("Ingrese el nombre de su contacto: ")
if pedido in lista_contactos:
    print(f"El número de su contacto {pedido} es: {lista_contactos[pedido]}")
else:
    print(f"No se encontró el contacto {pedido}")

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase = input("Ingrese su frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print(f"Las Palabras únicas son: {palabras_unicas}")
diccionario = {}
for palabra in palabras:
    diccionario[palabra] = diccionario.get(palabra, 0)+1
print(diccionario)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
alumnos = {}
for x in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    notas = (nota1, nota2, nota3)
    alumnos[nombre] = notas
    print(alumnos)

for nombre, notas in alumnos.items():
    promedio = sum(notas)/3
    print(f"El alumno {nombre} tuvo un promedio de {promedio}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
estudiantes_parcial_1 = {15, 20, 10, 6, 2, 7}
estudiantes_parcial_2 = {10, 12, 23, 6, 7, 5}
print(estudiantes_parcial_1 & estudiantes_parcial_2)
print(estudiantes_parcial_1 - estudiantes_parcial_2)
print(estudiantes_parcial_1 | estudiantes_parcial_2)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.
stock = {"Teclados": 2, "Mouses": 4, "Monitores": 6, "Cargadores": 5}
def mostrar_menu():
    print("SISTEMA DE GESTIÓN DE STOCK")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock")
    print("3. Agregar nuevo producto")
    print("4. Cerrar programa")

def consultar_stock():
    producto = input("Ingrese el nombre del producto: ").title()
    if producto in stock:
        print(f"La cantidad de stock de el producto {producto} es {stock[producto]}")
    else:
        print("Error: Producto no encontrado")

def restock():
    producto = input("Ingrese el nombre del producto a suministrar: ").title()
    if producto in stock:
        cantidad = int(input("Ingrese la cantidad de ese producto: "))
        stock[producto] += cantidad
    else:
        print("Error: El producto ingresado no se encuentra agregado")

def agregar_producto():
    producto = input("Ingrese el nombre del producto a agregar: ").title()
    if producto not in stock:
        cantidad = int(input("Ingrese la cantidad de ese producto: "))
        stock[producto] = cantidad
    else:
        print("Error: El producto ingresado ya esta en stock")

acceso = True
while acceso is True:
    mostrar_menu()
    opcion = input("Seleccione su opcion: ")
    if opcion == "1":
        consultar_stock()
    elif opcion == "2":
        restock()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        print("Cerrando...")
        acceso = False
    else:
        print("Error: No ingresó uno de los valores pedidos")

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
agenda = {("Martes", "8:00"): "Clase de programación presencial", ("Martes", "12:30"): "Terminan clases", ("Lunes", "15:00"): "Gimnasio", ("Miercoles", "17:00"): "Turno médico"}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora en formato de 24 horas: ")
clave = (dia,hora)
if clave in agenda:
    print(f"El día {dia} a las {hora} tenes {agenda[clave]}")
else:
    print(f"No hay nada en la agenda para el día {dia} a las {hora}")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
inverso = {}
for pais, capital in original.items():
    inverso[capital] = pais
print(inverso)