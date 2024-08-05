from collections import deque

def bfs(n, m, matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    
    queue = deque([(0, 0, 0)])
    
    while queue:
        x, y, broken = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                elif matrix[nx][ny] == 1 and broken == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))
    
    return -1

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(n, m, matrix))