
# unpacking

class Studente:
    def __init__(self, nome, cognome, valutazione):
        self.nome = nome
        self.cognome = cognome
        self.valutazione = valutazione


# list
studenti = list()



nome, cognome, valutazione = ['Pietro', 'Rossi', 28]

studenti.append(Studente(nome, cognome, valutazione))



