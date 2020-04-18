# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:14:05 2020

Functions around the use of google API to pull in motels based on 
ideal cities

@author: gshre
"""
import requests
import pandas as pd

from pprint import pprint
from api_keys import g_key

encrypt_api_key = ""

def Encrypt_PlusCode_API_Key(api_key):
    """
    Generates an encrypted API key for use of place codes

    Parameters
    ----------
    api_key : TYPE: string
        DESCRIPTION. unencrypted API key

    Returns
    -------
    TYPE: string
        DESCRIPTION. encrypted API key

    """
    url = f"https://plus.codes/api?encryptkey={g_key}" 
    response = requests.get(url).json()
    return response["key"]


def Find_Motels_For_Cities(cities):
    """
    Loads a series of hotels based on the cities provided

    Parameters
    ----------
    cities : TYPE: DataFrame
        DESCRIPTION. Cities Sample

    Returns
    -------
    DataFrame representing Motels of cities.

    """
    hotels = []
    encrypted_key = Encrypt_PlusCode_API_Key(g_key)
    for index, city in cities.iterrows():
        hotel = Find_Hotel_For_City(city, encrypted_key)
        if hotel != "":
            hotels.append(hotel)
            
    return pd.DataFrame(hotels)

def Find_Hotel_For_City(city, encrypted_key):
    """
    Using the google places API, find first motel within 500 meets of the 
    city coordinates

    Parameters
    ----------
    cities : TYPE: Dictionary of values representing city
        DESCRIPTION. A specific city found in sample
    encrypted_key : TYPE: string
        DESCRIPTION. An encrypted key to get place codes

    Returns
    -------
    Dictionary representing Hotel information

    """
    lat = city["Lat"]
    lng = city["Lng"]
    target_coordinates = f"{lat}, {lng}"
    target_search = "Hotel"
    target_radius = 500 # meters
    target_type = "lodging"

    # set up a parameters dictionary
    params = {
        "location": target_coordinates,
        "keyword": target_search,
        "radius": target_radius,
        "type": target_type,
        "country": "long_name",
        "locality": "long_name",
        "key": g_key
    }

    # base url
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    # run a request using our params dictionary
    response = requests.get(base_url, params=params)
    hotelData = response.json()
    #pprint(hotelData)
    print(f"Finding hotel for {city['City']}")
    
    # adding try catch in case the data is not there
    hotel = ""
    try:
        hotel_name = hotelData["results"][0]["name"]
        vicinity = hotelData["results"][0]["vicinity"]
        city_country = hotelData["results"][0]["plus_code"]["compound_code"]
        vicinity = hotelData["results"][0]["vicinity"]
        lat = hotelData["results"][0]["geometry"]["location"]["lat"]
        lng = hotelData["results"][0]["geometry"]["location"]["lng"]
        
        # last entry should be country
        country = city_country.split(",")[-1]
        ciyname = vicinity.split(",")[-1]
        #print(ciyname)
        
        hotel = { "name": hotel_name,
                 "city": ciyname,
                 "country": country,
                 "lat": lat,
                 "lng": lng}
        
    except IndexError:
        print(f"There is not hotel within the city radius of {target_radius} meters")
    
    return hotel
