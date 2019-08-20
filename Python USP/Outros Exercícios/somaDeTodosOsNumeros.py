i = int(input("Digite um numero "))
soma = 0

while (i > 0):
    soma = soma + (i % 10) 
    i = i//10

print("A soma dos numeros digitados é:",soma)