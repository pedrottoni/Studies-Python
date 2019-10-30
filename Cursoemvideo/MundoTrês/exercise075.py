"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
numbers = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(
    input('Digite mais um número: ')), int(input('Digite o ultimo número: ')))
pairs = 0

for i in numbers:
    if i % 2 == 0:
        pairs += 1

print(f'Você digitou os números: {numbers}')
if 9 in numbers:
    print(f'Quantas vezes o número 9 apareceu: {numbers.count(9)}')
if 3 in numbers:
    print(f'O primeiro valor 3 apareceu na posição: {numbers.index(3)+1}')
if pairs > 0:
    print(f'Quantidade de números pares: {pairs}')
