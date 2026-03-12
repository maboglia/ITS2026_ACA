'''Classe Libro, rappresenta un libro del database'''

class Libro:

    def __init__(self, libroId, collocazione, titolo, autore, editore, classificazione):
        self.libroId = libroId
        self.collocazione = collocazione
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.classificazione = classificazione

    def __str__(self):
        return f"""
            Titolo: {self.titolo}, 
            autore: {self.autore},
            editore: {self.editore},
            collocazione: {self.collocazione},
            """
    def toHtml(self):
        return f"""
            <div>
                <h2>Titolo: {self.titolo}</h2> 
                <h3>autore: {self.autore}</h3>
                <h4>editore: {self.editore}</h4>
                <h5>collocazione: {self.collocazione}</h5>
            </div>
            """
