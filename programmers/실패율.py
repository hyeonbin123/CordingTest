def solution(N, stages):
    reached = [0] * (N + 2)
    for stage in stages:
        reached[stage] += 1
    
    total = len(stages)
    failure_rates = {}
    for i in range(1, N + 1):
        if total == 0:
            failure_rates[i] = 0
        else:
            failure_rates[i] = reached[i] / total
        total -= reached[i]
    
    return sorted(range(1, N + 1), key=lambda x: (-failure_rates[x], x))



print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))