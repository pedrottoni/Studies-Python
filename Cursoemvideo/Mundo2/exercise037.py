'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''
number = int(input('Digite um número: '))

binary = bin(number)
octal = oct(number)
hexadecimal = hex(number)

choice = int(input(
    'Escolha uma das bases de conversão:\n[ 1 ] BINáRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL\nSua opção: ')
)

if choice == 1:
    print(binary[2:])
elif choice == 2:
    print(octal[2:])
else:
    print(hexadecimal[2:])
