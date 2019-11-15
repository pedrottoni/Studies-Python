"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
import datetime

person = {
    'Nome': True,
    'Ano de nascimento': True,
    'Idade': True,
    'Carteira de trabalho': True,
    'Ano de contratação': True,
    'Salário': True,
    'Aposentadoria': True
}
work_card = False

for items in person:
    if items != 'Idade' and items != 'Aposentadoria':
        person[items] = input(
            f'{items}{" - Pular [0]" if items == "Carteira de trabalho" else ""}: '
        )
    if person['Carteira de trabalho'] == '0':
        break

person['Idade'] = datetime.datetime.today(
).year - int(person['Ano de nascimento'])
person['Aposentadoria'] = int(person['Idade']) + (
    int(person['Ano de contratação']) + 35) - datetime.datetime.now().year

print('=○='*10)

for k, v in person.items():
    print(f'{k}: {v}')
    if k == 'Carteira de trabalho' and v == '0':
        break

print('=○='*10)
print(person)
