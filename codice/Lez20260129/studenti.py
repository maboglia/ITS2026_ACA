studenti = []

f = open('./studenti.txt')

for riga in f:
    # print(riga)
    # per ogni riga del file aggiungo la riga alla lista studenti
    studenti.append(riga)

f.close()

for s in studenti:
    print(s)


