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
