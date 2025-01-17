from Cities import euclidean_distance

def nn(current_city, cities_dict, visited_cities, whole_distance, starting_city, problem_type, print_details):
    visited_cities.append(current_city)
    current_city_coordinates = cities_dict[current_city]["coordinates"]
    current_city_neighbors = cities_dict[current_city]["neighbors"]

    if print_details is True:
        print(f"\nVisiting city: {current_city}")
        print(f"Visited cities: {visited_cities}")
        print(f"Current city coordinates: {current_city_coordinates}")
        print(f"Current city neighbors: {current_city_neighbors}")

    distances = []
    for next_city in current_city_neighbors:
        # If the city hasn't been visited yet, calculate the distance.
        if next_city not in visited_cities:
            next_city_coordinates = cities_dict[next_city]["coordinates"]
            # Calculate the distance
            distance_between_cities = euclidean_distance(current_city_coordinates, next_city_coordinates, problem_type)
            distances.append([distance_between_cities, next_city])

    # If there are unvisited neighbors 
    if distances:
        # Find the nearest unvisited city.
        min_distance, closest_city = min(distances, key=lambda x: x[0])
        whole_distance += min_distance

        if print_details is True:
            print(f"Next city to visit: {closest_city} with distance {min_distance}")   
            print(f"Whole distance: {whole_distance}")

        # Recursively visit the next closest city.
        return nn(closest_city, cities_dict, visited_cities, whole_distance, starting_city, problem_type, print_details)
    
    # If all neighbors have been visited goback to the starting city
    else:  
        last_city = current_city
        last_city_coordinates = current_city_coordinates
        starting_city_coordinates = cities_dict[starting_city]["coordinates"]

        
        distance_to_the_starting_city = euclidean_distance(last_city_coordinates, starting_city_coordinates, problem_type)
        whole_distance += distance_to_the_starting_city

        if print_details is True:
            print(f"Coming back to start city: {starting_city} with distance {distance_to_the_starting_city}")
            print(f"Whole distance: {whole_distance}")
            visited_cities.append(starting_city)
            print("...")
            print("NN has found a valid path!")
            print(f"Path: {visited_cities}")
            print(f"Whole distance: {whole_distance}")

        return visited_cities, whole_distance
