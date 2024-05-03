import numpy as np
import pandas as pd

# create adjacency matrix for 5 cities
# 1. create a list of cities
cities = ['Bend', 'Medford', 'Klamath Falls', 'Reno', 'San Francisco']

# 2. create a 5x5 matrix of zeros
adjacency_matrix = np.zeros((5, 5))

# 3. fill in the matrix with distances
adjacency_matrix[0, 1] = 50
adjacency_matrix[0, 2] = 40
adjacency_matrix[1, 0] = 50
adjacency_matrix[1, 4] = 200
adjacency_matrix[2, 0] = 40
adjacency_matrix[2, 3] = 130
adjacency_matrix[3, 2] = 130
adjacency_matrix[3, 4] = 180
adjacency_matrix[4, 1] = 200
adjacency_matrix[4, 2] = 175
adjacency_matrix[4, 3] = 180

# 4. create a pandas DataFrame
df = pd.DataFrame(adjacency_matrix, index=cities, columns=cities)
print(df)

# 5. find the shortest path from Bend to San Francisco
# 5.1. create a list of cities to visit
cities_to_visit = ['Bend', 'Medford', 'Klamath Falls', 'Reno', 'San Francisco']

# 5.2. create a list of distances
distances = [0, np.inf, np.inf, np.inf, np.inf]

# 5.3. create a list of visited cities
visited_cities = []

# 5.4. create a list of previous cities
previous_cities = [None, None, None, None, None]

# 5.5. create a function to find the next city to visit
def find_next_city():
    min_distance = np.inf
    next_city = None
    for i in range(len(cities_to_visit)):
        if distances[i] < min_distance and cities_to_visit[i] not in visited_cities:
            min_distance = distances[i]
            next_city = cities_to_visit[i]
    return next_city

# 5.6. create a function to update the distances
def update_distances(city):
    city_index = cities_to_visit.index(city)
    for i in range(len(cities_to_visit)):
        if adjacency_matrix[city_index, i] > 0:
            if distances[i] > distances[city_index] + adjacency_matrix[city_index, i]:
                distances[i] = distances[city_index] + adjacency_matrix[city_index, i]
                previous_cities[i] = city

# 5.7. find the shortest path
current_city = 'Bend'
visited_cities.append(current_city)
update_distances(current_city)
while len(visited_cities) < len(cities_to_visit):
    current_city = find_next_city()
    visited_cities.append(current_city)
    update_distances(current_city)

# 5.8. print the shortest path
current_city = 'San Francisco'
shortest_path = [current_city]
while current_city != 'Bend':
    current_city = previous_cities[cities_to_visit.index(current_city)]
    shortest_path.insert(0, current_city)

print(shortest_path)
