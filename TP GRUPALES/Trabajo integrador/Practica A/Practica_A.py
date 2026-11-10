from pedir_golosina import pedir_golosina
from mostrar_golosinas import mostrar_golosinas
from rellenar_golosinas import rellenar_golosinas
from apagar_maquina import apagar_maquina


opcion = ""
while opcion != "d":
    print("\n=== Máquina de Golosinas ===")
    print("a. Pedir golosina")
    print("b. Mostrar golosinas")
    print("c. Rellenar golosinas")
    print("d. Apagar máquina")
    opcion = input("Seleccione una opción: ")

    if opcion == "a":
        pedir_golosina()
    elif opcion == "b":
        mostrar_golosinas()
    elif opcion == "c":
        rellenar_golosinas()
    elif opcion == "d":
        apagar_maquina()
    else:
        print("Opción inválida.")
