from collections import defaultdict

def count_outfit_combinations(clothes):
    category_count = defaultdict(int)
    
    for _, category in clothes:
        category_count[category] += 1
    
    result = 1
    for count in category_count.values():
        result *= (count + 1)
    
    return result - 1

T = int(input())

for _ in range(T):
    n = int(input())
    clothes = [input().split() for _ in range(n)]
    print(count_outfit_combinations(clothes))