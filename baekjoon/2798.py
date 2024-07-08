# 입력 받기
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 결과를 저장할 변수
result = 0

# 모든 카드 조합을 확인
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_cards = cards[i] + cards[j] + cards[k]
            # 합이 M 이하이면서 현재 결과보다 크다면 결과 갱신
            if sum_cards <= M and sum_cards > result:
                result = sum_cards

# 결과 출력
print(result)