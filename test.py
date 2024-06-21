def solution(heights):
    heights.sort()  # 높이 배열을 오름차순으로 정렬
    rearranged = []  # 재배치할 높이를 저장할 배열
    
    # 정렬된 배열에서 큰 값과 작은 값을 번갈아가며 선택
    for i in range(len(heights)//2):
        rearranged.append(heights[i])  # 작은 값
        rearranged.append(heights[~i])  # 큰 값 (~i는 -i-1과 동일, 즉 배열의 끝에서 시작)
    
    # 배열의 길이가 홀수인 경우 마지막 중간값 추가
    if len(heights) % 2 != 0:
        rearranged.append(heights[len(heights)//2])
    
    # 이웃한 지점 사이의 높이 차이의 최솟값 찾기
    min_diff = float('inf')  # 가능한 가장 큰 값으로 초기화
    for i in range(1, len(rearranged)):
        min_diff = min(min_diff, abs(rearranged[i] - rearranged[i-1]))
    
    return min_diff


print(solution([1, 8, 5]))  # 예상 결과: 4
print(solution([11, 6, 4, 11]))  # 예상 결과: 5
print(solution([9, 9, 9, 9, 30]))  # 예상 결과: 0