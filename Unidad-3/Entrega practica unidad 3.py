# 1 edad mayor
edad = int(input("Ingrese una edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("No eres mayor de edad")
# 2 nota examen
nota = float(input("Ingrese la nota de su examen: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
# 3 numero par
numero = int(input("Ingrese su número: "))
numero_par = numero % 2
if numero_par == 0:
    print("este número es par")
else:
    print("este número es impar")
# 4 clasificaciones de edad
edad = int(input("Ingrese su edad en años: "))
if edad <12 and edad > 0:
    print("Eres un Niño/a")
elif edad >=12 and edad <18:
    print("Eres un Adolescente")
elif edad >=18 and edad <30:
    print("Eres un Adulto/a joven")
elif edad >=30:
    print("Eres un Adulto/a")
else:
    print("Error: Edad inválida")
# 5 contraseña numeros
contraseña = input("Ingrese su contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
# 6 media, mediana y moda
from statistics import mode, median, mean 
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mean  = mean(numeros_aleatorios)
median = median(numeros_aleatorios)
mode = mode(numeros_aleatorios)
print(f"La media es {mean}, la mediana es {median} y la moda es {mode}")
if mean > median > mode:
    print("Es Sesgo positivo")
elif mean < median < mode:
    print("Es Sesgo negativo")
else:
    print("No hay Sesgo")
# 7 frase vocal
frase = input("Introduzca su frase o palabra: ")
if frase.lower()[-1] in "aeiou":
    print(f"{frase}!")
else:
    print(f"{frase}")
# 8 nombre variado
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese si quiere su nombre en Mayúsculas, Minusculas, Primera letra en mayúscula (1/2/3): "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Introduzca un número válido")
# 9 magnitud terremoto
magnitud = float(input("Introduzca la magnitud del terremoto a clasificar según la escala de Richter: "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
# 10 estaciones del año
hemisferio = input("¿En qué hemisferio se encuentra? (N/S) ").lower()
mes = input("Introduzca el nombre del mes: ").lower()
dia = int(input("¿Qué día del mes es? "))
if dia < 1 or dia > 31:
    print("Día inválido")
elif hemisferio not in ["n", "s"]:
    print("Hemisferio inválido")
elif hemisferio == "n":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        print("Se encuentra en Invierno")
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        print("Se encuentra en Primavera")
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        print("Se encuentra en Otoño")
    else:
        print("Mes inválido")
elif hemisferio == "s":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        print("Se encuentra en Verano")
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        print("Se encuentra en Otoño")
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        print("Se encuentra en Invierno")
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        print("Se encuentra en Primavera")
    else:
        print("Mes inválido")
