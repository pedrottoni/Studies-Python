# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. a² + b² = c²
import math

catetoOposto = float(input("Digite o comprimento do cateto oposto: "))
catetoAdjacente = float(input("Digite o comprimento do cateto adjacente: "))

print(
    f"A hipotenuza vai medir:\nUsando a fórmula: {(catetoOposto ** 2 + catetoAdjacente ** 2) ** .5:.2f}\nUsando o pow/sqrt: {math.sqrt(math.pow(catetoOposto,2) + math.pow(catetoAdjacente,2)):.2f}\nUsando o hypot: {math.hypot(catetoOposto,catetoAdjacente):.2f}")
