from Ciudad import Ciudad


class DiaViaje:
    def __init__(self, numeroDia: int):
        self.numeroDia = numeroDia
        self.ciudades = []

    def agregar_ciudad(self, ciudad: Ciudad):
        self.ciudades.append(ciudad)
