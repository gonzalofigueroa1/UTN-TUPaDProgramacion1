from Articulo import Articulo

class RemitoVentaDetalle:
    def __init__(self, cantidad: int, articulo: Articulo):
        self.cantidad = cantidad
        self.articulo = articulo
        self.subtotal = cantidad * articulo.precio