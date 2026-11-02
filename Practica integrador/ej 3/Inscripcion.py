from Actividad import Actividad
class Inscripcion:
    def __init__(self, meses: int, actividad: Actividad):
        self.meses = meses
        self.actividad = actividad
        self.subtotal = float(meses * actividad.cuotaMensual)