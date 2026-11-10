from typing import Optional

#Punto 1
def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento: float = 0.0, envio_prioritario: Optional[float] = None) -> float:
    monto_descuento = monto_base * (1 - descuento / 100)
    monto_impuesto = monto_descuento * (1 + impuesto / 100)
    if envio_prioritario is not None:
        costo = monto_impuesto + envio_prioritario
    else:
        costo = monto_impuesto
    return round(costo, 2)
print(f"Prueba 1: {calcular_factura_final (1000.0)}") #esperado 1210.0
print(f"Prueba 2: {calcular_factura_final (1000.0, descuento=10.0)}") #esperado 1089.0
print(f"Prueba 3: {calcular_factura_final (1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0)}") #esperado 1195.0

#Ejercicio 2
class ValidadorFinanciero:  
    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        return cuit.isdigit() and len(cuit)==11
    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
        monto_tot= (monto* tasa_cambio)*(1-comision)
        return monto_tot
print("")
print(ValidadorFinanciero.es_cuit_valido("20384920194"))
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))
print("")
#Punto 3

class Notificador:
    """Clase responsable de notificar transacciones."""

    def enviar_recibo(self, cliente: str, total: float):
        #Cambio 2: Implementar la lógica de impresión
        print("=" * 40)
        print("       RECIBO DE COMPRA")
        print("=" * 40)
        print(f"Cliente: {cliente}")
        print(f"Total a Pagar: ${total:.2f}")
        print("=" * 40)


class ProcesadorPagos:  #Cambio 3: PascalCase
    """Clase responsable de procesar pagos."""

    def __init__(self, notificador=None):  #Cambio 4: Agregar valor por defecto
        #Cambio 5: Validar si notificador es None
        if notificador is None:
            self.notificador = Notificador()
        else:
            self.notificador = notificador

    def procesar_transaccion(self, cliente: str, items: list[dict],
                            descuento_cupon: float = 0.0):
        #Cambio 6: Implementar la lógica completa

        #Paso 1: Iterar items y sumar precios
        total = 0.0
        for item in items:
            total += item["precio"]

        #Paso 2: Aplicar descuento
        total_final = total - descuento_cupon

        #Paso 3: Delegar la emisión del recibo al notificador
        self.notificador.enviar_recibo(cliente, total_final)

        #Paso 4: Retornar el total
        return total_final


# ========== PRUEBA ==========
if __name__ == "__main__":
    carrito = [
        {"nombre": "Teclado", "precio": 50.0},
        {"nombre": "Mouse", "precio": 30.0}
    ]

    procesador = ProcesadorPagos()  # Crea notificador automáticamente
    total = procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)
    print(f"\nTotal final: ${total:.2f}")

#Punto 4
print()
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    datos = f"Modulo: {modulo.upper()}\n"
    numero = 1
    datos += "Mensajes:\n"
    for mensaje in mensajes:
        datos += (f"[{numero}] {mensaje}\n")
        numero += 1
    datos += "Metadatos:\n"
    for clave in metadatos:
        valor = metadatos[clave]
        datos += (f"{clave.upper()}: {valor}\n")
    return datos
log = generar_auditoria_sistema("AUTH", "Intento fallido", "Bloqueo de IP", usuario="admin", ip="192.168.1.10")
print(log)


#Punto 5
class CalculadoraFitness:

    @staticmethod
    def calcular_imc(peso_kg, altura_m):
        imc = peso_kg / (altura_m ** 2)
        return round(imc, 2)

    @staticmethod
    def clasificar_nivel(imc):
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Normal"
        else:
            return "Sobrepeso"


class Atleta:

    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def obtener_reporte(self, incluir_recomendacion=False, **metricas_extra):

        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        nivel = CalculadoraFitness.clasificar_nivel(imc)

        reporte = "Nombre: " + self.nombre
        reporte += "\nPeso: " + str(self.peso) + " kg"
        reporte += "\nAltura: " + str(self.altura) + " m"
        reporte += "\nIMC: " + str(imc)
        reporte += "\nNivel: " + nivel

        for clave, valor in metricas_extra.items():
            reporte += "\n" + clave + ": " + str(valor)

        if incluir_recomendacion == True:
            if nivel == "Bajo peso":
                reporte += "\nRecomendación: Aumentar el peso de forma saludable."
            elif nivel == "Normal":
                reporte += "\nRecomendación: Mantener los hábitos actuales."
            else:
                reporte += "\nRecomendación: Mejorar alimentación y actividad física."

        return reporte


atleta1 = Atleta("Juan", 70, 1.75)

print(atleta1.obtener_reporte(
    incluir_recomendacion=True,
    edad=25,
    pulsaciones=75
))