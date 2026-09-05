#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

#programa principal

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#programa principal

nombre_saludar = input("Ingrese su nombre: ")
saludar_usuario(nombre_saludar)

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#Pedir los datos al usuario y llamar a esta función con los valores ingresados

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.1416 * (radio **2)
    return area
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    return perimetro

radio_usuario = float(input("Ingrese el radio del círculo: "))
if radio_usuario <= 0:
    print("El radio debe ser mayor a 0")
else:
    print(f"El area de su círculo es: {calcular_area_circulo(radio_usuario)}")
    print(f"El perímetro de su círculo es: {calcular_perimetro_circulo(radio_usuario)}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    return horas

segundos = float(input("Ingrese la cantidad de segundos para transformar a horas: "))
print(f"Sus {segundos} segundos son igual a {segundos_a_horas(segundos)} horas")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(0,11):
        print(f"{i} x {numero} = {i * numero}")

tabla_multiplicar(numero = int(input("Ingrese un número para su tabla de multiplicar: ")))

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b
    mi_tupla = (suma, resta, multiplicar, dividir)
    return(mi_tupla)

a = 10
b = 20
resultado = operaciones_basicas(a, b)
print(f"Tupla: {resultado}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su indice de masa corporal es: {calcular_imc(peso, altura)}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fa = (celsius * 1.8) + 32
    return fa

celsius = float(input("Ingrese la temperatura en celsius: "))
print(f"Sus {celsius}°C se transforman en {celsius_a_fahrenheit(celsius)}°F")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

primer_numero = float(input("Ingrese el primer numero: "))
segundo_numero = float(input("Ingrese el segundo numero: "))
tercer_numero = float(input("Ingrese el tercer numero: "))
print(f"El promedio de sus números son {calcular_promedio(primer_numero, segundo_numero, tercer_numero)}")