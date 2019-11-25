"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def factorial(num=0, show=False):
    """
    Keyword Arguments:
        num {int} -- [Numero a ser calculado] (default: {0})
        show {bool} -- [(Opcional) Mostra a conta] (default: {False})
    """
    multiplier = 1

    for n in range(num, 0, -1):
        multiplier *= n
        if show:
            print(f'{n}', end=' x ' if n > 1 else ' = ')

    return multiplier


help(factorial)
print(factorial(5, show=True))
