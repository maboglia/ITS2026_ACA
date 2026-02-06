
libri = []

source = open("database\libri.csv", 'r')

for riga in source:
    riga_splittata = riga.split(",")
    titolo = riga_splittata[0].replace('"', '')
    pagine = int(riga_splittata[2].replace('"', ''))
    prezzo = float(riga_splittata[4].replace('"', ''))
    print(f"Il libro {titolo} ha {pagine} pagine e costa €{prezzo}")
    # trovare una strategia per l'editore
    #aggiungiamo i dati di ciascun libro alla lista di libri
    libri.append([titolo, pagine, prezzo, 1])

source.close()

f = open("database\libri.html", "w")

f.write("<table>")
f.write("<tr><th>Titolo</th><th>pagine</th><th>prezzo</th></tr>")
for libro in libri:
    f.write("<tr>")
    titolo = str(libro[0]).replace("'", "\\'")  
    f.write(f"<td>{titolo}</td>")

    pagine = libro[1]
    f.write(f"<td>{pagine}</td>")

    prezzo = libro[2]
    f.write(f"<td>{prezzo}</td>")

    editore_id = libro[3]
    f.write("</tr>")


f.write("</table>")
f.close()

print("GAME OVER - Tutto liscio - TOP!")