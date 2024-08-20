import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

# 숫자를 리스트에 저장
numbers = sorted([int(input()) for _ in range(n)])

for num in numbers:
    print(str(num) + '\n')