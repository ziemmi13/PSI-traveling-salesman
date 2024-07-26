import heapq
import numpy as np
from Cities import allCities


def euclidean_distance(city1_coordinates, city2_coordinates):
    return np.linalg.norm(np.array(city1_coordinates) - np.array(city2_coordinates))

def nearest_city_heuristic(current_city_coordinates, unvisited_cities, cities_dict):
    """
    Nieadmisowalna heurystyka (inadmissible heuristic)
    Ta heurystyka oblicza minimalną odległość do najbliższego nieodwiedzonego miasta.
    Jest podatna na przeszacowanie rzeczywistego kosztu pozostałej trasy, ponieważ skupia się tylko na najbliższym mieście, 
    a nie na całkowitym koszcie podróży.
    
    Args:
        current_city_coordinates (list): Koordynaty obecnego miasta.
        unvisited_cities (list): Lista nieodwiedzonych miast.
        cities_dict (dict): Słownik zawierający dane wszystkich miast, ich koordynaty oraz sąsiadów.

    Returns:
        float: Minimalna odległość do najbliższego nieodwiedzonego miasta.
    """
    if not unvisited_cities:
        return 0
    min_distance = float('inf')
    for city in unvisited_cities:
        city_coordinates = cities_dict[city]["coordinates"]
        dist = euclidean_distance(current_city_coordinates, city_coordinates)
        if dist < min_distance:
            min_distance = dist
    return min_distance

def average_distance_heuristic(current_city_coordinates, visited_cities, total_distance, cities_dict):
    """
    Admisowalna heurystyka (admissible heuristic)
    Ta heurystyka oblicza średnią odległość na podstawie przebytej już trasy.
    Jest admisowalna, ponieważ nigdy nie przeszacowuje rzeczywistego kosztu pozostałej trasy.
    
    Args:
        current_city_coordinates (list): Koordynaty obecnego miasta.
        visited_cities (list): Lista odwiedzonych miast.
        total_distance (float): Całkowita odległość przebyta do tej pory.
        cities_dict (dict): Słownik zawierający dane wszystkich miast, ich koordynaty oraz sąsiadów.

    Returns:
        float: Szacunkowy koszt pozostałej trasy.
    """
    num_visited_edges = len(visited_cities) - 1
    if num_visited_edges == 0:
        return 0
    average_distance = total_distance / num_visited_edges
    num_unvisited_cities = len(cities_dict) - len(visited_cities)
    estimated_remaining_edges = num_unvisited_cities + 1
    return average_distance * estimated_remaining_edges

def a_star(starting_city, cities_dict, heuristic_type='nearest', print_details=False):
    """
    Algorytm A* do znalezienia najkrótszej trasy dla problemu komiwojażera (TSP).
    
    Args:
        starting_city (str): Nazwa miasta początkowego.
        cities_dict (dict): Słownik zawierający dane wszystkich miast, ich koordynaty oraz sąsiadów.
        heuristic_type (str): Typ używanej heurystyki ('nearest' lub 'average').
        print_details (bool): Flaga określająca, czy szczegóły przetwarzania mają być drukowane.

    Returns:
        tuple: Najkrótsza trasa (lista miast) i całkowita odległość.
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, starting_city, [starting_city], 0))

    while priority_queue:
        estimated_cost, current_city, path, current_cost = heapq.heappop(priority_queue)
        
        if len(path) == len(cities_dict):
            return_to_start_cost = euclidean_distance(cities_dict[current_city]["coordinates"], cities_dict[starting_city]["coordinates"])
            total_cost = current_cost + return_to_start_cost
            path.append(starting_city)
            if print_details:
                print(f"A* with {heuristic_type} heuristic has found the shortest path!")
                print(f"Path: {path}")
                print(f"Total distance: {total_cost}")
            return path, total_cost

        current_city_coordinates = cities_dict[current_city]["coordinates"]
        for neighbor in cities_dict[current_city]["neighbors"]:
            if neighbor not in path:
                neighbor_coordinates = cities_dict[neighbor]["coordinates"]
                travel_cost = euclidean_distance(current_city_coordinates, neighbor_coordinates)
                new_cost = current_cost + travel_cost
                new_path = path + [neighbor]
                unvisited_cities = [city for city in cities_dict if city not in new_path]
                
                if heuristic_type == 'nearest':
                    heuristic_cost = nearest_city_heuristic(current_city_coordinates, unvisited_cities, cities_dict)
                elif heuristic_type == 'average':
                    heuristic_cost = average_distance_heuristic(current_city_coordinates, new_path, new_cost, cities_dict)
                else:
                    raise ValueError("Unknown heuristic type. Use 'nearest' or 'average'.")
                
                estimated_total_cost = new_cost + heuristic_cost
                heapq.heappush(priority_queue, (estimated_total_cost, neighbor, new_path, new_cost))
                if print_details:
                    print(f"Exploring city: {neighbor}, Estimated total cost: {estimated_total_cost}, New path: {new_path}")

# Example usage:
num_cities = 5
problem_type = 'symmetrical'
percent_of_connections = 100
random_seed = 42

cities_instance = allCities(num_cities, problem_type, percent_of_connections, random_seed)
cities_dict = cities_instance.return_cities()

# Display generated cities with coordinates and neighbors
cities_instance.display_cities()

starting_city = 'A'
heuristic_type = 'nearest'  # or 'average'
path, total_distance = a_star(starting_city, cities_dict, heuristic_type, print_details=True)
print(f"Shortest path: {path}")
print(f"Total distance: {total_distance}")
