# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:00:03 2020

Contains city related functions

@author: gshre
"""
import pandas as pd
import numpy as np
from citipy import citipy

cities_file_loc = "Output_Data/cities.csv"

#Returns data frame with loaded cities latitue and logitude
def Load_Random_Cities_Locations(lattitude_low, latitude_high):
    """
    Used to load random cities by generating samples of latitue and
    logitude values and finding nearby cities.  Uses the citypy module

    Parameters
    ----------
    lattitude_low : TYPE: int
        DESCRIPTION. Lowest latitude value to use in generating sample
    latitude_high : TYPE: int
        DESCRIPTION. Highest latitude value to use in generating sample

    Returns
    -------
    TYPE: DataFrame
        DESCRIPTION. random cities within bounded latitude range

    """
    # List for holding lat_lngs and cities
    lat_lngs = []
    cities = []
    # Create a set of random lat and lng combinations
    lats = np.random.uniform(low=lattitude_low, high=latitude_high, size=2000)
    lngs = np.random.uniform(low=-180.000, high=180.000, size=2000)
    lat_lngs = zip(lats, lngs)
    
    # Identify nearest city for each lat, lng combination
    for lat_lng in lat_lngs:
        city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
        
        # If the city is unique, then add it to a our cities list
        if city not in cities:
            cities.append(city)
    
    # Print the city count to confirm sufficient count
    print(len(cities))
    return pd.DataFrame(cities)
    

def Chunk_Cities_Into_Sets(cities, chunksize):
    '''
    
    Parameters
    ----------
    cities : TYPE: dataframe
        DESCRIPTION. cities dataframe
    chunksize : TYPE: int
        DESCRIPTION. the number of cities in each chuck or set

    Returns
    -------
    sets : TYPE
        DESCRIPTION.

    '''
    print("starting chunk")

    sets = []
    whileMoreToChunk = True
    startValue = 0
    iteration = 1
    while whileMoreToChunk:
        print(startValue, iteration, chunksize, iteration * chunksize)
        citySet = cities.iloc[startValue : iteration * chunksize]
        print(citySet.head(chunksize))
        sets.append(citySet)
        
        if len(citySet) < chunksize:
            whileMoreToChunk = False
        startValue = chunksize * iteration
        iteration += 1
    
    print(f"Sets found: {len(sets)}")

    return sets

def Save_City_Data(cities_data):
    """
    Saves the cities dataframe to the desired location

    Parameters
    ----------
    cities_data : TYPE: DataFrame
        DESCRIPTION. cities dataframe to persist for later use

    Returns
    -------
    None.

    """
    cities_data.to_csv(cities_file_loc)


def Load_City_Data():
    """
    returns the CSV file of city data generated in earlier steps

    Returns
    -------
    cities_df : TYPE : Data Frame
        DESCRIPTION. Data Frame loaded from csv file

    """
    cities_df = pd.read_csv(cities_file_loc)
    return cities_df



def Find_Ideal_Cities(cities):
    '''
    Finds cities that meet the below criteria
* A max temperature lower than 80 degrees but higher than 70.
  * Wind speed less than 10 mph.
  * Zero cloudiness.
  
    Parameters
    ----------
    cities : TYPE: DataFrame
        DESCRIPTION. Cities data frame loaded from csf file

    Returns
    -------
    data frame with ideal cities.
    '''
    ideal_cities = cities[(cities["Max Temp"] <= 80) 
                            & (cities["Max Temp"] >= 70) 
                            & (cities["Wind Speed"] < 10)
                            & (cities["Cloudiness"] == 0)]
    
    print(ideal_cities.head())
    return ideal_cities
    
    
