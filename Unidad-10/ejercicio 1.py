class celda:
    def __init__(self, fila: int, columna: int, valor: str):
        self.fila= fila
        self.columna= columna
        self.valor= valor
class matriz:
    def __init__(self):
        self.celdasMatriz=[]
    def buscar_valor(self, fila_buscada: int, columna_buscada: int):
        for c in self.celdasMatriz:
            if c.fila == fila_buscada and c.columna == columna_buscada:
                return c.valor
        
        return "La fila y columna indicada no ha sido asignada en ninguna celda"
mi_matriz= matriz()
while True:
    valor= input("INGRESE EL VALOR O FIN PARA TERMINAR")
    if valor.upper()=="FIN":
        break
    fila= int(input("INGRESE LA FILA"))
    columna= int(input("INGRESE LA COLUMNA"))

    existe= False
    for c in mi_matriz.celdasMatriz:
        if c.fila==fila and c.columna==columna:
            existe= True 
            break
    if existe == True:
        print("La celda ya existe")

    else:
        nueva_celda = celda(fila, columna, valor)
        mi_matriz.celdasMatriz.append(nueva_celda)


for c in mi_matriz.celdasMatriz:
    print(f"Fila: {c.fila}, Columna: {c.columna}, Valor: {c.valor}")