def find_sequence(N, L):
    for length in range(L, 101):
        start = (N - (length * (length - 1) // 2)) / length
        if start == int(start) and start >= 0:
            return [int(start + i) for i in range(length)]
    
    return [-1]

N, L = map(int, input().split())

result = find_sequence(N, L)

print(-1 if result == [-1] else ' '.join(map(str, result)))