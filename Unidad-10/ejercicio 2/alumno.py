class Alumno:
    def __init__(self, nombreCompleto:str, legajo: int):
        self.nombreCompleto= nombreCompleto
        self.legajo= legajo
        self.notas=[]
    def calcular_promedio(self):
        suma=0
        for i in self.notas:
            suma+= i.notaExamen
        promedio= suma/len(self.notas)
        return promedio