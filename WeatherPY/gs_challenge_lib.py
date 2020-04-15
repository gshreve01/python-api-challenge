import pandas as pd
import numpy as np
from api_keys import weather_api_key
from citipy import citipy
from pprint import pprint
import requests

from weather_lib import Perform_Weather_Check
from weatherplots_lib import Generate_Scatter_Plots
from weatherplots_lib import Generate_Hemispher_Plots

#TODO: Remove this function as it is pulled from citypy
# read in the cities .csv file
# def load_random_cities(sample_size):
#     world_cities = pd.read_csv("../resources/world-cities.csv")

#     np.random.seed(411)
#     chosen_idx = np.random.choice(len(world_cities), replace=True, size=sample_size)             
#     sample_cities = world_cities.iloc[chosen_idx]
    
#     return sample_cities

#Returns data frame with loaded cities latitue and logitude
def Load_Random_Cities_Locations(lattitude_low, latitude_high):
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
    

def Load_City_Data():
    csv_file = 'Output_Data/Cities.csv'
    cities_df = pd.read_csv(csv_file)
    return cities_df


# northern_cities = Load_Random_Cities_Locations(0, 90)
# southern_cities = Load_Random_Cities_Locations(-90, 0)
# cities = pd.concat([northern_cities.head(300), southern_cities.head(300)]
#                         , sort = False)

# print(f"Number of cities: {len(cities)}")
# print(cities.head())
# cities_data = Perform_Weather_Check(cities)
# cities_data.to_csv("Output_Data/cities.csv")


    
    
cities_df = Load_City_Data()
print(cities_df.head())
#Generate_Scatter_Plots(cities_df)
Generate_Hemispher_Plots(cities_df)

