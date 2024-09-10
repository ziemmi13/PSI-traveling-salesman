# Example usage
from Cities import allCities
from aco import AntCities
import time
from a_star import a_star


# Dane problemu 
num_cities = 5 
problem_type = "symmetrical" # or 'asymmetrical'
starting_city = "A"
percent_connections = 100
random_seed = 254472


# Creating cities
cities = allCities(num_cities, problem_type, 
                   percent_of_connections = percent_connections, 
                   random_seed=random_seed)
cities_dict = cities.return_cities()
cities.display_cities()


# Starting the a* - nearest
print("Starting a* with heuristic = 'nearest'")
start_a_star1 = time.time()
a_star_path1, astar_cost1, heuristic_type1 = a_star(starting_city, 
                                              cities_dict, 
                                              problem_type=problem_type, 
                                              heuristic_type = "nearest", 
                                              print_details=False)
end_a_star1 = time.time()
a_star_time1 = end_a_star1 - start_a_star1
print("\nValid path found:")
print(a_star_path1)
print(f"With a total distance of: {astar_cost1}")
print(f"Valid path found in {a_star_time1:.10f}s")
print("")