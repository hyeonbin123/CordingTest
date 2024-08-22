import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True
    dp[node][1] = 1  # 현재 노드가 얼리 어답터인 경우

    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]  # 현재 노드가 얼리 어답터가 아닌 경우
            dp[node][1] += min(dp[child])  # 현재 노드가 얼리 어답터인 경우

n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
dp = [[0, 0] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dfs(0)
print(min(dp[0]))