'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

first_value = int(input('Digite o primeiro valor: '))
second_value = int(input('Digite o segundo valor: '))
option = 0

while option != 5:
    option = int(input(
        f'{"-=" *5}\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n{"-=" *5}\nQual é a sua opção? '))
    if option > 5 or option < 0:
        option = int(input(
            f'Opção Invalida.\n{"-=" *5}\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n{"-=" *5}\nQual é a sua opção? '))
    if option == 1:
        print(first_value + second_value)
    elif option == 2:
        print(first_value * second_value)
    elif option == 3:
        if first_value > second_value:
            print(first_value)
        else:
            print(second_value)
    elif option == 4:
        first_value = int(input('Digite o primeiro valor: '))
        second_value = int(input('Digite o segundo valor: '))

print('Volte sempre!')
