import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    distances = [INF] * (n + 1)
    distances[start] = 0
    heap = [(0, start)]
    prev = [-1] * (n + 1)

    while heap:
        dist, node = heapq.heappop(heap)

        if node == end:
            return dist, prev

        if distances[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                prev[next_node] = node
                heapq.heappush(heap, (cost, next_node))
            elif cost == distances[next_node] and node < prev[next_node]:
                prev[next_node] = node
                heapq.heappush(heap, (cost, next_node))

    return INF, prev

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

min_cost, prev = dijkstra(start)

if min_cost == INF:
    print(-1)
else:
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()

    print(min_cost)
    print(len(path))
    print(*path)