class NumeroComplejo():

    def __init__(self, real, img):
        self.real = real
        self.imag = img
   
    def sumar(self, y):
        """Suma 2 numeros complejos"""
        real = self.real + y.real
        imaginario = self.imag + y.imag

        return NumeroComplejo(real, imaginario)

    def restar(self, y):
        """Resta 2 numeros complejos"""
        real = self.real - y.real
        imaginario = self.imag - y.imag

        return NumeroComplejo(real, imaginario)

    def multiplicar(self, y):
        """Multiplica 2 numeros complejos"""
        real = (self.real * y.real) - (self.imag * y.imag)
        imaginario = (self.real * y.imag) + (self.imag * y.real)

        return NumeroComplejo(real, imaginario)

    def dividir(self, y):
        """Divide 2 numeros complejos"""
        real = (self.real * y.real + self.imag * y.imag ) / ( y.real ** 2 + y.imag ** 2)
        imaginario = (self.imag * y.real - self.real * y.imag ) / ( y.real ** 2 + y.imag ** 2)

        return NumeroComplejo(real, imaginario)

    def __str__(self):
        return f'{self.real}+{self.imag}i'
