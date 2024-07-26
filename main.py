from Cities import allCities
from dfs import dfs
from bfs import bfs
from nn import nn
from ni import ni
from a_star import a_star
import time

# Dane problemu 
num_cities = 6
problem_type = "symmetrical" # or 'asymmetrical'
starting_city = "C"
percent_connections = 100
random_seed = 254472

# Stworzenie sieci miast
cities = allCities(num_cities, problem_type, 
                   percent_of_connections = percent_connections, 
                   random_seed=random_seed)
cities_dict = cities.return_cities()
cities.display_cities()

# print(cities_dict)

# Starting the DFS 
print("Starting DFS")
dfs_start = time.time()
dfs(current_city=starting_city, cities_dict=cities_dict, 
    visited_cities=[], whole_distance=0, starting_city=starting_city,
    print_details=False)
dfs_end = time.time()
dfs_time = dfs_end - dfs_start
print(f"Valid path found in {dfs_time:.10f}s")
print("")

# Starting the BFS 
print("Starting BFS")
start_bfs = time.time()
bfs(starting_city, cities_dict, print_details = False)
end_bfs = time.time()
bfs_time = end_bfs - start_bfs
print(f"Valid path found in {bfs_time:.10f}s")
print("")

# Starting the nn
print("Starting nn")
start_nn = time.time()
nn(current_city=starting_city, cities_dict=cities_dict, 
   visited_cities = [], whole_distance=0, starting_city=starting_city,
   print_details=False)
end_nn = time.time()
nn_time = end_nn - start_nn
print(f"Valid path found in {nn_time:.10f}s")
print("")

# Starting the ni
print("Starting ni")
start_ni = time.time()
ni(starting_city, cities_dict, print_details=False)
end_ni = time.time()
ni_time = end_ni - start_ni
print(f"Valid path found in {ni_time:.10f}s")
print("")

# Starting the a* - nearest
print("Starting a* with heuristic = 'nearest'")
start_a_star1 = time.time()
a_star(starting_city, cities_dict, heuristic_type = "nearest", print_details=False)
end_a_star1 = time.time()
a_star_time1 = end_a_star1 - start_a_star1
print(f"Valid path found in {a_star_time1:.10f}s")
print("")

# Starting the a* - average
print("Starting a* with heuristic = 'average'")
start_a_star2 = time.time()
a_star(starting_city, cities_dict, heuristic_type = "average", print_details=False)
end_a_star2 = time.time()
a_star_time2 = end_a_star2 - start_a_star2
print(f"Valid path found in {a_star_time2:.10f}s")


# add:
# nonsymetrical problem test wtf is that all about