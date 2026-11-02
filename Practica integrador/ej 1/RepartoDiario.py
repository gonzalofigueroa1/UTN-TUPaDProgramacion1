from RemitoVenta import RemitoVenta

class RepartoDiario:
    def __init__(self, fecha: str):
        self.fecha = fecha
        self.remitosVenta = []
        self.totalReparto = 0.0

    def agregar_venta(self, venta: RemitoVenta):
        self.remitosVenta.append(venta)
        suma = 0.0
        for v in self.remitosVenta:
            suma += v.totalVenta
        self.totalReparto = suma