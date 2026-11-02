from Actividad import Actividad
from Inscripcion import Inscripcion
from Socio import Socio
from PlanillaMensual import PlanillaMensual
class CrearPlanilla:
    def main():
        actividadesDisponibles = [
            Actividad("10", "Natación", 8000),
            Actividad("20", "Fútbol", 5000),
            Actividad("30", "Yoga", 6000),
            Actividad("40", "Musculación", 7000),
            Actividad("50", "Tenis", 9500)
        ]
        sociosRegistrados = {
            "31254789": "Valeria Quiroga",
            "29874512": "Andrés Maldonado",
            "34125896": "Florencia Arias",
            "27458963": "Sergio Benavidez",
            "36987412": "Camila Torres"
        }
        planilla_mes = PlanillaMensual(input("Ingrese el Mes: "))

        while True:
            dni = input("Ingrese el DNI del socio: ")
            if dni in sociosRegistrados:
                nombre = sociosRegistrados[dni]
            else:
                print("Nuevo documento")
                nombre = input("Ingrese el nombre del socio nuevo: ")
                sociosRegistrados[dni] = nombre
            numero_repetido = 0
            while numero_repetido <= 0:
                numeroSocio = int(input("Ingrese el número de socio: "))
                if numeroSocio < 0:
                    print("el número de socio no es válido, ingrese otro")
            socio = Socio(nombre,numeroSocio)
            while True:
                actividad = None
                while actividad is None:
                    codigo = input("Ingrese el codigo de la actividad: ")
                    for a in actividadesDisponibles:
                        if a.codigo == codigo:
                            actividad == a
                    if actividad is None:
                        print("el código es incorrecto, ingrese nuevamente")
                meses = 0
                while meses < 0:
                    meses = int(input("Ingrese la cantidad de meses: "))
                    if meses < 0:
                        print("Los meses no pueden ser menores o igual a 0")
                if actividad == socio.nombre:
                    print("Error: Este socio ya esta registrado en esta actividad")
                else:
                    inscripcion = Inscripcion(meses, actividad)
                    seguir = input("¿Quiere seguir añadiendo actividades? SI/NO")
                    if seguir.lower() == "no":
                        break
            seguir = input("¿Quiere seguir añadiendo socios? SI/NO")
            if seguir.lower() == "no":
                break
        print("Planilla Mensual")
        print("Mes",planilla_mes.mes)
        print("--------------Socios del Club----------------")
        for s in planilla_mes.socios:
            print("Socio: ",s.nombre)
            print("Numero socio: ",s.numeroSocio)
            print("| Actividad | Meses | Cuota Mensual | Subtotal |")
            for i in s.inscripciones:
                print(f"| {i.actividad.codigo} | {i.meses} | {i.actividad.cuotaMensual} | {i.subtotal} |")
            print("Total Socio: ",s.totalRecaudado)
        print("-----------------------------------------------")