"""App per processare file JSON"""

import json


istruzioni_insert = []

# prendo i dati e li trasformo e li ricolleziono
with open('games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)
    for game in games:
        nome = str(game.get('Game', 'Nome gioco')).replace("'", "\\'")
        genere = game.get('Genre', 'Genere').replace("'", "\\'")
        publisher = game.get('Publisher').replace("'", "\\'")
        platform = game.get('Original platform(s)[a]').replace("'", "\\'")
        year = game.get('year', 0)
        year = int(year)


        istruzioni_insert.append(f"INSERT INTO games (nome, genere, publisher, platform, `year`) VALUES ('{nome}','{genere}','{publisher}','{platform}',{year});")

# preparo un file sql per inserire i dati su database

query_tabella = """
CREATE TABLE games (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100), 
    genere VARCHAR(100), 
    publisher VARCHAR(100), 
    platform VARCHAR(100), 
    year INT CHECK (year > 1960)
); 
"""

with open('games.sql', 'w', encoding='utf-8') as f:
    f.write(query_tabella)

    for istruzione in istruzioni_insert:
        f.write(istruzione)
        f.write('\n')

print("Elaborazione terminata")
print("TOP!!!")