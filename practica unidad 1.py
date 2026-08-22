#1
print("Hola Mundo!")

#2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su país de residencia: ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {lugar}!")

#4
radio_circulo = int(input("Ingrese el radio del circulo: "))
area_circulo = 3.14 * radio_circulo * radio_circulo
perimetro = 2 * 3.14 * radio_circulo
print(f"El área del círculo es {area_circulo}")
print(f"El perímetro del círculo es {perimetro}")

#5
segundos = int(input("Ingrese la cantidad de segundos a medir: "))
minutos = segundos / 60
horas = minutos / 60
print(f"Los {segundos} segundos equivalen a {horas} horas")

#6
numero = int(input("Ingrese su número a multiplicar: "))
for x in range(1,11):
    multiplicacion = numero * x
    print(f"{numero} x {x} = {multiplicacion}")

#7
primer_numero = int(input("Ingrese el primer número entero: "))
segundo_numero = int(input("Ingrese el segundo número entero: "))
if primer_numero <= 0 or 0 >= segundo_numero:
    print("Error: Ingresó un número menor o igual a 0")
else:
    print("Suma:", primer_numero + segundo_numero)
    print("Resta:", primer_numero - segundo_numero)
    print("Multiplicación:", primer_numero * segundo_numero)
    print("División:", primer_numero / segundo_numero)

#8
peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura **2)
print(f"Su índice de masa corporal es {imc}")

#9
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (temperatura * 9/5) + 32
print(f"{temperatura} grados Celsius son {fahrenheit} grados Fahrenheit.")

#10
primer_entero = float(input("Ingrese el primer número entero: "))
segundo_entero = float(input("Ingrese el segundo número entero: "))
tercer_entero = float(input("Ingrese el tercer número entero: "))
promedio = (primer_numero + segundo_numero + tercer_entero) / 3
print(f"El promedio de {primer_numero}, {segundo_numero} y {tercer_entero} es {promedio}")