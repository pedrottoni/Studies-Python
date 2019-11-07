"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
user = []
users_list = []

higher_weight = True
higher_weight_users = []
lower_weight = True
lower_weight_users = []
choice = True
print(lower_weight)

while choice != "0":
    choice = input(
        f"{'-'*100}\n{users_list}\nAo todo você cadastrou: {len(users_list)} usuários\nCadastrar nova pessoa:[1]  Mostrar maior peso:[2] Mostrar menor peso:[3] Sair [0]\n{'-'*100}\nEscolha: ")

    if choice == "1":
        name = str(input("Nome: "))
        weight = float(input("Peso: "))
        user = [name, weight]
        users_list.append(user)

        if weight > higher_weight:
            higher_weight = weight
            higher_weight_users.clear()
            higher_weight_users.append(user[0])
        elif weight == higher_weight:
            higher_weight_users.append(user[0])

        if weight < lower_weight or lower_weight == True:
            lower_weight = weight
            lower_weight_users.clear()
            lower_weight_users.append(user[0])
        elif weight == lower_weight:
            lower_weight_users.append(user[0])

    elif choice == "2":
        print(
            f"Maior peso: {higher_weight}\nUsuários com o maior peso: {higher_weight_users}")

    elif choice == "3":
        print(
            f"Menor peso: {lower_weight}\nUsuários com o menor peso: {lower_weight_users}")
