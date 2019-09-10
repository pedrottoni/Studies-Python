# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import floor, trunc

value = float(input("Digite um valor: "))

print(
    f"O valor digitado foi {value} e sua porção inteira é:\n Usando floor {floor(value)}\n Usando trunc {trunc(value)}\n Usando int {int(value)}")
