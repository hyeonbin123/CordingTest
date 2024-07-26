def optimize_strange_multiplication(a, b):
    count_a = [0] * 10
    count_b = [0] * 10
    
    for digit in a:
        count_a[int(digit)] += 1
    
    for digit in b:
        count_b[int(digit)] += 1
    
    result = 0
    for i in range(10):
        for j in range(10):
            result += i * j * count_a[i] * count_b[j]
    
    return result

a, b = input().split()

print(optimize_strange_multiplication(a, b))