
from flask import Flask, jsonify

import numpy as np 
import datetime as dt
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func, inspect

#create engine
engine = create_engine("sqlit:///Resources/hawaii.sqlite")

#database
Base = automap_base()
Base.prepare(engine, reflect = True)

#table references
Measurement = Base.classes.measurement
Station = Base.classes.station

#routes
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/prescription<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")



# @app.route("/api/v1.0/prescription")
# def population():

        
@app.route("/api/v1.0/stations")
def stations():
    stations_data = session.query(Station).all()
        
    stations_list = []
    for station in stations_data:
        station_dict = {}
        station_dict["id"] = station.id
        station_dict["name"] = station.name
        station_dict["station"] = station.station
        station_dict["longitude"] = station.longitude
        station_dict["latitude"] = station.latitude
        station_dict["elevation"] = station.elevation
        stations_list.append(station_dict)
    return jsonify(stations_list)