from collections import deque
import sys

input = sys.stdin.readline

def solution(n, graph, times, target):
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in graph[i]:
            indegree[j] += 1
            
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = times[i]

    while q:
        curr = q.popleft()
        for next_node in graph[curr]:
            indegree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[curr] + times[next_node])
            if indegree[next_node] == 0:
                q.append(next_node)

    return dp[target]


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        times = [0] + list(map(int, input().split()))
        graph = [[] for _ in range(N + 1)]
        
        for _ in range(K):
            X, Y = map(int, input().split())
            graph[X].append(Y)
        
        W = int(input())
        print(solution(N, graph, times, W))

if __name__ == "__main__":
    main()

