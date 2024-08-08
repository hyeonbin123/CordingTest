MOD = 1000000007

def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def matrix_power(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        half = matrix_power(A, n // 2)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(A, matrix_power(A, n - 1))

def solve(D):
    # 인접 행렬 정의 (0: 정보과학관, 1: 전산관, 2: 미래관, 3: 진리관, 4: 학생회관, 5: 형남공학관, 6: 한경직기념관, 7: 신양관)
    adj_matrix = [
        [0, 1, 1, 0, 0, 0, 0, 0],  # 정보과학관
        [1, 0, 1, 0, 0, 0, 0, 1],  # 전산관
        [1, 1, 0, 0, 0, 0, 1, 1],  # 미래관
        [0, 0, 0, 0, 1, 0, 1, 1],  # 진리관
        [0, 0, 0, 1, 0, 1, 0, 0],  # 학생회관
        [0, 0, 0, 0, 1, 0, 1, 0],  # 형남공학관
        [0, 0, 1, 1, 0, 1, 0, 1],  # 한경직기념관
        [0, 1, 1, 1, 0, 0, 1, 0]   # 신양관
    ]
    
    result = matrix_power(adj_matrix, D)
    return result[0][0]

D = int(input())

print(solve(D))