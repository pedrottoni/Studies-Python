'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
chosen_number = int(input('Digite um número: '))
is_prime = 0

for i in range(1, chosen_number + 1):
    if chosen_number % i == 0:
        print(f'\033[1;33m{i}\033[m', end=' ')
        is_prime += 1
    else:
        print(f'\033[1;31m{i}\033[m', end=' ')

print(f'\nO número {chosen_number} foi dividido {is_prime} vezes')

if is_prime > 2 or is_prime == 1:
    print(f'Ele não é um número primo')
else:
    print(f'Ele é número primo')
