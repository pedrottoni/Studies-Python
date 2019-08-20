p = int(input("Digite um número inteiro:"))
cont = 0   
i = 1

while i <= p :
    if p % i == 0:         
        cont += 1                     
    i += 1

if cont > 2 :
    print("não primo")
else :
    print("primo")

