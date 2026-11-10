class Computadora:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.componentesCPU = []

    def costo(self):
        return sum(componente.subTotal() for componente in self.componentesCPU)

    def recargo(self):
        # 40% si el costo es menor a 50000, 30% en caso contrario
        costo = self.costo()
        if costo < 50000:
            return costo * 0.40
        return costo * 0.30

    def precioVenta(self):
        return self.costo() + self.recargo()
