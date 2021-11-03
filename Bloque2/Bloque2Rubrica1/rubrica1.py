import re

archivo = input("Introduzca la ruta del archivo: ")
contar_palabra = 0
palabras = []


def ask_word(words):
    while input("Añadir palabra [S] [N] ") == "S":
        user = input("Palabra: ")
        words.append(user)


def lineas_palabra(archive, words):
    with open(archive, "r") as lectura:
        for line in lectura:
            for user_word in words:
                if re.search(user_word, line):
                    print(line)


ask_word(palabras)
lineas_palabra(archivo, palabras)
