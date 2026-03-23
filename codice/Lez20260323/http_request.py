"""Gestione di richieste http"""

import requests
from film import Film 

URL = 'https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/imdb_top_2000_movies.json'

risposta = requests.get(URL)

if risposta.status_code == 200:
    oggetto_pitonico = risposta.json()
    for movie in oggetto_pitonico:
        title = movie['Movie Name']
        director = movie['Director']
        year = movie['Release Year']
        rating = movie['IMDB Rating']
        f = Film(title, director, year, rating)
        print(f)
