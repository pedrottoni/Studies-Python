# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
''' km | hm | dam | m | dm | cm | mm '''

distancia = float(input("Digite uma distância em metros:"))
quilometros = distancia / 1000
hectometros = distancia / 100
decametros = distancia / 10
decimetros = distancia * 10
centimetros = distancia * 100
milimetros = distancia * 1000

plural = "equivale"

if distancia > 1:
    plural = "equivalem"

print(f"{distancia}m {plural} a:\n{quilometros}km\n{hectometros}hm\n{decametros}dam\n{decimetros}dm\n{centimetros}cm\n{milimetros}mm")
