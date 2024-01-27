# ejercicio 1 

from datetime import datetime

def mostrar_tareas(tareas):
    print("\nTareas actuales:")
    for indice, tarea in enumerate(tareas, start=1):
        descripcion = tarea["descripcion"]
        fecha_vencimiento = tarea["fecha_vencimiento"]
        prioridad = tarea["prioridad"]
        print(f"{indice}. {descripcion} (Vence: {fecha_vencimiento}, Prioridad: {prioridad})")

def agregar_tarea(tareas):
    descripcion = input("Ingresa la descripción de la nueva tarea: ")
    fecha_vencimiento = input("Fecha de vencimiento (formato YYYY-MM-DD): ")
    prioridad = input("Prioridad (Alta, Media, Baja): ")
    tareas.append({
        "descripcion": descripcion,
        "fecha_vencimiento": fecha_vencimiento,
        "prioridad": prioridad
    })
    print("Tarea agregada.")

def editar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Elige el número de la tarea a editar: ")) - 1
        if indice < 0 or indice >= len(tareas):
            print("Número de tarea no válido.")
            return
        nueva_descripcion = input("Nueva descripción de la tarea: ")
        nueva_fecha_vencimiento = input("Nueva fecha de vencimiento (formato YYYY-MM-DD): ")
        nueva_prioridad = input("Nueva prioridad (Alta, Media, Baja): ")
        tareas[indice] = {
            "descripcion": nueva_descripcion,
            "fecha_vencimiento": nueva_fecha_vencimiento,
            "prioridad": nueva_prioridad
        }
        print("Tarea actualizada.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Elige el número de la tarea a eliminar: ")) - 1
        if indice < 0 or indice >= len(tareas):
            print("Número de tarea no válido.")
            return
        del tareas[indice]
        print("Tarea eliminada.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def main():
    tareas = []
    
    while True:
        print("\nGestor de Tareas")
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_tareas(tareas)
        elif opcion == '2':
            agregar_tarea(tareas)
        elif opcion == '3':
            editar_tarea(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("Gracias por usar el gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    main()