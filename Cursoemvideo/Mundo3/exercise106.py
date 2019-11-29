"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""
colors = (
    '\033[m',         # Defaut
    '\033[0;30;41m',  # red
    '\033[0;30;42m',  # green
    '\033[0;30;43m',  # yellow
    '\033[0;30;44m'   # blue
)


def custom_help(py_command):
    print(colors[2])
    help(py_command)
    print(colors[0])


def title(msg, color):
    print(colors[color])
    print(f'\n {msg} \n')


def interface():
    py_command = input('Digite um comando: ')
    title('Sistema de ajuda', 4)
    while py_command != 'fim':
        custom_help(py_command)
        py_command = input('Digite um comando: ').lower()
    title('Fim do dia', 1)
    print(colors[0])


interface()
