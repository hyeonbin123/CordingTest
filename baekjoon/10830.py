MOD = 1000

def matrix_multiply(A, B):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD
    return result

def matrix_power(A, B):
    N = len(A)
    result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    while B > 0:
        if B % 2 == 1:
            result = matrix_multiply(result, A)
        A = matrix_multiply(A, A)
        B //= 2
    return result

def main():
    N, B = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    result = matrix_power(A, B)
    
    for row in result:
        print(*row)

if __name__ == "__main__":
    main()