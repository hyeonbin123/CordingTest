import sys

input = sys.stdin.readline

def move_shark(r, c, s, d, R, C):
    if d in [1, 2]: 
        s %= (2 * R - 2)
        for _ in range(s):
            if r == 1:
                d = 2
            elif r == R:
                d = 1
            r += 1 if d == 2 else -1
    else:
        s %= (2 * C - 2)
        for _ in range(s):
            if c == 1:
                d = 3
            elif c == C:
                d = 4
            c += 1 if d == 3 else -1
    return r, c, d

def solve():
    R, C, M = map(int, input().split())
    sharks = {}
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks[(r, c)] = (s, d, z)
    
    total_size = 0
    for fisher in range(1, C + 1):
        for i in range(1, R + 1):
            if (i, fisher) in sharks:
                total_size += sharks[(i, fisher)][2]
                del sharks[(i, fisher)]
                break
        
        new_sharks = {}
        for (r, c), (s, d, z) in sharks.items():
            nr, nc, nd = move_shark(r, c, s, d, R, C)
            if (nr, nc) not in new_sharks or z > new_sharks[(nr, nc)][2]:
                new_sharks[(nr, nc)] = (s, nd, z)
        
        sharks = new_sharks
    
    return total_size

print(solve())