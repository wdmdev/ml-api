'''
Just testing how the flask framework works
'''
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return json.dumps({'name': 'William',
                        'region': 'København SV'})

@app.route('/animals', methods=['GET'])
def get_animals():
    return json.dumps({ 'name': 'elephant',
        'weight': '6 tonnes',
        'tusk weight': '140 kg'
    })

app.run()
