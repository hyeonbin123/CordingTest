n=int(input())
p=sorted(list(map(int,input().split())))
print(sum([sum(p[:i+1]) for i in range(len(p))]))