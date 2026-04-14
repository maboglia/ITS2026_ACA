from model.artist import Artist


class Album:

    def __init__(self, id: int, titolo: str, artista: Artist):
        self.id = id
        self.titolo = titolo
        self.artista = artista
    