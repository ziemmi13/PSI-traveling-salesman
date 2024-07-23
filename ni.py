import numpy as np

# Funkcja do obliczania odległości euklidesowej między dwoma miastami
def euclidean_distance(city1_coordinates, city2_coordinates):
    dist = np.linalg.norm(np.array(city1_coordinates) - np.array(city2_coordinates))
    return dist

# Algorytm "Nearest Insertion"
def ni(starting_city, cities_dict, print_details=True):
    unvisited_cities = set(cities_dict.keys())
    unvisited_cities.remove(starting_city)
    cycle = [starting_city, starting_city]
    whole_distance = 0

    if print_details:
        print(f"Starting city: {starting_city}")
    
    while unvisited_cities:
        # Znajdź najbliższe miasto do dowolnego miasta w cyklu
        min_distance = float('inf')
        for city in cycle[:-1]:
            city_coordinates = cities_dict[city]["coordinates"]
            for next_city in unvisited_cities:
                next_city_coordinates = cities_dict[next_city]["coordinates"]
                distance = euclidean_distance(city_coordinates, next_city_coordinates)
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = next_city
                    insert_after_city = city
        
        # Wstaw najbliższe miasto do cyklu w najlepszym miejscu
        best_increase = float('inf')
        best_position = None
        for i in range(len(cycle) - 1):
            current_city = cycle[i]
            next_city_in_cycle = cycle[i + 1]
            increase = (euclidean_distance(cities_dict[current_city]["coordinates"], cities_dict[nearest_city]["coordinates"]) +
                        euclidean_distance(cities_dict[nearest_city]["coordinates"], cities_dict[next_city_in_cycle]["coordinates"]) -
                        euclidean_distance(cities_dict[current_city]["coordinates"], cities_dict[next_city_in_cycle]["coordinates"]))
            if increase < best_increase:
                best_increase = increase
                best_position = i + 1
        
        cycle.insert(best_position, nearest_city)
        unvisited_cities.remove(nearest_city)
        whole_distance += best_increase

        if print_details:
            print(f"Added city: {nearest_city} at position {best_position}")
            print(f"Current cycle: {cycle}")
            print(f"Whole distance so far: {whole_distance}")

    # Dodaj powrót do miasta początkowego
    starting_city_coordinates = cities_dict[starting_city]["coordinates"]
    last_city_coordinates = cities_dict[cycle[-2]]["coordinates"]
    whole_distance += euclidean_distance(last_city_coordinates, starting_city_coordinates)

    if print_details:
        print(f"\nReturning to starting city: {starting_city}")
    
    print("...")
    print("ni has found a valid path")
    print(f"Path: {cycle}")
    print(f"Whole distance: {whole_distance}")
