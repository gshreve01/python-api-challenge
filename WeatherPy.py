import pandas as pd

from city_lib import (Load_Random_Cities_Locations, 
                          Load_City_Data,
                          Save_City_Data)


from weather_lib import Perform_Weather_Check

from weatherplots_lib import (Generate_Scatter_Plots,
                                 Generate_Hemispher_Plots)

northern_cities = Load_Random_Cities_Locations(0, 90)
southern_cities = Load_Random_Cities_Locations(-90, 0)
cities = pd.concat([northern_cities.head(300), southern_cities.head(300)]
                        , sort = False)

print(f"number of cities: {len(cities)}")
print(cities.head())
cities_data = perform_weather_check(cities)
save_city_data(cities_data)


    
cities_df = Load_City_Data()
print(cities_df.head())
Generate_Scatter_Plots(cities_df)
Generate_Hemispher_Plots(cities_df)

