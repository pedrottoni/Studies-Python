'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

year = int(input('Digite o ano de nacimento: '))
age = datetime.datetime.now().year - year

print(f'Quem nasceu em {year} tem {age} anos em {age + year} ')

if age < 18:
    if 18 - age == 1:
        print(
            f'Falta apenas {18 - age} ano para o alistamento\nSeu alistamento será em {year + 18}')
    else:
        print(
            f'Ainda faltam {18 - age} anos para o alistamento\nSeu alistamento será em {year + 18}')
elif age > 18:
    if 18 - age == 1:
        print(
            f'Você já deveria ter se alistado há {age - 18} ano\nSeu alistamento foi em {year + 18}')
    else:
        print(
            f'Você já deveria ter se alistado há {age - 18} anos\nSeu alistamento foi em {year + 18}')
else:
    print(f'Você deve se alistar imediatamente! {year + 18}')
