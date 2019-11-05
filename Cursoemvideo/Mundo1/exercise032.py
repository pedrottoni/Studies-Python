'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
import datetime

year = int(input('Digite o ano: '))

if year == 0:
    year = datetime.datetime.now().year

if year % 4 == 0 and year % 100 != 0 or year % 4 != 0 and year % 400 == 0:
    print(f'O ano {year} é BISSEXTO')
else:
    print(f'O ano {year} não é BISSEXTO')
