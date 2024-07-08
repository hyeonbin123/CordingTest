def solution(N, stages):
    # 각 스테이지에 도달한 플레이어 수를 계산
    reached = [0] * (N + 2)
    for stage in stages:
        reached[stage] += 1
    
    # 각 스테이지의 실패율을 계산
    total = len(stages)
    failure_rates = {}
    for i in range(1, N + 1):
        if total == 0:
            failure_rates[i] = 0
        else:
            failure_rates[i] = reached[i] / total
        total -= reached[i]
    
    # 실패율에 따라 스테이지를 정렬
    return sorted(range(1, N + 1), key=lambda x: (-failure_rates[x], x))



print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))