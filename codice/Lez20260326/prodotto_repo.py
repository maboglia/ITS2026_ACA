from connessione import Connessione
from prodotto import Prodotto

class ProdottoRepo:

    def __init__(self):
        self.conn = Connessione()
        self.db = self.conn.connetti()
        self.cursor = self.db.cursor(dictionary=True)

    def getProdotti(self):
        query = "SELECT nome, prezzo_unitario from Prodotti"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return [Prodotto(**row) for row in rows]

