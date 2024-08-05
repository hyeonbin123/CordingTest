import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, n):
    visited = [-1] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = 0
    max_node, max_dist = start, 0

    while queue:
        node, dist = queue.popleft()
        for next_node, next_dist in graph[node]:
            if visited[next_node] == -1:
                new_dist = dist + next_dist
                visited[next_node] = new_dist
                queue.append((next_node, new_dist))
                if new_dist > max_dist:
                    max_node, max_dist = next_node, new_dist

    return max_node, max_dist

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    info = list(map(int, input().split()))
    node = info[0]
    for i in range(1, len(info) - 1, 2):
        graph[node].append((info[i], info[i+1]))

farthest_node, _ = bfs(1, n)

_, diameter = bfs(farthest_node, n)

print(diameter)