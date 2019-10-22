"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

first_term = int(input('Digite o primeiro termo: '))
ratio = int(input('Digite a razão da PA: '))
counter = 0
terms = 10
total_counters = 0

while terms != 0:
    while counter < terms:
        print(f'{first_term} ► ', end='')
        first_term += ratio
        counter += 1
        total_counters += 1
    print('PAUSA')
    terms = int(input(f'\nQuantos termos você quer mostrar a mais? '))
    counter = 0

print(f'Progressão finalizada com {total_counters} termos')
