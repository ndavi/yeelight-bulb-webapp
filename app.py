from flask import render_template, request, abort, Flask
from yeelight import *
import json
from collections import namedtuple
import json

app = Flask(__name__)

bulbs = [Bulb('192.168.1.100'), Bulb('192.168.1.101'), Bulb('192.168.1.102')]


# ROUTING/VIEW FUNCTIONS


@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    # bulb_values = {}
    # it = 0
    # for bulb in bulbs:
    #     try:
    #         data = bulb.get_properties()
    #         bulb_values[str(it)] = data
    #         it = it + 1
    #     except Exception:
    #         bulb_values[str(it)] = {'connected': None}
    #         it = it + 1

    return render_template('index.html', data=json.dumps(bulb_values))


@app.route('/f/<lampID>', methods=['POST'])
def flashLight(lampID):
    bulbs[int(lampID)].toggle()
    return "OK"


@app.route('/color/<lampID>', methods=['POST'])
def color(lampID):
    colors = request.form
    bulbs[int(lampID)].set_rgb(int(colors.get('r')), int(colors.get('g')), int(colors.get('b')))
    return "OK"


@app.route('/changeIntensity/<lampID>', methods=['POST'])
def changeIntensity(lampID):
    bulbs[int(lampID)].set_brightness(int(request.form.get('intensity')))
    return "OK"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
