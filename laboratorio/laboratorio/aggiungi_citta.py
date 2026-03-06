import sqlite3

while True: 
    regione = input('Inserisci il nome della regione (q per uscire): ')
    if regione.lower() == 'q' :
        break
    capoluogo = input('Inserisci il nome della città capoluogo di regione: ')
    query = "insert into Regioni(regione_nome, capoluogo) values (?,?)"

    values = (regione, capoluogo)

    db = sqlite3.connect("Regioni.db")
    

    cursor = db.cursor()

    cursor.execute(query, values)

    db.commit()
    print(f"{regione} inserita con successo!")















