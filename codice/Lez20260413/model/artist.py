
class Artist(object):

    casa_discografica = "ACA Sound Top Records"

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    
    def __str__(self):
        return f"Artista {self.nome} etichetta: {Artist.casa_discografica}"
    
    def toTuple(self):
        return (self.nome, Artist.casa_discografica)
    
    def toDict(self):
        return {"nome": self.nome, "etichetta":Artist.casa_discografica}
    
    def toHtmlTable(self):
        return f"<tr><td>{self.nome}</td><td>{Artist.casa_discografica}</td><td>Profilo</td></tr>"
    
    def toHtmlListItem(self):
        return f"<li>{self.nome} - {Artist.casa_discografica}</li>"
