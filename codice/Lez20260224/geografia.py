<<<<<<< HEAD
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
=======
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
>>>>>>> 6946f19a7cc5421ce8fad76876fed9c3087c69d1
