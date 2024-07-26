def calculate_earliest_ring_time(N, L, D):
    album_duration = N * (L + 5) - 5
    ring_time = 0
    
    while ring_time <= album_duration:
        current_time = ring_time % (L + 5)
        if current_time >= L:
            return ring_time
        ring_time += D
    
    return ring_time

def main():
    N, L, D = map(int, input().split())
    print(calculate_earliest_ring_time(N, L, D))

if __name__ == "__main__":
    main()