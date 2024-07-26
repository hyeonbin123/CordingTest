from collections import deque

def min_operations(N, M, positions):
    queue = deque(range(1, N+1))
    total_operations = 0

    for target in positions:
        index = queue.index(target)
        
        if index <= len(queue) // 2:
            queue.rotate(-index)
            total_operations += index
        else:
            queue.rotate(len(queue) - index)
            total_operations += len(queue) - index
        
        queue.popleft()

    return total_operations

N, M = map(int, input().split())
positions = list(map(int, input().split()))

print(min_operations(N, M, positions))