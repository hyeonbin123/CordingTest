import sys
import heapq
from typing import List, Tuple

def solve(n: int, commutes: List[Tuple[int, int]], d: int) -> int:
    # 끝점을 기준으로 정렬된 통근 정보
    end_sorted_commutes = []
    for start, end in commutes:
        if start > end:
            start, end = end, start
        heapq.heappush(end_sorted_commutes, (end, start))

    max_count = 0
    current_count = 0
    active_commutes = []

    while end_sorted_commutes:
        end, start = heapq.heappop(end_sorted_commutes)
        
        # 현재 구간에 포함되는 통근 추가
        if start >= end - d:
            heapq.heappush(active_commutes, start)
            current_count += 1
        
        # 구간을 벗어난 통근 제거
        while active_commutes and active_commutes[0] < end - d:
            heapq.heappop(active_commutes)
            current_count -= 1
        
        max_count = max(max_count, current_count)

    return max_count

def main():
    input = sys.stdin.readline
    n = int(input())
    commutes = [tuple(map(int, input().split())) for _ in range(n)]
    d = int(input())

    result = solve(n, commutes, d)
    print(result)

if __name__ == "__main__":
    main()