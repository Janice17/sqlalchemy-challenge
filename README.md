# sqlalchemy-challenge
Module 10 Challenge: I've decided to do a climate analysis about the area.
# Code Source
Python (app.py)  
Jupyter Notebook (climate.ipynb)  
DB Browser for SQLite (hawaii.sqlite)
## Part 1: Analyze and Explore the Climate Data
Using Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. (SQLAlchemy ORM queries, Pandas, and Matplolib)  

1. Using climate.ipynb and hawaii.sqlite to complete climate analysis and data exploration.  
2. Using SQLAlchemy create_engine() function to connect to SQLite database.  
3. Using SQLAlchemy automap_base() function to reflect tables into classes, and then save references to the classes named station and measurement.  
4. Linked Python to the database by creating a SQLAlchemy session.  
5. Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.
### Precipitation Analysis
1. Found the most recent date in the dataset.  
2. Using the date, get the previous 12 months of precipitation data by quering the previous 12 months of data.  
3. Selected only the "date" and "prcp" values.  
4. Loaded the query results into a Pandas DataFrame. (Explicitly set the column names)  
5. Sort the DataFrame values by "date".  
6. Plotted the results by using the DataFrame plot method, as the following image shows:
![alt text](SurfsUp/Output/Last_12months_Precipitation.png)
7. Used Pandas to print the summary statistics for the precipiation data.
### Station Analysis
1. Designed a query to calculate the total number of stations in the dataset.  
2. Designed a query to find the most-activate stations (stations with most rows).  

- Listed the stations and observation counts in the descending order.  
- station id has the greatest number of observations.  

3. Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.  
4. Designed a query to get the previous 12 months of temperature observations (TOBS) data.  

- Filtered by the station that has the greates number of observations.  
- Query the previous 12 months of TOBS data for that station.  
- Plotted the results as a histogram with bias=12.  
![alt text](SurfsUp/Output/Last_12months_Temperature_Observations.png)
5. Closed session.
## Part 2: Design Your Climate App

