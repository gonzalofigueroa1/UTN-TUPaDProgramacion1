import os
from PaqueteViaje import PaqueteViaje
from DiaViaje import DiaViaje
from Ciudad import Ciudad
from Actividad import Actividad

LIMITE = 10000000
HOTELES = ["500", "600", "700"]     # mutuamente excluyentes (por ciudad)


class CotizarViaje:
    @staticmethod
    def main():
        # ---- 1. Cargar costoActividades[][] desde el archivo ----
        costoActividades = []
        ruta = os.path.join(os.path.dirname(__file__), "viajes2.txt")
        with open(ruta, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    continue
                # viajes2.txt separa con ";" y viajes.txt con tabulador
                separador = ";" if ";" in linea else "\t"
                datos = linea.split(separador)
                costoActividades.append([datos[0], datos[1], float(datos[2]), float(datos[3])])

        # ---- 2. Paquete y cantidad de días (7 a 30) ----
        paquete = PaqueteViaje(input("Ingrese el nombre del paquete: "))
        cantidadDias = 0
        while cantidadDias < 7 or cantidadDias > 30:
            cantidadDias = int(input("Ingrese la cantidad de días: "))
            if cantidadDias < 7 or cantidadDias > 30:
                print("Los días deben ser entre 7 y 30")

        # ---- 3. Carga de días, ciudades y actividades ----
        for numero in range(1, cantidadDias + 1):
            dia = DiaViaje(numero)
            paquete.agregar_dia(dia)
            print(f"----- Día {numero} -----")

            while True:                                   # ciudades del día
                ciudad = Ciudad(input("Nombre de la ciudad: "), input("País: "))
                dia.agregar_ciudad(ciudad)
                codigosCargados = []

                while True:                               # actividades de la ciudad
                    codigo = input("Código de la actividad: ")
                    fila = None
                    for f in costoActividades:
                        if f[0] == codigo:
                            fila = f

                    if fila is None:
                        print("el código es incorrecto, ingrese nuevamente")
                        continue
                    if codigo in codigosCargados:
                        print("la actividad ya fue agregada en esta ciudad")
                        continue
                    if codigo in HOTELES:
                        hayHotel = False
                        for h in HOTELES:
                            if h in codigosCargados:
                                hayHotel = True
                        if hayHotel:
                            print("ya hay un hotel en esta ciudad (500, 600 y 700 son excluyentes)")
                            continue

                    tipo = ""
                    while tipo != "S" and tipo != "E":
                        tipo = input("¿Estándar (S) o Exclusive (E)? ").upper()
                    costo = fila[2] if tipo == "S" else fila[3]

                    if paquete.totalCostoViaje + costo > LIMITE:
                        print("el costo total del viaje superaría los 10 millones, no se agrega")
                        continue

                    ciudad.agregar_actividad(Actividad(fila[1], tipo, costo))
                    paquete.calcular_total()
                    codigosCargados.append(codigo)

                    if len(ciudad.actividades) < 3:
                        print(f"Faltan {3 - len(ciudad.actividades)} actividad(es) como mínimo")
                    else:
                        if input("¿Agregar otra actividad? Si/No ").lower() == "no":
                            break

                if input("¿Agregar otra ciudad en este día? Si/No ").lower() == "no":
                    break

        # ---- 4. Mostrar el resultado ----
        print("-----------Paquete----------------")
        print("Nombre:", paquete.nombre)
        print("Total Días:", len(paquete.dias), "días")
        print("-----------Días-----------------")
        for d in paquete.dias:
            print("Día:", d.numeroDia)
            for c in d.ciudades:
                print("---------Ciudades------------------")
                print("Nombre Ciudad:", c.nombreCiudad)
                print("País:", c.nombrePais)
                print("--------Actividades----------------------")
                for a in c.actividades:
                    print(f"{a.tipoActividad:<20} tipo {a.tipo}   $ {a.costoActividad:.0f}")
                print(f"COSTO TOTAL ACTIVIDADES: $ {c.totalActividades:.0f}")
                print("---------------------------------------------")
        print(f"COSTO TOTAL VIAJE: $ {paquete.totalCostoViaje:.0f}")
        print(f"COSTO PROMEDIO POR DIA: $ {paquete.totalCostoViaje / len(paquete.dias):.2f}")


if __name__ == "__main__":
    CotizarViaje.main()
