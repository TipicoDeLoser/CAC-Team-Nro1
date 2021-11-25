class Rol(object):

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def describe_rol(self):
        """Muestra la info del rol."""
        print("\nRol:")
        print("  Nombre: " + self.nombre)
        print("  descripcion: " + self.descripcion)

    def __str__(self):
        return "Rol: {} " , self.nombre
