import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if field[y][x] == 1:
        field[y][x] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(j, i):
                count += 1
    
    print(count)