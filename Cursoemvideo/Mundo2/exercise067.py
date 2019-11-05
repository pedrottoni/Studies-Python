"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    multiplier = 0
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for multiplier in range(0, 10):
        multiplier += 1
        print(
            f'{"0" if num < 10 else ""}{num} X {"0" if multiplier < 10 else ""}{multiplier:2<} = {num * multiplier:2<}')
