# 입력 값 받기
N = int(input())

# 위쪽 피라미드 출력
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# 아래쪽 피라미드 출력
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))
