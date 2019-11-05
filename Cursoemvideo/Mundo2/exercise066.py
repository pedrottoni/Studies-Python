"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
sum = values = 0

while True:
    number = int(input('Digite um numero para somar ou [999] para parar: '))
    if number == 999:
        break
    sum += number
    values += 1

print(f'A soma dos {values} valores é igual a {sum}')
