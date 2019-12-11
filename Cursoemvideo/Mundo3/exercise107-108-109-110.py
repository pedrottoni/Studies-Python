"""
P1
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
P2
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
P3
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""
from Modules import coin

number = str(input('Digite um valor: R$'))

print(
    f'A metade de {coin.coin(number)} é: {coin.coin(coin.half(number))}\nO dobro de {coin.coin(number)} é {coin.coin(coin.double(number))}\nAumentando 10%, temos {coin.coin(coin.increase(number))}\nDiminuindo 10%, temos {coin.coin(coin.decrease(number))}')
