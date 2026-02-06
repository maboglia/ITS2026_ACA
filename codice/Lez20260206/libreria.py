
libri = [
    ['L\'uomo ragno', 120, 15, 2],
    ['La donna ragno', 150, 25, 2],
    ['Il bambino ragno', 220, 35, 2],
    ['L\'insetto verde', 80, 10, 1],
    ['L\'opossum grigio', 320, 45, 1]
]

f = open("database\insert_libri.sql", "w")

for libro in libri:
    titolo = str(libro[0]).replace("'", "\\'")  
    pagine = libro[1]
    prezzo = libro[2]
    editore_id = libro[3]
    f.write(f"INSERT INTO libri SET titolo = '{titolo}', pagine = {pagine}, prezzo = {prezzo}, editore_id = {editore_id};\n")

f.close()