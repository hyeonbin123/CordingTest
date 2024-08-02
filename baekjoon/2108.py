import sys
from collections import Counter

def calculate_statistics(numbers):
    mean = round(sum(numbers) / len(numbers))
    
    sorted_numbers = sorted(numbers)
    median = sorted_numbers[len(numbers) // 2]
    
    counter = Counter(numbers)
    mode_candidates = counter.most_common()
    if len(mode_candidates) > 1 and mode_candidates[0][1] == mode_candidates[1][1]:
        mode = sorted(num for num, count in mode_candidates if count == mode_candidates[0][1])[1]
    else:
        mode = mode_candidates[0][0]
    
    range_value = max(numbers) - min(numbers)
    
    return mean, median, mode, range_value

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

mean, median, mode, range_value = calculate_statistics(numbers)

print(mean)
print(median)
print(mode)
print(range_value)