n = int(input("Digite um número inteiro:"))
igual = int

while (n >= 0) :
    if n % 10 == igual : 
        print("sim")
        break  
    else:
        igual = n % 10          
    n = n // 10
    if n <= 0 :
        print("não")
        break        
