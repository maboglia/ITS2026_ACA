"""Regioni Italiane """

regioni ={
    "Piemonte" : ["Torino", "Cuneo", "Asti", "Alessandria"],
    "Liguria" : ["Genova", "Savona", "Imperia", "La Spezia"]
}

# print(help(regioni))
chiavi = regioni.keys()
valori = regioni.values()

# for chiavi in chiavi:
#     print(chiavi)
#     print(regioni.get(chiavi))

for regione, comuni in regioni.items():
    print(f"La regione {regione} ha i segueti comuni capoluogo di provincia {comuni}")