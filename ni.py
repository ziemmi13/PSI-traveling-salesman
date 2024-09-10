from Cities import euclidean_distance

def ni(starting_city, cities_dict, problem_type, print_details=True):
    # Initialization
    unvisited_cities = set(cities_dict.keys())
    unvisited_cities.remove(starting_city)
    cycle = [starting_city, starting_city]
    whole_distance = 0

    if print_details:
        print(f"Starting city: {starting_city}")
    
    while unvisited_cities:
        # Find the closest city to any city currently in the cycle
        min_distance = float('inf')
        # Check each city in the current cycle except the last (the starting city)
        for city in cycle[:-1]:  
            city_coordinates = cities_dict[city]["coordinates"]
            for next_city in unvisited_cities:
                next_city_coordinates = cities_dict[next_city]["coordinates"]
                distance = euclidean_distance(city_coordinates, next_city_coordinates, problem_type)
                # update the nearest city
                if distance < min_distance:  
                    min_distance = distance
                    nearest_city = next_city
                    insert_after_city = city
        
        # Determine the best position to insert the nearest city into the current cycle
        best_increase = float('inf')
        best_position = None

        # Check each pair of cities in the cycle to insert the city between them
        for i in range(len(cycle) - 1):  
            current_city = cycle[i]
            next_city_in_cycle = cycle[i + 1]
            
            # Calculate the increase in distance if the nearest city is inserted between current_city and next_city_in_cycle
            increase = (euclidean_distance(cities_dict[current_city]["coordinates"], cities_dict[nearest_city]["coordinates"], problem_type) +
                        euclidean_distance(cities_dict[nearest_city]["coordinates"], cities_dict[next_city_in_cycle]["coordinates"], problem_type) -
                        euclidean_distance(cities_dict[current_city]["coordinates"], cities_dict[next_city_in_cycle]["coordinates"], problem_type))
            
            # Updating position with the minimum increase in distance
            if increase < best_increase:
                best_increase = increase
                best_position = i + 1
        
        # Insert the nearest city into the cycle at the best position
        cycle.insert(best_position, nearest_city)
        unvisited_cities.remove(nearest_city)  # Mark the nearest city as visited
        whole_distance += best_increase  # Update the total distance

        if print_details:
            print(f"Added city: {nearest_city} at position {best_position}")
            print(f"Current cycle: {cycle}")
            print(f"Whole distance so far: {whole_distance}")

    # Return to the starting city
    starting_city_coordinates = cities_dict[starting_city]["coordinates"]
    last_city_coordinates = cities_dict[cycle[-2]]["coordinates"]
    whole_distance += euclidean_distance(last_city_coordinates, starting_city_coordinates, problem_type)

    if print_details:
        print(f"\nReturning to starting city: {starting_city}")
        print("...")
        print("ni has found a valid path")
        print(f"Path: {cycle}")
        print(f"Whole distance: {whole_distance}")

    return cycle, whole_distance
