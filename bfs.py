from collections import deque
from Cities import euclidean_distance

def bfs(starting_city, cities_dict, problem_type, print_details):
    all_paths = []
    # initialize queue with (current_city, path, total_distance)
    queue = deque([(starting_city, [starting_city], 0)])  
    num_cities = len(cities_dict.keys())

    # while queue not empty
    while queue:
        # print(queue)
        current_city, path, current_distance = queue.popleft() # pierwsze miasto z kolejki
        current_city_coordinates = cities_dict[current_city]["coordinates"]
        current_city_neighbors = cities_dict[current_city]["neighbors"]

        if print_details:
            print(f"\nVisiting city: {current_city}")
            print(f"Current path: {path}")
            print(f"Current distance: {current_distance}")
            print(f"Current city coordinates: {current_city_coordinates}")
            print(f"Current city neighbors: {current_city_neighbors}")

        for next_city in current_city_neighbors:
            if next_city not in path:
                next_city_coordinates = cities_dict[next_city]["coordinates"]
                distance_between_cities = euclidean_distance(current_city_coordinates, next_city_coordinates, problem_type)
                new_path = path + [next_city]
                new_distance = current_distance + distance_between_cities
                queue.append((next_city, new_path, new_distance))
                if print_details:
                    print(f"Next city to visit: {next_city} with distance {distance_between_cities}")
                    print(f"New path: {new_path}")
                    print(f"New total distance: {new_distance}")
                    print("")

        # If all the cities are visited
        if len(path) == num_cities:
            last_city_coordinates = cities_dict[path[-1]]["coordinates"]
            starting_city_coordinates = cities_dict[starting_city]["coordinates"]
            distance_to_the_starting_city = euclidean_distance(last_city_coordinates, starting_city_coordinates,problem_type)
            complete_distance = current_distance + distance_to_the_starting_city
            complete_path = path + [starting_city]
            all_paths.append((complete_path, complete_distance))

            if print_details:
                print(f"Returning to start city: {starting_city} with distance {distance_to_the_starting_city}")
                print(f"Complete path: {complete_path}")
                print(f"Complete distance: {complete_distance}")
                print("...")
                print("BFS has found a valid path!")

    return all_paths

def bfs_find_best_path(cities_dict, starting_city, problem_type, print_details=False):
    all_paths = bfs(starting_city, cities_dict, problem_type, print_details)
    if not all_paths:
        print("bfs didn't find any paths")
        return None, None
    best_path = min(all_paths, key=lambda x: x[1])
    return best_path
