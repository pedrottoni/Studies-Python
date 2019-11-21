"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


def write(text):
    print(f'{"~~"*len(text)}\n{text:-^{len(text)+9}}\n{"~~"*len(text)}')


write('Olá mundo')
