from Socio import Socio
class PlanillaMensual:
    def __init__(self, mes: str):
        self.mes = mes
        self.socios = []
        self.totalRecaudado = 0.0

    def agregar_socios(self, totalSocio: Socio):
        self.socios.append(totalSocio)
        total = 0.0
        for s in self.socios:
            total += s
        self.totalRecaudado = total