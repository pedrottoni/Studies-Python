'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
Com o for e com o while
'''
number = int(input('Digite um número para calcular o fatorial: '))
multiplier = number
factorial = 1

if -1 < number < 2:
    print(f'O fatorial de {number} é 1')

else:
    while multiplier > 0:
        print(f'{multiplier}', 'x ' if multiplier > 1 else '= ', end='')
        factorial *= multiplier
        multiplier -= 1

    print(factorial)

    multiplier = number
    factorial = 1

    for i in range(factorial, number + 1):
        factorial *= i
        print(f'{multiplier}', 'x ' if multiplier > 1 else '= ', end='')
        multiplier -= 1

    print(factorial)
