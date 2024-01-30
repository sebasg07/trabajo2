class Seat:
    def __init__(self):
        self.is_available = True

class Screen:
    def __init__(self, capacity):
        self.capacity = capacity
        self.filas, self.columnas = capacity
        self.asientos = [[Seat() for _ in range(self.columnas)] for _ in range(self.filas)]

def mostrar_asientos_disponibles(pantalla):
    """Mostrar los asientos disponibles para la pantalla dada."""
    print(f"\nAsientos disponibles para la Pantalla (Filas: {pantalla.filas}, Columnas: {pantalla.columnas}):")
    template_fila = " {:<2}" * pantalla.columnas
    for fila in range(1, pantalla.filas + 1):
        print(f"Fila {fila}:", template_fila.format(*['X' if not asiento.is_available else 'O' for asiento in pantalla.asientos[fila - 1]]))

def reservar_asiento(pantalla, fila, columna):
    """Reservar un asiento en la pantalla dada."""
    if 1 <= fila <= pantalla.filas and 1 <= columna <= pantalla.columnas:
        asiento = pantalla.asientos[fila - 1][columna - 1]
        if asiento.is_available:
            asiento.is_available = False
            print(f"Asiento ({fila}, {columna}) reservado.")
        else:
            print(f"Asiento ({fila}, {columna}) ya está reservado.")
    else:
        print("Fila o columna no válida. Por favor, inténtelo de nuevo.")

def seleccionar_asiento(pantalla):
    """Permitir al usuario seleccionar un asiento en la pantalla dada."""
    mostrar_asientos_disponibles(pantalla)
    while True:
        try:
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))
            reservar_asiento(pantalla, fila, columna)
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese una fila y columna válidas.")

cine = Screen((5, 10))
seleccionar_asiento(cine)
seleccionar_asiento(cine)
