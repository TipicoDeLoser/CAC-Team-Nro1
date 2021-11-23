from src.clases.NumeroComplejo import NumeroComplejo

# datos de ejemplo
x = NumeroComplejo(3,2)
y = NumeroComplejo(2,6)

print(str(x) + ' + ' + str(y) + ' = ' + str(x.sumar(y)))

print(str(x) + ' - ' + str(y) + ' = ' + str(x.restar(y)))

print(str(x) + ' * ' + str(y) + ' = ' + str(x.multiplicar(y)))

print(str(x) + ' / ' + str(y) + ' = ' + str(x.dividir(y)))
