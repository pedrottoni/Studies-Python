"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""
n = int(input('Digite quantos termos da sequência Fibonacci você gostaria de visualizar: '))

previous = -1
next = 1
result = 0
count = 0

while count < n:
    result = next + previous
    print(f'{result} → ', end='')
    previous = next
    next = result
    count += 1

print('FIM')
