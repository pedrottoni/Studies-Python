'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo(sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''
name = str(input("Digite seu nome completo: "))
name_up = name.upper()
name_low = name.lower()
name_len_replace = len(name.replace(" ", ""))
name_len_count = len(name) - name.count(" ")
name_firstname_len_split = name.split()
name_firstname_len_find = name.find(" ")

print(
    f"Seu nome em letras maiúsculas é: {name_up}\nSeu nome em letras minúsculas é: {name_low}\nSeu nome sem espaçoes possui {name_len_replace} letras, usando o replace\nSeu nome sem espaçoes possui {name_len_count} letras, usando o count\nSeu primeiro nome possui {len(name_firstname_len_split[0])} letras, usando o split\nSeu primeiro nome possui {name_firstname_len_find} letras, usando o find"
)
