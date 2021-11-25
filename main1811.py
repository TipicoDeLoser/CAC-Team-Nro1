from src.clases.NumeroComplejo import NumeroComplejo
from src.clases.vector import Vector

from src.clases.Aplicacion import Aplicacion

from src.clases.Administrador import Administrador
from src.clases.Reportero import Reportero
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

# Ejercicio 2-2

a = Vector(4,2,6)
b = Vector(2,6,4)
c = 2

print(str(a) + ' + ' + str(b) + ' = ' + str(a.sumar(b)))

print(str(a) + ' - ' + str(b) + ' = ' + str(a.restar(b)))

print(str(a) + ' * ' + str(c) + ' = ' + str(a.multiplicar(c)))

print(str(a) + ' / ' + str(c) + ' = ' + str(a.dividir(c)))


print("-----------------------------------------------")

appInfo = Aplicacion()

admin = Administrador("Admin", "Python", "admin@python.com")
appInfo.agregarAdmin(admin)
admin.describe_usuario()

reporter = Reportero("Reporter", "Python", "reporter@python.com")
appInfo.agregarReporter(reporter)
reporter.describe_usuario()

cliente = Cliente("Leo", "V", "leo@python.com")
appInfo.agregarCliente(cliente)
cliente.describe_cliente()

alfajor = Producto("Alfajor Capitan del espacio", 45)
item = Item(alfajor, 2)
cliente.CarritoDeCompras.agregarProducto(item)

mogul = Producto("Mogul", 40)
itemMogul = Item(mogul, 1)
cliente.CarritoDeCompras.agregarProducto(itemMogul)

cliente.CarritoDeCompras.describe_CarritoDeCompras()

admin.muestra_Rol()
admin.mostrar_info_clientes(appInfo)

reporter.muestra_Rol()
reporter.mostrar_info_clientes(appInfo)

