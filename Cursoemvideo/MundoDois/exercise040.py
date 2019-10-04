'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

first_grade = float(input('Primeira nota: '))
second_grade = float(input('Segunda nota: '))

average = (first_grade + second_grade) / 2

if average >= 6.9:
    average = 10
    print(f'A média é: {average:.1f}\nO aluno está aprovado')
elif 7 > average >= 5:
    print(f'A média é: {average:.1f}\nO aluno está de recuperação')
else:
    print(f'A média é: {average:.1f}\nO aluno está reprovado')
