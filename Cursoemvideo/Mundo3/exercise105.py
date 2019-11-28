"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""


def grade(*num, status=False):
    """
    [Analisa as notas e a situação da turma]

    Keyword Arguments:
        num {float} -- [Recebe as notas dos alunos]
        status {bool} -- [**Indica se deve adicionar a situação da turma] (default: {False})

    Returns:
        [type] -- [Retorna o dicionário criado]
    """
    grades = {}
    grades = {
        'Quantidade': len(num),
        'Maior nota': max(num),
        'Menor nota': min(num),
        'Média': sum(num) / len(num),
    }
    if status:
        if grades['Média'] > 7:
            grades['Situação'] = 'Exelente'
        elif grades['Média'] < 5:
            grades['Situação'] = 'Péssimo'
        else:
            grades['Situação'] = 'Médio'
    return grades


help(grade)
print(grade(3.5, 1.5, 10, 3.5, status=True))
