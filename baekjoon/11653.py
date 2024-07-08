def prime_factorization(n):
    # 2로 나누기
    while n % 2 == 0:
        print(2)
        n //= 2
    
    # 3부터 시작하여 홀수로만 나누기
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            print(i)
            n //= i
    
    # 남은 수가 2보다 크면 그 자체가 소수
    if n > 2:
        print(n)

N = int(input())
if N > 1:
    prime_factorization(N)