from Inscripcion import Inscripcion
class Socio:
    def __init__(self, nombre: str, numeroSocio: int):
        self.nombre = nombre
        self.numeroSocio = numeroSocio
        self.inscripciones = []
        self.totalSocio = 0.0

    def agregar_inscripcion(self, subtotal: Inscripcion):
        self.inscripciones.append(subtotal)
        total = 0.0
        for i in self.inscripciones:
            total += i 
        if len(self.inscripciones) >= 2:
            total = total * 0.90
        self.totalSocio = total