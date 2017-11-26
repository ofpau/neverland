from flask import Flask, jsonify, render_template, request, redirect, session
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')#, images=images, user=user)
    #return "Hello World!"

@app.route("/series")
def sesries():
    series = [{'id':'got', 'name': 'Game of Thrones'}, {'id': 'narcos', 'name': 'Narcos'}]
    return render_template('series.html', series=series)

@app.route("/obtainLocations")
def obtain():
    r = requests.get('https://api.finnair.com/aws/locations/prod/all')
    #print(r.text)
    return r.text
