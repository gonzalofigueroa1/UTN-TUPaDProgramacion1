from DiaViaje import DiaViaje


class PaqueteViaje:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.dias = []
        self.totalCostoViaje = 0.0      # calculado, no se pide por parámetro

    def agregar_dia(self, dia: DiaViaje):
        self.dias.append(dia)
        self.calcular_total()

    def calcular_total(self):
        total = 0.0
        for d in self.dias:
            for c in d.ciudades:
                total += c.totalActividades
        self.totalCostoViaje = total
