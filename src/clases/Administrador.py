from src.clases.Rol import Rol
from src.clases.Usuario import Usuario

class Administrador(Usuario):
    
    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)
        self.rol = Rol("Admin", "Administrador del sistema")

    def mostrar_info_clientes(self, application):
            """Muestra los clientes."""
            print("\nClientes:")
            for cliente in application.clientes:
                print("- " + cliente.nombre)
                print("Items en el carrito: " + str(len(cliente.CarritoDeCompras.items)) +  " - Total a pagar: " + str(cliente.CarritoDeCompras.total))
                for item in cliente.CarritoDeCompras.items:
                    print(item.producto.nombre)
                    print(str(item.cantidad) +  " x " + str(item.producto.precio) + " $")

    def muestra_Rol(self):
            """muestra rol del usuario."""
            print("\nRoles:")
            print("- " + self.rol.nombre)
