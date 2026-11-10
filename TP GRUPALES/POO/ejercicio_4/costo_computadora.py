from componente_cpu import ComponenteCPU
from computadora import Computadora


def pedirTexto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Error, el dato no puede quedar vacio")


def pedirEntero(mensaje, nombre):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print(f"Error, ingrese correctamente {nombre}")
            continue
        if valor > 0:
            return valor
        print(f"Error, {nombre} debe ser mayor a cero")


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


class CostoComputadora:
    def main(self):
        # Se cotiza una computadora por vuelta hasta que el usuario responda NO
        while True:
            computadora = self.cargarComputadora()
            self.mostrarComputadora(computadora)
            if not pedirSiNo("\nDesea cotizar una nueva computadora? (SI/NO): "):
                break

    def cargarComputadora(self):
        print("\nINGRESE DATOS DE LA COMPUTADORA")
        computadora = Computadora(
            pedirTexto("Marca: "),
            pedirTexto("Modelo: "),
        )
        # El bucle corre al menos una vez: toda computadora lleva 1 componente como minimo
        while True:
            computadora.componentesCPU.append(
                ComponenteCPU(
                    pedirTexto("Componente: "),
                    pedirTexto("Marca del componente: "),
                    pedirEntero("Cantidad: ", "la cantidad"),
                    pedirDecimal("Precio por unidad: ", "el precio"),
                )
            )
            if not pedirSiNo("Desea cargar otro componente? (SI/NO): "):
                break
        return computadora

    def mostrarComputadora(self, computadora):
        print("\n-----------Computadora----------------")
        print(f"Marca: {computadora.marca}")
        print(f"Modelo: {computadora.modelo}")
        print("Componentes:")
        print(f"{'Componente':<22}{'Marca':<15}{'Cantidad':<10}{'Precio X Unidad':<18}SubTotal")
        for componente in computadora.componentesCPU:
            print(
                f"{componente.componente:<22}"
                f"{componente.marca:<15}"
                f"{componente.cantidad:<10}"
                f"{componente.precio:<18.2f}"
                f"{componente.subTotal():.2f}"
            )
        print(f"\nCosto Total: {computadora.costo():.2f}")
        print(
            f"El precio sugerido de venta es {computadora.costo():.2f} + "
            f"{computadora.recargo():.2f} = {computadora.precioVenta():.2f}"
        )


CostoComputadora().main()
