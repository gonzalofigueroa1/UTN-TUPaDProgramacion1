from Servicio import Servicio
from OrdenServicioDetalle import OrdenServicioDetalle
from OrdenServicio import OrdenServicio
from OrdenDiaria import OrdenDiaria

class CrearOrdenDiaria:
    @staticmethod
    def main():
        serviciosDisponibles = [
            Servicio("101", "Cambio de aceite", 6000),
            Servicio("102", "Alineacion y balanceo", 9000),
            Servicio("103", "Revision de frenos", 12000),
            Servicio("104", "Diagnóstico electrónico", 15000),
            Servicio("105", "Cambio de embrague", 30000)
        ]
        clientesTaller = {
            "30123456": "Marcelo Ibáñez",
            "28456789": "Carolina Funes",
            "33789456": "Luciana Ortega",
            "27951357": "Diego Herrera",
            "20314159": "Taller Los Andes"
        }
        ordenDiaria = OrdenDiaria(input("Ingrese la fecha: "))

        while True:
            documento = input("Ingrese el documento del cliente: ")
            if documento in clientesTaller:
                nombreCliente = clientesTaller[documento]
            else:
                print("Número de documento nuevo")
                nombreCliente = input("Ingrese el nombre del cliente nuevo: ")
                clientesTaller[documento] = nombreCliente
            repetido = True
            while repetido:
                numeroOrden = int(input("Ingrese el número de la orden: "))
                repetido = False
                for o in ordenDiaria.ordenesServicio:
                    if o.numeroOrden == o.ordenesServicio:
                        repetido = True
                if repetido == True:
                    print("el número de orden ya fue cargado, ingrese otro")
            orden = OrdenServicio(nombreCliente, numeroOrden)
            while True:
                servicio = None
                while servicio is None:
                    codigo = input("Ingrese el codigo de la orden: ")
                    for c in serviciosDisponibles:
                        if c.codigo == codigo:
                            servicio = c
                    if servicio is None:
                            print("el código es incorrecto, ingrese nuevamente")
                horas = 0
                while horas <= 0:
                    horas = int(input("Ingrese las horas trabajadas: "))
                    if horas <= 0:
                        print("Las horas deben ser mayores a 0, intente otra vez")
                detalle = OrdenServicioDetalle(horas, servicio)
                orden.agregar_servicio(detalle)
                pregunta = input("¿Quiere seguir añadiendo detalles? Si/No ")
                if pregunta.lower() == "no":
                    break
            ordenDiaria.agregar_orden(orden)
            pregunta = input("¿Quiere seguir añadiendo ordenes? Si/No ")
            if pregunta.lower() == "no":
                break
        print("Orden Diaria")
        print("Fecha:", ordenDiaria.fecha)
        print("--------------Ordenes del Taller----------------")
        for o in ordenDiaria.ordenesServicio:
            print("Cliente:", o.nombreCliente)
            print("Número orden:", o.numeroOrden)
            print("| Horas | Servicio | Precio por Hora | Subtotal |")
            for s in o.detalleOrden:
                print(f"| {s.horas} | {s.servicio.descripcion} | {s.servicio.precioHora} | {s.subtotal} |")
            print("Total Orden:", o.totalOrden)
            print("-------------------------------------------------")
        print("Monto Total del Dia:", ordenDiaria.totalDia)

if __name__ == "__main__":
    CrearOrdenDiaria.main()