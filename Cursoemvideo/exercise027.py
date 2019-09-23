'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''
full_name = str(input('Digite seu nome completo: '))
full_name_divided = full_name.split()

print(
    f'Muito prazer em te conhecer {full_name}\nSeu primeiro nome é: {full_name_divided[0]}\nSeu ultimo nome é: {full_name_divided[-1]}')
