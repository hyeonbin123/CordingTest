def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

t=int(input().strip())
for _ in range(t):
    a,b=map(int,input().strip().split())
    print(lcm(a,b))