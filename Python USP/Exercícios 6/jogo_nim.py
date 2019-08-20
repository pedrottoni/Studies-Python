def main():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    modoJogo = int(input("1 - para jogar uma partida isolada 2 - para jogar um campeonato"))
    while modoJogo > 2 :
        print ("Voce escolheu um modo inválido")
        modoJogo = int(input("1 - para jogar uma partida isolada 2 - para jogar um campeonato"))
    if modoJogo == 1 :
        print ("Voce escolheu uma partida isolada")
        partida()
    if modoJogo == 2 :
        print ("Voce escolheu um campeonato!")
        rodada = 1
        placarComputador = 0
        placarJogador = 0
        while rodada <= 3 :
            print("**** Rodada",rodada, "****")
            rodada += 1
            if partida() == 1 :
                placarComputador += 1
            else:
                placarJogador += 1  
        print ("**** Final do campeonato! ****")
        print ("Placar: Você", placarJogador, "X", placarComputador, "Computador")

def partida() :
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    while m >= n :
        print ("Limite inválido")
        m = int(input("Limite de peças por jogada?"))
    if n % (m + 1) == 0 :
        print ("Voce começa!")
        while n > 0 :
            n = n - usuario_escolhe_jogada(n , m)
            if n == 1 :
                print ("Agora resta apenas uma peça no tabuleiro.")
            else :
                print ("Agora restam", n, "peças no tabuleiro.")
            if n == 0 :
                print ("Você ganhou!")
                vencedor = 2
                return vencedor
            n = n - computador_escolhe_jogada(n , m)
            if n == 1 :
                print ("Agora resta apenas uma peça no tabuleiro.")
            else :
                print ("Agora restam", n, "peças no tabuleiro.")
            if n == 0 :
                print ("Fim do jogo! O computador ganhou!")
                vencedor = 1
                return vencedor
    else :
        print ("Computador começa!")
        while n > 0 :
            n = n - computador_escolhe_jogada(n , m)
            if n == 1 :
                print ("Agora resta apenas uma peça no tabuleiro.")
            else :
                print ("Agora restam", n, "peças no tabuleiro.")
            if n == 0 :
                print ("Fim do jogo! O computador ganhou!")
                vencedor = 1
                return vencedor
            n = n - usuario_escolhe_jogada(n , m)
            if n == 1 :
                print ("Agora resta apenas uma peça no tabuleiro.")
            else :
                print ("Agora restam", n, "peças no tabuleiro.")
            if n == 0 :
                print ("Você ganhou!")
                vencedor = 2
                return vencedor

def computador_escolhe_jogada(n , m) :
    jogada = 1
    escolha = False
    if n - m < 0 :
        m = n
        escolha = True
        jogada = m
        if jogada == 1:
            print ("O computador tirou uma peça.")
        else:
            print ("O computador tirou", jogada, "peças.")
        return jogada
    while escolha == False or jogada < m :
        if (n - jogada) % (m + 1) == 0 :
            escolha = True   
            if jogada == 1:
                print ("O computador tirou uma peça.")
                return jogada
            else:
                print ("O computador tirou", jogada, "peças.")         
                return jogada
        if jogada == m :
            escolha = True    
            if jogada == 1:
                print ("O computador tirou uma peça.")
            else:
                print ("O computador tirou", jogada, "peças.")        
            return jogada
        else:
            jogada += 1

def usuario_escolhe_jogada(n , m) :
    jogada = int(input("Quantas peças você vai tirar?"))
    while jogada > m or jogada == 0 :
        print ("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar?"))
    if jogada == 1:
        print ("Você tirou uma peça.")
    else:
        print ("Você tirou", jogada, "peças.")  
    return jogada

main()