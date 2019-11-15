"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
player = {
    'Nome': input('Nome do Jogador: '),
    'Gols': []
}
games = int(input(f'Quantas partidas {player["Nome"]} jogou? '))
gols = 0

for p in range(0, games):
    player['Gols'].append(
        int(input(f'Quantos gols na {p + 1}ª partida? ')))
    gols += player['Gols'][p]

player['Total de Gols'] = gols

print('--'*28)
print(player)
print('--'*28)

for k, v in player.items():
    print(f'{k}: {v}')

print('--'*28)
print(f'{player["Nome"]} jogou {games} partidas.')

for p in range(0, games):
    print(f'Na partida {p + 1}, fez {player["Gols"][p]} Gols.')

print('--'*28)
