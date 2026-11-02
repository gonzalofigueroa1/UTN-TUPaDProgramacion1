from OrdenServicioDetalle import OrdenServicioDetalle

class OrdenServicio:
    def __init__(self, nombreCliente: str, numeroOrden: int):
        self.nombreCliente = nombreCliente
        self.numeroOrden = numeroOrden
        self.detalleOrden = []
        self.totalOrden = 0.0

    def agregar_servicio(self, servicio: OrdenServicioDetalle):
        self.detalleOrden.append(servicio)
        total = 0.0
        for s in self.detalleOrden:
            total += s.subtotal
        self.totalOrden = total