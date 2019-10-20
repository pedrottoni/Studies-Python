'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
lower_weight = 0
higher_weight = 0

for i in range(1, 6):
  weight = float(input(f'Peso da {i}ª pessoa: '))
  if lower_weight == 0:
    lower_weight = weight
  if weight > higher_weight:
    higher_weight = weight
  if weight < lower_weight:
    lower_weight = weight
    
print(higher_weight, lower_weight)