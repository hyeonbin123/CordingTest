import sys

def tsp(n, graph):
    sys.setrecursionlimit(10**6)
    ALL_VISITED = (1 << n) - 1
    dp = {}

    def find_path(mask, pos):
        if mask == ALL_VISITED:
            return graph[pos][0] or float('inf')
        
        key = (mask, pos)
        if key in dp:
            return dp[key]
        
        min_cost = float('inf')
        for next_city in range(n):
            if not (mask & (1 << next_city)) and graph[pos][next_city]:
                cost = graph[pos][next_city] + find_path(mask | (1 << next_city), next_city)
                min_cost = min(min_cost, cost)
        
        dp[key] = min_cost
        return min_cost

    return find_path(1, 0)

# 입력 처리
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(tsp(n, graph))