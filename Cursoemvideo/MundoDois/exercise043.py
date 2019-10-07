'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
* O cálculo do IMC é feito dividindo o peso pela altura ao quadrado
'''

weght = float(input('Digite o peso (Kg): '))
height = float(input('Digite a altura (m): '))
imc = weght / (height ** 2)

print(f'O IMC dessa pessoa é de \033[1;34m{imc:.1f}\033[m')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com o peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')
