from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/obtainLocations")
def obtain():
    r = requests.get('https://api.finnair.com/aws/locations/prod/all')
    #print(r.text)
    return r.text
