import math
def solution(A, B, V):
    days = math.ceil((V - B) / (A - B))
    return days

A, B, V = map(int, input().strip().split())
print(solution(A, B, V))