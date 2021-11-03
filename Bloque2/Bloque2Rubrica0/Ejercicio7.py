

cadena = input("Escriba la cadena de texto: ")


def invertir_cadena(cadena):
    return cadena[::-1]


def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

print(invertir_cadena(cadena))