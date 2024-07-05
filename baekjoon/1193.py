def solution(n):
    x = 1
    while n > x:
        n -= x
        x += 1

    if x % 2 == 0:
        numerator = n
        denominator = x - n + 1
    else:
        numerator = x - n + 1
        denominator = n

    return f"{numerator}/{denominator}"

n = int(input())
print(solution(n))