from Articulo import Articulo
from RemitoVentaDetalle import RemitoVentaDetalle
from RemitoVenta import RemitoVenta
from RepartoDiario import RepartoDiario

class CrearRepartoDiario:
    @staticmethod
    def main():
        articulosDisponibles = [
            Articulo("10", "Filtro de Aceite", 10000),
            Articulo("20", "Filtro de Aire", 8000),
            Articulo("30", "Filtro de Combustible", 7500),
            Articulo("40", "Aceite de Motor sw/10", 25000),
            Articulo("50", "Correa de Distribución", 20000)
        ]
        clientesReparto = {
            "20284569875": "Juan Alonso",
            "20157896542": "Emiliano Salas",
            "50258963654": "Pacallcar Autos",
            "27654987456": "Julieta Videla",
            "50335588945": "Todo Auto SRL"
        }
        #creacion y carga de la lista de los remitos de venta, asignando atributos correspondientes
        reparto = RepartoDiario(input("Fecha del reparto: "))


        while True:
            #para el atributo del nombre del cliente se debe buscar en el diccionario clientesreparto y agarrar su nombre
            cuit = input("CUIT del cliente: ")
            if cuit in clientesReparto:
                nombreCliente = clientesReparto[cuit]
            #si no existe el cuit se pide el nombre del cliente y agregarlo al diccionario
            else:
                nombreCliente = input("Nuevo CUIT, ingresé el nombre del nuevo cliente: ")
                clientesReparto[cuit] = nombreCliente
            numero = int(input("Ingrese el número del remito: "))
            remito = RemitoVenta(nombreCliente, numero)
            #cargar el remito detalle para cada venta, se pide el codigo en remitoventadetalle
            while True:
                articulo = None
                while articulo is None:
                    codigo = input("Ingrese el codigo de la venta: ")
                    #se busca el codigo en la lista articulosdisponibles, si se encuentra, asignarlo. caso contrario mostrar mensaje de error
                    for a in articulosDisponibles:
                        if a.codigo == codigo:
                            articulo = a
                    if articulo is None:
                        print("el código es incorrecto, ingrese nuevamente")
                cantidad = 0
                while cantidad <= 0:
                    cantidad = int(input("Ingrese la cantidad a añadir: "))
                    if cantidad <= 0:
                        print("El número debe ser mayor a 0")
                detalle = RemitoVentaDetalle(cantidad,articulo)
                remito.agregar_detalle(detalle)
                pregunta = input("¿Quiere seguir añadiendo detalles? Si/No ")
                if pregunta.lower() == "no":
                   break
            reparto.agregar_venta(remito)
            pregunta = input("¿Quiere seguir añadiendo remitos? Si/No ")
            if pregunta.lower() == "no":
                break

        print("Reparto Diario")
        print("Fecha:",reparto.fecha)
        print("--------------Remitos del Reparto----------------")
        for r in reparto.remitosVenta:
            print("Nombre del cliente:",r.nombreCliente)
            print("Número remito:",r.numeroRemito)
            print("| Cantidad items | Denominacion Artículo | Precio Unitario | Subtotal |")
            for v in r.detallesRemito:
                print(f"| {v.cantidad} | {v.articulo.denominacion} | {v.articulo.precio} | {v.subtotal} |")
            print("Total Remito Venta:",r.totalVenta)
            print("---------------------------------")
        print("Monto Total Reparto",reparto.totalReparto)

if __name__ == "__main__":
    CrearRepartoDiario.main()