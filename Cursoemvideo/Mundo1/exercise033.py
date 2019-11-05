'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
first_value = int(input('Digite o primeiro valor: '))
second_value = int(input('Digite o segundo valor: '))
third_value = int(input('Digite o terceiro valor: '))

if first_value > second_value and first_value > third_value:
    print(f'O maior valor digitado foi: {first_value}')

if second_value > first_value and second_value > third_value:
    print(f'O maior valor digitado foi: {second_value}')

if third_value > first_value and third_value > second_value:
    print(f'O maior valor digitado foi: {third_value}')

if first_value < second_value and first_value < third_value:
    print(f'O menor valor digitado foi: {first_value}')

if second_value < first_value and second_value < third_value:
    print(f'O menor valor digitado foi: {second_value}')

if third_value < first_value and third_value < second_value:
    print(f'O menor valor digitado foi: {third_value}')
