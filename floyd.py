def floyd(graph):
    n = len(graph)
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    next = [[None for _ in range(n)] for _ in range(n)]

    # Initialize distance matrix and next matrix
    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
                next[i][j] = j

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next


# Example graph represented by adjacency matrix
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'),4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

# Calculate the shortest path distances and next matrix
distances, next_nodes = floyd(graph)

# Print the resulting distance matrix
print("Shortest path distances:")
for row in distances:
    print(row)

# Print the resulting next matrix
print("\nNext nodes in the shortest path:")
for row in next_nodes:
    print(row)
