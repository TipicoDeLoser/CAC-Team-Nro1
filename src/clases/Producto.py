class Producto(object):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def describe_producto(self):
        """Muestra la info del producto."""
        print("\nProducto:")
        print("  Nombre: " + self.nombre)
        print("  Precio: " + str(self.precio))

    def __str__(self):
        return "Producto: {} - {}" , self.nombre, self.precio
