# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:36:23 2020

@author: gshre
"""

import matplotlib.pyplot as plt

def Generate_Scatter_Plots(cities_df):
    latitude = cities_df['Lat']
    Scatterplot_latitude(latitude,  cities_df['Max Temp']
                          , 'Temperature (F)')
    print("This plot is showing relationship of temperature being higher on average near the equator")

    Scatterplot_latitude(latitude,  cities_df['Humidity']
                          , 'Humidity (%)')
    print("This plot is showing relationship of humitity in general being higher near the equator")

    Scatterplot_latitude(latitude,  cities_df['Cloudiness']
                          , 'Cloudiness (%)')
    print("This plot is showing there is no relationship between cloudiness and the equator")

    Scatterplot_latitude(latitude,  cities_df['Wind Speed']
                          , 'Wind Speed (mph)')
    print("This plot is showing that wind speeds near the equator are generally low")
    
 
def Scatterplot_latitude(latitude, series, label):
    plt.scatter(latitude, series)
    plt.title(f"{label} vs. Latitude")
    plt.xlabel('Latitude')
    plt.ylabel(label)
    plt.show()
