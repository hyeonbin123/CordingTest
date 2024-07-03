def solution(m, trees):
    def wood_collected(height):
        return sum(j - height if j > height else 0 for j in trees)

    start, end = 0, max(trees)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        sum_tree = wood_collected(mid)

        if sum_tree == m:
            return mid
        elif sum_tree > m:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1

    return answer

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(M, trees))
