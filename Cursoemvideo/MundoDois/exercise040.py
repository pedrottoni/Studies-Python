'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO - Vermelho
- Média entre 5.0 e 6.9: RECUPERAÇÃO - Amarelo
- Média 7.0 ou superior: APROVADO - Verde

Use o código ANSI para aplicar as cores de acordo com a média
'''
# Cores
style = [0, 1]
color = {'approved': 32, 'recovery': 33, 'fail': 31}

first_grade = float(input('Primeira nota: '))
second_grade = float(input('Segunda nota: '))

average = (first_grade + second_grade) / 2

list = [first_grade, second_grade]

print("\nCriando uma lista com as notas:", list, "\nSomando as notas da lista:", sum(
    list), "\nDividindo pela quantidade de notas:", len(list), "\nTirando a media:", sum(list) / len(list))

if average >= 6.9:
    print(
        f'\nA média é:\033[{style[1]};{color["approved"]}m {average:.1f}\033[m\nO aluno está\033[{style[1]};{color["approved"]}m aprovado\033[m'
    )
elif 7 > average >= 5:
    print(
        f'\nA média é:\033[{style[1]};{color["recovery"]}m {average:.1f}\033[m\nO aluno está de\033[{style[1]};{color["recovery"]}m recuperação\033[m')
else:
    print(
        f'\nA média é:\033[{style[0]};{color["fail"]}m {average:.1f}\033[m \nO aluno está\033[{style[0]};{color["fail"]}m reprovado\033[m')
