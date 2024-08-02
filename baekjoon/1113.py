from collections import deque
import sys
input = sys.stdin.readline

def bfs(y, x):
    global answer, visited_global
    q = deque([(y, x)])
    visited = set([(y, x)])
    min_height = 10
    area = []
    current_height = pool[y][x]
    
    while q:
        y, x = q.popleft()
        area.append((y, x))
        
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = y + dy, x + dx
            
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                return False
            
            if (ny, nx) not in visited:
                if pool[ny][nx] <= current_height:
                    q.append((ny, nx))
                    visited.add((ny, nx))
                else:
                    min_height = min(min_height, pool[ny][nx])
    
    if min_height > current_height:
        for y, x in area:
            answer += min_height - pool[y][x]
            pool[y][x] = min_height
        visited_global.update(visited)
        return True
    return False

N, M = map(int, input().split())
pool = [list(map(int, input().rstrip())) for _ in range(N)]

answer = 0
visited_global = set()

changed = True
while changed:
    changed = False
    for y in range(N):
        for x in range(M):
            if (y, x) not in visited_global:
                if bfs(y, x):
                    changed = True

print(answer)