"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def counter(start, stop, step):
    if step < 0:
        step *= -1
    print(f'{start} até {stop} de {step} em {step}')
    if start > stop:
        stop -= 1
        step *= -1
    else:
        stop += 1

    for n in range(start, stop, step):
        print(f'{n}', end=f' ', flush=True)
        sleep(.1)
    print()


counter(1, 10, 1)
counter(10, 0, 2)

user_start = int(input('Início: '))
user_stop = int(input('Fim: '))
user_step = int(input('Passo: '))

counter(user_start, user_stop, user_step)
