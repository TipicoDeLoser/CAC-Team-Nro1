from src.clases.Rol import Rol
from src.clases.Usuario import Usuario

class Reportero(Usuario):
    
    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)
        self.rol = Rol("Reporter", "Reportero ??")

    def mostrar_info_clientes(self, application):
            """Muestra los carritos actuales."""
            print("\nCarritos:")
            for cliente in application.clientes:
                print("Items en el carrito: " + str(len(cliente.CarritoDeCompras.items)) +  " - Total a pagar: " + str(cliente.CarritoDeCompras.total))
                for item in cliente.CarritoDeCompras.items:
                    print(item.producto.nombre)
                    print(str(item.cantidad) +  " x " + str(item.producto.precio) + " $")

    def muestra_Rol(self):
            """muestra rol del usuario."""
            print("\nRoles:")
            print("- " + self.rol.nombre)
