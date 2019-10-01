# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
SENO = cateto oposto / hipotenuza
COSSENO = cateto adjacente / hipotenuza
TANGENTE = cateto oposto / cateto adjacente
'''
from math import sin, cos, tan, radians

angle = float(input("Digite o angulo que você deseja "))

print(f"O SENO de \033[4;32m{angle}º\033[m é: \033[4;32m{sin(radians(angle)):.2f}\033[m\nO COSSENO de \033[4;32m{angle}º\033[m é \033[4;32m{cos(radians(angle)):.2f}\033[m\nA TANGENTE de \033[4;32m{angle}º\033[m é: \033[4;32m{tan(radians(angle)):.2f}\033[m")
