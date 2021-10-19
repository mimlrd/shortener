# -*- coding: utf-8 -*-
## app.py
import os
from rest import create_app, api, config
from flask import jsonify

from datetime import datetime as dt


FLASK_ENV = os.environ.get('FLASK_ENV', 'default')
app = create_app(FLASK_ENV)



@app.route('/')
@api.representation(f'application/{config.get("RESPONSE_FORMAT")}')
def home():
    res = {
        'title': 'Welcome, you have reached the STEALTH INC PROJECT REST GATEWAY',
        'message': 'You are home now!',
        'date': dt.now()
    }
    return (jsonify(res), 200)




if __name__ == '__main__':

    app.run(host='0.0.0.0',port=5050)
