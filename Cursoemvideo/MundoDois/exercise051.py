'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
an = a1 + (a - 1) * r
'''

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for i in range(0, 10):
    print(a1)
    a1 = a1 + r
