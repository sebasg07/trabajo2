import random

# Estructura de datos para almacenar preguntas
preguntas = {
    "Ciencia": [
        {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "respuesta": "Júpiter"},
        {"pregunta": "¿Cuántos huesos tiene un adulto humano?", "respuesta": "206"},
    ],
    "Historia": [
        {"pregunta": "¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?", "respuesta": "1776"},
        {"pregunta": "¿Quién fue el primer presidente de Estados Unidos?", "respuesta": "George Washington"},
    ],
    # Agregar más categorías y preguntas según sea necesario
}

# Función para que un jugador seleccione una categoría
def seleccionar_categoria():
    print("Categorías disponibles:")
    for categoria in preguntas:
        print(f"- {categoria}")
    return input("Selecciona una categoría: ")

# Función para que un jugador responda una pregunta
def responder_pregunta(pregunta_actual):
    respuesta_jugador = input(f"Pregunta: {pregunta_actual['pregunta']} \nTu respuesta: ")
    return respuesta_jugador.lower() == pregunta_actual['respuesta'].lower()

# Función principal para el juego
def jugar_quiz():
    print("¡Bienvenido a QuizMaster!")

    # Puede personalizar el número de jugadores aquí
    num_jugadores = int(input("Ingresa el número de jugadores (1-4): "))

    jugadores = {f"Jugador {i + 1}": 0 for i in range(num_jugadores)}

    for _ in range(5):  # Puedes ajustar la cantidad de preguntas por ronda
        categoria_seleccionada = seleccionar_categoria()
        pregunta_actual = random.choice(preguntas[categoria_seleccionada])

        for jugador in jugadores:
            print(f"\nTurno de {jugador} en la categoría {categoria_seleccionada}:")
            if responder_pregunta(pregunta_actual):
                print("¡Respuesta correcta! Sumas 10 puntos.")
                jugadores[jugador] += 10
            else:
                print(f"Incorrecto. La respuesta correcta es: {pregunta_actual['respuesta']}.")

    # Mostrar resultados finales
    print("\nResultados finales:")
    for jugador, puntaje in jugadores.items():
        print(f"{jugador}: {puntaje} puntos")

    ganador = max(jugadores, key=jugadores.get)
    print(f"\n¡El ganador es {ganador}! ¡Felicidades!")

# Iniciar el juego
jugar_quiz()
