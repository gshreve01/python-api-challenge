# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:26:58 2020

Functions dedicated to plots related to vacation requirement

@author: gshre
"""
from api_keys import g_key
from matplotlib.pyplot import plot, show
import gmaps

info_box_template = "'"
gmaps.configure(api_key=g_key)


def heatmap_plot(hotels):
    """
    Generates a heatmap of the ideal cities

    Parameters
    ----------
    ideal_cities : TYPE: DataFrame
        DESCRIPTION. : ideal cities subset of entire cities sample based 
                        on the humidity

    Returns
    -------
    None.

    """
    
    print("generating heatmap plots hotels")
    hotel_locations = [(hotel["lat"], hotel["lng"]) for hotel in hotels]

    motel_info = [hotel["name"] for hotel in hotels]

    
    heat_layer = gmaps.heatmap_layer(hotel_locations,
                                 dissipating=False, max_intensity=100,
                                 point_radius = 5) 
    
    # marker_layer = gmaps.marker_layer(motel_locations,
    #                              info_box_content=motel_info)
    fig = gmaps.figure()
    fig.add_layer(heat_layer)
    # fig.add_layer(marker_layer)
    
    print("generation complete")
    show(block=False)
