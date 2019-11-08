"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
from random import randint
from time import sleep

matrix = [int, int, int]
even = []
sum_third_column = 0

print("-"*45)
for line in range(0, 3):
    matrix[line] = [int, int, int]
    for colunm in range(0, 3):
        matrix[line][colunm] = randint(0, 99)
        print(
            f"Adicionando o número {matrix[line][colunm]:2} na posição: {line}/{colunm}")
        sleep(.3)
        if matrix[line][colunm] % 2 == 0:
            even.append(matrix[line][colunm])
        if colunm == 2:
            sum_third_column += matrix[line][colunm]

print("-"*45)
for line in range(0, 3):
    for colunm in range(0, 3):
        print(f"[ {matrix[line][colunm]:2} ]", end=' ')
    print()

print("-"*45)

print(
    f"A soma dos valores pares é: {sum(even)} \nA soma dos valores da terceira coluna é: {sum_third_column}\nO maior valor da segunda linha é: {max(matrix[1])}")
