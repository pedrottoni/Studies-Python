'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
distance = float(input('Qual é a distância da viagem? '))

print(f'Você está prestes a iniciar uma viagem de {distance}Km')


if distance > 200:
    print(
        f'Com 0 if padrão:\nO preço da passagem será de R${distance * 0.45:.2f}')
else:
    print(f'O preço da passagem será de R${distance * 0.50:.2f}')


print(
    f'Com o if inline:\nO preço da passagem será de R${distance * 0.45:.2f}') if distance > 200 else print(f'O preço da passagem será de R${distance * 0.50:.2f}')
