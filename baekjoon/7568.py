def get_ranks(people):
    n = len(people)
    ranks = [1] * n  # 모든 사람의 초기 등수를 1로 설정
    
    for i in range(n):
        for j in range(n):
            if i != j:
                if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                    ranks[i] += 1  # i번째 사람보다 j번째 사람이 덩치가 크면 i의 등수 증가
    
    return ranks

# 입력 받기
n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

# 등수 계산 및 출력
result = get_ranks(people)
print(' '.join(map(str, result)))