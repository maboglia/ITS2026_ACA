""" Programma pitonico per gestire scontrini del bar """

menu = {
    "pizza" : 2.5,
    "panino": 4.0,
    "bibita": 2.5,
    "acqua" : 1.0,
    "caffé" : 1.3
}

scontrino = []
totale = 0

while True:
    print("------------MENU-------------")
    for p, prezzo in menu.items():
        print(f"{p:10}: €{prezzo:.2f}")

    food = input("Aggiungi un prodotto all'elenco (q per uscire) ")

    if food.lower() == 'q':
        break
    else:
        if food in menu:
            # print(food)
            scontrino.append(food)
            totale += menu.get(food)
        else:
            print("Prodotto non disponibile")

print("-----------------------------")
print("Scontrino")
print("-----------------------------")
for p in scontrino:
    print(p, end=" - ")

print()
print(f"Totale scontrino €{totale:.2f}")

print("-----------------------------")
print("Programma terminato")
print("-----------------------------")