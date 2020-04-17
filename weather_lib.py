# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:48:52 2020

@author: Greg Shreve
"""
import pandas as pd
from api_keys import weather_api_key
from pprint import pprint
import requests

#from datetime import datetime # original intent was to convert time

from city_lib import Chunk_Cities_Into_Sets
 
# Functions related to Weather API

def Perform_Weather_Check(cities):
    """
    Function to gather weather statistics for the provided cities
    DataFrame.  It will do this in chunks of 50 per example.

    Parameters
    ----------
    cities : TYPE: DataFrame
        DESCRIPTION. cities sample without weather attributes

    Returns
    -------
    cities_data : TYPE: DataFrame
        DESCRIPTION. cities sample with weather attributes

    """
    print("starting weather_check")
    print(cities.head())
    sets = Chunk_Cities_Into_Sets(cities, 50)

    print("beginning data retrieval")
    print("".join('-' for n in range(80)))
    cities_data = []
    
    setIdx = 0
    for citySet in sets:
        setIdx += 1
        new_cities = Retrieve_Weather_Data(setIdx, citySet)
        print(f"Number of new cities is {len(new_cities)}")
        if len(cities_data) > 0:
            cities_data = pd.concat([cities_data, new_cities], sort = False)
            print(f"new length is {len(cities_data)}")
        else:
            cities_data = new_cities
            print(cities_data)
 
    print("Data retrieval complete")

    #print(cities_data.head())

    # the concatenation has added an additional index, removing it
    cities_data = cities_data.sort_values(['City']).reset_index()[[
                                'City', 'Cloudiness', 'Country'
                               , 'Date', 'Humidity', 'Lat', 'Lng'
                               , 'Max Temp', 'Wind Speed']]
    cities_data.index.name = "City_ID"
    
    # Sorting the data and resetting the index
    return cities_data
       # .reset_index().drop([columns = ])
        
              
def Retrieve_Weather_Data(pageset, city_set):
    """
    calls weather api to pull weather information for the provided
    set of cities

    Parameters
    ----------
    pageset : TYPE: int
        DESCRIPTION. the specific page set being returned.  for logging
    city_set : TYPE: DataFrame
        DESCRIPTION. a set of cities

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # Create the base URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    cities_data = []
    
    # Set the params for the call
    params = { "appid" : weather_api_key
          , "units": "imperial" }
    
    record = 0
    for index, city in city_set.iterrows():  
        # Output information of the call
        record += 1
        print(f"Processing record {record} of set {pageset} | {city[0]}")
        
        params["q"] = city
        response = requests.get(base_url, params)
        
        # Not all cities will be found by API.  only add those found
        if (response.status_code == 200):
            #print(response)
            #print(response.request.url)
                
            city_weather_data = response.json()
            #pprint(city_weather_data)
            
            # Move the data to variables
            cloudiness = city_weather_data["clouds"]["all"]
            lat = city_weather_data["coord"]["lat"]
            lng = city_weather_data["coord"]["lon"]
            country = city_weather_data["sys"]["country"]
            max_temp = city_weather_data["main"]["temp_max"]
            wind_speed = city_weather_data["wind"]["speed"]
            humidity = city_weather_data["main"]["humidity"]
            
            # could convert to readible date
            #date = datetime.fromordinal(city_weather_data["dt"])
            date = city_weather_data["dt"]
               
            # Build and return dictionary
            city_data = { "City" : city[0]
                    , "Cloudiness" : cloudiness
                    , "Country" : country
                    , "Date" : date
                    , "Humidity": humidity
                    , "Lat" : lat
                    , "Lng" : lng
                    , "Max Temp" : max_temp
                    , "Wind Speed" : wind_speed
                }
            cities_data.append(city_data)  
        else:
            # Just assuming everything else is not found
            print("City not found...Skipping...")
    return pd.DataFrame(cities_data)  
     
    
