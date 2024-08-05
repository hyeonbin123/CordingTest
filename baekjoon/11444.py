def matrix_multiply(a, b, mod):
    return [[(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
            [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]]

def matrix_power(matrix, n, mod):
    if n == 1:
        return matrix
    if n % 2 == 0:
        half = matrix_power(matrix, n // 2, mod)
        return matrix_multiply(half, half, mod)
    else:
        return matrix_multiply(matrix, matrix_power(matrix, n-1, mod), mod)

def fibonacci(n, mod):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = matrix_power([[1, 1], [1, 0]], n-1, mod)
    return result[0][0]

n = int(input())
mod = 1000000007

print(fibonacci(n, mod))