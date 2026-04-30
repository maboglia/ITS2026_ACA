Ti propongo un **esercizio completo a pipeline (a step)** che ti fa usare davvero i principali moduli Python: `csv`, `json`, `math`, `random`, `datetime`, `os`, `sys`, `pathlib`, `collections`, `statistics`, `re`.

L’idea è costruire un mini-progetto CLI realistico: **Student Analytics Pipeline**.

---

# 🧩 PROGETTO: Student Analytics Pipeline (CLI)

## 🎯 Obiettivo

Creare un programma Python da riga di comando che:

1. genera dati studenti casuali
2. li salva su CSV
3. li converte in JSON
4. valida dati con regex
5. calcola statistiche voti
6. produce report finale (JSON + TXT)
7. gestisce cartelle e log temporali

---

# 📌 Struttura progetto consigliata

```
student_pipeline/
│
├── main.py
├── data/
│   ├── input/
│   ├── output/
│   └── backup/
│
├── report/
│
└── config.json
```

---

# STEP 0 — Preparazione (sys, pathlib, os)

## Task

* creare le cartelle se non esistono:

  * `data/input`
  * `data/output`
  * `data/backup`
  * `report`

📌 Moduli richiesti: `pathlib`, `os`

---

# STEP 1 — File di configurazione (json)

## Task

Creare un file `config.json` con parametri tipo:

```json
{
  "numero_studenti": 50,
  "voto_min": 2,
  "voto_max": 10,
  "materie": ["Matematica", "Informatica", "Italiano"],
  "classe": "5A"
}
```

📌 Moduli richiesti: `json`

---

# STEP 2 — Generazione studenti casuali (random, datetime)

## Task

Generare studenti casuali con:

* id progressivo
* nome casuale
* cognome casuale
* data di nascita casuale (tra 2004 e 2009)
* email generata automaticamente
* voti casuali per ogni materia

Esempio struttura studente:

```python
{
  "id": 1,
  "nome": "Mario",
  "cognome": "Rossi",
  "data_nascita": "2006-03-15",
  "email": "mario.rossi@scuola.it",
  "voti": {
      "Matematica": 7,
      "Informatica": 9,
      "Italiano": 6
  }
}
```

📌 Moduli richiesti: `random`, `datetime`

---

# STEP 3 — Salvataggio su CSV (csv)

## Task

Salvare un file CSV dentro `data/input/` chiamato:

```
studenti_YYYYMMDD_HHMMSS.csv
```

Formato CSV richiesto:

```
id,nome,cognome,data_nascita,email,Matematica,Informatica,Italiano
1,Mario,Rossi,2006-03-15,mario.rossi@scuola.it,7,9,6
...
```

📌 Moduli richiesti: `csv`, `datetime`, `pathlib`

---

# STEP 4 — Lettura CSV e validazione (csv, re, collections)

## Task

Leggere il CSV e validare:

* email valida con regex
* data valida formato `YYYY-MM-DD`
* voti compresi tra `voto_min` e `voto_max`

Se uno studente ha errori, inserirlo in lista `scartati`.

📌 Richiesto:

* contare errori per tipo con `collections.Counter`

Esempio output conteggio errori:

```
email_non_valida: 2
data_non_valida: 1
voto_fuori_range: 3
```

📌 Moduli richiesti: `csv`, `re`, `collections`

---

# STEP 5 — Conversione CSV → JSON (json)

## Task

Convertire gli studenti validi in un file JSON:

```
data/output/studenti_validi.json
```

Formato JSON: lista di studenti.

📌 Moduli richiesti: `json`

---

# STEP 6 — Calcolo statistiche per materia (statistics, math)

## Task

Calcolare per ogni materia:

* media (`mean`)
* mediana (`median`)
* deviazione standard (`stdev`)
* voto minimo e massimo

Salvare in una struttura tipo:

```python
{
  "Matematica": {"media": 6.8, "min": 2, "max": 10, "stdev": 1.5},
  ...
}
```

📌 Moduli richiesti: `statistics`, `math`

---

# STEP 7 — Classifica migliori studenti (collections)

## Task

Calcolare per ogni studente:

* media voti personale

Poi estrarre:

* TOP 5 studenti migliori

Suggerimento:

* usare `sorted()`
* oppure `heapq` (facoltativo)

📌 Moduli richiesti: `collections` (opzionale), `statistics`

---

# STEP 8 — Report finale (json + txt)

## Task

Creare un file report testuale in `report/`:

```
report_YYYYMMDD.txt
```

Contenuto richiesto:

* classe
* data generazione
* numero studenti totali
* validi / scartati
* statistiche per materia
* top 5 studenti migliori

📌 Moduli richiesti: `datetime`, `pathlib`

---

# STEP 9 — Backup automatico (os, pathlib)

## Task

Copiare il CSV originale in `data/backup/`
rinominandolo tipo:

```
backup_studenti_YYYYMMDD_HHMMSS.csv
```

📌 Moduli richiesti: `os` oppure `shutil` (consigliato)

---

# STEP 10 — Gestione CLI (sys)

## Task

Il programma deve accettare comandi:

Esempio:

```bash
python main.py generate
python main.py validate
python main.py report
python main.py all
```

* `generate` → crea CSV input
* `validate` → valida e produce JSON output
* `report` → produce report finale
* `all` → esegue tutto in sequenza

📌 Moduli richiesti: `sys`

---

# STEP 11 — Extra avanzato (facoltativo)

## Extra A: log errori su file

Salvare gli studenti scartati su file:

```
data/output/scartati.json
```

## Extra B: timestamp in ogni record

Aggiungere `timestamp_import` in ogni studente.

## Extra C: simulazione assenze

Generare un campo `assenze` casuale (0-20) e calcolare correlazioni base.

---

# 🎯 Output atteso del progetto

Alla fine avrai:

✅ CSV input
✅ JSON studenti validi
✅ JSON studenti scartati
✅ report txt con statistiche
✅ backup CSV
✅ CLI funzionante

---

# 🧠 Moduli Python usati

| Modulo        | Dove                                 |
| ------------- | ------------------------------------ |
| `random`      | generazione studenti e voti          |
| `datetime`    | timestamp file e date nascita        |
| `csv`         | input/output CSV                     |
| `json`        | config + export studenti             |
| `re`          | validazione email/data               |
| `collections` | conteggio errori e statistiche       |
| `statistics`  | mean/median/stdev                    |
| `math`        | eventuali arrotondamenti e controlli |
| `os`          | gestione file e directory            |
| `sys`         | comandi CLI                          |
| `pathlib`     | gestione percorsi                    |

---

# 📌 Consegna finale (criteri di completamento)

Il progetto è completo se:

* `python main.py all` produce tutti i file previsti
* nessuna eccezione non gestita
* report contiene statistiche coerenti
* studenti invalidi vengono tracciati

