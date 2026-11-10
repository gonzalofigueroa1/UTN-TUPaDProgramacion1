from habitacion import Habitacion
from vivienda import Vivienda
from barrio import Barrio


class PruebaBarrio:
    def main(self):
        barrio = self.armarBarrio()

        print(f"Barrio: {barrio.nombre} ({barrio.empresaConstructora})")
        print(f"Superficie total del terreno: {barrio.getSuperficieTotalTerreno()} m2")
        print(f"Superficie de la manzana A: {barrio.getSuperficieTotalTerrenoXManzana('A')} m2")
        print(f"Superficie de la manzana B: {barrio.getSuperficieTotalTerrenoXManzana('B')} m2")
        print(f"Superficie de la manzana Z: {barrio.getSuperficieTotalTerrenoXManzana('Z')} m2")

        print("\nCubiertos por vivienda:")
        for vivienda in barrio.viviendas:
            print(
                f"  {vivienda.calle} {vivienda.numero} (Mz {vivienda.manzana}, "
                f"Casa {vivienda.nroCasa}): {vivienda.getMetrosCuadradosCubiertos()} m2"
            )
        print(f"Superficie total cubierta del barrio: {barrio.getSuperficieTotalCubierta()} m2")

        self.probarExcepcion()

    def armarBarrio(self):
        barrio = Barrio("Las Lomas", "Constructora del Sur")

        vivienda1 = Vivienda("Av. Siempreviva", 742, "A", 1, 300)
        vivienda1.habitaciones.append(Habitacion("Cocina", 20))
        vivienda1.habitaciones.append(Habitacion("Comedor", 35))
        vivienda1.habitaciones.append(Habitacion("Dormitorio", 25))

        vivienda2 = Vivienda("Av. Siempreviva", 750, "A", 2, 250)
        vivienda2.habitaciones.append(Habitacion("Cocina comedor", 40))
        vivienda2.habitaciones.append(Habitacion("Dormitorio", 20))

        vivienda3 = Vivienda("Los Alamos", 120, "B", 1, 400)
        vivienda3.habitaciones.append(Habitacion("Living", 50))
        vivienda3.habitaciones.append(Habitacion("Cocina", 30))

        barrio.viviendas.append(vivienda1)
        barrio.viviendas.append(vivienda2)
        barrio.viviendas.append(vivienda3)
        return barrio

    def probarExcepcion(self):
        # Vivienda con mas metros construidos que terreno: debe fallar
        vivienda = Vivienda("Los Pinos", 50, "C", 1, 60)
        vivienda.habitaciones.append(Habitacion("Salon", 80))
        print("\nProbando una vivienda invalida:")
        try:
            vivienda.getMetrosCuadradosCubiertos()
        except ValueError as error:
            print(f"  Error: {error}")


PruebaBarrio().main()
