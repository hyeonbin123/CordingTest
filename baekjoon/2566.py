import sys

input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]

# 최댓값과 그 위치 초기화
max_value, max_y, max_x = matrix[0][0], 0, 0

for y in range(9):
    for x in range(9):
        if matrix[y][x] > max_value:
            max_value, max_y, max_x = matrix[y][x], y, x

print(max_value)
print(max_y + 1, max_x + 1)