from nota import Nota
from alumno import Alumno
class CargarNotas:
    def __init__(self):
        self.alumnos=[]
    def ejecutar(self):
        while True:
            nombreCompleto= input("INGRESE EL NOMBRE DEL ALUMNO: ")
            legajo= int(input("INGRESE EL LEGAJO: "))
            un_alumno=Alumno(nombreCompleto, legajo)
            while True:
                catedra= input("INGRESE LA CATEDRA: ")
                nota= float(input("INGRESE LA NOTA: "))
                una_nota = Nota(catedra, nota)
                un_alumno.notas.append(una_nota)
                
                decision= input("Si no desea agregar mas notas escriba salir o para continuar presione enter: ")
                if decision.upper()== "SALIR":
                    if len(un_alumno.notas) > 0:
                        print("FINALIZANDO CARGA DE NOTAS...")
                        break
                    else:
                        print("Debe ingresar al menos 1 nota antes de salir.")
            self.alumnos.append(un_alumno)
            otro= input("Desea agregar otro alumno? si/no")
            if otro.upper()=="NO":
                break
    def mostrar_alumnos(self):
        for i in self.alumnos:
            print(f"Alumno: {i.nombreCompleto} | Legajo: {i.legajo}")
            print("Notas:")
            for nota in i.notas:
                print(f" - {nota.catedra}: {nota.notaExamen}")
            
            promedio = i.calcular_promedio()
            print(f"El promedio del alumno es: {promedio}\n")
if __name__ == "__main__":
    sistema = CargarNotas()
    sistema.ejecutar()
    sistema.mostrar_alumnos()