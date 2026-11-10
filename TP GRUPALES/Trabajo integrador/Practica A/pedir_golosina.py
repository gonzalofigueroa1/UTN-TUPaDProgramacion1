from empleados import empleados
from golosinas_y_stock import golosinas
from golosinas_pedidas import golosinas_pedidas


def pedir_golosina():
    try:
        legajo = int(input("Ingrese su legajo: "))
    except ValueError:
        print("El legajo debe ser numérico.")
        return

    if legajo not in empleados:
        print("Usted no es un empleado de la empresa")
        return

    seguir = True
    while seguir:
        codigo = input("Ingrese el código de la golosina o 'salir': ")

        if codigo == "salir":
            return

        try:
            codigo = int(codigo)
        except ValueError:
            print("El código debe ser numérico (o 'salir').")
            continue

        encontrada = False
        for g in golosinas:
            if g[0] == codigo:
                encontrada = True
            if g[0] == codigo:
                if g[2] == 0:
                    print(f"Lo sentimos la golosina {g[1]} no se encuentra disponible, seleccione otra golosina o ingresa salir si no desea otra golosina")
                else:
                    g[2] -= 1

                    # registrar en golosinas_pedidas (1 fila por golosina)
                    yaRegistrada = False
                    for r in golosinas_pedidas:
                        if r[0] == codigo:
                            r[2] += 1
                            yaRegistrada = True
                    if not yaRegistrada:
                        golosinas_pedidas.append([g[0], g[1], 1])

                    print(f"Golosina {g[1]} entregada. ¡Que la disfrutes!")
                    seguir = False

        if not encontrada:
            print("No existe una golosina con ese código.")
