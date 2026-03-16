import mysql.connector
from libro import Libro

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'biblioteca'
)

cursor = db.cursor()

cursor.execute("SELECT libroId, collocazione, autore, titolo, editore, classificazione FROM libri;")

libri = cursor.fetchall()

tabella_libri = []

for libroId, collocazione, autore, titolo, editore, classificazione in libri:
    # libroId = libro[0] 
    # collocazione = libro[1]
    # autore = libro[2]
    # titolo = libro[3]
    # editore = libro[4]
    # classificazione = libro[8]

    libro = Libro(libroId, collocazione, titolo, autore, editore, classificazione)
    tabella_libri.append(libro)
    # print(libro)