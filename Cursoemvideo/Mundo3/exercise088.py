"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

numbers = []
games = int(input("Quantos jogos devem ser sorteados? "))

for game in range(0, games):
    for number in range(0, 6):
        chosen_number = randint(1, 6)
        while chosen_number in numbers:
            chosen_number = randint(1, 6)
        numbers.append(chosen_number)
    sleep(.3)
    print(f"Jogo {game + 1}: {numbers}")
    numbers.clear()
