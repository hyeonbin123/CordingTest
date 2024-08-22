import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    global id, scc_count
    id += 1
    visited[node] = low[node] = id
    stack.append(node)
    on_stack[node] = True
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            low[node] = min(low[node], low[next_node])
        elif on_stack[next_node]:
            low[node] = min(low[node], visited[next_node])
    
    if visited[node] == low[node]:
        scc_count += 1
        while True:
            top = stack.pop()
            on_stack[top] = False
            scc[top] = scc_count
            if top == node:
                break

def add_clause(a, b):
    graph[-a].append(b)
    graph[-b].append(a)

def solve():
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    
    for i in range(1, n+1):
        if scc[i] == scc[-i]:
            return "no"
    return "yes"

while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    graph = [[] for _ in range(2*n+1)]
    visited = [0] * (2*n+1)
    low = [0] * (2*n+1)
    scc = [0] * (2*n+1)
    on_stack = [False] * (2*n+1)
    stack = []
    id = 0
    scc_count = 0

    add_clause(1, 1)  # 상근이(1번)는 반드시 포함되어야 함

    for _ in range(m):
        a, b = map(int, input().split())
        add_clause(a, b)

    print(solve())