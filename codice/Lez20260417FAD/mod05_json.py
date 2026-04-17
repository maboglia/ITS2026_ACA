import json

from mod04_csv import leggi_file_csv


def converti_csv_in_json(nome_file_csv, nome_file_json):
    dati = leggi_file_csv(nome_file_csv)

    with open(nome_file_json, "w") as f:
        json.dump(dati, f, indent=4)


converti_csv_in_json("moto.csv", "moto.json")
converti_csv_in_json("auto.csv", "auto.json")