"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
-----
age
men
women under 20
"""
over_eighteen = men = women_under_twenty = age = 0

print(f'{"Cadastre um pessoa":-^50}')

while True:
    if age == 0:
        age = input('Idade: ')
        while age.isnumeric() == False:
            age = input('Idade: ')
    age = int(age)
    if age > 0:
        sex = str(input('Sexo [M|F]: ')).upper().strip()
        while sex not in 'MF' or len(sex) > 1:
            sex = str(
                input(f'Opção invalida.\nSexo [M|F]: ')).upper().strip()
        if age > 18:
            over_eighteen += 1
        if sex == 'F':
            if age < 20:
                women_under_twenty += 1
        elif sex == 'M':
            men += 1
    keep = str(input('Deseja continuar? S|N: ')).upper().strip()
    while keep not in 'SN' or len(keep) > 1:
        keep = str(input(f'Opção invalida.\nDeseja continuar? S|N: ')
                   ).upper().strip()
    if keep == 'S':
        age = 0
    elif keep == 'N':
        break

print(
    f'Total de pessoas com mais de 18 anos: {over_eighteen}\nHomens: {men}\nMulheres menores de vinte anos: {women_under_twenty}')
