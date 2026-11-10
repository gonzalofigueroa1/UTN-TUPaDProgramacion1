from ingrediente import Ingrediente
from plato import Plato


def pedirTexto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error, el dato no puede quedar vacio")


def pedirDecimal(mensaje, nombre):
    while True:
        try:
            # Se acepta coma como separador decimal
            valor = float(input(mensaje).replace(",", "."))
        except ValueError:
            print(f"Error, ingrese correctamente {nombre}")
            continue
        if valor > 0:
            return valor
        print(f"Error, {nombre} debe ser mayor a cero")


def pedirSiNo(mensaje):
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta in ("SI", "S"):
            return True
        if respuesta in ("NO", "N"):
            return False
        print("Error, responda SI o NO")


class MenuRestaurant:
    def __init__(self):
        self.platosMenu = []

    def main(self):
        self.cargarPlatos()
        self.mostrarMenu()

    def cargarPlatos(self):
        seguir = True
        while seguir:
            print("\nINGRESE DATOS DEL PLATO")
            plato = Plato(
                pedirTexto("Nombre del plato: "),
                pedirDecimal("Precio: ", "el precio"),
                pedirSiNo("Es una bebida? (SI/NO): "),
            )
            # A las bebidas no se les cargan ingredientes
            if not plato.esBebida:
                # El bucle corre al menos una vez: todo plato lleva 1 ingrediente como minimo
                while True:
                    plato.ingredientes.append(
                        Ingrediente(
                            pedirTexto("Nombre del ingrediente: "),
                            pedirDecimal("Cantidad: ", "la cantidad"),
                            pedirTexto("Unidad de medida: "),
                        )
                    )
                    if not pedirSiNo("Desea cargar otro ingrediente? (SI/NO): "):
                        break
            self.platosMenu.append(plato)
            seguir = pedirSiNo("Desea cargar otro plato? (SI/NO): ")

    def mostrarMenu(self):
        print("\n-----------MENU----------------")
        for plato in self.platosMenu:
            print(plato.nombreCompleto)
            print(f"Precio: $ {plato.precio:.2f}")
            if plato.ingredientes:
                print("Ingredientes:")
                print(f"{'Nombre':<25}{'Cantidad':<12}Unidad de Medida")
                for ingrediente in plato.ingredientes:
                    print(
                        f"{ingrediente.nombre:<25}"
                        f"{ingrediente.cantidad:<12g}"
                        f"{ingrediente.unidadMedida}"
                    )
            print("--------------------------------")


MenuRestaurant().main()
