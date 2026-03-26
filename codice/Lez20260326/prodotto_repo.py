from connessione import Connessione

class ProdottoRepo:

    def __init__(self):
        self.conn = Connessione()
        self.db = self.conn.connetti()
        self.cursor = self.db.cursor()

    def getProdotti(self):
        query = "SELECT nome, prezzo_unitario from Prodotti"
        self.cursor.execute(query)
        return self.cursor.fetchall()

