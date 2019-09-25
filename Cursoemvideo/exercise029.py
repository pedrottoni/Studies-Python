'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
from time import sleep

speed = float(input('Qual é a velocidade do carro? '))

print('Calculando\n...')
sleep(1.5)

if speed > 80:
    print(
        f'MULTADO! Você excedeu o limite de velocidade de 80km/h\nVocê deve pagar uma multa de R${(speed-80)*7:.2f}'
    )
else:
    print('Tenha um bom dia!! Dirija com segurança')
