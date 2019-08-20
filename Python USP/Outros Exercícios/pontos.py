import math

coordenadaXA = int(input("Valor de X do ponto A:"))
coordenadaYA = int(input("Valor de Y do ponto A:"))
coordenadaXB = int(input("Valor de X do ponto B:"))
coordenadaYB = int(input("Valor de Y do ponto B:"))

distanciaAB = math.sqrt((coordenadaXB - coordenadaXA) ** 2 + (coordenadaYB - coordenadaYA)** 2)

if (distanciaAB >= 10):
    print("longe")
else:
    print("perto")