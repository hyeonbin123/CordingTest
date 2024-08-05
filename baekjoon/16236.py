from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y, 0)])
    fish = []

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if space[nx][ny] <= shark_size:
                    visited[nx][ny] = 1
                    if 0 < space[nx][ny] < shark_size:
                        fish.append((nx, ny, dist + 1))
                    else:
                        queue.append((nx, ny, dist + 1))

    return sorted(fish, key=lambda x: (x[2], x[0], x[1]))

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

shark_size = 2
shark_x, shark_y = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0

time = 0
eat_count = 0

while True:
    fish = bfs(shark_x, shark_y)
    if not fish:
        break

    next_x, next_y, dist = fish[0]
    time += dist
    eat_count += 1
    space[next_x][next_y] = 0

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

    shark_x, shark_y = next_x, next_y

print(time)