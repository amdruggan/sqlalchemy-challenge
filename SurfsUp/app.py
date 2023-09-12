# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database into a new model
base = automap_base()

# Reflect tables
base.prepare(autoload_with=engine, reflect=True)

# Save references to each table
stations = base.classes.station
measurements = base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
# Create an app with __name__
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# 1. Home page ('/'), List all routes that are available.

@app.route("/")
def welcome():
    print("Home page request received...")
    """List all available api routes."""
    return (
        f"SQL Alchemy Challenge - Alec Druggan. <br/>"
        f"Available Routes:<br/>"
        "<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        "<br/>")

# 2. Precipitation ('/api/v1.0/precipitation') 
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
