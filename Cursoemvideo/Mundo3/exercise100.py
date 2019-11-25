"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""
from random import randint
from time import sleep


def draw():
    numbers = []
    even = []

    def sum_even(list):
        if numbers[n] % 2 == 0:
            list.append(numbers[n])
        if len(numbers) == 5:
            print('Resultado: ', end="", flush=True)
            sleep(.5)
            print(sum(even))

    print(f'Sorteando valores da lista: ', end="")

    for n in range(0, 5):
        numbers.append(randint(0, 10))
        print(numbers[n], end=" ", flush=True)
        sleep(.2)
        sum_even(even)


draw()
