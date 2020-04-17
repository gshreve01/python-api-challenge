# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:06:17 2020

Responsible for testing Vacation requirements

@author: gshre
"""

from city_lib import (Find_Ideal_Cities, Load_City_Data)
from vacations_lib import Find_Motels_For_Cities
from vacationplots_lib import heatmap_plot

cities_df = Load_City_Data()
ideal_cities = Find_Ideal_Cities(cities_df)
hotels = Find_Motels_For_Cities(ideal_cities)
heatmap_plot(hotels)
