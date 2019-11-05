"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
list = []
even = []
odd = []

while len(list) < 5:
    print(len(list))
    number = int(input("Digite um número: "))
    list.append(number)
    keep = str(input("Deseja acrescentar outro número? [S|N] ")).upper()
    if len(list) < 4:
        while keep not in "SN":
            keep = str(
                input("Deseja acrescentar outro número? [S|N] ")).upper()
        if keep == "N":
            break

for element in list:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)


print(
    f"A lista completa: {list}\nA lista de pares: {even}\nA lista de impares: {odd}")
