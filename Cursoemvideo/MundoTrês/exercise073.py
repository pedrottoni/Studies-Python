"""
Crie uma tupla preenchida com os 10 jogos com mais jogadores no momento na Steam, em ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""
games = "Counter-Strike: Global Offensive", "Dota 2", "PLAYERUNKNOWN'S BATTLEGROUNDS", "Destiny 2", "Tom Clancy's Rainbow Six Siege", "Team Fortress 2", "Rocket League", "Grand Theft Auto V", "Rust", "Football Manager 2019"

top_five = games[0:5]
last_four = games[-4:]
alphabetical_order = sorted(games)
gta = games.index("Grand Theft Auto V")

print(f'{"◄☼►"*50}\nLista de jogos da Steam com mais jogadores no momento:\n{games}\n{"◄☼►"*50}\nOs cinco primeiro são:\n{top_five}\n{"◄☼►"*50}\nOs quatro ultimos:\n{last_four}\n{"◄☼►"*50}\nOs jogos em ordem alfabética:\n{alphabetical_order}\n{"◄☼►"*50}\nO GTAV está em {gta}º lugar')
