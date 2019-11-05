# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um número para ver sua tabuada:"))

print("-"*10,
      f"\n{numero} x {1:>2} = {numero * 1}\n{numero} x {2:>2} = {numero * 2}\n{numero} x {3:>2} = {numero * 3}\n{numero} x {5:>2} = {numero * 4}\n{numero} x {5:>2} = {numero * 5}\n{numero} x {6:>2} = {numero * 6}\n{numero} x {7:>2} = {numero * 7}\n{numero} x {8:>2} = {numero * 8}\n{numero} x {9:>2} = {numero * 9}\n{numero} x {10:>2} = {numero * 10}\n", "-"*10)
