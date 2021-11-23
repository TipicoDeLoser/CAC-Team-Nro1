class Item(object):

    def __init__(self, producto, cantidad):
        self.producto  = producto
        self.cantidad = cantidad

    def describe_Item(self):
        """Muestra la info del Item."""
        print("\nProducto:")
        print("  Nombre: " + self.producto.nombre)
        print("  Cantidad: " + self.cantidad)

    def __str__(self):
        return " Item: {} - Cantidad: {} " , self.nombre, self.cantidad
