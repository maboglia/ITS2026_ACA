from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'Chinook'
)


@app.get("/artists")
def artisti():
    cursore = db.cursor(dictionary=True)
    
    cursore.execute("SELECT * FROM artist")

    artisti = cursore.fetchall()

    return artisti


@app.get("/albums")
def album():
    cursore = db.cursor()
    
    query = """
    SELECT 
        ar.Name, a.Title 
    FROM album a
    join artist ar using (ArtistId)
    ;
    """

    cursore.execute(query)

    albums = cursore.fetchall()

    return albums




app.run(debug=True, port=5000)