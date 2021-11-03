from random import randint

aleatorio = randint(0,20)
numero = int
intentos = 0

while aleatorio != numero:
    numero = int(input("Introduce un numero del 0,20: "))
    if numero > aleatorio:
        print("Menor")
    elif numero < aleatorio:
        print("Mayor")
    intentos +=1

print("Has acertado el numero es {}, en {} intentos".format(numero, intentos))


