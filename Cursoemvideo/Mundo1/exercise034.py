'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
salary = float(input('Digite o salário do funcionário: '))

if salary > 1250:
    print(
        f'Quem ganhava R${salary}, passa a ganhar R${(10 / 100)*salary + salary :.2f}'
    )

else:
    print(
        f'Quem ganhava R${salary}, passa a ganhar R${(15 / 100)*salary + salary :.2f}'
    )
