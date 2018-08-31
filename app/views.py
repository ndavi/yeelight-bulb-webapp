from flask import render_template, request, abort
import json
from app import app
from yeelight import *
bulbs = [Bulb('192.168.1.100')]

# ROUTING/VIEW FUNCTIONS


@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/f', methods=['POST'])
def flashLight():
    bulbs[0].toggle()
    return "OK"

@app.route('/color', methods=['POST'])
def color():
    colors = request.form
    bulbs[0].set_rgb(int(colors.get('r')), int(colors.get('g')), int(colors.get('b')))
    return "OK"

@app.route('/changeIntensity', methods=['POST'])
def changeIntensity():
    bulbs[0].set_brightness(int(request.form.get('intensity')))
    print(bulbs[0].get_properties())
    return "OK"