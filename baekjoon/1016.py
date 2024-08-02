def count_square_free_numbers(min_val, max_val):
    size = max_val - min_val + 1
    is_square_free = [True] * size
    i = 2
    
    while i * i <= max_val:
        start = max((min_val + i*i - 1) // (i*i), 1) * (i*i)
        
        for j in range(start, max_val + 1, i * i):
            if j >= min_val:
                is_square_free[j - min_val] = False
        
        i += 1
    
    return sum(is_square_free)

min_val, max_val = map(int, input().split())

print(count_square_free_numbers(min_val, max_val))