from collections import deque

def bfs(N, K):
    MAX = 100001
    visited = [0] * MAX
    count = [0] * MAX
    queue = deque([(N, 0)])
    visited[N] = 1
    count[N] = 1
    
    while queue:
        pos, time = queue.popleft()
        
        if pos == K:
            return time, count[pos]
        
        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos < MAX:
                if visited[next_pos] == 0:
                    visited[next_pos] = visited[pos] + 1
                    count[next_pos] = count[pos]
                    queue.append((next_pos, time + 1))
                elif visited[next_pos] == visited[pos] + 1:
                    count[next_pos] += count[pos]

def main():
    N, K = map(int, input().split())
    time, ways = bfs(N, K)
    print(time)
    print(ways)

if __name__ == "__main__":
    main()