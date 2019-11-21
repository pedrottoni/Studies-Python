"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from random import randint
from time import sleep


def higher(*n):
    print(f'Foram informados {len(n)} valores: ', end='')
    for i in n:
        print(i, end=' ', flush='True')
        sleep(.2)

    print(f'\nO maior valor foi: {max(n)}')


higher(2, 7, 6)
