from collections import defaultdict

def calculate_A(n, p, q, x, y):
    memo = defaultdict(int)
    
    def A(i):
        if i <= 0:
            return 1
        if memo[i]:
            return memo[i]
        memo[i] = A(i // p - x) + A(i // q - y)
        return memo[i]
    
    return A(n)

N, P, Q, X, Y = map(int, input().split())
print(calculate_A(N, P, Q, X, Y))