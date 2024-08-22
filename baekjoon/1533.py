import sys
from typing import List, Dict

MOD = 1000003

def read_input() -> tuple:
    input_func = sys.stdin.readline
    num_roads, start_idx, end_idx, late_time = map(int, input_func().split())
    graph = [list(map(int, input_func().strip())) for _ in range(num_roads)]
    return num_roads, start_idx, end_idx, late_time, graph

def create_matrix(num_roads: int, graph: List[List[int]]) -> List[List[int]]:
    size = 5 * num_roads
    mat = [[0] * size for _ in range(size)]
    
    for i in range(1, size):
        if i % 5:
            mat[i][i-1] = 1
    
    for i, row in enumerate(graph):
        for j, weight in enumerate(row):
            if weight:
                mat[i*5][5*j + weight-1] = 1
    
    return mat

def matrix_multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    n, m, p = len(a), len(b), len(b[0])
    result = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            result[i][j] = sum((a[i][k] * b[k][j]) % MOD for k in range(m)) % MOD
    return result

def matrix_power(matrix: List[List[int]], exp: int, memo: Dict[int, List[List[int]]]) -> List[List[int]]:
    if exp in memo:
        return memo[exp]
    
    if exp == 1:
        return matrix
    
    half = matrix_power(matrix, exp // 2, memo)
    result = matrix_multiply(half, half)
    
    if exp % 2:
        result = matrix_multiply(result, matrix)
    
    memo[exp] = result
    return result

def solve(num_roads: int, start_idx: int, end_idx: int, late_time: int, graph: List[List[int]]) -> int:
    matrix = create_matrix(num_roads, graph)
    memo: Dict[int, List[List[int]]] = {}
    result = matrix_power(matrix, late_time, memo)
    return result[(start_idx-1)*5][(end_idx-1)*5]

if __name__ == "__main__":
    num_roads, start_idx, end_idx, late_time, graph = read_input()
    print(solve(num_roads, start_idx, end_idx, late_time, graph))