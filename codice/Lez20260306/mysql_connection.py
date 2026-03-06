import mysql.connector
import json

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'its2026'
)

cursor = db.cursor()

cursor.execute("SHOW TABLES;")

for database in cursor.fetchall():
    print(database)

cursor.execute("SELECT * FROM games")

games = cursor.fetchall()

with open('games.json', 'w', encoding='utf-8') as f:
    json.dump(games, f, indent=4)

print("Abbiamo finito il tempo")