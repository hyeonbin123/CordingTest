def power_mod_10(a, b):
    result = 1
    a = a % 10
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % 10
        a = (a * a) % 10
        b = b // 2
    return result

def solve():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        last_digit = power_mod_10(a, b)
        print(10 if last_digit == 0 else last_digit)

if __name__ == "__main__":
    solve()