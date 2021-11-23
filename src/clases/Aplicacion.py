class Aplicacion(object):

    def __init__(self):
        self.clientes = []
        self.admins = []
        self.reporters = []

    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def agregarAdmin(self, administrador):
        self.admins.append(administrador)

    def agregarReporter(self, reportero):
        self.reporters.append(reportero)

    def describe_Clientes(self):
        """Muestra la info de los clientes."""
        print("\nClientes: " + str(len(self.clientes)))
        for item in self.clientes:
            print(item.clientes.id)

    def __str__(self):
        return "Clientes: {} " , str(len(self.clientes))
