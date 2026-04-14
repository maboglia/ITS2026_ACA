import requests

class DiscoService:

    def getAllArtists(self):
        risposta = requests.get('http://127.0.0.1:5000/artists')

        return risposta.json()
    
    
