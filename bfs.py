from collections import deque
from Cities import euclidean_distance

def bfs(starting_city, cities_dict, problem_type, print_details):
    all_paths = []  

    # Initialize the queue with the starting city, path (starting city), and initial distance (0).
    queue = deque([(starting_city, [starting_city], 0)])  
    num_cities = len(cities_dict.keys())  # Total number of cities to visit.

    # While the queue is not empty
    while queue:
        current_city, path, current_distance = queue.popleft() # First city from queue
        current_city_coordinates = cities_dict[current_city]["coordinates"]
        current_city_neighbors = cities_dict[current_city]["neighbors"]

        if print_details:
            print(f"\nVisiting city: {current_city}")
            print(f"Current path: {path}")
            print(f"Current distance: {current_distance}")
            print(f"Current city coordinates: {current_city_coordinates}")
            print(f"Current city neighbors: {current_city_neighbors}")

        # Explore neighbors
        for next_city in current_city_neighbors:
            if next_city not in path:
                next_city_coordinates = cities_dict[next_city]["coordinates"]
                # Calculate the distance
                distance_between_cities = euclidean_distance(current_city_coordinates, next_city_coordinates, problem_type)
                
                # Update path and distance for the new city to visit.
                new_path = path + [next_city]
                new_distance = current_distance + distance_between_cities
                
                # Add the next city to the queue for future exploration.
                queue.append((next_city, new_path, new_distance))
                
                if print_details:
                    print(f"Next city to visit: {next_city} with distance {distance_between_cities}")
                    print(f"New path: {new_path}")
                    print(f"New total distance: {new_distance}")
                    print("")

        # If we have visited all cities in this path.
        if len(path) == num_cities:
            # Go back to starting city
            last_city_coordinates = cities_dict[path[-1]]["coordinates"]
            starting_city_coordinates = cities_dict[starting_city]["coordinates"]
            distance_to_the_starting_city = euclidean_distance(last_city_coordinates, starting_city_coordinates, problem_type)
            
            complete_distance = current_distance + distance_to_the_starting_city
            complete_path = path + [starting_city]  # Add the starting city to complete the loop.
            
            all_paths.append((complete_path, complete_distance))

            if print_details:
                print(f"Returning to start city: {starting_city} with distance {distance_to_the_starting_city}")
                print(f"Complete path: {complete_path}")
                print(f"Complete distance: {complete_distance}")
                print("...")
                print("BFS has found a valid path!")

    return all_paths

# Function to find the best (shortest) path using BFS.
def bfs_find_best_path(cities_dict, starting_city, problem_type, print_details=False):
    # Get all possible paths from the BFS function.
    all_paths = bfs(starting_city, cities_dict, problem_type, print_details)
    
    # If no valid paths are found, return None.
    if not all_paths:
        print("BFS didn't find any paths")
        return None, None
    
    # Choose the best path
    best_path = min(all_paths, key=lambda x: x[1])
    
    return best_path
