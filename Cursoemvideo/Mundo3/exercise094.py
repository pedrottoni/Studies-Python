"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
people = []
women = []
above_average = []
option = True

while True:
    option = str(
        input('Cadastrar usuário [1] - Relatório [2] - Sair [0]\nOpção: '))
    if option == '1':
        people.append({'Nome': input('Nome: ')})
        while True:
            people[len(people) - 1]['Sexo'] = str(input('Sexo [M|F]: ')).upper()
            if people[len(people) - 1]['Sexo'] == 'M' or people[len(people) - 1]['Sexo'] == 'F':
                break
        people[len(people) - 1]['Idade'] = int(input('Idade: '))
    elif option == '2':
        print(people)
        print(f'Pessoas cadastradas: {len(people)}')
        average = 0
        women.clear()
        above_average.clear()
        for p in people:
            average += p['Idade']
        print(f'A média de idade é de: {average / len(people): 5.2f}')
        for p in people:
            for k, v in p.items():
                if k == 'Sexo' and v == 'F':
                    women.append(p['Nome'])
        print(f'Mulheres cadastradas: {women if len(women) > 0 else "0"}')
        for p in people:
            for k, v in p.items():
                if k == 'Idade' and v >= average / len(people):
                    above_average.append(p)
        print(
            f'Pessoas acima da média de idade: {above_average if len(above_average) > 0 else "0"}')
    elif option == '0':
        break
    else:
        print('Opção inválida')
