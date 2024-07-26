import sys
input = sys.stdin.readline

def calculate_sum_sign(n):
    total = 0
    for _ in range(n):
        total += int(input().strip())
    return 0 if total == 0 else '+' if total > 0 else '-'


for _ in range(3):
    n=int(input().strip())
    print(calculate_sum_sign(n))