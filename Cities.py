"""
Cities
"""

import random
import math

class allCities:
    def __init__(self, num_cities, problem_type, percent_of_connections, random_seed=None):
        self.num_cities = num_cities
        self.problem_type = problem_type
        self.random_seed = random_seed
        self.percent_of_connections  = percent_of_connections

        if random_seed is not None:
            random.seed(self.random_seed)
        self.cities = self.generate_cities()
        self.number_of_neighbours = 0

    def generate_cities(self):
        cities = {}
        for i in range(self.num_cities):
            city_name = chr(97+i).upper()
            coordinates = self.generate_coordinates()
            cities[city_name] = {"coordinates": coordinates, "neighbors": []}
        return cities

    def generate_coordinates(self):
        if self.problem_type == "symmetrical":
            x = random.randint(-100,100)
            y = random.randint(-100,100)
            return [x,y]
        elif self.problem_type == "asymmetrical":
            x = random.randint(-100,100)
            y = random.randint(-100,100)
            z = random.randint(0,50)
            return [x,y,z]
        else:
            raise ValueError("input valid problem type: 'symmetrical' or 'asymmetrical'")

    def generate_neighbors(self, city_name):
        cities_names = list(self.cities.keys())
        cities_names.remove(city_name)
        self.number_of_neighbours += len(cities_names)
        return (cities_names)

    def display_cities(self):
        print("Cities:")
        for city_name, data in self.cities.items():
            print(f"{city_name}: Coordinates = {data['coordinates']}, Neighbors = {data['neighbors']}")
        print("")
        

    def add_neighbors(self):
        for city_name in self.cities.keys():
            neighbors = self.generate_neighbors(city_name=city_name)
            self.cities[city_name]["neighbors"] = neighbors

    def return_cities(self):
        self.add_neighbors()
        if self.percent_of_connections == 80:
            self.remove_random_connections()
            return self.cities
        elif self.percent_of_connections == 100:
            return self.cities
        else:
            raise ValueError("Input valid percent_of_onnections '100' or '80'")

    def remove_random_connections(self):
        num_of_neighbors_to_delete = int(self.number_of_neighbours * 0.2)
        for _ in range(num_of_neighbors_to_delete):
            random_city_name = random.choice(list(self.cities.keys()))
            if self.cities[random_city_name]["neighbors"]:
                neighbor_to_remove = random.choice(self.cities[random_city_name]["neighbors"])
                if neighbor_to_remove in self.cities[random_city_name]["neighbors"]:
                    self.cities[random_city_name]["neighbors"].remove(neighbor_to_remove)
                else:
                    pass
                    

# # Dane problemu 
# num_cities = 5
# problem_type = "asymmetrical"
# starting_city = "A"
# percent_connections = 100
# random_seed = 254472

# # Stworzenie sieci miast
# cities = allCities(num_cities, problem_type, percent_of_connections = 80, random_seed=random_seed)
# cities_dict = cities.return_cities()
# cities.display_cities()

# print(cities_dict)