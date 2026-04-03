import mysql.connector
from dataclasses import dataclass

@dataclass
class Prodotto:
    nome: str
    prezzo: float
    giacenza: int

magazzino = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    password = 'root',
    database = 'magazzino'
)

cursore = magazzino.cursor()

query = "select nome, prezzo_unitario, quantita_stock from Prodotti"

cursore.execute(query)

prodotti = cursore.fetchall()

lista_prodotti = [Prodotto(n, p, q)  for n, p, q in prodotti ]

cursore.close()
magazzino.close()