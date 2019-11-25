"""
 Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def vote(born_year):
    from datetime import datetime
    if datetime.today().year - born_year < 18:
        return 'Voto negado'
    elif datetime.today().year - born_year >= 70:
        return 'Voto Opcional'
    else:
        return 'Voto Obrigatório'


born = int(input('Em que ano você nasceu? '))
print(vote(born))
