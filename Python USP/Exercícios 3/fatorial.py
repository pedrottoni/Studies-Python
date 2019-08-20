n = int(input("Digite o valor de n:"))
f = 1
prim = True

while (n > 1):
    if prim:        
        print (n, "*")
    f = f * n
    n = n - 1
    prim = False
    print (n, "*")

print(f)