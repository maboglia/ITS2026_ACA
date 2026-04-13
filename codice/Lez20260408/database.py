import mysql.connector

def connetti():
    DB = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "Chinook"
    )

    return DB

def interroga(DB, query):

    cursore = DB.cursor()
    cursore.execute(query)
    results = cursore.fetchall()
    cursore.close()
    return results

def disconnetti(DB):
    if DB:
        DB.close()
        print("Connessione chiusa con successo!")



def main():
    DB = connetti()
    if DB:
        print('connesso con successo')
        risultati_query = interroga(DB, "Employee")
        print(risultati_query)
        disconnetti(DB)
    else:
        print('Errore di connessione')



if __name__ == "__main__":
    main()

