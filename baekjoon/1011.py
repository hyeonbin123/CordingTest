def min_moves(x, y):
    distance = y - x
    
    n = 0
    while n * (n + 1) < distance:
        n += 1
    
    return 2 * n if n * (n + 1) == distance else 2 * n if n * (n + 1) - n < distance else 2 * n - 1

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    print(min_moves(x, y))