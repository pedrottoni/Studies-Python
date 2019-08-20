def fatorial (x):
    f = 1
    while x > 0:
        f = f * x
        x -= 1
    return f

def binomial (n , k):
    return int(fatorial (n) / (fatorial (k) * fatorial (n - k)))
    
    
print (binomial (7 , 7))