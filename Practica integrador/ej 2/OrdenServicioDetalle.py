from Servicio import Servicio
class OrdenServicioDetalle:
    def __init__(self, horas: int, servicio: Servicio):
        self.horas = horas
        self.servicio = servicio
        self.subtotal = float(horas * servicio.precioHora)