from nota import Nota
from alumno import Alumno


#verificacion si es un str
def esTexto(texto):
    while True:
        dato = input(texto).strip()
        if dato:
            return dato
        print("Error, ingrese correctamente lo solicitado.")

def esEntero(num):
    while True:
        try:
            return int(input(num))
        except ValueError:
            print("Error, Ingrese correctamente el n° solicitado.")

#verificacion de la nota: numero entre 0 y 10
def esNota(num):
    while True:
        try:
            nota = float(input(num).replace(",", "."))
        except ValueError:
            print("Error, Ingrese correctamente el n° solicitado.")
            continue
        if 0 <= nota <= 10:
            return nota
        print("Error, la nota debe estar entre 0 y 10.")

#verificacion de la respuesta SI/NO
def esSiNo(pregunta):
    while True:
        respuesta = input(pregunta).strip().upper()
        if respuesta in ("SI", "S"):
            return True
        if respuesta in ("NO", "N"):
            return False
        print("Error, responda SI o NO.")


class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def main(self):
        self.cargar_alumnos()
        self.mostrar_alumnos()

    def cargar_alumnos(self):
        seguir = True
        while seguir:
            print("\nINGRESE DATOS DEL ALUMNO")
            nombreCompleto = esTexto("Ingrese el nombre completo: ")
            legajo = esEntero("Ingrese el legajo: ")
            alumno = Alumno(nombreCompleto, legajo)
            self.cargar_notas(alumno)
            self.alumnos.append(alumno)
            seguir = esSiNo("Desea cargar otro alumno? (SI/NO): ")

    def cargar_notas(self, alumno):
        #el bucle corre al menos una vez, asi se garantiza 1 nota como minimo
        while True:
            catedra = esTexto("Ingrese el nombre de la catedra: ")
            notaExamen = esNota("Ingrese la nota: ")
            alumno.notas.append(Nota(catedra, notaExamen))
            if not esSiNo("Desea cargar otra nota? (SI/NO): "):
                break

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            print("\n-----------ALUMNO----------------")
            print(f"Nombre: {alumno.nombreCompleto}")
            print(f"Legajo: {alumno.legajo}")
            print("Notas:")
            for nota in alumno.notas:
                print(f"  {nota.catedra}: {nota.notaExamen}")
            print(f"El promedio del alumno es: {alumno.promedio():.2f}")


CargaNotas().main()
