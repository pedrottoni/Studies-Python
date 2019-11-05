# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

rentedDays = int(input("Por quantos dias o carro foi alugado? "))
kmTraveled = float(input("Quantos quilometros foram percorridos? "))

dayPrice = rentedDays * 60
kmPrice = kmTraveled * 0.15

print(f"O total a pagar é: R${dayPrice + kmPrice:.2f}")
