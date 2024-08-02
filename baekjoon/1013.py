import re

def check_pattern(signal):
    pattern = r'^((?:100+1+|01)+)$'
    
    return "YES" if re.match(pattern, signal) else "NO"

T = int(input())

for _ in range(T):
    signal = input().strip()
    result = check_pattern(signal)
    print(result)