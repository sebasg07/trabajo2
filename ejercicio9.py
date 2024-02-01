import json
import os
from datetime import datetime

def cargar_datos():
    if os.path.exists('gastos.json'):
        with open('gastos.json', 'r') as archivo:
            return json.load(archivo)
    else:
        return {'gastos': []}

def guardar_datos(datos):
    with open('gastos.json', 'w') as archivo:
        json.dump(datos, archivo, indent=2)

def ingresar_gasto():
    categoria = input("Ingrese la categoría del gasto: ")
    monto = float(input("Ingrese el monto del gasto: "))
    descripcion = input("Ingrese una descripción del gasto: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {'categoria': categoria, 'monto': monto, 'descripcion': descripcion, 'fecha': fecha}

def mostrar_gastos(gastos):
    if not gastos:
        print("No hay gastos registrados.")
    else:
        print("Lista de gastos:")
        for gasto in gastos:
            print(f"\nCategoría: {gasto['categoria']}\nMonto: {gasto['monto']}\nDescripción: {gasto['descripcion']}\nFecha: {gasto['fecha']}\n{'-'*20}")

def calcular_total(gastos):
    return sum(gasto['monto'] for gasto in gastos)

def generar_informe(gastos):
    mostrar_gastos(gastos)
    total = calcular_total(gastos)
    print(f"\nTotal de gastos: {total}")

def establecer_presupuesto():
    presupuesto = float(input("Ingrese su presupuesto mensual: "))
    return presupuesto

def verificar_presupuesto(gastos, presupuesto):
    total_gastos = calcular_total(gastos)
    if total_gastos > presupuesto:
        print(f"\n¡Alerta! Ha superado su presupuesto mensual. Total de gastos: {total_gastos}, Presupuesto: {presupuesto}")
    else:
        print(f"\n¡Felicidades! Está dentro de su presupuesto mensual. Total de gastos: {total_gastos}, Presupuesto: {presupuesto}")

def main():
    datos = cargar_datos()
    presupuesto = establecer_presupuesto()

    while True:
        print("\n----- Sistema de Registro de Gastos -----")
        print("1. Ingresar un nuevo gasto")
        print("2. Mostrar gastos")
        print("3. Generar informe")
        print("4. Establecer presupuesto")
        print("5. Verificar presupuesto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nuevo_gasto = ingresar_gasto()
            datos['gastos'].append(nuevo_gasto)
            guardar_datos(datos)
            print("Gasto registrado exitosamente.")

        elif opcion == '2':
            mostrar_gastos(datos['gastos'])

        elif opcion == '3':
            generar_informe(datos['gastos'])

        elif opcion == '4':
            presupuesto = establecer_presupuesto()
            print(f"Presupuesto actualizado: {presupuesto}")

        elif opcion == '5':
            verificar_presupuesto(datos['gastos'], presupuesto)

        elif opcion == '6':
            print("Saliendo del sistema de registro de gastos. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
