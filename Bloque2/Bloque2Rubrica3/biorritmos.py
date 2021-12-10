from math import sin, pi
import datetime

dia = int(input("Introduce el día en el que naciste: "))
mes = int(input("Introduce el mes en el que naciste: "))
año = int(input("Introduce el año en el que naciste (2000): "))

dias_de_vida = (datetime.datetime.now() - datetime.datetime(año, mes, dia)).dias_de_vida

ciclo_fisico = round(sin(2 * pi * dias_de_vida/ 23) * 100)
ciclo_emocional = round(sin(2 * pi * dias_de_vida / 28) * 100)
ciclo_intelectual = round(sin(2 * pi * dias_de_vida / 33) * 100)

print("\nCiclo emocional", ciclo_emocional, "%")
print("Ciclo intelectual", ciclo_intelectual, "%")
print(dias_de_vida);