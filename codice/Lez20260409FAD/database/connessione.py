import sqlite3

# 1. Connetti al database (crea il file se non esiste)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 2. Leggi il file SQL
with open('script.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# 3. Esegui lo script SQL
try:
    cursor.executescript(sql_script)
    conn.commit() # Conferma le modifiche
    print("Script eseguito con successo.")
except sqlite3.Error as e:
    print(f"Errore durante l'esecuzione: {e}")
finally:
    # 4. Chiudi la connessione
    conn.close()