n,m=map(int,input().strip().split())
baskets=[0]*n
for i in range(m):
    i,j,k=map(int,input().strip().split())
    for z in range(i-1,j):
        baskets[z]=k
print(' '.join(map(str, baskets)))