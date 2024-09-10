from Cities import euclidean_distance

def dfs(current_city, cities_dict, visited_cities, whole_distance, starting_city, problem_type, print_details, all_paths):
    # Mark the current city as visited by appending it to the visited_cities list.
    visited_cities.append(current_city)
    
    # Get the coordinates and neighbors of the current city.
    current_city_coordinates = cities_dict[current_city]["coordinates"]
    current_city_neighbors = cities_dict[current_city]["neighbors"]
    
    # Total number of cities to visit.
    num_cities = len(cities_dict.keys())

    if print_details:
        print(f"\nVisiting city: {current_city}")
        print(f"Visited cities: {visited_cities}")
        print(f"Current city coordinates: {current_city_coordinates}")
        print(f"Current city neighbors: {current_city_neighbors}")

    # Explore the neighbors
    for next_city in current_city_neighbors:
        # Visit the city if it hasn't been visited yet.
        if next_city not in visited_cities:
            next_city_coordinates = cities_dict[next_city]["coordinates"]
            # Calculate the distance 
            distance_between_cities = euclidean_distance(current_city_coordinates, next_city_coordinates, problem_type)
            # Recursive DFS call for the next city, with updated path and distance.
            dfs(next_city, cities_dict, visited_cities[:], whole_distance + distance_between_cities, starting_city, problem_type, print_details, all_paths)

    # If all cities visited go back to tartsing city
    if len(visited_cities) == num_cities:
        last_city_coordinates = current_city_coordinates
        starting_city_coordinates = cities_dict[starting_city]["coordinates"]
        distance_to_the_starting_city = euclidean_distance(last_city_coordinates, starting_city_coordinates, problem_type)
        whole_distance += distance_to_the_starting_city
        visited_cities.append(starting_city)

        if print_details:
            print(f"Coming back to start city: {starting_city} with distance {distance_to_the_starting_city}")
            print(f"Whole distance: {whole_distance}")
            print("...")
            print("DFS has found a valid path!")
            print(f"Path: {visited_cities}")
            print(f"Whole distance: {whole_distance}")
        
        all_paths.append((visited_cities, whole_distance))

        if print_details:
            print("\nAll paths:")
            print(all_paths)
            print("")

    # Return the visited cities and the total distance for the current path (used in recursive calls).
    return visited_cities, whole_distance

# Function to find the best (shortest) path using DFS.
def dfs_find_best_path(cities_dict, starting_city, problem_type, print_details):
    all_paths = []  
    dfs(starting_city, cities_dict, [], 0, starting_city, problem_type, print_details, all_paths)
    
    # If no valid paths are found, return None.
    if not all_paths:
        print("DFS didn't find any paths")
        return None, None
    
    # Choose the best path
    best_path = min(all_paths, key=lambda x: x[1])
    
    return best_path
