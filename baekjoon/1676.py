def count_trailing_zeros(n):
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count

# 입력 받기
N = int(input())

# 결과 출력
print(count_trailing_zeros(N))