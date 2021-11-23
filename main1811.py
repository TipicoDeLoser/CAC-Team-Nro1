from src.clases.NumeroComplejo import NumeroComplejo

from src.clases.Administrador import Administrador
from src.clases.Producto import Producto
from src.clases.Item import Item
from src.clases.Cliente import Cliente

# datos de ejemplo
x = NumeroComplejo(3,2)
y = NumeroComplejo(2,6)

print(str(x) + ' + ' + str(y) + ' = ' + str(x.sumar(y)))

print(str(x) + ' - ' + str(y) + ' = ' + str(x.restar(y)))

print(str(x) + ' * ' + str(y) + ' = ' + str(x.multiplicar(y)))

print(str(x) + ' / ' + str(y) + ' = ' + str(x.dividir(y)))


print("-----------------------------------------------")

admin = Administrador("Admin", "Python", "admin@python.com")
admin.describe_usuario()
admin.muestra_privilegios()

cliente = Cliente("Leo", "V", "leo@python.com")
cliente.describe_cliente()

alfajor = Producto("Alfajor Capitan del espacio", 45)
item = Item(alfajor, 2)
cliente.CarritoDeCompras.agregarProducto(item)

mogul = Producto("Mogul", 40)
itemMogul = Item(mogul, 1)
cliente.CarritoDeCompras.agregarProducto(itemMogul)

cliente.CarritoDeCompras.describe_CarritoDeCompras()
