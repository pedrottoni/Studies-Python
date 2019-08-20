def n_primos(n):
    contador = 0
    divisor = 1
    i = 1
    primo = 0
    while divisor <= n:
        while i <= n:
            if divisor %  i == 0:
                contador += 1
            i += 1
        if contador == 2:
            primo += 1
        i = 1
        contador = 0
        divisor += 1   
    return (primo)

print (n_primos(90))