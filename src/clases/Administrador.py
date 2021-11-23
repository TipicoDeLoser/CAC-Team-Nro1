from src.clases.Usuario import Usuario

class Administrador(Usuario):
    
    def __init__(self, nombre, apellido, email):
        super().__init__(nombre, apellido, email)
        self.privilegios = ['admin']

    def muestra_privilegios(self):
            """muestra los privilegios del usuario."""
            print("\nPrivilegios:")
            for privilege in self.privilegios:
                print("- " + privilege)
