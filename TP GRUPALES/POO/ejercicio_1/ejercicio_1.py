class Celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila = fila
        self.columna = columna
        self.valor = valor


class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def buscar(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda
        return None

    def obtenerValor(self, fila, columna):
        celda = self.buscar(fila, columna)
        if celda is None:
            return "La fila y columna indicada no ha sido asignada en ninguna celda"
        return celda.valor


def pedirEntero(mensaje, nombre):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(f"Error, ingrese correctamente el N° de la {nombre}")


matriz = Matriz()

while True:
    valor = input("Valor (FIN para terminar): ")
    if valor == "FIN":
        break
    fila = pedirEntero("Fila: ", "fila")
    columna = pedirEntero("Columna: ", "columna")
    if matriz.buscar(fila, columna):
        print("Esa celda ya fue cargada")
    else:
        matriz.celdasMatriz.append(Celda(fila, columna, valor))

for celda in matriz.celdasMatriz:
    print(f"[{celda.fila}, {celda.columna}] = {celda.valor}")

fila = pedirEntero("Fila a consultar: ", "fila")
columna = pedirEntero("Columna a consultar: ", "columna")
print(matriz.obtenerValor(fila, columna))
