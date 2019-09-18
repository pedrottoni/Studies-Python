'''
Faça um programa que leia um número de e mostre na tela cada um dos dígitos separados.
'''
number = int(input('Digite um número: '))  # Receive a number
unit_number = number // 1 % 10  # Returns the unit
dozen_number = number // 10 % 10  # Returns the dozen
hundred_number = number // 100 % 10  # Returns the hundred
thousands_number = number // 1000 % 10  # Returns the thousand

print(
    f'Unidade: {unit_number}\nDezena {dozen_number}\nCentena {hundred_number}\nMilhar {thousands_number}')
