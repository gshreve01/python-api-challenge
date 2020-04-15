# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:36:23 2020

@author: gshre
"""

import matplotlib.pyplot as plt
from scipy.stats import linregress
import scipy.stats as st

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
    
def Generate_Hemispher_Plots(cities_df):
    # split the data between northern and souther hemispher
    northern_df = cities_df[(cities_df['Lat'] >= 0)]
    southern_df = cities_df[(cities_df['Lat'] < 0)]
    print(northern_df['Lat'].head())
    print(southern_df['Lat'].head())
    
    # split the latitude values into northern and soutern
    northern_latitude = northern_df['Lat']
    southern_latitude = southern_df['Lat']
    
    print(len(northern_latitude))
    print(len(southern_latitude))
        
    # Temperature
    series_type = 'Max Temp'
    label = 'Temperature (F)'
    Regression_latitude('Northern', northern_latitude, northern_df[series_type] 
                        , label)
    print("A high negative correlation value indicates that the farther from 0 latitude, the colder the temperature")

    Regression_latitude('Southern', southern_latitude, southern_df[series_type] 
                        ,label)
    print("A high positive correlation value indicates that the closer to 0 latitude, the higher the temperature")
        
    # Humidity
    series_type = 'Humidity'
    label = 'Humidity (%)'
    Regression_latitude('Northern', northern_latitude, northern_df[series_type] 
                        ,label)
    print("A slight correlation in this data indicates that the humidity is lower near the equator")

    Regression_latitude('Southern', southern_latitude, southern_df[series_type] 
                        , label)
    print("A very slight correlation value indicates that the humidity is higher near the equator")
       
    # Cloudiness
    series_type = 'Cloudiness'
    label = 'Cloudiness (%)'
    Regression_latitude('Northern', northern_latitude, northern_df[series_type] 
                        ,label)
    print("A slight correlation in this data indicates that the cloudiness is lower near the equator")

    Regression_latitude('Southern', southern_latitude, southern_df[series_type] 
                        , label)
    print("A correlation between cloudiness and latitude is so low that it should not be considered")
    
    
def Regression_latitude(hemispere, latitude, series, label):
    ax, fig = plt.subplots(figsize=(8, 5))
    plt.scatter(latitude, series)
    
    # Calculate the linear regression
    (slope, intercept, rvalue, pvalue, stderr) = linregress(latitude, series)
    regress_values = latitude * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    plt.plot(latitude,regress_values,"r-")
    print(line_eq)
    xplot_loc = latitude.min() + 10
    yplot_loc = series.min()
    plt.annotate(line_eq,(xplot_loc,yplot_loc),fontsize=12,color="red")

    plt.title(f"{hemispere} Hemisphere - {label} vs Latitude")
    plt.xlabel('Latitude')
    plt.ylabel(label)
    plt.show()
    
    correlation = st.pearsonr(latitude, series)
    print(f"The correlation between {hemispere} Hemisphere {label} and latitude: {round(correlation[0],2)}")

        
    
    
 
def Scatterplot_latitude(latitude, series, label):
    plt.scatter(latitude, series)
    plt.title(f"{label} vs. Latitude")
    plt.xlabel('Latitude')
    plt.ylabel(label)
    plt.show()
