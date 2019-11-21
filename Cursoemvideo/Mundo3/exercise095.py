"""
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
players = []
player = len(players) - 1
option = True

while True:
    option = str(
        input('Novo jogador: [1] - Ver dados: [2] - Sair: [0]\nEscolha: '))
    if option == '1':
        players.append({'Nome': str(input('Jogador: '))})
        players[player]['Partidas'] = int(
            input(f'Quantas partidas {players[player]["Nome"]} jogou? '))
        players[player]['Gols'] = []
        for p in range(0, players[player]['Partidas']):
            players[player]['Gols'].append(
                int(input(f'Gols na {p+1}ª partida: ')))
        total = 0
        for g in players[player]['Gols']:
            total += g
        players[player]['Total'] = total
    if option == '2':
        print(players)
        print(f'{"*"*58}\n{"COD":5}{"NOME":15}{"GOLS":30}{"TOTAL":10}\n{"-"*58}')
        for l in players:
            print(
                f'{str(players.index(l)):5}{l["Nome"]:15}{str(l["Gols"]):25}{l["Total"]:>10}')
        while True:
            option = str(
                input('Digite o COD do jogador para ver detalhes ou [X] para voltar: ').upper())
            if str(option) == 'X':
                break
            print(f'Detalhes do jogador {players[int(option)]["Nome"]}')
            for p, g in enumerate(players[player]['Gols']):
                print(f'No {p + 1}º jogo, {g}')
    if option == '0':
        break
