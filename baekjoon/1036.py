def to_decimal(s):
    return int(s, 36)

def to_base_36(n):
    if n == 0:
        return '0'
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while n:
        result = digits[n % 36] + result
        n //= 36
    return result

def solve(numbers, k):
    char_count = {}
    for num in numbers:
        for char in num:
            char_count[char] = char_count.get(char, 0) + 1
    
    char_value = sorted(char_count.keys(), key=lambda x: (char_count[x], x), reverse=True)
    
    decimal_numbers = [to_decimal(num) for num in numbers]
    
    max_values = []
    for char in char_value:
        value_increase = sum((35 - to_decimal(char)) * (36 ** i) 
                             for num in numbers 
                             for i, c in enumerate(reversed(num)) if c == char)
        max_values.append((char, value_increase))
    
    selected_chars = sorted(max_values, key=lambda x: x[1], reverse=True)[:k]
    
    for char, _ in selected_chars:
        for i, num in enumerate(numbers):
            decimal_numbers[i] += sum((35 - to_decimal(char)) * (36 ** j) 
                                      for j, c in enumerate(reversed(num)) if c == char)
    
    return to_base_36(sum(decimal_numbers))

n = int(input())
numbers = [input().strip() for _ in range(n)]
k = int(input())

print(solve(numbers, k))