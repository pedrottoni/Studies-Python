w = int(input("digite a largura:"))
h = int(input("digite a altura:"))

while w < 0 or h < 0:
    if w < 0:
        print("Número inválido ")
        w = int(input("digite a largura:"))
    if h < 0:
        print("Número inválido ")
        h = int(input("digite a altura:"))

linha = 0
coluna = 0
bordaLinha = 1
bordaColuna = 1

while linha < h:
    if bordaColuna == 1 or bordaColuna == h:
        while coluna < w:
            print("#", end = '')
            coluna += 1
    else:
        print("#", end = '')
        coluna += 1
        while coluna > 0 and coluna < w-1:
            print(" ", end = '')
            coluna += 1
        print("#", end = '')
    print("")
    bordaColuna += 1
    coluna = 0
    linha += 1
