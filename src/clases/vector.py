class Vector():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sumar(self, a):
        """Suma 2 vectores de 3 dimensiones"""
        x = self.x + a.x
        y = self.y + a.y
        z = self.z + a.z

        return Vector(x, y, z)

    def restar(self, a):
        """Resta 2 vectores de 3 dimensiones"""
        x = self.x - a.x
        y = self.y - a.y
        z = self.z - a.z

        return Vector(x, y, z)

    def multiplicar(self, a):
        """Multiplica un vector de 3 dimensiones por un escalar"""
        x = self.x * a
        y = self.y * a
        z = self.z * a

        return Vector(x, y, z)

    def dividir(self, a):
        """Divide un vector de 3 dimensiones por un escalar"""
        x = self.x / a
        y = self.y / a
        z = self.z / a

        return Vector(x, y, z)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'
        