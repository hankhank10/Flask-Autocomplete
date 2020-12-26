from flask import Flask, Response, render_template, request
import json

app = Flask(__name__)

cities = ["Bratislava",
          "Banská Bystrica",
          "Prešov",
          "Považská Bystrica",
          "Žilina",
          "Košice",
          "Ružomberok",
          "Zvolen",
          "Poprad"]

countries = ["UK",
             "France",
             "Poland"]


@app.route('/_autocomplete/<what_to_get>', methods=['GET'])
def autocomplete(what_to_get):
    
    if what_to_get == "cities":
        output = cities

    if what_to_get == "countries":
        output = countries
    
    return Response(json.dumps(output), mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("search.html")

if __name__ == '__main__':
    app.run(debug=True)
