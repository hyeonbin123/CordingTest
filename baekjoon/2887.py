import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(n, edges):
    parent = list(range(n))
    edges.sort(key=lambda x: x[2])
    total_cost = 0
    edge_count = 0

    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            edge_count += 1
            if edge_count == n - 1:
                break

    return total_cost

def main():
    input = sys.stdin.readline
    n = int(input())
    planets = [list(map(int, input().split())) + [i] for i in range(n)]

    edges = []
    for i in range(3):
        planets.sort(key=lambda x: x[i])
        for j in range(1, n):
            cost = abs(planets[j][i] - planets[j-1][i])
            edges.append((planets[j-1][3], planets[j][3], cost))

    print(kruskal(n, edges))

if __name__ == "__main__":
    main()