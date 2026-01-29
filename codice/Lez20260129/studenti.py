studenti = []

f = open('studenti.txt')

for riga in f:
    # print(riga)
    # per ogni riga del file aggiungo la riga alla lista studenti
    riga = riga.replace("\n", "")
    riga = riga.replace("\t", ",")
    studenti.append(riga)

f.close()

f = open('studenti.sql', 'w')

query_tabella = """
DROP TABLE IF EXISTS studenti;\n\n

CREATE TABLE studenti(\n
    id int primary key auto_increment,\n
    nome varchar(30) not null,\n
    cognome varchar(50) not null\n
);\n\n

"""
f.write(query_tabella)

for s in studenti:
    s = str(s)
    pezzi = s.split(",")
    nome = pezzi[0]
    cognome = pezzi[1]
    f.write(f"insert into studenti (nome, cognome) value ('{nome}', '{cognome}');\n")
    # print(f"Il nome dello studente è {nome} e il cognome è {cognome}")
f.close()

