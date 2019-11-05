"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

products = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00)
print(f"{'▼'*50}")

for i, product in enumerate(products):
    if i % 2 == 0:
        print(f"{products[i]:.<42}R${products[i+1]:>6.2f}")

print(f"{'▲'*50}")
