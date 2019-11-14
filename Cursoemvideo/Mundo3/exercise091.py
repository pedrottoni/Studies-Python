"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

O jogador "X" tirou "Y"
...
--------
1º Lugar: Jogador "X" com "Y" pontos
...
"""
from random import randint
from time import sleep
from operator import itemgetter

game = {}
podium = {}
podium_itemgetter = {}

for p in range(0, 4):
    game["Jogador "+str(p+1)] = randint(1, 6)

print("-=-"*10)

for k, v in game.items():
    print(f"O {k} tirou {v}")
    sleep(.3)

# Com o "itemgetter" - Transforma o Dict em lista
podium_itemgetter = dict(sorted(game.items(), key=itemgetter(1), reverse=True))

# Com "while" - Mantém o Dict
while len(game) > 0:
    for k, v in game.items():
        if max(game.values()) == v:
            podium[k] = v
            del game[k]
            break

print("-=-"*10)
print("Ranking:", podium)
print("Ranking:", podium_itemgetter)
print("-=-"*10)
