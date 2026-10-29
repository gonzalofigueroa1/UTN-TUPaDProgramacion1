class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def getSuperficieTotalTerreno(self):
        return sum(vivienda.superficieTerreno for vivienda in self.viviendas)

    def getSuperficieTotalTerrenoXManzana(self, manzana):
        return sum(
            vivienda.superficieTerreno
            for vivienda in self.viviendas
            if vivienda.manzana == manzana
        )

    def getSuperficieTotalCubierta(self):
        # Reutiliza el metodo de Vivienda del punto c)
        return sum(
            vivienda.getMetrosCuadradosCubiertos() for vivienda in self.viviendas
        )
