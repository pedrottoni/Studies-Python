# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

width = float(input("A parede tem quantos metros de largura?"))
height = float(input("A parede tem quantos metros de altura?"))

area = width * height
liter = area / 2

print(
    f"Sua parede tem a dimenção de {width}m x {height}m e sua área é de {area}m².\nPara pintar essa parede, você vai precisar de {liter}l de tinta")
