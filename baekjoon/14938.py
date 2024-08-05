import sys
input = sys.stdin.readline
INF = float('inf')

def floyd_warshall(n, graph):
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for a, b, l in graph:
        dist[a][b] = min(dist[a][b], l)
        dist[b][a] = min(dist[b][a], l)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def max_items(n, m, items, dist):
    max_sum = 0
    for i in range(1, n+1):
        item_sum = sum(items[j] for j in range(1, n+1) if dist[i][j] <= m)
        max_sum = max(max_sum, item_sum)
    return max_sum

def solve():
    n, m, r = map(int, input().split())
    items = [0] + list(map(int, input().split()))
    graph = [list(map(int, input().split())) for _ in range(r)]
    
    dist = floyd_warshall(n, graph)
    result = max_items(n, m, items, dist)
    
    print(result)

solve()