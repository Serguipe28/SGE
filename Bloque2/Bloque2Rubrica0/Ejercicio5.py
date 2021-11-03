

cadena = input("Escriba aqui su cadena: ")
subcadena = 0

for i in range (1, len(cadena)-1):
    cadena = cadena.lower()
    if cadena[i - 1] == "a":
        if cadena[i] == "a":
            if cadena[i + 1] == "a":
                subcadena += 1

print(subcadena)