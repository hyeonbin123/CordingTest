import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = float('inf')

def encode_state(arr):
    return tuple(arr)

def decode_state(state):
    return list(state)

def get_neighbors(state, operations):
    neighbors = []
    arr = decode_state(state)
    for i, (l, r, c) in enumerate(operations):
        new_arr = arr[:]
        new_arr[l-1], new_arr[r-1] = new_arr[r-1], new_arr[l-1]
        neighbors.append((encode_state(new_arr), c, i))
    return neighbors

def dijkstra(start, target, operations):
    dist = defaultdict(lambda: INF)
    dist[start] = 0
    pq = [(0, start, [])]
    
    while pq:
        cost, state, path = heapq.heappop(pq)
        
        if state == target:
            return cost, path
        
        if cost > dist[state]:
            continue
        
        for next_state, op_cost, op_index in get_neighbors(state, operations):
            next_cost = cost + op_cost
            if next_cost < dist[next_state]:
                dist[next_state] = next_cost
                new_path = path + [op_index]
                heapq.heappush(pq, (next_cost, next_state, new_path))
    
    return -1, []

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    operations = [list(map(int, input().split())) for _ in range(M)]

    start_state = encode_state(A)
    target_state = encode_state(sorted(A))

    min_cost, path = dijkstra(start_state, target_state, operations)
    
    if min_cost == -1:
        return -1
    else:
        return min_cost

print(solve())