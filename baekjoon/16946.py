from collections import deque

def bfs(x, y, id):
    queue = deque([(x, y)])
    visited[x][y] = id
    size = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = id
                size += 1
    return size

# 입력 받기
N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]

# 방문 배열 및 영역 크기 딕셔너리 초기화
visited = [[0] * M for _ in range(N)]
area_size = {}
current_id = 1

# 모든 빈 칸에 대해 BFS 수행
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 and visited[i][j] == 0:
            area_size[current_id] = bfs(i, j, current_id)
            current_id += 1

# 결과 저장을 위한 배열
result = [[0] * M for _ in range(N)]

# 각 벽에 대해 인접한 영역의 크기 합산
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            adjacent_areas = set()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 0:
                    adjacent_areas.add(visited[nx][ny])
            result[i][j] = (sum(area_size[area] for area in adjacent_areas) + 1) % 10
        else:
            result[i][j] = 0

# 결과 출력
for row in result:
    print(''.join(map(str, row)))