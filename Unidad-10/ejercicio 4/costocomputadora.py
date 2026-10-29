from computadora import Computadora
from componentecpu import ComponenteCPU
class CostoComputadora:
    def __init__(self):
        self.computadoras_cotizadas = []

    def ejecutar(self):
        while True:
            marca_pc = input("Ingrese la marca de la computadora: ")
            modelo_pc = input("Ingrese el modelo de la computadora: ")
            
            pc = Computadora(marca_pc, modelo_pc)

            while True:
                nombre_comp = input("Ingrese el componente: ")
                marca_comp = input("Ingrese la marca del componente: ")
                cantidad_comp = int(input("Ingrese la cantidad: "))
                precio_comp = float(input("Ingrese el precio por unidad: "))

                componente = ComponenteCPU(nombre_comp, marca_comp, cantidad_comp, precio_comp)
                pc.lista_componentes.append(componente)

                decision_comp = input("¿Desea ingresar otro componente? (Presione enter para continuar o escriba 'salir'): ")
                if decision_comp.upper() == "SALIR":
                    break

            costo_total = pc.calcular_costo_total()
            
            if costo_total < 50000:
                precio_sugerido = costo_total + (costo_total * 0.40)
            else:
                precio_sugerido = costo_total + (costo_total * 0.30)

            print("\n-----------Computadora----------------")
            print(f"Marca: {pc.marca}")
            print(f"Modelo: {pc.modelo}")
            print("Componentes:")
            print(f"{'Componente':<20} {'Marca':<12} {'Cantidad':<10} {'Precio X Unidad':<16} {'SubTotal'}")
            
            for comp in pc.lista_componentes:
                subtotal = comp.cantidad * comp.precio
                print(f"{comp.componente:<20} {comp.marca:<12} {comp.cantidad:<10} {comp.precio:<16} {subtotal}")
                
            print(f"Costo Total: {costo_total}")
            print(f"Precio de Venta Sugerido: {precio_sugerido}")
            print("--------------------------------------")

            respuesta = input("¿Desea cotizar una nueva computadora? (SI/NO): ")
            if respuesta.upper() != "SI":
                print("Finalizando programa..")
                break

if __name__ == "__main__":
    app = CostoComputadora()
    app.ejecutar()
