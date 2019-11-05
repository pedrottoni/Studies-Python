primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

number = int(input(
    "Escolha um númer ona lista: \n [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"))
while number > primes[len(primes)-1]:
    number = int(input(
        "Escolha um númer ona lista: \n [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]\n"))

min = 0
max = len(primes)-1
f = True

while primes[f] != number:
    f = int((min + max) / 2)
    print(primes[f])
    if primes[f] < number:
        min = f + 1
    elif primes[f] > number:
        max = f - 1
    else:
        print(f"O número {number} está na posição {primes.index(number)}")
    if max < min:
        print("O número não está na lista")
        break
