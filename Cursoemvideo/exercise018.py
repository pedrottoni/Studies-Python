# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
SENO = cateto oposto / hipotenuza
COSSENO = cateto adjacente / hipotenuza
TANGENTE = cateto oposto / cateto adjacente
'''
from math import sin, cos, tan, radians

angle = float(input("Digite o angulo que você deseja "))

print(f"O SENO de {angle}º é: {sin(radians(angle)):.2f}\nO COSSENO de {angle}º é {cos(radians(angle)):.2f}\nA TANGENTE de {angle}º é: {tan(radians(angle)):.2f}  ")
