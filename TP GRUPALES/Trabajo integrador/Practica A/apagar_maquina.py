from golosinas_pedidas import golosinas_pedidas


def apagar_maquina():
    print("\n=== Golosinas pedidas durante la sesión ===")
    total = 0
    for r in golosinas_pedidas:
        print(r[0], "-", r[1], "-", r[2])
        total += r[2]
    print("Total de golosinas pedidas:", total)
    print("\nMáquina apagada. ¡Hasta luego!")
