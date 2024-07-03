from itertools import combinations, product
from collections import Counter

def calculate_score_distribution(dice):
    score_distribution = Counter()
    for outcomes in product(*dice):
        score_distribution[sum(outcomes)] += 1
    return score_distribution

def compare_distributions(dist_a, dist_b):
    a_wins = 0
    total_games = sum(dist_a.values()) * sum(dist_b.values())
    for score_a, count_a in dist_a.items():
        for score_b, count_b in dist_b.items():
            if score_a > score_b:
                a_wins += count_a * count_b
    return a_wins / total_games

def solution(dice):
    n = len(dice)
    half_n = n // 2
    max_win_probability = -1
    best_combination = []

    for a_comb in combinations(range(n), half_n):
        a_dice = [dice[i] for i in a_comb]
        b_dice = [dice[i] for i in range(n) if i not in a_comb]

        a_distribution = calculate_score_distribution(a_dice)
        b_distribution = calculate_score_distribution(b_dice)

        win_probability = compare_distributions(a_distribution, b_distribution)

        if win_probability > max_win_probability:
            max_win_probability = win_probability
            best_combination = a_comb

    return [x + 1 for x in best_combination]