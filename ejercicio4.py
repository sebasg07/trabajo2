import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "juego", "ahorcado", "desarrollo"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_correctas):
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def verificar_letra(letra, palabra_secreta, letras_correctas, letras_incorrectas):
    if letra in letras_correctas or letra in letras_incorrectas:
        return False  # La letra ya ha sido ingresada
    elif letra in palabra_secreta:
        letras_correctas.append(letra)
        return True  # La letra es correcta
    else:
        letras_incorrectas.append(letra)
        return False  # La letra es incorrecta

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_correctas = []
    letras_incorrectas = []
    intentos_maximos = 6
    intentos = 0

    print("¡Bienvenido al Juego del Ahorcado!")
    print(mostrar_tablero(palabra_secreta, letras_correctas))

    while intentos < intentos_maximos:
        intento = input("\nIngresa una letra: ").lower()

        if len(intento) == 1 and intento.isalpha():
            acierto = verificar_letra(intento, palabra_secreta, letras_correctas, letras_incorrectas)

            if acierto:
                print("¡Correcto!")
            else:
                intentos += 1
                print("Incorrecto. Te quedan {} intentos.".format(intentos_maximos - intentos))

            tablero = mostrar_tablero(palabra_secreta, letras_correctas)
            print(tablero)

            if "_" not in tablero:
                print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                break
        else:
            print("\nIngresa una letra válida.")

    if "_" in mostrar_tablero(palabra_secreta, letras_correctas):
        print("\n¡Oh no! Te has quedado sin intentos. La palabra era:", palabra_secreta)

if __name__ == "__main__":
    jugar_ahorcado()
