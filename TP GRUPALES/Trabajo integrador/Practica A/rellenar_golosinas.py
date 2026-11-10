from golosinas_y_stock import golosinas
from clavesTecnico import tuplaClavesTecnico


def rellenar_golosinas():
    clave1 = input("Ingrese palabra clave 1: ")
    clave2 = input("Ingrese palabra clave 2: ")
    clave3 = input("Ingrese palabra clave 3: ")

    if clave1 == tuplaClavesTecnico[0] and clave2 == tuplaClavesTecnico[1] and clave3 == str(tuplaClavesTecnico[2]):
        try:
            codigo = int(input("Ingrese el código de la golosina a recargar: "))
        except ValueError:
            print("El código debe ser numérico.")
            return

        encontrada = False
        for g in golosinas:
            if g[0] == codigo:
                encontrada = True
                try:
                    cantidad = int(input("Ingrese la cantidad a recargar: "))
                except ValueError:
                    print("La cantidad debe ser numérica.")
                    return
                if cantidad > 0:
                    g[2] += cantidad
                    print(f"Stock de {g[1]} actualizado a {g[2]}.")
                else:
                    print("La cantidad debe ser mayor a cero.")

        if not encontrada:
            print("No existe una golosina con ese código.")
    else:
        print("No tiene permiso para ejecutar la función de recarga")
