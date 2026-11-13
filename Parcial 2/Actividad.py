class Actividad:
    def __init__(self, tipoActividad: str, tipo: str, costoActividad: float):
        self.tipoActividad = tipoActividad
        self.tipo = tipo                      # "S" (standar) o "E" (exclusive)
        self.costoActividad = costoActividad
