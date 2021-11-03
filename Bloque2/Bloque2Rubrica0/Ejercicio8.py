
tabla = [1,2,3,4,5,6,7]

def sum(tabla):
    resultado = 0
    for i in range(0, len(tabla)):
        resultado += tabla[i]
    return resultado
print(sum(tabla))