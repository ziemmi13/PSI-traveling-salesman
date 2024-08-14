from Cities import allCities
from dfs import dfs_find_best_path
from bfs import bfs_find_best_path
from nn import nn
from ni import ni
from a_star import a_star
import time
from aco import AntCities
import pandas as pd

# Dane problemu 
num_cities = 6 #10 is where my computer starts to hate me
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


# Starting the DFS 
print("Starting DFS")
dfs_start = time.time()
dfs_best_path, dfs_best_distance = dfs_find_best_path(cities_dict=cities_dict, 
                                                      starting_city=starting_city, 
                                                      problem_type=problem_type,
                                                      print_details=False)
dfs_end = time.time()
print("\nBest path found:")
print(dfs_best_path)
print(f"With a total distance of: {dfs_best_distance}")
dfs_time = dfs_end - dfs_start
print(f"Valid path found in {dfs_time:.10f}s")
print("")

# Starting the BFS 
print("Starting BFS")
start_bfs = time.time()
bfs_best_path, dfs_best_distance = bfs_find_best_path(cities_dict=cities_dict, 
                                                      starting_city=starting_city, 
                                                      problem_type=problem_type,
                                                      print_details=False
                                                      )
end_bfs = time.time()
print("\nBest path found:")
print(bfs_best_path)
print(f"With a total distance of: {dfs_best_distance}")
bfs_time = end_bfs - start_bfs
print(f"Valid path found in {bfs_time:.10f}s")
print("")

# Starting the nn
print("Starting nn")
start_nn = time.time()
nn_path, nn_distance = nn(current_city=starting_city, 
                                       cities_dict=cities_dict, 
                                       visited_cities = [], 
                                       whole_distance=0, 
                                       starting_city=starting_city,
                                       problem_type=problem_type,
                                       print_details=True)
end_nn = time.time()
nn_time = end_nn - start_nn
print("\nValid path found:")
print(nn_path)
print(f"With a total distance of: {nn_distance}")
print(f"Valid path found in {nn_time:.10f}s")
print("")

# Starting the ni
print("Starting ni")
start_ni = time.time()
ni_path, ni_distance = ni(starting_city, 
                          cities_dict, 
                          problem_type, 
                          print_details=False)
end_ni = time.time()
ni_time = end_ni - start_ni
print("\nValid path found:")
print(ni_path)
print(f"With a total distance of: {ni_distance}")
print(f"Valid path found in {ni_time:.10f}s")
print("")

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

# Starting the a* - average
print("Starting a* with heuristic = 'average'")
start_a_star2 = time.time()
a_star_path2, astar_cost2, heuristic_type2 = a_star(starting_city, 
                                                    cities_dict, 
                                                    problem_type=problem_type, 
                                                    heuristic_type = "average", 
                                                    print_details=False)
end_a_star2 = time.time()
a_star_time2 = end_a_star2 - start_a_star2
print("\nValid path found:")
print(a_star_path2)
print(f"With a total distance of: {astar_cost2}")
print(f"Valid path found in {a_star_time2:.10f}s")
print("")


# Starting aco
print("Starting aco")

ant_cities = AntCities(num_cities, 
                       problem_type, 
                       percent_connections, 
                       random_seed)
cities = ant_cities.return_cities()

# Parameters for ACO
n_ants = 50
n_iterations = 50
alpha = 1.0  # Influence of pheromone
beta = 2.0   # Influence of distance
evaporation_rate = 0.5
Q = 10

# Run ACO

start_aco = time.time()
aco_path, aco_path_length = ant_cities.ant_colony_optimization(n_ants, 
                                                               n_iterations, 
                                                               alpha, 
                                                               beta, 
                                                               evaporation_rate, 
                                                               Q, 
                                                               starting_city=starting_city)
end_aco = time.time()
aco_time = end_aco - start_aco

print(f"ACO has found a valid path:")
print(f"Path: {aco_path}")
print(f"Path cost: {aco_path_length}")
print(f"Valid path found in {aco_time:.10f}s")
print("")

# dataframe visualization
print("DATAFRAME RESULTS:")
results = {
    'Algorithm': ['DFS', 'BFS', 'Nearest Neighbor', 'Nearest Insertion', 'A* (Nearest)', 'A* (Average)', 'ACO'],
    'Best Path': [dfs_best_path, bfs_best_path, nn_path, ni_path, a_star_path1, a_star_path2, aco_path],
    'Total Distance': [dfs_best_distance, dfs_best_distance, nn_distance, ni_distance, astar_cost1, astar_cost2, aco_path_length],
    'Execution Time (s)': [dfs_time, bfs_time, nn_time, ni_time, a_star_time1, a_star_time2, aco_time]
}

df_results = pd.DataFrame(results)
print(df_results)


# add:
# error handling for too many iterations
