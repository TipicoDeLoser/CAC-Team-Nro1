from src.clases.Usuario import Usuario
from src.clases.CarritoDeCompras import CarritoDeCompras

class Cliente(Usuario):

    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)
        self.CarritoDeCompras = CarritoDeCompras()

    def describe_cliente(self):
        """Muestra la info del usuario."""
        print("\nCliente:")
        print("  ID: " + str(self.id))
        print("  Nombre: " + self.nombre + " " + self.apellido)
        print("  Email: " + self.email)
        print("  Items en el carrito: " + str(len(self.CarritoDeCompras.items)))

    def __str__(self):
        return " Cliente: {} - {} {}" , (str(self.id), self.apellido, self.nombre)
