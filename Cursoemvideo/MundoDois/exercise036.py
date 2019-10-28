'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
house_price = float(input('Qual o valor da casa? '))
buyer_salary = float(input('Qual o salário do comprador? '))
years_paying = int(input('Quantos anos de financiamento? '))

monthly_installment = house_price / (years_paying * 12)
thirty_percent = 30 / 100 * buyer_salary

print(
    f'Para pagar uma casa de R${house_price:.2f} em {int(years_paying)} anos, a prestação será de R${monthly_installment:.2f}'
)

if monthly_installment <= thirty_percent:
    print('Emprestimno concedido')
else:
    print(f'Emprestimno negado')
