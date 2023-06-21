import random

# Lista de palabras en alemán
palabras = ["Haus", "Auto", "Apfel", "Schule", "Blume"]

# Función para seleccionar una palabra aleatoria
def seleccionar_palabra():
    return random.choice(palabras)

# Función principal del juego
def juego_adivinanzas():
    palabra_secreta = seleccionar_palabra()
    intentos = 3

    print("Willkommen zum Spiel der Rätselwörter!")
    print("Ich habe ein Wort gewählt. Versuche es zu erraten.")

    while intentos > 0:
        print("\nDu hast noch", intentos, "Versuch(e).")
        adivinanza = input("Rätselwort: ")

        if adivinanza.lower() == palabra_secreta.lower():
            print("Gut gemacht! Du hast das Wort richtig erraten.")
            return

        print("Leider falsch. Versuche es erneut.")

        intentos -= 1

    print("\nDu hast alle Versuche verbraucht.")
    print("Das Wort war:", palabra_secreta)
    print("Übersetzung:", palabra_secreta, "->", palabra_secreta.capitalize().lower())
    print("Erklärung: Ein", palabra_secreta, "ist ein ...")

# Ejecutar el juego
juego_adivinanzas()
