numero = int(input("Digite um numero: "))
buzz = numero % 5 == 0

if (buzz):
    print("Buzz")
else:
    print(numero)