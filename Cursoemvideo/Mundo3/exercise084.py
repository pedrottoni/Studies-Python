"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
from random import randint

list = [[], []]

for number in range(0, 7):
    number = randint(0, 10)
    if number % 2 == 0:
        list[0].append(number)
        list[0].sort()
    else:
        list[1].append(number)
        list[1].sort()

print(list)
