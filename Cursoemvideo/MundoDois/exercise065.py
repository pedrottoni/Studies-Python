"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
numbers = sum = highest = lower = 0
keep = True

while keep:
    chosen_number = float(input('Digite um número: '))
    sum += chosen_number
    if chosen_number > highest:
        highest = chosen_number
    if lower == 0:
        lower = chosen_number
    elif chosen_number < lower:
        lower = chosen_number
    numbers += 1
    keep = str(input('Deseja continuar? [S|N] ')).upper().strip()
    while keep not in 'SN':
        keep = str(
            input('Opção inválida.\nDeseja continuar? [S|N] ')).upper().strip()
    if keep == 'N':
        keep = False

print(f'Você digitou {numbers} números e a média entre eles é {sum / numbers}\nO maior valor foi {highest} e o menor valor foi {lower}')
