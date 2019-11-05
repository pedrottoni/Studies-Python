"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
max_min_list = []

for i in range(0, 5):
    max_min_list.append(int(input(f"Digite um número para a posição {i+1}: ")))

max_number = max(max_min_list)
min_number = min(max_min_list)
max_count = max_min_list.count(max(max_min_list))
min_count = max_min_list.count(min(max_min_list))

print(
    f"Você digitou os valores: {max_min_list}\nO maior número da lista foi: {max_number} na posição: ", end="")

for position, numbers in enumerate(max_min_list):
    if numbers == max_number:
        print(position, end=', ')

print(
    f"O menor número da lista foi: {min_number} na posição: ", end="")

for position, numbers in enumerate(max_min_list):
    if numbers == min_number:
        print(position, end=', ')
