def calculate_points(N):
    return (2**N + 1)**2

# 입력 받기
N = int(input())

# 결과 계산 및 출력
result = calculate_points(N)
print(result)