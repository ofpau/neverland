from flask import Flask, jsonify, render_template, request, redirect, session
import requests
import json
app = Flask(__name__)

series_list = [
        {'id':'got', 'name': 'Game of Thrones', 'img': 'got.jpeg', 'city':'LON'},
        {'id': 'sv', 'name': 'Silicon Valley', 'img': 'siliconValley.jpg', 'city': 'SFO'},
        # {'id': 'br', 'name': 'Blade Runner 2049', 'img': 'bladeRunner2049.jpg'},
        {'id': 'dexter', 'name': 'Dexter', 'img': 'dexter_size.jpg', 'city': 'MIA'},
        {'id': 'suits', 'name': 'Suits', 'img': 'suits.jpg', 'city': 'YTO'},
        {'id': 'himym', 'name': 'How I Met Your Mother', 'img': 'dexter_size.jpg', 'city': 'NYC'},
        {'id': 'hoc', 'name': 'House Of Cards', 'img': 'hoc.jpg', 'city': 'DCA'}
]

@app.route("/")
def hello():
    return render_template('index.html')#, images=images, user=user)
    #return "Hello World!"

@app.route("/series")
def series():
    return render_template('series.html', series=series_list)

@app.route("/series/<s>")
def serie_detail(s):
    p = [p for p in series_list if p['id'] == s][0]
    print(p)
    price = obtain_flight_price(p['city'])
    flight = {'city': p['city'], 'price': price}
    return render_template('series_detail.html', s=p, flight=flight)
    # return "You're watching the page for " + s

def obtain_flight_price(airport_code):#airportCodeDestination):
    #TODO: start day harcoded for now
    #days=1
    #startDay="2017-12-01"
    url="https://instantsearch-junction.ecom.finnair.com/api/instantsearch/pricesforperiod/fixeddeparture?departureLocationCode=HEL&destinationLocationCode={}&departureDate=2017-12-01&numberOfDays=5".format(airport_code)
    r = requests.get(url)
    js = json.loads(r.text)
    #print(js['prices'])
    #print(r.text[3])
    #print(r.text)
    print(js['prices'][0]['price'])
    return js['prices'][0]['price']
