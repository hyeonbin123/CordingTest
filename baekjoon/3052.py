su=set()
for _ in range(10):
    n=int(input().strip())
    su.add(n%42)
print(len(su))