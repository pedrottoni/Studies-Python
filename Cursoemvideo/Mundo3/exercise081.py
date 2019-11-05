"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
list = []

while True:
    number = int(input("Digite um valor: "))
    list.append(number)
    keep = str(input("Deseja acrescentar mais um número? [S|N] ")).upper()[0]
    while keep not in "SN":
        keep = str(
            input("Deseja acrescentar mais um número? [S|N] ")).upper()[0]
    if keep == "N":
        list.sort(reverse=True)
        print(
            f"Você digitou {len(list)} números.\nOs valores em ordem decrescente são? {list}")
        if 5 in list:
            print(f"O número 5 faz parte da sua lista")
        break
