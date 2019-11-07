"""
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""
from random import randint
from time import sleep

list = [[], [], []]

for sub in range(0, 3):
    for element in range(0, 3):
        number = randint(0, 99)
        print(f"Adicionando o número {number:2} na posição: {sub}/{element}")
        list[sub].append(number)
        sleep(.3)
# Mostrando a Matriz com "for"
for line in range(0, 3):
    for coluna in range(0, 3):
        print(f"[ {list[line][coluna]:2} ]", end=' ')
    print()

# Ou direto no "print"
print(f"\n[ {list[0][0]:2} ] [ {list[0][1]:2} ] [ {list[0][2]:2} ]\n[ {list[1][0]:2} ] [ {list[1][1]:2} ] [ {list[1][2]:2} ]\n[ {list[2][0]:2} ] [ {list[2][1]:2} ] [ {list[2][2]:2} ]\n")
