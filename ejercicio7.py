import random

def seleccionar_elemento(opciones):
    return random.choice(opciones)

def generar_historia(personajes, lugares, eventos):
    
    personaje = seleccionar_elemento(personajes)
    lugar = seleccionar_elemento(lugares)
    evento = seleccionar_elemento(eventos)

    
    historia = f"{personaje} fue a {lugar} y {evento}."

    return historia


usuarios_personajes = input("Ingresa personajes separados por comas: ").split(',')
usuarios_lugares = input("Ingresa lugares separados por comas: ").split(',')
usuarios_eventos = input("Ingresa eventos separados por comas: ").split(',')


historia_generada = generar_historia(usuarios_personajes, usuarios_lugares, usuarios_eventos)
print(historia_generada)
