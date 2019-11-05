'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
average_age = 0
old_man_name = ''
old_man_age = 0
women_under_twenty = 0

for i in range(1, 5):
    print(f'{"-"*5} {i}ª Pessoa {"-"*5}')
    name = str(input('Nome: ').title())
    age = int(input(f'Idade: '))
    sex = str(input(f'Sexo [M/F]: ').upper())
    average_age += age

    if sex == 'M':
        if age > old_man_age:
            old_man_age = age
            old_man_name = name
    if sex == 'F':
        if age < 20:
            women_under_twenty += 1

print(
    f'\nA média de idade do grupo é de {average_age/4} anos.\nO homem mais velho do grupo tem {old_man_age} anos e se chama {old_man_name}.\nNumero de mulheres com menos de 20 anos: {women_under_twenty}'
)
