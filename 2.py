from itertools import permutations
def solution(heights):
    n=len(heights)
    max_score=0
    for a_comb in permutations(range(n), n):
        choice = [heights[i] for i in a_comb]
        max_score = max(max_score,min([abs(choice[i+1] - choice[i]) for i in range(n-1)]))
    return max_score


print(solution([1, 8, 5]))  # 예상 결과: 4
print(solution([11, 6, 4, 11]))  # 예상 결과: 5
print(solution([9, 9, 9, 9, 30]))  # 예상 결과: 0

# def solution(heights):
#     # 높이를 정렬합니다.
#     heights.sort()
#     # 인접한 높이 차이들의 리스트를 생성합니다.
#     height_diffs = [heights[i+1] - heights[i] for i in range(len(heights)-1)]
#     print(height_diffs)
#     # 높이 차이들 중 최대값을 찾습니다.
#     max_min_diff = max(height_diffs)
#     return max_min_diff