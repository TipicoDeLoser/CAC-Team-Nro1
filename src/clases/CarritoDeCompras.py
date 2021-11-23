from src.clases.Item import Item

class CarritoDeCompras(object):

    def __init__(self):
        self.items = []
        self.total = 0

    def agregarProducto(self, item):
        self.items.append(item)
        self.total += item.producto.precio * item.cantidad

    def eliminarProducto(self, item):
        self.items.remove(item)
        self.total -= item.producto.precio * item.cantidad

    def mostrarTotalaPagar(self):
        print("\nTotal a pagar: " + + " $")

    def describe_CarritoDeCompras(self):
        """Muestra los Items que contiene el carrito de compras."""
        print("\nItems en el carrito: " + str(len(self.items)))
        for item in self.items:
            print(item.producto.nombre)
            print(str(item.cantidad) +  " x " + str(item.producto.precio) + " $")

        print("\nTotal a pagar: " + str(self.total) + " $")