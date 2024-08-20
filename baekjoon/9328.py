from collections import deque

def solve(h, w, building, initial_keys):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    keys = set(initial_keys)
    documents = 0
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    doors = {chr(65+i): [] for i in range(26)}  # A-Z 문에 대한 위치 저장

    def visit(x, y):
        nonlocal documents
        if building[x][y] == '$':
            documents += 1
        elif building[x][y].islower():
            keys.add(building[x][y])
            for door_x, door_y in doors[building[x][y].upper()]:
                if not visited[door_x][door_y]:
                    queue.append((door_x, door_y))
                    visited[door_x][door_y] = True
        elif building[x][y].isupper():
            if building[x][y].lower() not in keys:
                doors[building[x][y]].append((x, y))
                return
        queue.append((x, y))
        visited[x][y] = True

    # 시작점 찾기 (가장자리)
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if building[i][j] != '*' and not visited[i][j]:
                    visit(i, j)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and building[nx][ny] != '*':
                visit(nx, ny)
    
    return documents

# 입력 처리
T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    building = [list(input().strip()) for _ in range(h)]
    initial_keys = input().strip()
    if initial_keys == '0':
        initial_keys = ''
    
    result = solve(h, w, building, initial_keys)
    print(result)