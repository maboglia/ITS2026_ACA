

# LISTA (1 elemento tra virgole, format : x,x,x,x,x,x)
cities = ["Torino", "Milano", "Roma", "Loano"]

# TUPLA : immutabile (1 elemento tra virgole, format : x,x,x,x,x,x)
# cities = ("Torino", "Milano", "Roma", "Loano")

# SET : filtra doppioni (1 elemento tra virgole, format : x,x,x,x,x,x)
# cities = {"Torino", "Milano", "Roma", "Loano", "Torino"}


# aggiungi a una lista
# cities.append("Genova")

# aggiungi a un set
# cities.add("Genova")


# collection (2 elemento tra virgole, format : xx,xx,xx,xx,xx,xx)
regioni = {
    "Piemonte" : ["Torino", "Alessandria", "Asti"],
    "Lombardia" : ["Milano", "Como", "Pavese"],
    "Liguria" : ["Genova", "Savona", "Imperia", "Loano"],
    "Toscana" : ["Firenze", "Livorno", "Pisa"],
    "Veneto" : ["Venezia", "Verona", "Treviso"],
    
    "Calabria" : {"Reggio Calabria"},
    "Lazio" : ("Roma"),

    "Campania" : "Napoli",
}

#  stampa
# print(regioni)

#  stampa il tipo
# print(type(regioni))

# # visualizza gli elementi con il dudermode
# print(dir(regioni))

# stessa funzione di dir(), visualizzi tipi elemento
# print(help(regioni))


# stampa gli oggetti in lista per ogni elemento "city" in "cities"
# for city in cities:
#     print(city)

# stampa gli oggetti in lista per ogni elemento "city" in "cities"
# for regione in regioni.items():
#     print(regione)

# stampa della collection con fromattazione in output
# for regione,comuni in regioni.items():
#     print(f"La regione {regione} ha i seguenti comuni {comuni}")

# for regione in regioni.keys():
#     print(f"La regione {regione} ha i seguenti comuni {regioni.get(regione, "regione sconosciuta")}")

# for regione in regioni.keys():
#     print(f"La regione {regione} ha i seguenti comuni {regioni[regione]}")

for regione in regioni.keys():
    print(f"La regione {regione} ha i seguenti comuni:")
    for comune in regioni.get(regione) : 
        print(comune)

    


