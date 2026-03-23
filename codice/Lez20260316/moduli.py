import requests


url = 'https://api.tvmaze.com/singlesearch/shows?q='

cerca = input("Scrivi il titolo di un tv-show: ")

risposta = requests.get(url + cerca)

if risposta.status_code == 200:
    show = risposta.json()
    
    titolo = show.get('name')
    rating = show.get('rating')
    image = show.get('image')

    print(titolo, rating['average'], image['medium'])        

        
