#1
for i in range(0,101):
    print(i)

#2
numero_entero = input("Ingrese un número entero: ")
cantidad_digitos = len(numero_entero)
print(f"El número tiene {cantidad_digitos} dígitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores
primer_numero = int(input("Introduzca el primer número: "))
segundo_numero = int(input("Introduzca el segundo número: "))
suma = 0

for i in range(primer_numero +1, segundo_numero):
    suma += i
    print(f"La suma es {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
contador = 1
total = 0

while contador != 0:
    numero_suma = int(input("Ingrese un número a sumar: "))
    total += numero_suma
    contador = numero_suma
    print("Ingrese 0 si quiere terminar el programa")
print(f"Su total es de {total}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_random = random.randint(0,9)
intentos = 0
print("Intentá adivinar el numero aleatorio entre 0 y 9")
intento_acertar = False

while intento_acertar == False:
    intento_usuario = int(input("Ingrese un numero entre 0 y 9: "))
    intentos += 1
    if intento_usuario == numero_random:
        intento_acertar = True
print(f"Encontraste el numero aleatorio en {intentos} intentos")
#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,-2,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero_positivo = int(input("Ingrese un número entero positivo: "))
suma_positivo = 0
for i in range(0,numero_positivo + 1):
    suma_positivo += i
print(f"La suma de todos los números es: {suma_positivo}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros.
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cantidad_pares = 0
cantidad_impares = 0
cantidad_negativos = 0
cantidad_positivos = 0

for i in range(100):
    numero_clasificar = int(input("Ingrese un número entero a clasificar: "))
    if numero_clasificar % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1
    if numero_clasificar > 0:
        cantidad_positivos += 1
    elif numero_clasificar == 0:
        print("Cero es un número neutro, no es positivo ni negativo")
    else:
        cantidad_negativos += 1

print(f"Ingresó {cantidad_pares} números pares")
print(f"Ingresó {cantidad_impares} números impares")
print(f"Ingresó {cantidad_positivos} números positivos")
print(f"Ingresó {cantidad_negativos} números negativos")
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debepoder procesar 100 números cambiando solo un valor).
media = 0
for i in range(100):
    numero_media = int(input("Ingrese un número entero a la media: "))
    media += numero_media
total_media = media / 100
print(f"La media es: {total_media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero_a_invertir = input("Ingrese un número entero: ")
numero_invertido = ""
for i in numero_a_invertir:
    numero_invertido = i + numero_invertido
print(f"El número {numero_a_invertir} se convierte en {numero_invertido} al invertirlo")