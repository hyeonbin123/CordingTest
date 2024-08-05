from collections import deque
import copy
from itertools import combinations

def spread_virus(lab):
    n, m = len(lab), len(lab[0])
    virus_positions = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 2]
    queue = deque(virus_positions)
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx, ny))

def count_safe_area(lab):
    return sum(row.count(0) for row in lab)

def solve():
    n, m = map(int, input().split())
    original_lab = [list(map(int, input().split())) for _ in range(n)]
    
    empty_spaces = [(i, j) for i in range(n) for j in range(m) if original_lab[i][j] == 0]
    
    max_safe_area = 0
    
    for walls in combinations(empty_spaces, 3):
        lab = copy.deepcopy(original_lab)
        
        for x, y in walls:
            lab[x][y] = 1
        
        spread_virus(lab)
        safe_area = count_safe_area(lab)
        max_safe_area = max(max_safe_area, safe_area)
    
    return max_safe_area

print(solve())