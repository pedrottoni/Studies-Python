def maior_primo(p) :
    d = 1
    cont = 0
    if p <= 1 :
        print("Não é primo")
    else:
        while d <= p :
            if p % d == 0 :            
                cont += 1
            d += 1
        if cont > 2 :
            while cont > 2 :
                d = 1            
                cont = 0                    
                p -= 1                
                while d <= p :
                    if p % d == 0 :
                        cont += 1
                    d += 1
            return (p)
        else :
            return (p)