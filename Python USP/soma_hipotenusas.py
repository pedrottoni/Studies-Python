def é_hipotenusa(h):
    c1 = 1
    c2 = 1
    while c1 < h:
        while c2 < h:    
            if h == ((c1**2) + (c2**2)) ** (1/2):
                return h                 
            else:                
                c2 += 1
        c2 = 1
        c1 += 1

def soma_hipotenusas(n):
    h = 1
    hipotenusa = 0
    while h <= n:
        if é_hipotenusa(h) != None:                        
            hipotenusa = é_hipotenusa(h) + hipotenusa
            h += 1    
        else:                 
            h += 1
    return hipotenusa