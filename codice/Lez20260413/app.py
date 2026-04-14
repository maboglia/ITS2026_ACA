from controller.disco_controller import DiscoController
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin 

app = Flask(__name__)

ctrl = DiscoController()

@app.get("/")
def homepage():
    return "home page"

@app.get("/artisti")
def artisti():
    artisti = ctrl.getArtists()
    return render_template("artisti.html", artists = artisti)

@app.get("/api/artisti")
@cross_origin()
def artisti_json():

    return ctrl.getArtistiJson()




app.run(debug=True, port=5001)