'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

first_line = float(input('Primeiro segmento: '))
second_line = float(input('Segundo segmento: '))
third_line = float(input('Terceiro segmento: '))

if first_line < (second_line + third_line) and second_line < (first_line + third_line) and third_line < (first_line + second_line):
    print(f'{"-"*41}\n{"O segmento pode formar um triangulo: "}', end='')
    if first_line == second_line == third_line:
        print('EQUILÁTERO')
    elif first_line == second_line and first_line != third_line or first_line == third_line and first_line != second_line or second_line == third_line and first_line != second_line:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
    print(f'{"-"*41}')
else:
    print('O segmento não pode formar um triangulo')
