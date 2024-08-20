import sys
input = sys.stdin.readline

n = int(input())

# 좌표를 저장할 리스트
points = []

# 좌표 입력 받기
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 정렬
# x좌표를 첫 번째 기준으로, y좌표를 두 번째 기준으로 정렬
points.sort(key=lambda p: (p[0], p[1]))

# 정렬된 좌표 출력
for x, y in points:
    print(x, y)