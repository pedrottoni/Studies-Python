'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint

computer_number = randint(0, 10)
player_number = -1
attempts = 1

print(f'Acabei de pensar em um número entre 0 e 10.\n')

while computer_number != player_number:
    player_number = int(input('Qual é seu palpite? '))
    while player_number > 10:
        player_number = int(
            input('Palpite inválido, digite um número de 0 a 10: ')
        )
    if player_number > computer_number:
        print('Menos...')
        attempts += 1
    if player_number < computer_number:
        print('Mais...')
        attempts += 1


print(f'Acertou com {attempts} tentativas!')
