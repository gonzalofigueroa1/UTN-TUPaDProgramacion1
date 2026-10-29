class Vivienda:
    def __init__(self, calle: str, numero: int, manzana: str, nroCasa: int,
                 superficieTerreno: float):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def getMetrosCuadradosCubiertos(self):
        total = sum(habitacion.metrosCuadrados for habitacion in self.habitaciones)
        # Lo construido nunca puede superar al terreno
        if total > self.superficieTerreno:
            raise ValueError(
                "La superficie cubierta no puede ser mayor a la superficie del terreno"
            )
        return total
