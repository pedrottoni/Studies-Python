'''
Crie um programa que leia o ano de nascimento de cinco pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
import datetime

adulthood = 0
minority = 0

for i in range(1, 6):
    persona_year = int(input(f'Em que ano a {i} pessoa nasceu? '))
    if datetime.date.today().year - persona_year > 18:
        adulthood += 1
    else:
        minority += 1

print(
    f'\nAo todo temos:\n\033[1;35m{adulthood}\033[m maiores de idade\n\033[1;35m{minority}\033[m menores de idade'
)
