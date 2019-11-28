"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""


def read_int(my_input):
    """[Recebe um parâmetro e só retorna o valor se for um número]

    Arguments:
        my_input {[type]} -- [Recebe um número de parâmetro]

    Returns:
        [type] -- [Se for um número, retorna o número]
    """
    int = input(my_input)
    while int.isnumeric() == False:
        print('\033[0;31mERRO!\033[m')
        int = input(my_input)
    return int


n = read_int('Digite um número: ')
print(f'Você digitou o número {n}')
