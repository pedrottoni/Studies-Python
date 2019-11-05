'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep

computer_number = int(random.uniform(0, 6))  # ou random.randint(0, 5)
player_number = int(
    input('Em que número pensei?\nEscolha um número de 0 a 5:')
)

print('PROCESSANDO...')
sleep(2)

if computer_number == player_number:
    print('Parabens, você acertou!!')
else:
    print(f'Errado, eu pensei no número {computer_number}')
