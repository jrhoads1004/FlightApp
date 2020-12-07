import io
import sys
import csv
import os
import uuid
import csv
import json
import flask_pymongo
from flask_pymongo import PyMongo
from pprint import pprint
import datetime
import flask
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,)
import bson
from bson.json_util import dumps
from pymongo import MongoClient
app=Flask(__name__)

# Use PyMongo to establish Mongo connection

# try:
#     uri = os.environ["MONGODB_URI"]
    
<<<<<<< HEAD
except KeyError:
    uri = "mongodb://localhost:27017/flight"

   
app.config["mongodb://localhost:27017"] = uri
=======
# except KeyError:
#     uri = "mongodb://127.0.0.1:27017/"


   
app.config["MONGO_URI"] = "mongodb://localhost:27017/flight"
mongo = PyMongo(app) = uri

>>>>>>> bfd92d4e594227b99f8bd77a1c30eaa2da2a8195


mongo = PyMongo(app, uri)

# Call the Database and Collection
# @app.route("/")
# def home():
#     flightPorts = list(flight.db.find())
#     flightOutput = list(flight.db.find())
#     return render_template("index.html", flightData=(flightOutput, flightPorts))
        

#loaded json to Mongo, json created from a df using pandas to clean a csv
flight = mongo.db
<<<<<<< HEAD
flightPorts = flight.flightData
=======
flightData = flight.flightData
>>>>>>> bfd92d4e594227b99f8bd77a1c30eaa2da2a8195

jsonpath = os.path.join("data", "airports.json")
with open(jsonpath) as datafile:
    air_data = json.load(datafile)
    if isinstance(air_data, list):
        flightPorts.insert_many(air_data)
    else:
        flightPorts.insert_one(air_data)
        
flight = mongo.db
flightOutput = flight.flightData

jsonpathO = os.path.join("data", "Airport_Output.json")
with open(jsonpathO) as datafile:
    airportOut = json.load(datafile)
    if isinstance(airportOut, list):
        flightOutput.insert_many(airportOut)
    else:
        flightOutput.insert_one(airportOut)
        
@app.route("/")
<<<<<<< HEAD
def home():
    flightPorts = list(flight.db.find())
    flightOutput = list(flight.db.find())
    return render_template("index.html", flightData=(flightOutput, flightPorts))
=======
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)

@app.route("/uploads/<path:filename>", methods=["POST"])
def save_upload(filename):
    mongo.save_file(filename, request.files["file"])
    return redirect(url_for("get_upload", filename=filename))
>>>>>>> bfd92d4e594227b99f8bd77a1c30eaa2da2a8195
        
# Dump json into Database
# @app.route('/users')
# def users():
#     users = flight.flightData.find()
#     resp = json.dumps(users)
#     return resp

#Pull javascript Data to run with flask
# @app.route('/data')
# def get_javascript_data(json_from_csv):
    
#     return json.load("data", "airports.csv")[0]       


# def create_csv(text):
#     unique_id = str(uuid.uuid4())
#     with open('images/'+unique_id+'.csv', 'a') as file:
#         file.write(text[1:-1]+"\n")
#     return unique_id    

# def get_file_content(uuid):
#     with open(uuid+'.csv', 'r') as file:
#         return file.read()
    
   
    #return render_template("index.html", flightData=(flightOutput, flightPorts)


    return redirect("/", code=302)

if __name__=="__main__":
    client = MongoClient()
    db = client.flight
    collection = db.flightData
    cursor = collection.find({})
    # with open('collection.json', 'w') as file:
    #     file.write('[')
    #     for document in cursor:
    #         file.write(dumps(document))
    #         file.write(',')
    #     file.write(']')
    app.run(debug=True)