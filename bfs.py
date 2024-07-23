from Cities import allCities
import numpy as np
from collections import deque

def euclidean_distance(city1_coordinates, city2_coordinates):
    dist = np.linalg.norm(np.array(city1_coordinates) - np.array(city2_coordinates))
    return dist

def bfs(starting_city, cities_dict, print_details):
    visited_cities = []
    queue = deque([starting_city])
    whole_distance = 0
    visited_set = set()

    while queue:
        current_city = queue.popleft()
        if current_city in visited_set:
            continue
        visited_set.add(current_city)
        visited_cities.append(current_city)
        current_city_coordinates = cities_dict[current_city]["coordinates"]
        current_city_neighbors = cities_dict[current_city]["neighbors"]

        if print_details is True:
            print(f"\nVisiting city: {current_city}")
            print(f"Visited cities: {visited_cities}")
            print(f"Current city coordinates: {current_city_coordinates}")
            print(f"Current city neighbors: {current_city_neighbors}")

        for next_city in current_city_neighbors:
            if next_city not in visited_set:
                next_city_coordinates = cities_dict[next_city]["coordinates"]
                distance_between_cities = euclidean_distance(current_city_coordinates, next_city_coordinates)
                queue.append(next_city)
                whole_distance += distance_between_cities
                if print_details is True:
                    print(f"Next city to visit: {next_city} with distance {distance_between_cities}")
                    print(f"Whole distance: {whole_distance}")

    # Zakonczenie, gdy wszystkie miasta są odwiedzone
    last_city_coordinates = current_city_coordinates
    starting_city_coordinates = cities_dict[starting_city]["coordinates"]
    distance_to_the_starting_city = euclidean_distance(last_city_coordinates, starting_city_coordinates)
    whole_distance += distance_to_the_starting_city

    if print_details is True:
        print(f"Coming back to start city: {starting_city} with distance {distance_to_the_starting_city}")
        print(f"Whole distance: {whole_distance}")

    visited_cities.append(starting_city)
    print("...")
    print("BFS has found a valid path!")
    print(f"Path: {visited_cities}")
    print(f"Whole distance: {whole_distance}")

