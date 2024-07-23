from itertools import combinations

heights = [int(input()) for _ in range(9)]

for seven_heights in combinations(heights,7):
    if sum(seven_heights)==100:
        for height in sorted(seven_heights):
            print(height)
        break