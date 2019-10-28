'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
first_value = int(input('Primeiro número: '))
second_value = int(input('Segundo número: '))
third_value = int(input('Terceiro número: '))

if first_value > second_value and first_value > third_value:
    print('O primeiro número é o maior')
elif second_value > first_value and second_value > third_value:
    print('O segundo número é o maior')
elif third_value > first_value and third_value > second_value:
    print('O terceiro número é o maior')
else:
    print('Os três números são iguais')
