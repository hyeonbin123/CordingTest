from collections import deque

def bfs(n, m, cheese):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    time = 0
    while True:
        air = [[0] * m for _ in range(n)]
        queue = deque([(0, 0)])
        air[0][0] = 1
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and air[nx][ny] == 0:
                    if cheese[nx][ny] == 0:
                        air[nx][ny] = 1
                        queue.append((nx, ny))
        
        melted = False
        for i in range(n):
            for j in range(m):
                if cheese[i][j] == 1:
                    count = 0
                    for k in range(4):
                        ni, nj = i + dx[k], j + dy[k]
                        if 0 <= ni < n and 0 <= nj < m and air[ni][nj] == 1:
                            count += 1
                    if count >= 2:
                        cheese[i][j] = 0
                        melted = True
        
        if not melted:
            return time
        
        time += 1

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

print(bfs(n, m, cheese))