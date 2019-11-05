'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

first_term = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão da PA: '))
counter = 0

while counter < 10:
    print(f'{first_term} ► ', end='')
    first_term += ratio
    counter += 1
print('FIM')
