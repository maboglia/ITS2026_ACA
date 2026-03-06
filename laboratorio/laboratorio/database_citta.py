
# import json

import sqlite3

regioni = {
    "Piemonte" : ["Torino", "Alessandria", "Asti"],
    "Lombardia" : ["Milano", "Como", "Pavese"],
    "Liguria" : ["Genova", "Savona", "Imperia", "Loano"],
    "Toscana" : ["Firenze", "Livorno", "Pisa"],
    "Veneto" : ["Venezia", "Verona", "Treviso"],
    
    # "Calabria" : {"Reggio Calabria"},
    # "Lazio" : ("Roma"),
    # "Campania" : "Napoli",
}

# stampa in json del record, puramente perché il formato è molto simile quindi la conversione non da errori 
# regionipy = json.dumps(regioni)

# regionijson = json.loads(regionipy)

# print(regionipy)
# print(regionijson)


db = sqlite3.connect("Regioni.db")
cursor = db.cursor()

cursor.execute('drop table if exists regioni;')



query = """
    CREATE TABLE if not exists Regioni (
        regione_id INTEGER primary key AUTOINCREMENT,
        regione_nome TEXT NOT NULL,
        capoluogo TEXT NOT NULL
        );
"""

cursor.execute(query)

for regione in regioni :
    query = f"insert into Regioni (regione_nome, capoluogo) VALUES ('{regione}','{regioni.get(regione)[0]}');"
    cursor.execute(query)



db.commit()

item = (1,2,3,4,5,6,7,8,9)

for i in item :
    print("AURA")



