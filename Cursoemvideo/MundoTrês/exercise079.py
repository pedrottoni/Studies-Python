"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
"""
list = []
keep = ""
while True:
    chosen_number = int(input("Digite um número: "))
    if chosen_number not in list:
        list.append(chosen_number)
    else:
        print("Não é possivel adicionar valores duplicados")
    keep = str(input("Deseja adicionar mais um valor? [S|N] ")).upper()
    if keep == "N":
        list.sort()
        break

print(list)
