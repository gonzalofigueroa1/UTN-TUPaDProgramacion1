class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.lista_componentes = []

    def calcular_costo_total(self):
        costo_total = 0.0
        for comp in self.lista_componentes:
            costo_total += comp.cantidad * comp.precio
        return costo_total