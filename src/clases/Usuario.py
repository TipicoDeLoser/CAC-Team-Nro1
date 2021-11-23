import uuid

class Usuario(object):

    def __init__(self, nombre, apellido, email):
        self.id  = uuid.uuid4()
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def describe_usuario(self):
        """Muestra la info del usuario."""
        print("\nUsuario:")
        print("  ID: " + str(self.id))
        print("  Nombre: " + self.nombre + " " + self.apellido)
        print("  Email: " + self.email)

    def __str__(self):
        return " Usuario: {} - {} {}" , (str(self.id), self.apellido, self.nombre)
