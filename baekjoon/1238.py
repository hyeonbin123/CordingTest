import heapq

def dijkstra(start, graph):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

N, M, X = map(int, input().split())

graph = {i: {} for i in range(1, N + 1)}
reverse_graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start][end] = time
    reverse_graph[end][start] = time

from_party = dijkstra(X, graph)

to_party = dijkstra(X, reverse_graph)

max_time = 0
for i in range(1, N + 1):
    total_time = from_party[i] + to_party[i]
    max_time = max(max_time, total_time)

print(max_time)