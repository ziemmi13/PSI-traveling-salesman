import heapq
from Cities import euclidean_distance

def nearest_city_heuristic(current_city_coordinates, unvisited_cities, cities_dict, problem_type):
    """
    Inadmissible heuristic - prone to overestimate the real cost of the path
    """
    if not unvisited_cities:
        return 0
    min_distance = float('inf')
    for city in unvisited_cities:
        city_coordinates = cities_dict[city]["coordinates"]
        dist = euclidean_distance(current_city_coordinates, city_coordinates, problem_type)
        if dist < min_distance:
            min_distance = dist
    return min_distance

def average_distance_heuristic(current_city_coordinates, visited_cities, total_distance, cities_dict):
    """"
    Admissible heuristic - doesn't overestimate the real cost of the path
    """
    num_visited_edges = len(visited_cities) - 1
    if num_visited_edges == 0:
        return 0
    average_distance = total_distance / num_visited_edges
    num_unvisited_cities = len(cities_dict) - len(visited_cities)
    estimated_remaining_edges = num_unvisited_cities + 1
    return average_distance * estimated_remaining_edges

def a_star(starting_city, cities_dict, problem_type, heuristic_type='nearest', print_details=False):
    priority_queue = []
    heapq.heappush(priority_queue, (0, starting_city, [starting_city], 0))

    if print_details:
        print(f"Starting A* with heuristic = '{heuristic_type}'")
        print("INITIALIZING")
        print(priority_queue)
        print("")

    best_path = None
    best_cost = float('inf')

    while priority_queue:
        estimated_cost, current_city, path, current_cost = heapq.heappop(priority_queue)

        if print_details:
            print(f"Evaluating city: {current_city}, Current Path: {path}, Current Cost: {current_cost}")

        if len(path) == len(cities_dict):  # if all cities are visited, come back to starting city
            return_to_start_cost = euclidean_distance(cities_dict[current_city]["coordinates"], cities_dict[starting_city]["coordinates"], problem_type)
            total_cost = current_cost + return_to_start_cost
            path.append(starting_city)

            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path

            if print_details:
                print("\nFound complete path:")
                print(f"Path: {path}")
                print(f"Total Distance: {total_cost}\n")

            continue

        current_city_coordinates = cities_dict[current_city]["coordinates"]
        for neighbor in cities_dict[current_city]["neighbors"]:
            if neighbor not in path:
                neighbor_coordinates = cities_dict[neighbor]["coordinates"]
                travel_cost = euclidean_distance(current_city_coordinates, neighbor_coordinates, problem_type)
                g_cost = current_cost + travel_cost  # current cost to given neighbor
                new_path = path + [neighbor]
                unvisited_cities = [city for city in cities_dict if city not in new_path]

                # heuristic cost
                if heuristic_type == 'nearest':
                    h_cost = nearest_city_heuristic(current_city_coordinates, unvisited_cities, cities_dict, problem_type)
                elif heuristic_type == 'average':
                    h_cost = average_distance_heuristic(current_city_coordinates, new_path, g_cost, cities_dict)
                else:
                    raise ValueError("Unknown heuristic type. Use 'nearest' or 'average'.")

                f_cost = g_cost + h_cost  # estimated total cost

                heapq.heappush(priority_queue, (f_cost, neighbor, new_path, g_cost))

                if print_details:
                    print(f"Exploring neighbor {neighbor}")
                    print(f"Heuristic cost ({heuristic_type}): {h_cost}")
                    print(f"Updated Priority Queue: {priority_queue}\n")

    if print_details:
        print(f"Final Path Found: {best_path}")
        print(f"Total Cost: {best_cost}\n")

    return best_path, best_cost, heuristic_type
