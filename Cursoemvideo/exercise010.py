# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

wallet = float(input("Quanto dinheiro você tem na carteira? R$"))
dollar = 4.09
equivalent = wallet / dollar

print(f"Com R${wallet} você pode comprar US${equivalent:.2f}")
