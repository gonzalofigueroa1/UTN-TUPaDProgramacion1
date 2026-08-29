# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range
lista_multiplos = list(range(4,101,4))
print(lista_multiplos)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
lista_favoritos = ["Milanesa", "Gatos", "Juegos", "Anillos", "Mate cocido"]
print(lista_favoritos[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = [] 
lista_vacia = []
lista_vacia.append("123")
lista_vacia.append("test")
lista_vacia.append("hola")
print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# El programa, primero crea una lista de números y busca el número más alto
# modifica la lista quitando el número más alto y despues imprime la lista en pantalla.