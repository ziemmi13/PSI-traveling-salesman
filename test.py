# Example usage
from Cities import allCities
from aco import AntCities

# Create the cities
num_cities = 5
problem_type = "symmetrical"  # Change to "asymmetrical" if needed
percent_of_connections = 80
random_seed = 42

# Instantiate AntCities
ant_cities = AntCities(num_cities, problem_type, percent_of_connections, random_seed)

# Initialize cities and neighbors
cities = ant_cities.return_cities()
# ant_cities.display_cities()

# Parameters for ACO
n_ants = 100
n_iterations = 100
alpha = 1.0  # Influence of pheromone
beta = 2.0   # Influence of distance
evaporation_rate = 0.5
Q = 100

# Run ACO
path, path_length = ant_cities.ant_colony_optimization(n_ants, n_iterations, alpha, beta, evaporation_rate, Q, starting_city="E")

print(f"ACO has found a valid path:")
print(f"Path: {path}")
print(f"Path cost: {path_length}")
