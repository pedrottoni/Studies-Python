# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
price = float(input("Digite o preço do produto: R$"))

percentage = price - (price * 5 / 100)

print(f"O preço do produto com 5% de desconto é R${percentage:.2f}")
