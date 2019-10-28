'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
sum = 0
pair_numbers = 0

for i in range(0, 6):
    chosen_number = int(input(f'Digite o {i+1}º número: '))
    if chosen_number % 2 == 0:
        chosen_number = chosen_number + sum
        sum = chosen_number
        pair_numbers += 1

print(
    f'A soma de todos os {pair_numbers} números pares digitados é igual a: {chosen_number}'
)
