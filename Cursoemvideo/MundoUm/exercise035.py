'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
* Para ser um triangulo, a soma das medidas dos três ângulos internos deve ser igual a 180 graus
'''

first_line = float(input('Primeiro segmento: '))
second_line = float(input('Segundo segmento: '))
third_line = float(input('Terceiro segmento: '))

if first_line < (second_line + third_line) and second_line < (first_line + third_line) and third_line < (first_line + second_line):
    print(f'{"-"*41}\n{"O segmento pode formar um triangulo":^41}\n{"-"*41}')
else:
    print(f'{"-"*41}\n{"O segmento não pode formar um triangulo":^41}\n{"-"*41}')
