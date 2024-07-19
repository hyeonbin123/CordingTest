def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a,b=map(int,input().strip().split())
print(gcd(a,b))
print(lcm(a,b))