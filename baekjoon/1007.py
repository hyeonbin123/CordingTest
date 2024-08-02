import sys
import math

input = sys.stdin.readline

def vector_matching(points):
    n = len(points)
    half_n = n // 2
    min_length_squared = float('inf')
    
    total_x = sum(p[0] for p in points)
    total_y = sum(p[1] for p in points)
    
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    for mask in range(1 << (n - 1)):
        if bin(mask).count('1') != half_n:
            continue
        
        sum_x = sum(x_coords[i] for i in range(n - 1) if mask & (1 << i))
        sum_y = sum(y_coords[i] for i in range(n - 1) if mask & (1 << i))
        
        if mask & (1 << (n - 1)):
            sum_x += x_coords[-1]
            sum_y += y_coords[-1]
        
        diff_x = 2 * sum_x - total_x
        diff_y = 2 * sum_y - total_y
        
        length_squared = diff_x**2 + diff_y**2
        min_length_squared = min(min_length_squared, length_squared)
    
    return math.sqrt(min_length_squared)

T = int(input())
for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    result = vector_matching(points)
    print(f"{result:.12f}")