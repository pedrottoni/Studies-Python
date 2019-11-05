'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print(f'{"•"*50}\n{"Lojas GUanabara":^50}\n{"•"*50}')

product_price = float(input('Preço do produto: R$'))

print('Formas de pagamento:')

payment = int(
    input('[ 1 ] à vista\n[ 2 ] à vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\nEscolha a  forma de pagamento: '))

if payment == 1:
    print(
        f'Pagando à vista, você recebe 10% de desconto e sua compra sairá por R${product_price - (10 / 100) * product_price:.2f}')
elif payment == 2:
    print(
        f'Pagando à vista no cartão, você recebe 5% de desconto e sua compra sairá por R${product_price - (5 / 100) * product_price:.2f}')
elif payment == 3:
    print(
        f'Sua compra será parcelada em 2x de R${product_price / 2:.2f} sem juros no cartão')
else:
    parcel = int(input('Quantas parcelas: '))
    print(
        f'Sua compra será parcelada em {parcel}x vezes de {(product_price + (20 / 100) * product_price) / parcel:.2f}\nO preço final do produto será de {product_price + (20 / 100) * product_price:.2f}')

print('\n{:•^50}\n'.format('VOLTE SEMPRE!'))
