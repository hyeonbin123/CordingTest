from itertools import combinations, product
from collections import Counter

# 각 주사위 조합의 가능한 점수 분포를 계산하는 함수입니다.
def calculate_score_distribution(dice):
    # 점수 분포를 저장할 Counter 객체를 초기화합니다.
    score_distribution = Counter()
    # 주사위 조합의 모든 가능한 결과에 대해 반복합니다.
    for outcomes in product(*dice):
        # 각 결과의 합계를 계산하고, 해당 합계가 나타나는 횟수를 카운트합니다.
        score_distribution[sum(outcomes)] += 1
    return score_distribution

# 두 점수 분포 사이의 승리 확률을 계산하는 함수입니다.
def compare_distributions(dist_a, dist_b):
    a_wins = 0  # A가 이긴 경우의 수를 카운트합니다.
    # 전체 게임 수는 두 분포의 가능한 결과 수의 곱입니다.
    total_games = sum(dist_a.values()) * sum(dist_b.values())
    # A의 모든 가능한 점수에 대해 반복합니다.
    for score_a, count_a in dist_a.items():
        # B의 모든 가능한 점수에 대해 반복합니다.
        for score_b, count_b in dist_b.items():
            # A의 점수가 B의 점수보다 클 경우,
            # A가 이긴 경우의 수에 (A가 해당 점수를 얻은 횟수 * B가 해당 점수를 얻은 횟수)를 더합니다.
            if score_a > score_b:
                a_wins += count_a * count_b
    # A의 승리 확률을 계산하여 반환합니다.
    return a_wins / total_games

# 최적의 주사위 조합을 찾는 함수입니다.
def solution(dice):
    n = len(dice)  # 주사위의 총 개수
    half_n = n // 2  # 반으로 나눈 주사위의 개수
    max_win_probability = -1  # 최대 승리 확률을 추적합니다.
    best_combination = []  # 최적의 조합을 저장합니다.

    # 가능한 모든 주사위 조합에 대해 반복합니다.
    for a_comb in combinations(range(n), half_n):
        a_dice = [dice[i] for i in a_comb]  # A의 주사위 조합
        b_dice = [dice[i] for i in range(n) if i not in a_comb]  # A가 선택하지 않은 주사위들로 B의 조합을 만듭니다.

        # A와 B의 점수 분포를 계산합니다.
        a_distribution = calculate_score_distribution(a_dice)
        b_distribution = calculate_score_distribution(b_dice)

        # A와 B의 분포를 비교하여 승리 확률을 계산합니다.
        win_probability = compare_distributions(a_distribution, b_distribution)

        # 현재 조합의 승리 확률이 지금까지 찾은 최대 승리 확률보다 높다면, 정보를 갱신합니다.
        if win_probability > max_win_probability:
            max_win_probability = win_probability
            best_combination = sorted(a_comb)

    # 최적의 조합을 1-based index로 조정하여 반환합니다.
    return [x + 1 for x in best_combination]



# 테스트 케이스
dice1 = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
dice2 = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
dice3 = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]

print(solution(dice1))
print(solution(dice2))
print(solution(dice3))
