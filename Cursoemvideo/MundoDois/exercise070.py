"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 
"""

amount = greater_thousand = cheapeast_product = 0
cheapeast_product_name = ''

while True:
    product = str(input('Nome do produto: '))
    # Recebe o preço e garante que ele seja um número
    price = input('Preço: ')
    while price.isnumeric() == False:
        price = input('Valor inválido\nPreço: ')
    price = float(price)
    # Faz o produto mais barato ser o primeiro se ele for igual a zero, caso não seja, verifica se o preço atual é menor do que o valor mais barato recebido
    if cheapeast_product == 0:
        cheapeast_product = price
    if price < cheapeast_product:
        cheapeast_product = price
        cheapeast_product_name = product
    # Verifica se o preço é maior que 1000, caso for, acrescenta um produto na contagem dos maiores que 1000
    if price > 1000:
        greater_thousand += 1
    # Calcula o valor total da compra
    amount += price
    keep = str(input('Deseja continuar? [S|N]')).upper().strip()
    while len(keep) > 1 or keep not in 'SN':
        keep = str(
            input('Valor inválido\nDeseja continuar? [S|N]')).upper().strip()
    if keep == 'N':
        break

print(f'O total da compra foi: R${amount:.2f}\nProdutos que custaram mais de 1000: {greater_thousand}\nO produto mais barato foi {cheapeast_product_name} que custou R${cheapeast_product:.2f} ')
