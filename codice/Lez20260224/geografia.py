""" Regioni italiane """

regioni = {
    "Piemonte" : ["Torino", "Cuneo", "Asti", "Alessandria"],
    "Liguria"  : ["Genova", "Savona", "Imperia", "La Spezia"]
}

# print(help(regioni))

chiavi = regioni.keys()
valori = regioni.values()

# for chiave in chiavi:
#     print(chiave)
#     print(regioni.get(chiave))

for regione, comuni in regioni.items():
    print(f"La regione {regione} ha i seguenti comuni capoluogo di provincia {comuni}")

