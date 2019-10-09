'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep


print(f'{"•○•○•"*10}\n{"JOKENPO":^50}\n{"•○•○•"*10}')


player_choice_number = int(input(
    'Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nQual é sua jogada? ')
)

if player_choice_number == 0:
    player_choice = 'PEDRA'
elif player_choice_number == 1:
    player_choice = 'PAPEL'
elif player_choice_number == 2:
    player_choice = 'TESOURA'
else:
    player_choice = 'OPÇÃO INVÁLIDA'


computer_choice_number = randint(0, 2)

if computer_choice_number == 0:
    computer_choice = 'PEDRA'
elif computer_choice_number == 1:
    computer_choice = 'PAPEL'
elif computer_choice_number == 2:
    computer_choice = 'TESOURA'


print('\nJO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO')
sleep(.5)

print(f'\n{"•○•○•"*10}\n{"O computador jogou: " + computer_choice:^50}\n{"Você jogou: " + player_choice:^50}\n{"•○•○•"*10}\n')

if player_choice_number == 0 and computer_choice_number == 1:
    print(f'{"VOCÊ PERDEU":^50}\n')
elif player_choice_number == 1 and computer_choice_number == 2:
    print(f'{"VOCÊ PERDEU":^50}\n')
elif player_choice_number == 2 and computer_choice_number == 0:
    print(f'{"VOCÊ PERDEU":^50}\n')
elif player_choice_number == computer_choice_number:
    print(f'{"EMPATE":^50}\n')
elif player_choice_number > 2:
    print(f'{"TENTE NOVAMENTE":^50}\n')
else:
    print(f'{"VOCÊ VENCEU":^50}\n')
