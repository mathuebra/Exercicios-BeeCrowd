def find_minimax_distance(N, M, roads):
    # Initialize the graph with infinity
    inf = float('inf')
    dist = [[inf] * N for _ in range(N)]
    
    # Distance from a city to itself is 0
    for i in range(N):
        dist[i][i] = 0
    
    # Fill in the given roads
    for u, v, w in roads:
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)
    
    # Floyd-Warshall algorithm to find all pairs shortest path
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Find the city with the minimum of the maximum distances to any other city
    minimax_distance = inf
    
    for i in range(N):
        max_dist = max(dist[i])
        minimax_distance = min(minimax_distance, max_dist)
    
    return minimax_distance

entry = input().split(' ')
for current in range(0, entry[2]):
    current_line = input().split(' ')
    u, v, w = current_line[0], current_line[1], current_line[2]
    roads.append((u, v, w))

print(find_minimax_distance(entry[0], entry[1], roads))
