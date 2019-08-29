# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** (1/2)
raizQuadradaPower = pow(numero, (1/2))

print(f"O dobro de {numero} é: {dobro}\nO triplo de {numero} é: {triplo}\nA raiz quadrada de {numero} é: {raizQuadrada:.2f}\nA raiz quadrada \'Power\' de {numero} é: {raizQuadradaPower:3f}'")
