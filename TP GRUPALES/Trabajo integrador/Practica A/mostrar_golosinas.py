from golosinas_y_stock import golosinas


def mostrar_golosinas():
    print("\nCód  Golosina               Stock")
    print("-" * 35)
    for g in golosinas:
        print(g[0], "-", g[1], "-", g[2])
