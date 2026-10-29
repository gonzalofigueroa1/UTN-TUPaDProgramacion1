from plato import Plato
from ingrediente import Ingrediente
class MenuRestaurant:
    def __init__(self):
        self.platosMenu=[]
    def ejecutar(self):
        while True:
            nombreCompleto= input("INGRESE EL NOMBRE DEL PLATO: ")
            precio= float(input("INGRESE EL PRECIO: "))
            esBebida= input("INGRESE SI ES BEBIDA O NO: ")
            platillo= Plato(nombreCompleto, precio, esBebida)
            self.platosMenu.append(platillo)
                      
            if esBebida.upper()!="SI":

                while True:

                    nombre= input("INGRESE EL INGREDIENTE: ")
                    cantidad= float(input("INGRESE LA CANTIDAD: "))
                    unidad_de_medida= input("INGRESE LA UNIDAD DE MEDIDA: ")

                    ing= Ingrediente(nombre,cantidad, unidad_de_medida)
                    platillo.lista_ingredientes.append(ing)
                    decision1=input("Si no desea ingresar mas ingredientes ponga salir de lo contrario presione enter: ")
                    if decision1.upper()=="SALIR":
                        break

            decision= input("Si no desea ingresar mas platos ingrese salir o para continuar presione enter: ")
            if decision.upper()== "SALIR":
                break
        print("-----------MENÚ----------------")
        for plato in self.platosMenu:
            print(f"{plato.nombreCompleto}")
            print(f"Precio: $ {plato.precio}")
            
            if plato.lista_ingredientes: 
                print("Ingredientes:")
                print(f"{'Nombre':<15} {'Cantidad':<10} {'Unidad de Medida'}")
                for ing in plato.lista_ingredientes:
                    print(f"{ing.nombre:<15} {ing.cantidad:<10} {ing.unidad_de_medida}")
                    
            print("----------------------------------")


if __name__ == "__main__":
    mi_menu = MenuRestaurant()
    
    mi_menu.ejecutar()