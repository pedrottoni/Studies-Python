'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''
# Comente as linhas da forma que você não dezeja visualizar

# Forma 1
userName = input('Digite seu nome:')
print('\033[7;37mBoas vindas,', userName.isalpha())

# Forma 2
userName = input('Digite seu nome:')
print('\033[1;31;43mBoas vindas, {}!\033[m'.format(userName))
