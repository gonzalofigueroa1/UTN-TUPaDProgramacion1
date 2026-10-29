from habitacion import Habitacion
from vivienda import Vivienda
from barrio import Barrio


class PruebaBarrio:
    def main(self):
        barrio = self.armarBarrio()

        print(f"=== BARRIO: {barrio.nombre} ({barrio.empresaConstructora}) ===")
        print(f"Superficie total del terreno: {barrio.getSuperficieTotalTerreno()} m2")
        
        # 1. Ejemplo usando input para consultar una manzana ingresada por el usuario
        manzana_buscada = input("Ingrese la letra de la manzana a consultar (ej. A, B, Z): ").strip().upper()
        superficie_manzana = barrio.getSuperficieTotalTerrenoXManzana(manzana_buscada)
        print(f"Superficie de la manzana {manzana_buscada}: {superficie_manzana} m2")

        print("Cubiertos por vivienda:")
        for vivienda in barrio.viviendas:
            print(
                f"  {vivienda.calle} {vivienda.numero} (Mz {vivienda.manzana}, "
                f"Casa {vivienda.nroCasa}): {vivienda.getMetrosCuadradosCubiertos()} m2"
            )
        print(f"Superficie total cubierta del barrio: {barrio.getSuperficieTotalCubierta()} m2")

        # 2. Ejemplo opcional para agregar una vivienda de forma interactiva con input
        self.agregarViviendaInteractiva(barrio)

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

    def agregarViviendaInteractiva(self, barrio):
        print("--- Registro de una nueva vivienda ---")
        calle = input("Ingrese la calle: ")
        numero = int(input("Ingrese el número: "))
        manzana = input("Ingrese la manzana: ").strip().upper()
        nro_casa = int(input("Ingrese el número de casa: "))
        superficie_terreno = float(input("Ingrese la superficie del terreno (m2): "))

        nueva_vivienda = Vivienda(calle, numero, manzana, nro_casa, superficie_terreno)

        # Agregar habitaciones
        while True:
            agregar_hab = input("¿Desea agregar una habitación? (s/n): ").strip().lower()
            if agregar_hab != 's':
                break
            nombre_hab = input("  Nombre de la habitación: ")
            metros_hab = float(input("  Metros cuadrados de la habitación: "))
            nueva_vivienda.habitaciones.append(Habitacion(nombre_hab, metros_hab))

        barrio.viviendas.append(nueva_vivienda)
        print(f"¡Vivienda agregada con éxito! Nueva superficie total del terreno del barrio: {barrio.getSuperficieTotalTerreno()} m2")

    def probarExcepcion(self):
        # Vivienda con mas metros construidos que terreno: debe fallar
        vivienda = Vivienda("Los Pinos", 50, "C", 1, 60)
        vivienda.habitaciones.append(Habitacion("Salon", 80))
        print("Probando una vivienda invalida:")
        try:
            vivienda.getMetrosCuadradosCubiertos()
        except ValueError as error:
            print(f"  Error: {error}")


PruebaBarrio().main()