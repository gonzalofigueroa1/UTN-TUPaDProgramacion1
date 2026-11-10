class Alumno:
    def __init__(self, nombreCompleto: str, legajo: int):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def promedio(self):
        #sin notas no hay promedio: se evita la division por cero
        if not self.notas:
            return 0
        return sum(nota.notaExamen for nota in self.notas) / len(self.notas)
