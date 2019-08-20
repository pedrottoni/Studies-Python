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


while linha < h:
    while coluna < w:
        print("#", end = '')
        coluna += 1
    print("")
    coluna = 0
    linha += 1
