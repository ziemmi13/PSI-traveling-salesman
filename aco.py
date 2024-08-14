import random
import numpy as np
from Cities import allCities, euclidean_distance

class AntCities(allCities):
    def __init__(self, num_cities, problem_type, percent_of_connections, random_seed=None):
        super().__init__(num_cities, problem_type, percent_of_connections, random_seed)
        self.pheromone = None

    def initialize_pheromone(self):
        n = len(self.cities)
        self.pheromone = np.ones((n, n)) * 1e-10  # Initialize pheromone to a small value for all city pairs (0 caused errors)
        for i in range(n):
            city1 = chr(i + ord("A"))
            for j in range(n):
                city2 = chr(j + ord("A"))
                if city2 in self.cities[city1]["neighbors"]:
                    self.pheromone[i][j] = 1
        # print("Initializing pheromone")
        # print(self.pheromone)

    def update_pheromone(self, paths, path_lengths, Q, evaporation_rate):
        # Q regulates the ammount of ferromone added to edges
        # Apply evaporation
        self.pheromone *= evaporation_rate

        for path, path_length in zip(paths, path_lengths):
            for i in range(len(path)):
                city1_idx = ord(path[i]) - 65
                city2_idx = ord(path[(i + 1) % len(path)]) - 65
                self.pheromone[city1_idx, city2_idx] += Q / path_length

    def get_pheromone(self, city1_idx, city2_idx):
        return self.pheromone[city1_idx, city2_idx]

    def get_distance(self, city1, city2):
        coords1 = self.cities[city1]["coordinates"]
        coords2 = self.cities[city2]["coordinates"]
        return euclidean_distance(coords1, coords2, self.problem_type)

    def ant_colony_optimization(self, n_ants, n_iterations, alpha, beta, evaporation_rate, Q, starting_city):
        if starting_city not in self.cities:
            raise ValueError(f"Starting city {starting_city} is not in the list of cities")

        # Initialization
        self.initialize_pheromone()
        best_path = None
        best_path_length = np.inf

        for iteration in range(n_iterations):
            paths = []
            path_lengths = []

            for _ in range(n_ants):
                visited = [False] * len(self.cities)
                current_city = starting_city
                visited[ord(current_city) - 65] = True
                path = [current_city]
                path_length = 0

                while len(path) < len(self.cities):
                    unvisited = [city for city in self.cities.keys() if not visited[ord(city) - 65]]
                    probabilities = np.zeros(len(unvisited))

                    for i, unvisited_city in enumerate(unvisited):
                        city_idx = ord(current_city) - 65
                        next_city_idx = ord(unvisited_city) - 65
                        pheromone_level = self.get_pheromone(city_idx, next_city_idx)
                        distance = self.get_distance(current_city, unvisited_city)
                        probabilities[i] = (pheromone_level ** alpha) / (distance ** beta)
                    
                    probabilities /= np.sum(probabilities)
                    next_city = np.random.choice(unvisited, p=probabilities)
                    
                    path.append(next_city)
                    path_length += self.get_distance(current_city, next_city)
                    visited[ord(next_city) - 65] = True
                    current_city = next_city

                # Add return distance to the starting city
                path_length += self.get_distance(path[-1], starting_city)
                path.append(starting_city)  # Ensure the path includes the starting city at the end
                paths.append(path)
                path_lengths.append(path_length)

                if path_length < best_path_length:
                    best_path = path
                    best_path_length = path_length

            self.update_pheromone(paths, path_lengths, Q, evaporation_rate)

        return best_path, best_path_length
