def calculate_A(n, p, q, memo={}):
    if n == 0: return 1
    if n in memo: return memo[n]
    
    memo[n] = calculate_A(n // p, p, q, memo) + calculate_A(n // q, p, q, memo)
    return memo[n]

N, P, Q = map(int, input().split())

print(calculate_A(N, P, Q))