import sys

input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def intersect(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    
    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)
    
    if abc * abd <= 0 and cda * cdb <= 0:
        if abc * abd == 0 and cda * cdb == 0:
            if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
               min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return True
        else:
            return True
    return False

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
parent = list(range(N))

for i in range(N):
    for j in range(i+1, N):
        if intersect(lines[i], lines[j]):
            union(parent, i, j)

groups = {}
for i in range(N):
    root = find(parent, i)
    if root not in groups:
        groups[root] = 0
    groups[root] += 1

group_count = len(groups)
max_group_size = max(groups.values()) if groups else 0

print(group_count)
print(max_group_size)