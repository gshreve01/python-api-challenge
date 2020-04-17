# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:36:23 2020

Contains functions related to generating weather plots

@author: gshre
"""

import matplotlib.pyplot as plt
from scipy.stats import linregress
import scipy.stats as st

def Generate_Scatter_Plots(cities_df):
    """
    Function to generate scatter plots of different weather attributes against
    latitude

    Parameters
    ----------
    cities_df : TYPE: DataFrame
        DESCRIPTION. cities sample

    Returns
    -------
    None.

    """
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
    """
    Function to generate the hemispher plats 

    Parameters
    ----------
    cities_df : TYPE: DataFrame
        DESCRIPTION. cities sample

    Returns
    -------
    None.

    """
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
    print("A slight correlation value indicates that the humidity is higher near the equator")
       
    # Cloudiness
    series_type = 'Cloudiness'
    label = 'Cloudiness (%)'
    Regression_latitude('Northern', northern_latitude, northern_df[series_type] 
                        ,label)
    print("A slight correlation in this data indicates that the cloudiness is lower near the equator")

    Regression_latitude('Southern', southern_latitude, southern_df[series_type] 
                        , label)
    print("A slight correlation between cloudiness and latitude that indicates the farther south you are the less cloudy")
    print("This is a different observation than the Norther hemispher provided.")
       
    # Wind Speed
    series_type = 'Wind Speed'
    label = 'Wind Speed (mph)'
    Regression_latitude('Northern', northern_latitude, northern_df[series_type] 
                        ,label)
    print("A slight correlation in this data indicates that the wind speed is lower near the equator")

    Regression_latitude('Southern', southern_latitude, southern_df[series_type] 
                        , label)
    print("A slight correlation in this data indicates that the wind speed is lower near the equator")
    
    
def Regression_latitude(hemispere, latitude, series, label):
    """
    Used to generate the regression plots

    Parameters
    ----------
    hemispere : TYPE: string
        DESCRIPTION. the Northern or Southern hemispher.  Used in title
    latitude : TYPE: number series
        DESCRIPTION. latitude values
    series : TYPE: number series
        DESCRIPTION. series to compare against latitude
    label : TYPE: string
        DESCRIPTION.lable to use in title and yaxis label

    Returns
    -------
    None.

    """
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
    """
    Generic method for generating latitude scatter plot

    Parameters
    ----------
    latitude : TYPE: number series
        DESCRIPTION. latitude values
    series : TYPE: number series
        DESCRIPTION. a series to compare against latitude
    label : TYPE: string
        DESCRIPTION. Used in generation of tile and ylabel

    Returns
    -------
    None.

    """
    plt.scatter(latitude, series)
    plt.title(f"{label} vs. Latitude")
    plt.xlabel('Latitude')
    plt.ylabel(label)
    plt.show()
