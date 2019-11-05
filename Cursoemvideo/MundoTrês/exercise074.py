"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

numbers = randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10)
lower = highest = 0

print('Os números sorteados foram: ', end="")
# Usando o 'for'
for i in range(0, 5):
    if lower == 0:
        lower = numbers[i]
    if numbers[i] < lower:
        lower = numbers[i]
    if numbers[i] > highest:
        highest = numbers[i]
    print(numbers[i], end=" ")

print(
    f'\n\nO menor número sorteado foi: {lower}\nO maior número sorteado foi: {highest}')

# Usando o 'min max'
lower = min(numbers)
highest = max(numbers)

print(
    f'\nO menor número sorteado foi: {lower}\nO maior número sorteado foi: {highest}')
