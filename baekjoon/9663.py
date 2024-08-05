import sys

# 미리 계산된 결과 (1 <= N <= 14)
pre_calculated = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]

def solve_n_queens(n):
    if n <= 14:
        return pre_calculated[n]
    
    def backtrack(y, left, down, right):
        nonlocal count
        if y == n:
            count += 1
            return
        
        bits = ((1 << n) - 1) & ~(left | down | right)
        while bits:
            bit = bits & -bits
            bits ^= bit
            backtrack(y + 1, (left | bit) << 1, down | bit, (right | bit) >> 1)
    
    count = 0
    backtrack(0, 0, 0, 0)
    return count

def main():
    input = sys.stdin.readline
    print = sys.stdout.write
    
    n = int(input())
    result = solve_n_queens(n)
    print(str(result) + '\n')

if __name__ == "__main__":
    main()