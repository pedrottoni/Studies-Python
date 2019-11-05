"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
count = 'zero', 'une', 'two', 'three', 'four', 'five', 'six,', 'secen', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
chosen_number = int(input('Digite um número entre 0 e 20: '))

while chosen_number < 0 or chosen_number > 20:
    chosen_number = int(
        input('Número inválido\nDigite um número entre 1 e 20: '))

print(count[chosen_number])
