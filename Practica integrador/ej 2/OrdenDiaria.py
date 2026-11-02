from OrdenServicio import OrdenServicio

class OrdenDiaria:
    def __init__(self, fecha: str):
        self.fecha = fecha
        self.ordenesServicio = []
        self.totalDia = 0.0

    def agregar_orden(self, orden: OrdenServicio):
        self.ordenesServicio.append(orden)
        total = 0.0
        for o in self.ordenesServicio:
            total += o.totalOrden
        self.totalDia = total