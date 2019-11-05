"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
numbers_list = []

for i in range(0, 4):
    count = 0
    number = int(input("Digite um número para acrescentar a lista: "))
    if len(numbers_list) == 0:
        numbers_list.append(number)
    else:
        for position in range(0, len(numbers_list)):
            if number > numbers_list[position]:
                count += 1
        numbers_list.insert(count, number)
    print(f"O numero {number} foi inserido na posição: {count}")

print(numbers_list)
