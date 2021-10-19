import urllib.parse
import os
from flask import Response, make_response
from flask.json import jsonify
from simplexml import dumps
from rest import config

app_config = config[os.environ.get('FLASK_ENV', 'default')]

def base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path   = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()

def response_type(data, status_code=200):

    resp_type = app_config.RESPONSE_FORMAT

    if resp_type == 'json':
        return make_response(jsonify(data),status_code)
    elif resp_type == 'xml':  
        r = make_response(dumps({'response':data}), status_code)  
        r.mimetype = "text/xml"
        return r
    else:
        return make_response(jsonify({"message":f"Sorry, at the moment only 2 types of serialization are available: (json or xml), and you have requested: {app_config.RESPONSE_FORMAT}"}))



