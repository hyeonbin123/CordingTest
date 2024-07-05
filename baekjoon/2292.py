def solution(n):
    if n == 1:
        return 1

    rooms=1
    answer=1
    while rooms<n:
        rooms += 6*answer
        answer+=1
    return answer

n = int(input())
print(solution(n))