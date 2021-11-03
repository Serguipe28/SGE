
lista_numeros = []
ceros = 0
mayores = 0
menores = 0

for i in range(0 , 10):
    a = int(input("Introduce el numero: "))
    lista_numeros.insert(i,a)
    if lista_numeros[i] == 0:
        ceros += 1
    elif lista_numeros[i] > 0:
        mayores += 1
    else:
        menores += 1

print("Ceros = {}\nMayores = {}\nMenores = {}".format(ceros, mayores, menores))

