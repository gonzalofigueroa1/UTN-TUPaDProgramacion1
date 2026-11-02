from RemitoVentaDetalle import RemitoVentaDetalle

class RemitoVenta:
    def __init__(self, nombreCliente: str, numeroRemito: int):
        self.nombreCliente = nombreCliente
        self.numeroRemito = numeroRemito
        self.detallesRemito = []
        self.totalVenta = 0.0

    def agregar_detalle(self, detalle: RemitoVentaDetalle):
        self.detallesRemito.append(detalle)
        total = 0.0
        for d in self.detallesRemito:
            total += d.subtotal
        self.totalVenta = total