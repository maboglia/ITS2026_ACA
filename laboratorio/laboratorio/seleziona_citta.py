import sqlite3

query = "select * from Regioni;"
db = sqlite3.connect("Regioni.db")

cursor = db.cursor()

cursor.execute(query)

result = cursor.fetchall()

for riga in result:
    print(f"Il capoluogo della regione {riga[1]} è: {riga[2]}")