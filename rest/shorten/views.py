# -*- coding: utf-8 -*-
## views.py
## The views file to connect to the dashboard backend
import os
import string
import random
from flask import (Blueprint, jsonify, request, make_response, Response)
from werkzeug.utils import redirect
from rest import mongo_client, api, config
from rest.utils.helpers import base_url, response_type

shortendb = mongo_client["shortendb"]
app_config = config[os.environ.get('FLASK_ENV', 'default')]

shorten_blueprint = Blueprint('shorten',
                            __name__,
                            template_folder=None)



@shorten_blueprint.route('/api/v1/shorten', methods=['POST'])
@api.representation(f'application/{app_config.RESPONSE_FORMAT}')
def shorten_uri():
    '''
      Function to create a short url from the URL that the user posted.
      How to use it:
      POST a url to this route (/api/v1/shorten):
      e.g: (with cURL)
      curl -XPOST http://localhost:5050/api/v1/shorten \
            -H "Content-Type: application/json" \ 
            -d '{"url":"https://element.io"}'

    '''
    req_data = request.get_json()
    url_to_encode = req_data.get("url")
    el = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
    identifier = "".join(random.choices(el, k=7))

    try:
        if shortendb.get_collection("shorten"):
            short_collection = shortendb["shorten"]
            short_collection.create_index([("shorten", -1)])
        else:
            short_collection = shortendb.create_collection("shorten")
            short_collection.create_index([("shorten", -1)])

        short_collection.insert_one({
            "_id": identifier,
            "identifier": identifier,
            "url": url_to_encode
        })
        ## return the shorten url to the user
        base_uri = base_url(request.url, with_path=False)
        url_res = f"{base_uri}/{identifier}"

        res = {
            "status_code": "200",
            "url_shorten": url_res
        }

        return response_type(res, 200)
        
    except Exception as e:
        print(f"error: {e}")
        err_msg = f'Sorry we could not shorten the url at this time'

        err ={
            "error": "Bad Request",
            "message": err_msg,
            "status_code": 400
        }

        return response_type({"error":err}, 400)

@shorten_blueprint.route('/api/v1/lookup/<url_id>', methods=['GET'])
@api.representation(f"application/{app_config.RESPONSE_FORMAT}")
def lookup(url_id):
    '''
      Function to lookup for the original url. 
      How to use it:
      Please use the following example with cURL:
      $ curl -XGET http://localhost:5050/api/v1/lookup/<short_url_identifier>
    '''
    try:
        ## query db for lookup
        res = shortendb.shorten.find_one({
            "identifier": url_id
        })

        if res != None:
            r = {"original_url": res.get("url"), "status_code":200}       
            return response_type(r, 200)
        else:
            return response_type({"message":"Sorry we cannot seem to find the url you are looking for."}, 404)

        
    except Exception as e:
        print(f"error lookup {e}")
        err_msg = "An error has just happen, please see the logs to know more about it, as we were short in time to implement a full error system :)"
  
        err = {
            "error": "Bad Request",
            "message": err_msg,
            "status_code": 400
        }
        return response_type({"error":err}, 400)



@shorten_blueprint.route("/<url_id>")
@api.representation(f'application/{app_config.RESPONSE_FORMAT}')
def redirecting(url_id):
    '''
     Function to redirect the user to the original URL.
     How to use it: 
     Go to your browser and insert the short URL to the navigation bar.
     You will then be redirected to the original website
    '''
    try:
        res = shortendb.shorten.find_one({
        "identifier": url_id
         })  
        if res != None:
            redirect_url = res.get("url")
            return redirect(redirect_url)
        else:
            return response_type({"message":"Sorry this not a valid url"}, 400)
    except Exception as e:
        err_msg = "An error has just happen, please see the logs to know more about it, as we were short in time to implement a full error system :)"
  
        err = {
            "error": "Bad Request",
            "message": err_msg,
            "status_code": 400
        }
        return response_type({"error":e}, 400)


    