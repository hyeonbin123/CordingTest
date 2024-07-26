def find_most_common_sum(s1, s2, s3):
    min_sum = 3
    max_sum = s1 + s2 + s3 
    
    frequency = [0] * (max_sum + 1)
    
    for i in range(1, s1 + 1):
        for j in range(1, s2 + 1):
            for k in range(1, s3 + 1):
                frequency[i + j + k] += 1
    
    max_frequency = 0
    most_common_sum = 0
    for sum_value in range(min_sum, max_sum + 1):
        if frequency[sum_value] > max_frequency:
            max_frequency = frequency[sum_value]
            most_common_sum = sum_value
    
    return most_common_sum

s1, s2, s3 = map(int, input().strip().split())

print(find_most_common_sum(s1, s2, s3))