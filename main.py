from flask import Flask, jsonify, render_template, request, redirect, session
import requests
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
    return render_template('series.html', series=series)
