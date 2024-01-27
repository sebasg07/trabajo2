class BancoDeDatos:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, nombre, saldo):
        if nombre not in self.clientes:
            self.clientes[nombre] = saldo
            print(f"Cliente {nombre} agregado con un saldo inicial de {saldo}")
        else:
            print(f"Error: El cliente {nombre} ya existe en la base de datos.")

    def actualizar_saldo(self, nombre, nuevo_saldo):
        if nombre in self.clientes:
            self.clientes[nombre] = nuevo_saldo
            print(f"Saldo de {nombre} actualizado a {nuevo_saldo}")
        else:
            print(f"Error: No se encontró al cliente {nombre} en la base de datos.")

    def eliminar_cliente(self, nombre):
        if nombre in self.clientes:
            del self.clientes[nombre]
            print(f"Cliente {nombre} eliminado de la base de datos")
        else:
            print(f"Error: No se encontró al cliente {nombre} en la base de datos.")

    def buscar_cliente(self, nombre):
        if nombre in self.clientes:
            saldo = self.clientes[nombre]
            print(f"Cliente {nombre}: Saldo = {saldo}")
        else:
            print(f"Error: No se encontró al cliente {nombre} en la base de datos.")

    def visualizar_todos(self):
        print("Lista de clientes y saldos:")
        for nombre, saldo in self.clientes.items():
            print(f"{nombre}: {saldo}")

if __name__ == "__main__":
    banco = BancoDeDatos()

    while True:
        print("\n1. Agregar cliente")
        print("2. Actualizar saldo")
        print("3. Eliminar cliente")
        print("4. Buscar cliente")
        print("5. Visualizar todos los clientes")
        print("6. Salir")

        opcion = input("Ingrese la opción (1-6): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            saldo = float(input("Ingrese el saldo inicial: "))
            banco.agregar_cliente(nombre, saldo)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente: ")
            nuevo_saldo = float(input("Ingrese el nuevo saldo: "))
            banco.actualizar_saldo(nombre, nuevo_saldo)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente que desea eliminar: ")
            banco.eliminar_cliente(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del cliente que desea buscar: ")
            banco.buscar_cliente(nombre)
        elif opcion == "5":
            banco.visualizar_todos()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
