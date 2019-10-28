"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
flag = sum = numbers = 0

while flag != 999:
    sum += flag
    flag = int(input('Digite um número para somar ou [999] para parar: '))
    numbers += 1

print(f'Você digitou {numbers - 1} números e a soma entre eles é: {sum}')
