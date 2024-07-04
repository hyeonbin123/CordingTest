def solution(n, cables):
    start, end = 1, max(cables)  # 시작점을 1로 설정
    
    while start <= end:
        mid = (start + end) // 2
        count = sum(cable // mid for cable in cables)
        
        if count >= n:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

print(solution(n, cables))