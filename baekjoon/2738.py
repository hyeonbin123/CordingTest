n,m=map(int,input().strip().split())
a=[list(map(int,input().strip().split())) for _ in range(n)]
for i in range(n):
    num = list(map(int,input().strip().split()))
    for j in range(m):
        a[i][j]+=num[j]
for i in a:
    print(' '.join(map(str, i)))