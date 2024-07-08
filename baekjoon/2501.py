N,K = map(int,input().split())

factor = [i for i in range(1,N+1) if N%i==0]

print(factor[K-1] if len(factor)>=K else 0)