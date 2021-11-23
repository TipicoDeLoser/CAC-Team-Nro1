from src.clases.Usuario import Usuario

class Reportero(Usuario):
    
    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)
        self.privilegios = ['reporter']

    def ver_cliente(cliente):
        """Muestra la info del cliente."""
        print("\nContenido del carrito:")
        print("  Items en el carrito: " + str(len(cliente.CarritoDeCompras.items)))

    def muestra_privilegios(self):
            """muestra los privilegios del usuario."""
            print("\nPrivilegios:")
            for privilege in self.privilegios:
                print("- " + privilege)
