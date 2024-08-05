import math

def min_squares(n):
    if int(math.sqrt(n))**2 == n:
        return 1
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i*i))**2 == n - i*i:
            return 2
    
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i*i)) + 1):
            if int(math.sqrt(n - i*i - j*j))**2 == n - i*i - j*j:
                return 3
    
    return 4

n = int(input())
print(min_squares(n))