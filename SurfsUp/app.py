# Import the dependencies.
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

# Start at the homepage and lists all the available routes
@app.route("/")
def welcome():
    return(
        '''
        Welcome to the Hawaii Climate Analysis API!<br/>
        <p>Available Routes:<br/>
        /api/v1.0/precipitation<br/>
        /api/v1.0/stations<br/>
        /api/v1.0/tobs<br/>
        /api/v1.0/temp/start<br/>
        /api/v1.0/temp/start/end<br/>
        <p>start and end date should be in the MMDDYYYY.
        '''
    )

# Returns the precipitation data for the last year available data
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Using 8-23-2017 find the previous year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query for the date and precipitation for the last year of available data
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    session.close()
    # Convert the query results to a dictionary
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Returns the list of stations from dataset
@app.route("/api/v1.0/stations")
def stations():
    # Results a list of stations
    results = session.query(Station.station).all()

    session.close()

    # Converts results to 1D array then to a list
    stations = list(np.ravel(results)) # np.ravel used to flatten a multi-dimensional array into a one-dimensional array
    return jsonify(stations=stations)

# Return the temperature observations of the most active station for the previous year of data
@app.route("/api/v1.0/tobs")
def temperature_monthly():
    
    # Using 8-23-2017 find the previous year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the primary station for all the tobs
    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()

    session.close()

    # Return results to 1D arry and convert to a list
    temps = list(np.ravel(results)) # np.ravel used to flatten a multi-dimensional array into a one-dimensional array
    return jsonify(temps=temps)

# Return minimum temperature, the average temperature, and maximum temperature for a specified start or start-end range
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    # Select statement that calculates min, avg, and max
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)] # sel is a method that indexes arrays by labels along specified dimensions

    if not end:
        start = dt.datetime.strptime(start, "%m%d%Y") # datetime.strptime is a method that parses a string represeting a date and time and converts it to a datetime object
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        
        session.close()
        
        # Return results to 1D arry and convert to a list
        temps = list(np.ravel(results)) # np.ravel used to flatten a multi-dimensional array into a one-dimensional array
        return jsonify(temps=temps)
    
    # Calculate TMIN, TAVG, and TMAX with start-end range
    start = dt.datetime.strptime(start, "%m%d%Y") 
    end = dt.datetime.strptime(end, "%m%d%Y") 

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    
    session.close()
    # Return results to 1D arry and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == '__main__':
    app.run(debug=True)
