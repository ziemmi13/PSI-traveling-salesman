from Cities import allCities
import math
import numpy as np

# Dane problemu 
num_cities = 5
problem_type = "asymmetrical"
starting_city = "A"
percent_connections = 100
random_seed = 254472

# Stworzenie sieci miast
cities = allCities(num_cities, problem_type, percent_of_connections = 80, random_seed=random_seed)
cities_dict = cities.return_cities()
cities.display_cities()

print(cities_dict)