N = int(input())
li = list(map(int, input().split()))
y = m = 0
for n in li:
    y += (n//30 + 1) * 10
    m += (n//60 + 1) * 15
print(f"Y M {m}" if m == y else f"M {m}" if m < y else f"Y {y}")