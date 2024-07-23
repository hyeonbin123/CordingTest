r = 31
M = 1234567891

def calculate_hash(s):
    hash_value = 0
    for i, char in enumerate(s):
        a = ord(char) - ord('a') + 1  # a=1, b=2, ..., z=26
        hash_value += a * (r ** i)
    return hash_value % M

L = int(input())
string = input().strip()

result = calculate_hash(string)
print(result)