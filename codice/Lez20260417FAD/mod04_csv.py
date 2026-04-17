import csv



def leggi_file_csv(nome_file):

    with open(nome_file, mode="r", newline="", encoding="utf-8") as f:
        #reader = csv.reader(f)
        reader = csv.DictReader(f)

        return list(reader)
    

moto = leggi_file_csv("moto.csv")

for m in moto:
    print(m['Modello'])

print("*" * 25)

auto = leggi_file_csv("auto.csv")

for a in auto:
    print(a['Modello'])