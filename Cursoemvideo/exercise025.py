'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
full_name = str(input('Qual é seu nome completo? ')).lower()
print('Seu nome tem Silva:', 'silva' in full_name)
