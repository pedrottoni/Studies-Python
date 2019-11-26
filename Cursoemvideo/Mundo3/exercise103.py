"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def record(name='Desconhecido', goals=0):
    """[summary]

    Keyword Arguments:
        name {str} -- [Recebe o Nome do jogador] (default: {'Desconhecido'})
        goals {int} -- [Recebe a quantidade de gols] (default: {0})

    Returns:
        [type] -- [Retorna uma frase com o nome do jogador e a quantidade de gols]
    """

    rec_name = str(input('Nome do jogador: '))
    rec_goals = str(input('Gols: '))
    if rec_name and rec_name.isalpha():
        name = rec_name
    if rec_goals and rec_goals.isnumeric():
        goals = rec_goals
    return f'O jogador {name} fez {goals} gols'


print(record())
