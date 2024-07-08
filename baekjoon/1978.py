def solution(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
prime_count = sum(1 for num in numbers if solution(num))

# 결과 출력
print(prime_count)