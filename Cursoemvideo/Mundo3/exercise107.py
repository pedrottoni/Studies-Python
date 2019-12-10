"""
P1
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
P2
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

"""
from Modules import coin

number = str(input('Digite um valor: R$'))

print(
    f'A metade de {coin.coin(number)} é: {coin.coin(coin.half(coin.string_to_float(number)))}\nO dobro de {coin.coin(number)} é {coin.coin(coin.double(coin.string_to_float(number)))}\nAumentando 10%, temos {coin.coin(coin.increase(coin.string_to_float(number)))}\nDiminuindo 10%, temos {coin.coin(coin.decrease(coin.string_to_float(number)))}')
