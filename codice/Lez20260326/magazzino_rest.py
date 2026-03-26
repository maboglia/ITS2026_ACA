from magazzino_service import MagazzinoService
#pip install flask
from flask import Flask, jsonify

app = Flask(__name__)

service = MagazzinoService()

@app.get('/api/prodotti')
def prodotti():
    return jsonify(service.getAllProducts())


@app.get('/api/categorie')
def prodotti():
    return jsonify(service.getAllProducts())



app.run(debug=True)
