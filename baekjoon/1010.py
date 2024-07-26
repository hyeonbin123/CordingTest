def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def solve_bridge_problem():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        result = combination(M, N)
        print(result)

if __name__ == "__main__":
    solve_bridge_problem()