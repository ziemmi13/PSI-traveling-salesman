import numpy as np

def euclidean_distance(city1_coordinates, city2_coordinates):
    dist = np.linalg.norm(np.array(city1_coordinates) - np.array(city2_coordinates))
    return dist

def dfs(current_city, cities_dict, visited_cities, whole_distance, starting_city, print_details):
    visited_cities.append(current_city)
    current_city_coordinates = cities_dict[current_city]["coordinates"]
    current_city_neighbors = cities_dict[current_city]["neighbors"]
    num_cities = len(cities_dict.keys())

    if print_details is True:
        print(f"\nVisiting city: {current_city}")
        print(f"Visited cities: {visited_cities}")
        print(f"Current city coordinates: {current_city_coordinates}")
        print(f"Current city neighbors: {current_city_neighbors}")

    for next_city in current_city_neighbors:
        if next_city not in visited_cities:
            next_city_coordinates = cities_dict[next_city]["coordinates"]
            distance_between_cities = euclidean_distance(current_city_coordinates, next_city_coordinates)
            whole_distance += distance_between_cities
            if print_details is True:
                print(f"Next city to visit: {next_city} with distance {distance_between_cities}")
                print(f"Whole distance: {whole_distance}")
            dfs(next_city, cities_dict, visited_cities, whole_distance, starting_city, print_details)

    # Warunek końcowy, gdy wszystkie miasta są odwiedzone
    if len(visited_cities) == num_cities:
        last_city_coordinates = current_city_coordinates
        starting_city_coordinates = cities_dict[starting_city]["coordinates"]
        distance_to_the_starting_city = euclidean_distance(last_city_coordinates, starting_city_coordinates)
        whole_distance += distance_to_the_starting_city

        if print_details is True:
            print(f"Coming back to start city: {starting_city} with distance {distance_to_the_starting_city}")
            print(f"Whole distance: {whole_distance}")
        visited_cities.append(starting_city)
        print("...")
        print("DFS has found a valid path!")
        print(f"Path: {visited_cities}")
        print(f"Whole distance: {whole_distance}")


