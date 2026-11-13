from Actividad import Actividad


class Ciudad:
    def __init__(self, nombreCiudad: str, nombrePais: str):
        self.nombreCiudad = nombreCiudad
        self.nombrePais = nombrePais
        self.actividades = []
        self.totalActividades = 0.0

    def agregar_actividad(self, actividad: Actividad):
        self.actividades.append(actividad)
        total = 0.0
        for a in self.actividades:
            total += a.costoActividad
        self.totalActividades = total
