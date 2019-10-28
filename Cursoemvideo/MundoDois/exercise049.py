'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
chosen_number = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{chosen_number} x {i:2} = {chosen_number * i}')
