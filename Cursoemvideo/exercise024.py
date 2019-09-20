'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''
city = str(input("Digite o nome de uma cidade: ")).upper().split()

print('SANTO' in city[0])
