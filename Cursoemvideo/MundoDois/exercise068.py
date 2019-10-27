"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print(
    f'{"○"*50}\n\033[1;32m{"Vamos Jogar Par ou Impar":^50}\033[m\n{"○"*50}')

sum = victory = defeat = 0

while True:
    even_or_odd = str(input('Par ou Impar? [P|I]: ')).upper()
    if even_or_odd == 'P' or even_or_odd == 'I':
        value = int(input('Diga o valor de 1 a 10: '))
        if value > 0 and value < 11:
            computer_value = int(randint(1, 10))
            sum = computer_value + value
            print(
                f'{"-"*50}\nVocê jogou {value} e o Computador jogou {computer_value}\nTotal: {sum}\n{"-"*50}'
            )
            if sum % 2 == 0 and even_or_odd == 'P' or sum % 2 != 0 and even_or_odd == 'I':
                victory += 1
                print('Venceu!')
            else:
                print('Perdeu')
                break
        else:
            print(f'Valor inválido')
    else:
        print(f'Valor inválido')
print(f'GAME OVER\nVocê venceu {victory} vezes')
