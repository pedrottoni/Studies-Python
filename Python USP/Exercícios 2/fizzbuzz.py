numero = int(input("Digite um numero: "))
Fizz = numero % 3 == 0
Buzz = numero % 5 == 0

if (Fizz and Buzz):
    print("FizzBuzz")
else:
    print(numero)