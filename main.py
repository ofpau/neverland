from flask import Flask, jsonify, render_template, request, redirect, session
import requests
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')#, images=images, user=user)
    #return "Hello World!"

@app.route("/series")
def sesries():
    series = [{'id':'got', 'name': 'Game of Thrones', 'img': 'got.jpeg'},
              {'id': 'sv', 'name': 'Silicon Valley', 'img': 'siliconValley.jpg'},
              # {'id': 'br', 'name': 'Blade Runner 2049', 'img': 'bladeRunner2049.jpg'},
              {'id': 'dexter', 'name': 'Dexter', 'img': 'dexter.jpg'}]
    obtainFlights("NYC")
    return render_template('series.html', series=series)

@app.route("/tests")
def obtainFlights():#airportCodeDestination):
    #TODO: start day harcoded for now
    #days=1
    #startDay="2017-12-01"
    airportCodeDestination="NYC"
    url="https://instantsearch-junction.ecom.finnair.com/api/instantsearch/pricesforperiod/fixeddeparture?departureLocationCode=HEL&destinationLocationCode={}&departureDate=2017-12-01&numberOfDays=5".format(airportCodeDestination)
    r = requests.get(url)
    js = json.loads(r.text)
    #print(js['prices'])
    #print(r.text[3])
    #print(r.text)
    return jsonify(js['prices'][0]['price'])#"Hey"#r.text
